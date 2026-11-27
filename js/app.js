/* BioMaster Pro Exam Bank — Main Client Application (works identically on file:// & http://) */
(function () {
  "use strict";

  const BM = window.BIOMASTER || {};
  const TOPICS = BM.TOPICS || {};
  const TOPIC_KEYS = Object.keys(TOPICS);
  const EXAMS_BUNDLE = BM.EXAMS_BUNDLE || { exams: [], audit: {} };
  const FIXED_EXAMS = EXAMS_BUNDLE.exams || [];

  const STORAGE_KEY = "biomaster_exam_bank_v2";
  const EXAM_DURATION_SEC = 60 * 60; // 60 minutes

  // --- Data Indexing ---
  const mcqMap = new Map();
  const tfMap = new Map();
  const saMap = new Map();
  const qToExamMap = new Map();
  const allQuestions = [];

  function ingestData() {
    const mcqArrays = [
      BM.MCQ_CELLBIO || [],
      BM.MCQ_MOLECULAR || [],
      BM.MCQ_CELLULAR || [],
      BM.MCQ_MENDEL || [],
      BM.MCQ_POPULATION || [],
      BM.MCQ_PHYSIOLOGY || [],
    ];
    mcqArrays.forEach((arr) => {
      arr.forEach((q) => {
        mcqMap.set(q.id, q);
        allQuestions.push({ kind: "MCQ", data: q, search: buildSearchText("MCQ", q) });
      });
    });

    (BM.TF_BANK || []).forEach((q) => {
      tfMap.set(q.id, q);
      allQuestions.push({ kind: "TF", data: q, search: buildSearchText("TF", q) });
    });

    (BM.SA_BANK || []).forEach((q) => {
      saMap.set(q.id, q);
      allQuestions.push({ kind: "SA", data: q, search: buildSearchText("SA", q) });
    });

    FIXED_EXAMS.forEach((ex) => {
      [...ex.mcqIds, ...ex.tfIds, ...ex.saIds].forEach((qid) => {
        qToExamMap.set(qid, ex.id);
      });
    });
  }

  function stripHtml(html) {
    return String(html || "").replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim();
  }

  function buildSearchText(kind, q) {
    let txt = `${q.id} ${q.subtopic || ""} `;
    if (kind === "TF") {
      txt += `${q.stem} ${(q.statements || []).map((s) => s.text + " " + s.exp).join(" ")}`;
    } else if (kind === "SA") {
      txt += `${q.q} ${q.answer} ${q.exp}`;
    } else {
      txt += `${q.q} ${(q.opts || []).join(" ")} ${q.exp}`;
    }
    return stripHtml(txt).toLowerCase();
  }

  // --- Persistent State ---
  let store = loadStore();

  function defaultStore() {
    return {
      completed: {},   // { [examId]: { score, p1, p2, p3, usedSec, answers, timestamp } }
      drafts: {},      // { [examId]: { answers, remainingSec, startedAt } }
      customExams: [], // User-generated <=5% overlap custom exams
    };
  }

  function loadStore() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return defaultStore();
      const parsed = JSON.parse(raw);
      return {
        completed: parsed.completed || {},
        drafts: parsed.drafts || {},
        customExams: Array.isArray(parsed.customExams) ? parsed.customExams : [],
      };
    } catch (_) {
      return defaultStore();
    }
  }

  function saveStore() {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(store));
    } catch (_) {
      // Ignore storage quota issues cleanly
    }
    updateTopStats();
  }

  // --- Global UI State ---
  let currentTab = "exams";
  let activeExam = null;
  let activeAnswers = createEmptyAnswers();
  let activeRemainingSec = EXAM_DURATION_SEC;
  let activeSubmittedResult = null;
  let reviewFilter = "all"; // "all" | "wrong"
  let timerHandle = null;
  let bankPage = 1;
  const BANK_PAGE_SIZE = 18;
  let theoryMounted = false;
  let auditMounted = false;

  function createEmptyAnswers() {
    return {
      mcq: {}, // { [qid]: optionIdx (0..3) }
      tf: {},  // { [qid]: { a: bool|null, b: ..., c: ..., d: ... } }
      sa: {},  // { [qid]: string }
    };
  }

  // --- Helpers ---
  function escapeHtml(str) {
    return String(str ?? "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function levelBadgeHtml(level) {
    if (level === "basic") return '<span class="px-2 py-0.5 rounded-full text-[11px] font-bold level-badge-basic">🟢 Cơ bản</span>';
    if (level === "adv") return '<span class="px-2 py-0.5 rounded-full text-[11px] font-bold level-badge-adv">🟡 Nâng cao</span>';
    return '<span class="px-2 py-0.5 rounded-full text-[11px] font-bold level-badge-hsg">🔴 HSG Tỉnh</span>';
  }

  function topicBadgeHtml(topicId) {
    const t = TOPICS[topicId] || { icon: "📘", short: topicId, badgeClass: "bg-slate-100 text-slate-800 border-slate-200" };
    return `<span class="px-2 py-0.5 rounded-full text-[11px] font-semibold border ${t.badgeClass}">${t.icon} ${escapeHtml(t.short)}</span>`;
  }

  function formatMMSS(totalSec) {
    const s = Math.max(0, Math.floor(totalSec));
    const mm = String(Math.floor(s / 60)).padStart(2, "0");
    const ss = String(s % 60).padStart(2, "0");
    return `${mm}:${ss}`;
  }

  function typesetMath(el) {
    if (!el) return;
    if (window.MathJax && typeof window.MathJax.typesetPromise === "function") {
      try {
        if (window.MathJax.typesetClear) {
          window.MathJax.typesetClear([el]);
        }
        window.MathJax.typesetPromise([el]).catch(() => {});
      } catch (_) {}
    } else if (window.MathJax && window.MathJax.startup && window.MathJax.startup.promise) {
      window.MathJax.startup.promise.then(() => typesetMath(el)).catch(() => {});
    }
  }

  function getAllAvailableExams() {
    return [...store.customExams, ...FIXED_EXAMS];
  }

  function findExamById(examId) {
    return getAllAvailableExams().find((e) => e.id === examId) || null;
  }

  function updateTopStats() {
    const elDone = document.getElementById("statDoneCount");
    const elTotal = document.getElementById("statTotalExams");
    const elQs = document.getElementById("statTotalQs");
    const elOv = document.getElementById("statMaxOverlap");
    if (elTotal) elTotal.textContent = String(FIXED_EXAMS.length);
    if (elQs) elQs.textContent = allQuestions.length.toLocaleString("vi-VN");
    if (elOv && EXAMS_BUNDLE.audit) {
      elOv.textContent = `${Number(EXAMS_BUNDLE.audit.maxPairwiseOverlapPct || 0).toFixed(2)}%`;
    }
    const doneFixed = FIXED_EXAMS.filter((ex) => Boolean(store.completed[ex.id])).length;
    if (elDone) elDone.textContent = String(doneFixed);
  }

  // --- Navigation ---
  function switchTab(tabName) {
    currentTab = tabName;
    const views = ["exams", "runner", "bank", "audit", "theory"];
    views.forEach((v) => {
      const el = document.getElementById(`view-${v}`);
      if (el) el.classList.toggle("hidden", v !== tabName);
    });

    document.querySelectorAll("#mainNav .nav-tab").forEach((btn) => {
      btn.classList.toggle("active", btn.getAttribute("data-tab") === tabName);
    });

    if (tabName === "exams") {
      renderExamsView();
    } else if (tabName === "runner") {
      renderRunnerShell();
    } else if (tabName === "bank") {
      renderBankView();
    } else if (tabName === "audit") {
      mountAuditView();
    } else if (tabName === "theory") {
      mountTheoryView();
    }
  }

  // ==================== TAB 1: EXAMS REPOSITORY ====================
  function renderExamsView() {
    const grid = document.getElementById("examsGrid");
    if (!grid) return;

    const search = (document.getElementById("examSearchInput")?.value || "").trim().toLowerCase();
    const statusFilter = document.getElementById("examStatusFilter")?.value || "all";
    const partTopicFilter = document.getElementById("examPartTopicFilter")?.value || "all";

    const list = getAllAvailableExams().filter((ex) => {
      const done = Boolean(store.completed[ex.id]);
      const draft = Boolean(store.drafts[ex.id]);

      if (statusFilter === "done" && !done) return false;
      if (statusFilter === "draft" && (!draft || done)) return false;
      if (statusFilter === "todo" && (done || draft)) return false;

      if (partTopicFilter !== "all") {
        const hasInP23 = (ex.part2Topics || []).includes(partTopicFilter) || (ex.part3Topics || []).includes(partTopicFilter);
        if (!hasInP23) return false;
      }

      if (search) {
        const hay = `${ex.id} ${ex.title} ${ex.subtitle || ""}`.toLowerCase();
        if (!hay.includes(search)) return false;
      }
      return true;
    });

    const countEl = document.getElementById("examFilterCount");
    if (countEl) {
      countEl.textContent = `Hiển thị ${list.length} / ${getAllAvailableExams().length} đề`;
    }

    if (list.length === 0) {
      grid.innerHTML = `
        <div class="col-span-full bg-white border border-slate-200 rounded-2xl p-8 text-center text-slate-500">
          Không tìm thấy đề thi phù hợp bộ lọc. Hãy thử đặt lại bộ lọc tìm kiếm.
        </div>`;
      return;
    }

    grid.innerHTML = list
      .map((ex) => {
        const comp = store.completed[ex.id];
        const draft = store.drafts[ex.id];
        const isCustom = Boolean(ex.isCustom);

        let statusBadge = `<span class="px-2 py-0.5 rounded-full text-[11px] font-bold bg-slate-100 text-slate-600">Chưa làm</span>`;
        let actionBtn = `<button data-start-exam="${ex.id}" class="flex-1 py-2 px-3 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs transition cursor-pointer">🚀 Bắt đầu thi (60p)</button>`;

        if (comp) {
          statusBadge = `<span class="px-2 py-0.5 rounded-full text-[11px] font-bold bg-emerald-100 text-emerald-800 border border-emerald-300">✅ ${comp.score.toFixed(2)}đ</span>`;
          actionBtn = `
            <button data-review-exam="${ex.id}" class="flex-1 py-2 px-3 rounded-xl bg-teal-600 hover:bg-teal-700 text-white font-bold text-xs transition cursor-pointer">📄 Xem bài giải</button>
            <button data-retake-exam="${ex.id}" class="py-2 px-3 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-xs transition cursor-pointer">🔄 Làm lại</button>`;
        } else if (draft) {
          const answered = countAnswered(draft.answers, ex);
          statusBadge = `<span class="px-2 py-0.5 rounded-full text-[11px] font-bold bg-amber-100 text-amber-800 border border-amber-300">⏳ Còn ${formatMMSS(draft.remainingSec)} (${answered}/24)</span>`;
          actionBtn = `
            <button data-resume-exam="${ex.id}" class="flex-1 py-2 px-3 rounded-xl bg-amber-500 hover:bg-amber-600 text-white font-bold text-xs transition cursor-pointer">▶ Tiếp tục làm</button>
            <button data-retake-exam="${ex.id}" class="py-2 px-3 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-xs transition cursor-pointer">Làm mới</button>`;
        }

        const p2Badges = (ex.part2Topics || []).map((t) => topicBadgeHtml(t)).join(" ");
        const p3Badges = (ex.part3Topics || []).map((t) => topicBadgeHtml(t)).join(" ");
        const lc = ex.levelCounts || { basic: 7, adv: 7, hsg: 6 };

        return `
          <article class="content-card p-4 flex flex-col justify-between gap-3 ${isCustom ? "border-2 border-amber-300 bg-amber-50/20" : ""}">
            <div class="space-y-2.5">
              <div class="flex items-start justify-between gap-2">
                <div class="flex items-center gap-2 flex-wrap">
                  <span class="px-2.5 py-0.5 rounded-lg text-xs font-extrabold ${isCustom ? "bg-amber-200 text-amber-900" : "bg-slate-900 text-white"}">${escapeHtml(ex.id)}</span>
                  ${isCustom && ex.overlapNote ? `<span class="text-[11px] font-bold text-teal-700">${escapeHtml(ex.overlapNote)}</span>` : ""}
                </div>
                ${statusBadge}
              </div>

              <div>
                <h3 class="font-extrabold text-sm sm:text-base text-slate-900 leading-snug">${escapeHtml(ex.title)}</h3>
                <p class="text-[11px] text-slate-500 mt-0.5">20 TN (${lc.basic} CB · ${lc.adv} NC · ${lc.hsg} HSG) · 2 Đ/S · 2 TLN · 60 phút</p>
              </div>

              <div class="space-y-1.5 text-[11px] pt-1 border-t border-slate-100">
                <div class="flex items-center gap-1.5 flex-wrap">
                  <span class="font-bold text-slate-600">Phần II (Đ/S):</span> ${p2Badges}
                </div>
                <div class="flex items-center gap-1.5 flex-wrap">
                  <span class="font-bold text-slate-600">Phần III (TLN):</span> ${p3Badges}
                </div>
              </div>
            </div>

            <div class="flex items-center gap-2 pt-2 border-t border-slate-100">
              ${actionBtn}
            </div>
          </article>
        `;
      })
      .join("");
  }

  // --- Custom Smart Exam Generator (enforces <= 5% overlap <= 1/24) ---
  function createCustomExam() {
    const focusTopic = document.getElementById("customFocusTopic")?.value || "balanced";
    const excludeMode = document.getElementById("customExcludeExam")?.value || "recent";

    const forbiddenSets = [];
    if (excludeMode === "DE-01" && FIXED_EXAMS[0]) {
      const e0 = FIXED_EXAMS[0];
      forbiddenSets.push(new Set([...e0.mcqIds, ...e0.tfIds, ...e0.saIds]));
    } else if (excludeMode === "recent" && store.customExams.length > 0) {
      store.customExams.slice(0, 5).forEach((ce) => {
        forbiddenSets.push(new Set([...ce.mcqIds, ...ce.tfIds, ...ce.saIds]));
      });
    } else if (excludeMode === "all_done") {
      Object.keys(store.completed).forEach((id) => {
        const found = findExamById(id);
        if (found) forbiddenSets.push(new Set([...found.mcqIds, ...found.tfIds, ...found.saIds]));
      });
    }

    const isAllowed = (qid) => {
      for (const s of forbiddenSets) {
        if (s.has(qid)) return false;
      }
      return true;
    };

    const pickFromPool = (pool, count, alreadyPickedSet) => {
      const shuffled = [...pool].sort(() => Math.random() - 0.5);
      const preferred = shuffled.filter((q) => !alreadyPickedSet.has(q.id) && isAllowed(q.id));
      const fallback = shuffled.filter((q) => !alreadyPickedSet.has(q.id));
      const out = [];
      for (const q of preferred) {
        if (out.length >= count) break;
        out.push(q);
        alreadyPickedSet.add(q.id);
      }
      for (const q of fallback) {
        if (out.length >= count) break;
        out.push(q);
        alreadyPickedSet.add(q.id);
      }
      return out;
    };

    const usedSet = new Set();
    const mcqsAll = Array.from(mcqMap.values());
    const tfsAll = Array.from(tfMap.values());
    const sasAll = Array.from(saMap.values());

    let pickedMcqs = [];
    let pickedTfs = [];
    let pickedSas = [];

    if (focusTopic === "balanced") {
      // Balanced 7 basic, 7 adv, 6 hsg across all 6 topics
      const bPool = pickFromPool(mcqsAll.filter((q) => q.level === "basic"), 7, usedSet);
      const aPool = pickFromPool(mcqsAll.filter((q) => q.level === "adv"), 7, usedSet);
      const hPool = pickFromPool(mcqsAll.filter((q) => q.level === "hsg"), 6, usedSet);
      pickedMcqs = [...bPool, ...aPool, ...hPool];
      pickedTfs = pickFromPool(tfsAll, 2, usedSet);
      pickedSas = pickFromPool(sasAll, 2, usedSet);
    } else {
      // 10 MCQs from focusTopic + 10 MCQs from others, preserving 7 basic / 7 adv / 6 hsg
      const fBasic = pickFromPool(mcqsAll.filter((q) => q.topic === focusTopic && q.level === "basic"), 3, usedSet);
      const fAdv = pickFromPool(mcqsAll.filter((q) => q.topic === focusTopic && q.level === "adv"), 4, usedSet);
      const fHsg = pickFromPool(mcqsAll.filter((q) => q.topic === focusTopic && q.level === "hsg"), 3, usedSet);
      const oBasic = pickFromPool(mcqsAll.filter((q) => q.topic !== focusTopic && q.level === "basic"), 4, usedSet);
      const oAdv = pickFromPool(mcqsAll.filter((q) => q.topic !== focusTopic && q.level === "adv"), 3, usedSet);
      const oHsg = pickFromPool(mcqsAll.filter((q) => q.topic !== focusTopic && q.level === "hsg"), 3, usedSet);
      pickedMcqs = [...fBasic, ...oBasic, ...fAdv, ...oAdv, ...fHsg, ...oHsg];

      const tfFocus = pickFromPool(tfsAll.filter((q) => q.topic === focusTopic), 1, usedSet);
      const tfOther = pickFromPool(tfsAll.filter((q) => q.topic !== focusTopic), 1, usedSet);
      pickedTfs = [...tfFocus, ...tfOther];

      const saFocus = pickFromPool(sasAll.filter((q) => q.topic === focusTopic), 1, usedSet);
      const saOther = pickFromPool(sasAll.filter((q) => q.topic !== focusTopic), 1, usedSet);
      pickedSas = [...saFocus, ...saOther];
    }

    const lvlRank = { basic: 0, adv: 1, hsg: 2 };
    pickedMcqs.sort((x, y) => lvlRank[x.level] - lvlRank[y.level]);

    const newNum = store.customExams.length + 1;
    const examId = `CUSTOM-${String(newNum).padStart(2, "0")}`;
    const newIds = new Set([...pickedMcqs, ...pickedTfs, ...pickedSas].map((x) => x.id));

    let maxOv = 0;
    forbiddenSets.forEach((fs) => {
      let c = 0;
      newIds.forEach((id) => {
        if (fs.has(id)) c++;
      });
      if (c > maxOv) maxOv = c;
    });
    const ovPct = ((maxOv / 24) * 100).toFixed(2);
    const focusName = focusTopic === "balanced" ? "Tổng hợp 6 chuyên đề" : TOPICS[focusTopic]?.short || focusTopic;

    const customExam = {
      id: examId,
      num: newNum,
      isCustom: true,
      title: `Đề Tự Sinh #${String(newNum).padStart(2, "0")} — ${focusName}`,
      subtitle: "Đề sinh ngẫu nhiên 60 phút kiểm soát trùng lặp ≤ 5%",
      overlapNote: `Trùng tối đa nhóm loại trừ: ${ovPct}%`,
      durationMin: 60,
      totalQuestions: 24,
      maxScore: 10.0,
      mcqIds: pickedMcqs.map((q) => q.id),
      tfIds: pickedTfs.map((q) => q.id),
      saIds: pickedSas.map((q) => q.id),
      levelCounts: {
        basic: pickedMcqs.filter((q) => q.level === "basic").length,
        adv: pickedMcqs.filter((q) => q.level === "adv").length,
        hsg: pickedMcqs.filter((q) => q.level === "hsg").length,
      },
      part2Topics: pickedTfs.map((q) => q.topic),
      part3Topics: pickedSas.map((q) => q.topic),
    };

    store.customExams.unshift(customExam);
    saveStore();
    startNewExam(customExam.id);
  }

  // ==================== TAB 2: 60-MINUTE EXAM RUNNER ====================
  function stopTimer() {
    if (timerHandle) {
      clearInterval(timerHandle);
      timerHandle = null;
    }
  }

  function startTimer() {
    stopTimer();
    timerHandle = setInterval(() => {
      if (!activeExam || activeSubmittedResult) {
        stopTimer();
        return;
      }
      activeRemainingSec = Math.max(0, activeRemainingSec - 1);
      updateTimerDisplay();

      if (activeRemainingSec % 5 === 0) {
        persistCurrentDraft();
      }
      if (activeRemainingSec === 0) {
        stopTimer();
        submitActiveExam(true);
      }
    }, 1000);
  }

  function updateTimerDisplay() {
    const box = document.getElementById("runnerTimerBox");
    const txt = document.getElementById("runnerTimerText");
    if (!box || !txt) return;
    txt.textContent = formatMMSS(activeRemainingSec);
    box.classList.remove("timer-danger", "bg-amber-50", "border-amber-300", "text-amber-900", "bg-emerald-50", "border-emerald-300", "text-emerald-900");
    if (activeSubmittedResult) {
      box.classList.add("bg-slate-100", "border-slate-300", "text-slate-700");
    } else if (activeRemainingSec <= 180) {
      box.classList.add("timer-danger");
    } else if (activeRemainingSec <= 600) {
      box.classList.add("bg-amber-50", "border-amber-300", "text-amber-900");
    } else {
      box.classList.add("bg-emerald-50", "border-emerald-300", "text-emerald-900");
    }
  }

  function persistCurrentDraft() {
    if (!activeExam || activeSubmittedResult) return;
    store.drafts[activeExam.id] = {
      answers: JSON.parse(JSON.stringify(activeAnswers)),
      remainingSec: activeRemainingSec,
      updatedAt: Date.now(),
    };
    saveStore();
  }

  function startNewExam(examId) {
    const ex = findExamById(examId);
    if (!ex) return;
    delete store.completed[examId];
    delete store.drafts[examId];
    activeExam = ex;
    activeAnswers = createEmptyAnswers();
    activeRemainingSec = EXAM_DURATION_SEC;
    activeSubmittedResult = null;
    reviewFilter = "all";
    persistCurrentDraft();
    switchTab("runner");
    startTimer();
  }

  function resumeDraftExam(examId) {
    const ex = findExamById(examId);
    const draft = store.drafts[examId];
    if (!ex) return;
    activeExam = ex;
    activeAnswers = draft && draft.answers ? JSON.parse(JSON.stringify(draft.answers)) : createEmptyAnswers();
    activeRemainingSec = draft && typeof draft.remainingSec === "number" ? draft.remainingSec : EXAM_DURATION_SEC;
    activeSubmittedResult = null;
    reviewFilter = "all";
    switchTab("runner");
    startTimer();
  }

  function openCompletedReview(examId) {
    const ex = findExamById(examId);
    const comp = store.completed[examId];
    if (!ex || !comp) return;
    stopTimer();
    activeExam = ex;
    activeAnswers = JSON.parse(JSON.stringify(comp.answers || createEmptyAnswers()));
    activeRemainingSec = Math.max(0, EXAM_DURATION_SEC - (comp.usedSec || 0));
    activeSubmittedResult = comp;
    reviewFilter = "all";
    switchTab("runner");
  }

  function checkSaAnswer(q, rawInput) {
    const trimmed = String(rawInput || "").trim();
    if (!trimmed) return false;
    const norm = trimmed.replace(/\s+/g, "").replace(/,/g, ".").replace(/%$/, "");
    const acceptedNorms = (q.accepted || []).map((x) => String(x).trim().replace(/\s+/g, "").replace(/,/g, ".").replace(/%$/, "").toLowerCase());
    if (acceptedNorms.includes(norm.toLowerCase())) return true;
    if (typeof q.numericValue === "number" && Number.isFinite(q.numericValue)) {
      const parsed = Number(norm);
      if (Number.isFinite(parsed)) {
        const tol = Math.max(q.tolerance || 0, 1e-6);
        return Math.abs(parsed - q.numericValue) <= tol;
      }
    }
    return false;
  }

  function submitActiveExam(isAuto = false) {
    if (!activeExam) return;
    if (!isAuto) {
      const ansCnt = countAnswered(activeAnswers, activeExam);
      if (ansCnt < 24 && !confirm(`Bạn mới hoàn thành ${ansCnt}/24 câu hỏi. Bạn có chắc chắn muốn nộp bài ngay không?`)) {
        return;
      }
    }
    stopTimer();

    // Grade Part I (20 MCQs * 0.25 = 5.00)
    let p1 = 0;
    const mcqScores = {};
    const topicPerf = {};
    TOPIC_KEYS.forEach((t) => {
      topicPerf[t] = { earned: 0, max: 0 };
    });

    activeExam.mcqIds.forEach((qid) => {
      const q = mcqMap.get(qid);
      if (!q) return;
      const userIdx = activeAnswers.mcq[qid];
      const ok = userIdx === q.ans;
      const pts = ok ? 0.25 : 0;
      p1 += pts;
      mcqScores[qid] = { ok, pts };
      if (topicPerf[q.topic]) {
        topicPerf[q.topic].earned += pts;
        topicPerf[q.topic].max += 0.25;
      }
    });

    // Grade Part II (2 TF * 1.00 = 2.00; 2025 scale: 1=0.10, 2=0.25, 3=0.50, 4=1.00)
    const TF_SCALE = [0, 0.1, 0.25, 0.5, 1.0];
    let p2 = 0;
    const tfScores = {};
    activeExam.tfIds.forEach((qid) => {
      const q = tfMap.get(qid);
      if (!q) return;
      const userObj = activeAnswers.tf[qid] || {};
      let rightCount = 0;
      const stmtCorrect = {};
      q.statements.forEach((st) => {
        const isRight = userObj[st.key] === st.ans;
        stmtCorrect[st.key] = isRight;
        if (isRight) rightCount++;
      });
      const pts = TF_SCALE[rightCount];
      p2 += pts;
      tfScores[qid] = { rightCount, pts, stmtCorrect };
      if (topicPerf[q.topic]) {
        topicPerf[q.topic].earned += pts;
        topicPerf[q.topic].max += 1.0;
      }
    });

    // Grade Part III (2 SA * 1.50 = 3.00)
    let p3 = 0;
    const saScores = {};
    activeExam.saIds.forEach((qid) => {
      const q = saMap.get(qid);
      if (!q) return;
      const ok = checkSaAnswer(q, activeAnswers.sa[qid]);
      const pts = ok ? 1.5 : 0;
      p3 += pts;
      saScores[qid] = { ok, pts };
      if (topicPerf[q.topic]) {
        topicPerf[q.topic].earned += pts;
        topicPerf[q.topic].max += 1.5;
      }
    });

    const totalScore = Math.round((p1 + p2 + p3) * 100) / 100;
    const usedSec = Math.max(1, EXAM_DURATION_SEC - activeRemainingSec);

    const result = {
      score: totalScore,
      p1: Math.round(p1 * 100) / 100,
      p2: Math.round(p2 * 100) / 100,
      p3: Math.round(p3 * 100) / 100,
      usedSec,
      mcqScores,
      tfScores,
      saScores,
      topicPerf,
      answers: JSON.parse(JSON.stringify(activeAnswers)),
      timestamp: Date.now(),
      autoSubmitted: isAuto,
    };

    activeSubmittedResult = result;
    delete store.drafts[activeExam.id];
    store.completed[activeExam.id] = result;
    saveStore();
    renderRunnerShell();
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  function countAnswered(ansObj, ex) {
    if (!ansObj || !ex) return 0;
    let c = 0;
    ex.mcqIds.forEach((id) => {
      if (typeof ansObj.mcq?.[id] === "number") c++;
    });
    ex.tfIds.forEach((id) => {
      const sub = ansObj.tf?.[id] || {};
      if (["a", "b", "c", "d"].every((k) => typeof sub[k] === "boolean")) c++;
    });
    ex.saIds.forEach((id) => {
      if (String(ansObj.sa?.[id] || "").trim().length > 0) c++;
    });
    return c;
  }

  function renderRunnerShell() {
    const emptyEl = document.getElementById("runnerEmptyState");
    const activeEl = document.getElementById("runnerActiveContainer");
    if (!emptyEl || !activeEl) return;

    if (!activeExam) {
      emptyEl.classList.remove("hidden");
      activeEl.classList.add("hidden");
      return;
    }

    emptyEl.classList.add("hidden");
    activeEl.classList.remove("hidden");

    document.getElementById("runnerExamBadge").textContent = activeExam.id;
    document.getElementById("runnerExamTitle").textContent = activeExam.title;
    document.getElementById("runnerExamMeta").textContent = activeExam.subtitle || "20 Trắc nghiệm + 2 Đúng/Sai + 2 Trả lời ngắn • Thời gian 60 phút";
    document.getElementById("runnerAnsweredCount").textContent = String(countAnswered(activeAnswers, activeExam));
    updateTimerDisplay();

    const submitBtn = document.getElementById("btnSubmitExam");
    const resultPanel = document.getElementById("runnerResultPanel");
    if (activeSubmittedResult) {
      submitBtn.classList.add("hidden");
      resultPanel.classList.remove("hidden");
      renderResultSummary(activeSubmittedResult);
    } else {
      submitBtn.classList.remove("hidden");
      resultPanel.classList.add("hidden");
    }

    renderPalettes();
    renderRunnerQuestions();
  }

  function renderResultSummary(res) {
    document.getElementById("resTotalScore").textContent = res.score.toFixed(2);
    document.getElementById("resPart1Score").textContent = `${res.p1.toFixed(2)} / 5.00`;
    document.getElementById("resPart2Score").textContent = `${res.p2.toFixed(2)} / 2.00`;
    document.getElementById("resPart3Score").textContent = `${res.p3.toFixed(2)} / 3.00`;
    const mins = Math.floor(res.usedSec / 60);
    const secs = res.usedSec % 60;
    document.getElementById("resTimeUsed").textContent = `Thời gian làm bài: ${mins} phút ${secs} giây${res.autoSubmitted ? " (Tự động nộp khi hết 60 phút)" : ""}`;

    const breakdownEl = document.getElementById("resTopicBreakdown");
    breakdownEl.innerHTML = TOPIC_KEYS.map((t) => {
      const info = TOPICS[t];
      const st = res.topicPerf?.[t] || { earned: 0, max: 0 };
      const pct = st.max > 0 ? Math.round((st.earned / st.max) * 100) : 0;
      return `
        <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 text-xs">
          <div class="font-bold text-slate-800 truncate">${info.icon} ${escapeHtml(info.short)}</div>
          <div class="text-[11px] text-slate-600 mt-0.5">${st.earned.toFixed(2)} / ${st.max.toFixed(2)}đ (${pct}%)</div>
          <div class="w-full h-1.5 bg-slate-200 rounded-full mt-1.5 overflow-hidden">
            <div class="h-full ${pct >= 75 ? "bg-emerald-500" : pct >= 50 ? "bg-amber-500" : "bg-rose-500"}" style="width:${pct}%"></div>
          </div>
        </div>`;
    }).join("");
  }

  function renderPalettes() {
    const p1El = document.getElementById("palettePart1");
    const p2El = document.getElementById("palettePart2");
    const p3El = document.getElementById("palettePart3");

    p1El.innerHTML = activeExam.mcqIds
      .map((qid, i) => {
        let cls = "";
        if (activeSubmittedResult) {
          cls = activeSubmittedResult.mcqScores?.[qid]?.ok ? "review-ok" : "review-bad";
        } else if (typeof activeAnswers.mcq[qid] === "number") {
          cls = "answered";
        }
        return `<button type="button" data-jump-q="exam-q-${i + 1}" class="q-pill ${cls}">${i + 1}</button>`;
      })
      .join("");

    p2El.innerHTML = activeExam.tfIds
      .map((qid, i) => {
        const qNum = 21 + i;
        let cls = "";
        if (activeSubmittedResult) {
          const r = activeSubmittedResult.tfScores?.[qid]?.rightCount || 0;
          cls = r === 4 ? "review-ok" : r > 0 ? "partial" : "review-bad";
        } else {
          const sub = activeAnswers.tf[qid] || {};
          const doneCnt = ["a", "b", "c", "d"].filter((k) => typeof sub[k] === "boolean").length;
          if (doneCnt === 4) cls = "answered";
          else if (doneCnt > 0) cls = "partial";
        }
        return `<button type="button" data-jump-q="exam-q-${qNum}" class="q-pill ${cls} w-auto px-3">Câu ${i + 1}</button>`;
      })
      .join("");

    p3El.innerHTML = activeExam.saIds
      .map((qid, i) => {
        const qNum = 23 + i;
        let cls = "";
        if (activeSubmittedResult) {
          cls = activeSubmittedResult.saScores?.[qid]?.ok ? "review-ok" : "review-bad";
        } else if (String(activeAnswers.sa[qid] || "").trim().length > 0) {
          cls = "answered";
        }
        return `<button type="button" data-jump-q="exam-q-${qNum}" class="q-pill ${cls} w-auto px-3">Câu ${i + 1}</button>`;
      })
      .join("");
  }

  function renderRunnerQuestions() {
    const host = document.getElementById("runnerQuestionsContainer");
    if (!host) return;
    const isReview = Boolean(activeSubmittedResult);
    const optLetters = ["A", "B", "C", "D"];

    const partsHtml = [];

    // PART I HEADER + 20 MCQs
    partsHtml.push(`
      <div class="bg-emerald-900 text-white rounded-2xl px-5 py-3.5 shadow-sm flex items-center justify-between flex-wrap gap-2">
        <div>
          <h3 class="font-extrabold text-sm sm:text-base uppercase tracking-wide">Phần I. Câu Trắc Nghiệm Nhiều Phương Án Lựa Chọn (20 câu — 5.00 điểm)</h3>
          <p class="text-xs text-emerald-100">Thí sinh trả lời từ câu 1 đến câu 20. Mỗi câu chỉ chọn 1 phương án đúng nhất (0.25đ/câu).</p>
        </div>
      </div>`);

    activeExam.mcqIds.forEach((qid, idx) => {
      const q = mcqMap.get(qid);
      if (!q) return;
      const num = idx + 1;
      const userChoice = activeAnswers.mcq[qid];
      const sc = isReview ? activeSubmittedResult.mcqScores?.[qid] : null;
      if (isReview && reviewFilter === "wrong" && sc?.ok) return;

      const optsHtml = q.opts
        .map((optText, oIdx) => {
          let extraCls = userChoice === oIdx ? "selected" : "";
          if (isReview) {
            if (oIdx === q.ans) extraCls = "correct-ans";
            else if (userChoice === oIdx && userChoice !== q.ans) extraCls = "wrong-ans";
          }
          return `
            <label class="opt-label ${extraCls}" data-mcq-qid="${qid}" data-opt-idx="${oIdx}">
              <input type="radio" name="mcq-${qid}" value="${oIdx}" class="mt-1 accent-emerald-600" ${userChoice === oIdx ? "checked" : ""} ${isReview ? "disabled" : ""} />
              <div class="text-sm text-slate-800 flex-1">
                <strong class="mr-1.5">${optLetters[oIdx]}.</strong>${optText}
              </div>
            </label>`;
        })
        .join("");

      partsHtml.push(`
        <div id="exam-q-${num}" class="content-card p-4 sm:p-5 space-y-3 ${isReview ? (sc?.ok ? "border-emerald-300" : "border-rose-300") : ""}">
          <div class="flex flex-wrap items-center justify-between gap-2">
            <div class="flex items-center gap-2 flex-wrap">
              <span class="px-2.5 py-1 rounded-lg text-xs font-extrabold bg-slate-900 text-white">Câu ${num}</span>
              ${topicBadgeHtml(q.topic)}
              ${levelBadgeHtml(q.level)}
              <span class="text-xs font-semibold text-slate-500">${escapeHtml(q.subtopic || "")}</span>
            </div>
            ${isReview ? `<span class="text-xs font-extrabold px-2.5 py-1 rounded-full ${sc?.ok ? "bg-emerald-100 text-emerald-800" : "bg-rose-100 text-rose-800"}">${sc?.ok ? "✔ Đúng (+0.25đ)" : "✘ Sai (0.00đ)"}</span>` : ""}
          </div>
          <div class="text-sm sm:text-[15px] font-semibold text-slate-900 leading-relaxed">${q.q}</div>
          <div class="grid grid-cols-1 gap-2">${optsHtml}</div>
          ${isReview ? `
            <div class="mt-3 p-3.5 rounded-xl bg-emerald-50/70 border border-emerald-200 text-xs sm:text-sm text-slate-800 space-y-1">
              <div class="font-extrabold text-emerald-900">💡 Đáp án đúng: ${optLetters[q.ans]}</div>
              <div>${q.exp}</div>
            </div>` : ""}
        </div>`);
    });

    // PART II HEADER + 2 TRUE/FALSE
    partsHtml.push(`
      <div class="bg-teal-900 text-white rounded-2xl px-5 py-3.5 shadow-sm">
        <h3 class="font-extrabold text-sm sm:text-base uppercase tracking-wide">Phần II. Câu Trắc Nghiệm Đúng / Sai (2 câu — 2.00 điểm)</h3>
        <p class="text-xs text-teal-100">Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn Đúng hoặc Sai (Đúng 1 ý: 0.10đ · 2 ý: 0.25đ · 3 ý: 0.50đ · 4 ý: 1.00đ).</p>
      </div>`);

    activeExam.tfIds.forEach((qid, idx) => {
      const q = tfMap.get(qid);
      if (!q) return;
      const num = 21 + idx;
      const userObj = activeAnswers.tf[qid] || {};
      const sc = isReview ? activeSubmittedResult.tfScores?.[qid] : null;
      if (isReview && reviewFilter === "wrong" && sc?.rightCount === 4) return;

      const stmtsHtml = q.statements
        .map((st) => {
          const val = userObj[st.key];
          const ok = sc?.stmtCorrect?.[st.key];
          const trueCls = val === true ? "active-true" : "";
          const falseCls = val === false ? "active-false" : "";
          return `
            <div class="p-3 rounded-xl border ${isReview ? (ok ? "border-emerald-300 bg-emerald-50/40" : "border-rose-300 bg-rose-50/40") : "border-slate-200 bg-slate-50/60"} space-y-2">
              <div class="flex flex-col sm:flex-row sm:items-start justify-between gap-3">
                <div class="text-sm text-slate-800 flex-1">
                  <strong class="text-teal-800 mr-1">${st.key})</strong> ${st.text}
                </div>
                <div class="flex items-center gap-1.5 shrink-0">
                  <button type="button" data-tf-qid="${qid}" data-tf-key="${st.key}" data-tf-val="true" class="tf-btn ${trueCls}" ${isReview ? "disabled" : ""}>Đúng</button>
                  <button type="button" data-tf-qid="${qid}" data-tf-key="${st.key}" data-tf-val="false" class="tf-btn ${falseCls}" ${isReview ? "disabled" : ""}>Sai</button>
                </div>
              </div>
              ${isReview ? `
                <div class="text-xs pt-1.5 border-t ${ok ? "border-emerald-200 text-emerald-900" : "border-rose-200 text-rose-900"}">
                  <strong>${ok ? "✔ Chính xác" : "✘ Chưa đúng"} · Đáp án chuẩn: ${st.ans ? "ĐÚNG" : "SAI"}.</strong> ${st.exp}
                </div>` : ""}
            </div>`;
        })
        .join("");

      partsHtml.push(`
        <div id="exam-q-${num}" class="content-card p-4 sm:p-5 space-y-3">
          <div class="flex flex-wrap items-center justify-between gap-2">
            <div class="flex items-center gap-2 flex-wrap">
              <span class="px-2.5 py-1 rounded-lg text-xs font-extrabold bg-teal-800 text-white">Phần II · Câu ${idx + 1}</span>
              ${topicBadgeHtml(q.topic)}
              ${levelBadgeHtml(q.level)}
              <span class="text-xs font-semibold text-slate-500">${escapeHtml(q.subtopic || "")}</span>
            </div>
            ${isReview ? `<span class="text-xs font-extrabold px-2.5 py-1 rounded-full ${sc?.rightCount === 4 ? "bg-emerald-100 text-emerald-800" : "bg-amber-100 text-amber-900"}">Đúng ${sc?.rightCount}/4 ý (+${(sc?.pts || 0).toFixed(2)}đ)</span>` : ""}
          </div>
          <div class="text-sm sm:text-[15px] font-semibold text-slate-900 leading-relaxed">${q.stem}</div>
          <div class="space-y-2.5">${stmtsHtml}</div>
        </div>`);
    });

    // PART III HEADER + 2 SHORT ANSWER
    partsHtml.push(`
      <div class="bg-amber-800 text-white rounded-2xl px-5 py-3.5 shadow-sm">
        <h3 class="font-extrabold text-sm sm:text-base uppercase tracking-wide">Phần III. Câu Trắc Nghiệm Trả Lời Ngắn (2 câu — 3.00 điểm)</h3>
        <p class="text-xs text-amber-100">Thí sinh điền giá trị số (dùng dấu chấm "." hoặc dấu phẩy "," đều được hệ thống chấp nhận). Mỗi câu đúng đạt 1.50 điểm.</p>
      </div>`);

    activeExam.saIds.forEach((qid, idx) => {
      const q = saMap.get(qid);
      if (!q) return;
      const num = 23 + idx;
      const userVal = activeAnswers.sa[qid] || "";
      const sc = isReview ? activeSubmittedResult.saScores?.[qid] : null;
      if (isReview && reviewFilter === "wrong" && sc?.ok) return;

      partsHtml.push(`
        <div id="exam-q-${num}" class="content-card p-4 sm:p-5 space-y-3 ${isReview ? (sc?.ok ? "border-emerald-300" : "border-rose-300") : ""}">
          <div class="flex flex-wrap items-center justify-between gap-2">
            <div class="flex items-center gap-2 flex-wrap">
              <span class="px-2.5 py-1 rounded-lg text-xs font-extrabold bg-amber-700 text-white">Phần III · Câu ${idx + 1}</span>
              ${topicBadgeHtml(q.topic)}
              ${levelBadgeHtml(q.level)}
              <span class="text-xs font-semibold text-slate-500">${escapeHtml(q.subtopic || "")}</span>
            </div>
            ${isReview ? `<span class="text-xs font-extrabold px-2.5 py-1 rounded-full ${sc?.ok ? "bg-emerald-100 text-emerald-800" : "bg-rose-100 text-rose-800"}">${sc?.ok ? "✔ Chính xác (+1.50đ)" : "✘ Sai (0.00đ)"}</span>` : ""}
          </div>
          <div class="text-sm sm:text-[15px] font-semibold text-slate-900 leading-relaxed">${q.q}</div>
          <div class="bg-slate-50 p-3.5 rounded-xl border border-slate-200 space-y-1.5">
            <label class="block text-xs font-bold text-slate-700">Đáp án của bạn <span class="font-normal text-slate-500">(${escapeHtml(q.unitHint || "")})</span>:</label>
            <input type="text" data-sa-qid="${qid}" value="${escapeHtml(userVal)}" ${isReview ? "disabled" : ""} placeholder="Nhập đáp án số..." class="w-full sm:w-72 px-3.5 py-2 rounded-lg border border-slate-300 font-mono text-sm font-bold text-slate-900 bg-white focus:outline-none focus:border-amber-600" />
          </div>
          ${isReview ? `
            <div class="mt-2 p-3.5 rounded-xl bg-amber-50/80 border border-amber-200 text-xs sm:text-sm text-slate-800 space-y-1">
              <div class="font-extrabold text-amber-900">💡 Đáp án chuẩn: <span class="font-mono bg-white px-2 py-0.5 rounded border border-amber-300">${escapeHtml(q.answer)}</span></div>
              <div>${q.exp}</div>
            </div>` : ""}
        </div>`);
    });

    if (!isReview) {
      partsHtml.push(`
        <div class="flex justify-center pt-3 pb-6">
          <button type="button" id="btnSubmitExamBottom" class="px-8 py-3.5 rounded-2xl bg-gradient-to-r from-emerald-600 to-teal-700 hover:from-emerald-700 hover:to-teal-800 text-white font-extrabold text-base shadow-lg transition cursor-pointer">
            ✅ Hoàn Thành & Nộp Bài (24 Câu)
          </button>
        </div>`);
    }

    host.innerHTML = partsHtml.join("");
    typesetMath(host);
  }

  // ==================== TAB 3: QUESTION BANK (1,080 QUESTIONS) ====================
  function initBankExamSelect() {
    const sel = document.getElementById("bankExamFilter");
    if (!sel) return;
    const opts = ['<option value="all">Tất cả 45 đề gốc</option>'];
    FIXED_EXAMS.forEach((ex) => {
      opts.push(`<option value="${ex.id}">${escapeHtml(ex.id)} (Đề ${ex.num})</option>`);
    });
    sel.innerHTML = opts.join("");
  }

  function renderBankView() {
    const host = document.getElementById("bankListContainer");
    const pagEl = document.getElementById("bankPagination");
    const countEl = document.getElementById("bankMatchCount");
    if (!host) return;

    const kw = (document.getElementById("bankSearchInput")?.value || "").trim().toLowerCase();
    const kindF = document.getElementById("bankKindFilter")?.value || "all";
    const topicF = document.getElementById("bankTopicFilter")?.value || "all";
    const levelF = document.getElementById("bankLevelFilter")?.value || "all";
    const examF = document.getElementById("bankExamFilter")?.value || "all";

    const filtered = allQuestions.filter((entry) => {
      const q = entry.data;
      if (kindF !== "all" && entry.kind !== kindF) return false;
      if (topicF !== "all" && q.topic !== topicF) return false;
      if (levelF !== "all" && q.level !== levelF) return false;
      if (examF !== "all" && qToExamMap.get(q.id) !== examF) return false;
      if (kw && !entry.search.includes(kw)) return false;
      return true;
    });

    if (countEl) countEl.textContent = `${filtered.length.toLocaleString("vi-VN")} câu phù hợp`;

    const totalPages = Math.max(1, Math.ceil(filtered.length / BANK_PAGE_SIZE));
    if (bankPage > totalPages) bankPage = 1;
    const start = (bankPage - 1) * BANK_PAGE_SIZE;
    const slice = filtered.slice(start, start + BANK_PAGE_SIZE);

    if (slice.length === 0) {
      host.innerHTML = `<div class="bg-white border border-slate-200 rounded-2xl p-8 text-center text-slate-500">Không có câu hỏi nào khớp điều kiện lọc.</div>`;
      if (pagEl) pagEl.innerHTML = "";
      return;
    }

    const optLetters = ["A", "B", "C", "D"];
    host.innerHTML = slice
      .map((entry) => {
        const q = entry.data;
        const exId = qToExamMap.get(q.id) || "Ngẫu nhiên";
        const kindBadge =
          entry.kind === "MCQ"
            ? '<span class="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-700 text-white">Trắc nghiệm</span>'
            : entry.kind === "TF"
              ? '<span class="px-2 py-0.5 rounded text-[11px] font-bold bg-teal-700 text-white">Đúng / Sai</span>'
              : '<span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-700 text-white">Trả lời ngắn</span>';

        let bodyHtml = "";
        let solHtml = "";
        if (entry.kind === "MCQ") {
          bodyHtml = `<div class="text-sm font-semibold text-slate-900">${q.q}</div>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-1.5 text-xs text-slate-700 pt-1">
              ${q.opts.map((o, i) => `<div class="p-2 rounded-lg bg-slate-50 border border-slate-200"><strong>${optLetters[i]}.</strong> ${o}</div>`).join("")}
            </div>`;
          solHtml = `<div><strong>Đáp án đúng: ${optLetters[q.ans]}.</strong> ${q.exp}</div>`;
        } else if (entry.kind === "TF") {
          bodyHtml = `<div class="text-sm font-semibold text-slate-900">${q.stem}</div>
            <div class="space-y-1 text-xs text-slate-700 pt-1">
              ${q.statements.map((s) => `<div class="p-2 rounded-lg bg-slate-50 border border-slate-200"><strong>${s.key})</strong> ${s.text}</div>`).join("")}
            </div>`;
          solHtml = q.statements
            .map((s) => `<div class="mb-1"><strong>${s.key}) ${s.ans ? "ĐÚNG" : "SAI"}:</strong> ${s.exp}</div>`)
            .join("");
        } else {
          bodyHtml = `<div class="text-sm font-semibold text-slate-900">${q.q}</div>`;
          solHtml = `<div><strong>Đáp án chuẩn: ${escapeHtml(q.answer)}</strong><br/>${q.exp}</div>`;
        }

        return `
          <div class="content-card p-4 space-y-2.5">
            <div class="flex flex-wrap items-center justify-between gap-2">
              <div class="flex items-center gap-1.5 flex-wrap">
                ${kindBadge}
                <span class="px-2 py-0.5 rounded bg-slate-900 text-white text-[11px] font-mono font-bold">${escapeHtml(q.id)}</span>
                ${topicBadgeHtml(q.topic)}
                ${levelBadgeHtml(q.level)}
                <span class="text-xs text-slate-500 font-semibold">${escapeHtml(q.subtopic || "")}</span>
              </div>
              <span class="text-[11px] font-bold text-slate-500 bg-slate-100 px-2 py-0.5 rounded">Thuộc ${escapeHtml(exId)}</span>
            </div>
            ${bodyHtml}
            <div>
              <button type="button" data-toggle-bank-sol class="text-xs px-3 py-1.5 rounded-lg bg-slate-100 hover:bg-emerald-50 text-emerald-800 border border-slate-200 font-bold cursor-pointer">
                👁️ Xem đáp án & lời giải
              </button>
              <div class="hidden mt-2 p-3 rounded-xl bg-emerald-50/70 border border-emerald-200 text-xs sm:text-sm text-slate-800">
                ${solHtml}
              </div>
            </div>
          </div>`;
      })
      .join("");

    // Pagination buttons
    if (pagEl) {
      const btns = [];
      btns.push(`<button type="button" data-bank-page="${Math.max(1, bankPage - 1)}" class="px-3 py-1.5 rounded-lg border border-slate-300 bg-white text-xs font-bold ${bankPage === 1 ? "opacity-40 cursor-not-allowed" : "hover:bg-slate-100 cursor-pointer"}">← Trước</button>`);
      const lo = Math.max(1, bankPage - 3);
      const hi = Math.min(totalPages, bankPage + 3);
      for (let p = lo; p <= hi; p++) {
        btns.push(`<button type="button" data-bank-page="${p}" class="px-3 py-1.5 rounded-lg text-xs font-bold cursor-pointer ${p === bankPage ? "bg-emerald-600 text-white" : "border border-slate-300 bg-white hover:bg-slate-100"}">${p}</button>`);
      }
      btns.push(`<button type="button" data-bank-page="${Math.min(totalPages, bankPage + 1)}" class="px-3 py-1.5 rounded-lg border border-slate-300 bg-white text-xs font-bold ${bankPage === totalPages ? "opacity-40 cursor-not-allowed" : "hover:bg-slate-100 cursor-pointer"}">Sau →</button>`);
      btns.push(`<span class="text-xs text-slate-500 ml-2">Trang ${bankPage} / ${totalPages}</span>`);
      pagEl.innerHTML = btns.join("");
    }

    typesetMath(host);
  }

  // ==================== TAB 4: OVERLAP AUDIT DASHBOARD ====================
  function mountAuditView() {
    if (auditMounted) return;
    auditMounted = true;

    // Live verification directly on the 45 loaded exams
    const n = FIXED_EXAMS.length;
    const examSets = FIXED_EXAMS.map((ex) => new Set([...ex.mcqIds, ...ex.tfIds, ...ex.saIds]));
    let maxOvCnt = 0;
    let totalOvCnt = 0;
    let pairCount = 0;
    const perExamMax = new Array(n).fill(0);

    for (let i = 0; i < n; i++) {
      for (let j = i + 1; j < n; j++) {
        let ov = 0;
        examSets[i].forEach((id) => {
          if (examSets[j].has(id)) ov++;
        });
        pairCount++;
        totalOvCnt += ov;
        if (ov > maxOvCnt) maxOvCnt = ov;
        if (ov > perExamMax[i]) perExamMax[i] = ov;
        if (ov > perExamMax[j]) perExamMax[j] = ov;
      }
    }

    const maxPct = ((maxOvCnt / 24) * 100).toFixed(2);
    const avgPct = pairCount > 0 ? (((totalOvCnt / pairCount) / 24) * 100).toFixed(4) : "0.0000";
    const uniquePoolSize = new Set(examSets.flatMap((s) => Array.from(s))).size;

    const kpiEl = document.getElementById("auditKpiGrid");
    if (kpiEl) {
      kpiEl.innerHTML = `
        <div class="p-3.5 rounded-xl bg-emerald-50 border border-emerald-200">
          <div class="text-xs font-semibold text-emerald-700">Tổng số Đề Cố Định</div>
          <div class="text-2xl font-black text-emerald-900 mt-0.5">${n} đề (≥ 40)</div>
        </div>
        <div class="p-3.5 rounded-xl bg-teal-50 border border-teal-200">
          <div class="text-xs font-semibold text-teal-700">Câu hỏi Độc nhất Đã Dùng</div>
          <div class="text-2xl font-black text-teal-900 mt-0.5">${uniquePoolSize.toLocaleString("vi-VN")} câu</div>
        </div>
        <div class="p-3.5 rounded-xl bg-emerald-50 border border-emerald-200">
          <div class="text-xs font-semibold text-emerald-700">Trùng lặp Max (${pairCount} cặp)</div>
          <div class="text-2xl font-black text-emerald-900 mt-0.5">${maxPct}% (${maxOvCnt}/24)</div>
        </div>
        <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200">
          <div class="text-xs font-semibold text-slate-600">Trùng lặp Trung bình</div>
          <div class="text-2xl font-black text-slate-900 mt-0.5">${avgPct}%</div>
        </div>`;
    }

    const selA = document.getElementById("cmpExamA");
    const selB = document.getElementById("cmpExamB");
    if (selA && selB) {
      const opts = FIXED_EXAMS.map((ex) => `<option value="${ex.id}">${escapeHtml(ex.id)} — Đề ${ex.num}</option>`).join("");
      selA.innerHTML = opts;
      selB.innerHTML = opts;
      if (FIXED_EXAMS.length > 1) selB.selectedIndex = 1;
      updatePairComparator();
    }

    const tbody = document.getElementById("auditTableBody");
    if (tbody) {
      tbody.innerHTML = FIXED_EXAMS.map((ex, i) => {
        const lc = ex.levelCounts || {};
        const p2 = (ex.part2Topics || []).map((t) => TOPICS[t]?.short || t).join(", ");
        const p3 = (ex.part3Topics || []).map((t) => TOPICS[t]?.short || t).join(", ");
        const maxOv = perExamMax[i];
        const ovPct = ((maxOv / 24) * 100).toFixed(2);
        return `
          <tr class="hover:bg-slate-50">
            <td class="p-2.5 font-extrabold text-slate-900 whitespace-nowrap">${escapeHtml(ex.id)}</td>
            <td class="p-2.5 text-slate-700">${ex.mcqIds.length} TN · 6 chuyên đề</td>
            <td class="p-2.5 text-slate-700">${lc.basic || 7} CB · ${lc.adv || 7} NC · ${lc.hsg || 6} HSG</td>
            <td class="p-2.5 text-teal-800 font-semibold">${escapeHtml(p2)}</td>
            <td class="p-2.5 text-amber-800 font-semibold">${escapeHtml(p3)}</td>
            <td class="p-2.5 text-center">
              <span class="px-2.5 py-0.5 rounded-full font-bold ${maxOv <= 1 ? "ov-cell-0" : "bg-rose-100 text-rose-800"}">${maxOv}/24 (${ovPct}%)</span>
            </td>
          </tr>`;
      }).join("");
    }
  }

  function updatePairComparator() {
    const idA = document.getElementById("cmpExamA")?.value;
    const idB = document.getElementById("cmpExamB")?.value;
    const exA = findExamById(idA);
    const exB = findExamById(idB);
    const badge = document.getElementById("cmpResultBadge");
    const details = document.getElementById("cmpDetails");
    if (!exA || !exB || !badge || !details) return;

    const setA = new Set([...exA.mcqIds, ...exA.tfIds, ...exA.saIds]);
    const setB = new Set([...exB.mcqIds, ...exB.tfIds, ...exB.saIds]);
    const inter = [...setA].filter((id) => setB.has(id));
    const pct = ((inter.length / 24) * 100).toFixed(2);

    if (idA === idB) {
      badge.textContent = "Cùng 1 đề (100% — tự so sánh)";
      details.textContent = "Hãy chọn 2 đề khác nhau để kiểm tra tỷ lệ trùng lặp chéo.";
    } else {
      badge.textContent = `Trùng ${inter.length}/24 câu (${pct}%) — ${inter.length <= 1 ? "ĐẠT ≤ 5%" : "VƯỢT 5%"}`;
      details.textContent = inter.length === 0
        ? `Hai đề ${idA} và ${idB} hoàn toàn tách biệt về tập câu hỏi ở cả 3 phần (0 câu trùng).`
        : `Các mã câu hỏi trùng nhau: ${inter.join(", ")}`;
    }
  }

  // ==================== TAB 5: THEORY & PROVINCIAL HSG ====================
  window.toggleSolution = function (btn) {
    const sol = btn && btn.nextElementSibling;
    if (!sol) return;
    const hidden = sol.classList.toggle("hidden");
    btn.textContent = hidden ? "Xem lời giải chi tiết" : "Ẩn lời giải";
    if (!hidden) typesetMath(sol);
  };

  function mountTheoryView() {
    const host = document.getElementById("theoryContentHost");
    if (!host) return;
    if (!theoryMounted) {
      host.innerHTML = BM.THEORY_HTML || "<p class='text-slate-500'>Chưa có dữ liệu lý thuyết.</p>";
      theoryMounted = true;
      typesetMath(host);
    }
    filterTheoryCards();
  }

  function filterTheoryCards() {
    const topicF = document.getElementById("theoryTopicFilter")?.value || "all";
    const levelF = document.getElementById("theoryLevelFilter")?.value || "all";
    const kw = (document.getElementById("theorySearchInput")?.value || "").trim().toLowerCase();

    document.querySelectorAll("#theoryContentHost .content-card").forEach((card) => {
      const t = card.getAttribute("data-topic") || "";
      const l = card.getAttribute("data-level") || "";
      const txt = card.textContent.toLowerCase();
      const matchT = topicF === "all" || t === topicF;
      const matchL = levelF === "all" || l === levelF;
      const matchK = !kw || txt.includes(kw);
      card.classList.toggle("hidden", !(matchT && matchL && matchK));
    });
  }

  // ==================== EVENT DELEGATION ====================
  function bindEvents() {
    // Tab navigation
    document.getElementById("mainNav")?.addEventListener("click", (e) => {
      const btn = e.target.closest("[data-tab]");
      if (btn) switchTab(btn.getAttribute("data-tab"));
    });

    document.getElementById("btnBackToExamsEmpty")?.addEventListener("click", () => switchTab("exams"));
    document.getElementById("btnCreateCustomExam")?.addEventListener("click", createCustomExam);

    // Exams filter listeners
    ["examSearchInput", "examStatusFilter", "examPartTopicFilter"].forEach((id) => {
      document.getElementById(id)?.addEventListener("input", renderExamsView);
      document.getElementById(id)?.addEventListener("change", renderExamsView);
    });

    document.getElementById("btnResetProgress")?.addEventListener("click", () => {
      if (confirm("Xóa toàn bộ lịch sử làm bài, điểm số và nháp đang lưu trên trình duyệt?")) {
        store = defaultStore();
        saveStore();
        activeExam = null;
        stopTimer();
        renderExamsView();
      }
    });

    // Exams Grid button delegation
    document.getElementById("examsGrid")?.addEventListener("click", (e) => {
      const startBtn = e.target.closest("[data-start-exam]");
      if (startBtn) return startNewExam(startBtn.getAttribute("data-start-exam"));

      const resumeBtn = e.target.closest("[data-resume-exam]");
      if (resumeBtn) return resumeDraftExam(resumeBtn.getAttribute("data-resume-exam"));

      const reviewBtn = e.target.closest("[data-review-exam]");
      if (reviewBtn) return openCompletedReview(reviewBtn.getAttribute("data-review-exam"));

      const retakeBtn = e.target.closest("[data-retake-exam]");
      if (retakeBtn) {
        const eid = retakeBtn.getAttribute("data-retake-exam");
        if (confirm(`Bắt đầu làm lại mới hoàn toàn ${eid} với đồng hồ 60 phút?`)) {
          startNewExam(eid);
        }
      }
    });

    // Runner Header Controls
    document.getElementById("btnSubmitExam")?.addEventListener("click", () => submitActiveExam(false));
    document.getElementById("btnExitExam")?.addEventListener("click", () => {
      persistCurrentDraft();
      switchTab("exams");
    });
    document.getElementById("btnRetakeExam")?.addEventListener("click", () => {
      if (activeExam) startNewExam(activeExam.id);
    });
    document.getElementById("btnReviewAll")?.addEventListener("click", () => {
      reviewFilter = "all";
      renderRunnerQuestions();
    });
    document.getElementById("btnReviewWrong")?.addEventListener("click", () => {
      reviewFilter = "wrong";
      renderRunnerQuestions();
    });

    // Palette jump delegation
    document.getElementById("view-runner")?.addEventListener("click", (e) => {
      const jumpBtn = e.target.closest("[data-jump-q]");
      if (jumpBtn) {
        const target = document.getElementById(jumpBtn.getAttribute("data-jump-q"));
        if (target) target.scrollIntoView({ behavior: "smooth", block: "center" });
        return;
      }

      if (e.target.id === "btnSubmitExamBottom") {
        submitActiveExam(false);
        return;
      }

      // TF statement click
      const tfBtn = e.target.closest("[data-tf-qid]");
      if (tfBtn && !activeSubmittedResult) {
        const qid = tfBtn.getAttribute("data-tf-qid");
        const key = tfBtn.getAttribute("data-tf-key");
        const val = tfBtn.getAttribute("data-tf-val") === "true";
        if (!activeAnswers.tf[qid]) activeAnswers.tf[qid] = {};
        activeAnswers.tf[qid][key] = val;

        // Update sibling styling immediately without full DOM redraw (keeps scroll/MathJax smooth)
        const group = tfBtn.parentElement;
        group.querySelectorAll(".tf-btn").forEach((b) => {
          b.classList.remove("active-true", "active-false");
        });
        tfBtn.classList.add(val ? "active-true" : "active-false");

        persistCurrentDraft();
        renderPalettes();
        document.getElementById("runnerAnsweredCount").textContent = String(countAnswered(activeAnswers, activeExam));
      }
    });

    // MCQ radio change & SA text input inside runner
    document.getElementById("runnerQuestionsContainer")?.addEventListener("change", (e) => {
      if (activeSubmittedResult) return;
      const radio = e.target.closest('input[type="radio"][name^="mcq-"]');
      if (radio) {
        const qid = radio.name.replace("mcq-", "");
        const idx = Number(radio.value);
        activeAnswers.mcq[qid] = idx;

        // Highlight selected option label immediately
        const card = radio.closest(".content-card");
        if (card) {
          card.querySelectorAll(".opt-label").forEach((lbl) => {
            lbl.classList.toggle("selected", Number(lbl.getAttribute("data-opt-idx")) === idx);
          });
        }
        persistCurrentDraft();
        renderPalettes();
        document.getElementById("runnerAnsweredCount").textContent = String(countAnswered(activeAnswers, activeExam));
      }
    });

    document.getElementById("runnerQuestionsContainer")?.addEventListener("input", (e) => {
      if (activeSubmittedResult) return;
      const inp = e.target.closest("[data-sa-qid]");
      if (inp) {
        const qid = inp.getAttribute("data-sa-qid");
        activeAnswers.sa[qid] = inp.value;
        persistCurrentDraft();
        renderPalettes();
        document.getElementById("runnerAnsweredCount").textContent = String(countAnswered(activeAnswers, activeExam));
      }
    });

    // Bank filters & pagination
    ["bankSearchInput", "bankKindFilter", "bankTopicFilter", "bankLevelFilter", "bankExamFilter"].forEach((id) => {
      const ev = id === "bankSearchInput" ? "input" : "change";
      document.getElementById(id)?.addEventListener(ev, () => {
        bankPage = 1;
        renderBankView();
      });
    });

    document.getElementById("bankPagination")?.addEventListener("click", (e) => {
      const btn = e.target.closest("[data-bank-page]");
      if (btn) {
        const p = Number(btn.getAttribute("data-bank-page"));
        if (Number.isFinite(p) && p !== bankPage) {
          bankPage = p;
          renderBankView();
          window.scrollTo({ top: 0, behavior: "smooth" });
        }
      }
    });

    document.getElementById("bankListContainer")?.addEventListener("click", (e) => {
      const btn = e.target.closest("[data-toggle-bank-sol]");
      if (btn) {
        const sol = btn.nextElementSibling;
        if (!sol) return;
        const hidden = sol.classList.toggle("hidden");
        btn.textContent = hidden ? "👁️ Xem đáp án & lời giải" : "🙈 Ẩn lời giải";
        if (!hidden) typesetMath(sol);
      }
    });

    // Audit comparator
    document.getElementById("cmpExamA")?.addEventListener("change", updatePairComparator);
    document.getElementById("cmpExamB")?.addEventListener("change", updatePairComparator);

    // Theory filters & expand/collapse
    ["theoryTopicFilter", "theoryLevelFilter"].forEach((id) => {
      document.getElementById(id)?.addEventListener("change", filterTheoryCards);
    });
    document.getElementById("theorySearchInput")?.addEventListener("input", filterTheoryCards);

    document.getElementById("btnExpandAllTheory")?.addEventListener("click", () => {
      const host = document.getElementById("theoryContentHost");
      host?.querySelectorAll(".solution").forEach((s) => s.classList.remove("hidden"));
      host?.querySelectorAll('button[onclick^="toggleSolution"]').forEach((b) => (b.textContent = "Ẩn lời giải"));
      typesetMath(host);
    });

    document.getElementById("btnCollapseAllTheory")?.addEventListener("click", () => {
      const host = document.getElementById("theoryContentHost");
      host?.querySelectorAll(".solution").forEach((s) => s.classList.add("hidden"));
      host?.querySelectorAll('button[onclick^="toggleSolution"]').forEach((b) => (b.textContent = "Xem lời giải chi tiết"));
    });
  }

  // ==================== INIT ====================
  function bootstrap() {
    ingestData();
    initBankExamSelect();
    updateTopStats();
    bindEvents();
    renderExamsView();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", bootstrap);
  } else {
    bootstrap();
  }
})();
