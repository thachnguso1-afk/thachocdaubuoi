# -*- coding: utf-8 -*-
"""
Generates 90 unique Short-Answer (SA) questions (15 per topic across all 6 topics)
and writes C:\\Users\\User\\.gemini\\antigravity\\scratch\\biomaster-exam-bank\\data\\bank_sa.js.
"""
from collections import Counter
from common import make_sa, validate_question_list, write_js_module


def build_sa_bank():
    items = []
    idx = 1

    def add(topic, level, subtopic, q, answer, exp, unit_hint="Nhập kết quả dạng số (dùng dấu chấm cho phần thập phân, ví dụ: 0.25)", accepted=None, tolerance=0.0):
        nonlocal idx
        qid = f"SA-{idx:03d}"
        items.append(make_sa(qid, topic, level, subtopic, q, answer, exp, unit_hint=unit_hint, accepted=accepted, tolerance=tolerance))
        idx += 1

    # ==================== TOPIC 1: CELLBIO (SA-001 .. SA-015) ====================
    # SA-001
    add("cellbio", "basic", "Độ pH & Bào quan",
        "Trong tế bào động vật, xoang bên trong bào quan lizôxôm duy trì môi trường axit ở $pH = 5.0$ nhờ bơm proton $H^+$, trong khi tế bào chất bên ngoài giữ ở $pH = 7.0$. Nồng độ ion $H^+$ trong lizôxôm cao gấp bao nhiêu lần so với tế bào chất?",
        "100",
        "Vì $pH = -\\log_{10}[H^+]$, độ chênh $7.0 - 5.0 = 2.0$ đơn vị pH ứng với tỷ số nồng độ $[H^+]_{\\text{lyso}} / [H^+]_{\\text{bào tương}} = 10^2 = 100$ lần.",
        unit_hint="Nhập số nguyên (ví dụ: 100)")

    # SA-002
    add("cellbio", "basic", "Hô hấp Hiếu khí",
        "Một tế bào nhân thực phân giải hiếu khí hoàn toàn $3$ phân tử đường Glucose ($C_6H_{12}O_6$) qua đường phân, chu trình Krebs và chuỗi truyền điện tử (theo hiệu suất tối đa $32\\text{ ATP}$ trên mỗi phân tử Glucose nhờ hệ thống con thoi malat-aspartat). Tổng số phân tử ATP ròng thu được là bao nhiêu?",
        "96",
        "Tổng sản lượng ATP $= 3 \\times 32 = 96$ phân tử ATP.",
        unit_hint="Nhập số nguyên")

    # SA-003
    add("cellbio", "adv", "Chuỗi Chuyển hóa Hô hấp",
        "Trong chất nền và màng trong ty thể, khi oxy hóa hiếu khí hoàn toàn $4\\text{ mol}$ axit pyruvic ($C_3H_4O_3$) thành khí $CO_2$ và nước theo phương trình cân bằng $C_3H_4O_3 + 2.5 O_2 \\rightarrow 3 CO_2 + 2 H_2O$, tổng số **mol khí $O_2$** cần tiêu thụ là bao nhiêu?",
        "10",
        "Mỗi mol axit pyruvic tiêu tốn $2.5\\text{ mol } O_2$. Với $4\\text{ mol}$ axit pyruvic: $4 \\times 2.5 = 10\\text{ mol } O_2$.",
        unit_hint="Nhập số nguyên")

    # SA-004
    add("cellbio", "adv", "So sánh Hô hấp Hiếu khí & Lên men",
        "Một quần thể nấm men tiêu thụ hết đúng $1\\text{ mol}$ ($180\\text{ g}$) đường Glucose, trong đó $20\\%$ lượng glucose đi vào hô hấp hiếu khí (thu $32\\text{ ATP}$/mol glucose) và $80\\%$ lượng glucose thực hiện lên men rượu (thu $2\\text{ ATP}$/mol glucose). Tổng số **mol ATP** ròng mà quần thể nấm men thu được là bao nhiêu?",
        "8",
        "ATP từ hô hấp hiếu khí $= 0.2 \\times 32 = 6.4\\text{ mol}$; ATP từ lên men $= 0.8 \\times 2 = 1.6\\text{ mol}$. Tổng cộng $= 6.4 + 1.6 = 8.0\\text{ mol ATP}$.",
        accepted=["8", "8.0", "8,0"],
        unit_hint="Nhập số nguyên hoặc thập phân")

    # SA-005
    add("cellbio", "basic", "Sinh trưởng Vi sinh vật",
        "Cấy $500$ tế bào vi khuẩn *E. coli* đang ở pha sinh trưởng lũy thừa (thời gian thế hệ $g = 30\\text{ phút}$) vào môi trường dinh dưỡng tối ưu. Sau đúng $4\\text{ giờ}$ sinh trưởng liên tiếp không có tế bào chết, số tế bào vi khuẩn trong bình tăng lên thành bao nhiêu **nghìn tế bào**?",
        "128",
        "$4\\text{ giờ} = 240\\text{ phút} \\Rightarrow$ số lần phân chia $n = 240 / 30 = 8$. Tổng tế bào $N_t = 500 \\times 2^8 = 500 \\times 256 = 128\\,000 = 128$ nghìn tế bào.",
        unit_hint="Nhập số nguyên (đơn vị: nghìn tế bào)")

    # SA-006
    add("cellbio", "adv", "Thời gian Thế hệ Vi khuẩn",
        "Trong pha lũy thừa của nuôi cấy vi khuẩn, chỉ sau $100\\text{ phút}$ người ta ghi nhận mật độ vi khuẩn tăng từ $10^5\\text{ tế bào/ml}$ lên đến $3.2 \\times 10^6\\text{ tế bào/ml}$. Thời gian thế hệ ($g$) của chủng vi khuẩn này là bao nhiêu **phút**?",
        "20",
        "Ta có $2^n = \\frac{3.2 \\times 10^6}{10^5} = 32 = 2^5 \\Rightarrow n = 5$ lần phân chia. Vậy $g = \\frac{100}{5} = 20\\text{ phút}$.",
        unit_hint="Nhập số nguyên (đơn vị: phút)")

    # SA-007
    add("cellbio", "hsg", "Chuỗi Truyền Electron Ty thể",
        "Tại màng trong ty thể, trung bình cứ mỗi phân tử $NADH$ được oxy hóa bơm $10$ ion $H^+$ và mỗi $FADH_2$ bơm $6$ ion $H^+$ từ chất nền ra khoảng gian màng; phức hệ $ATP\\text{ synthase}$ cần $4$ ion $H^+$ đi xuôi dốc về chất nền để tổng hợp $1$ phân tử $ATP$ (kèm vận chuyển photphat). Khi oxy hóa qua chuỗi truyền điện tử hỗn hợp gồm $6\\text{ NADH}$ và $4\\text{ FADH}_2$, tổng số phân tử $ATP$ tối đa tổng hợp được là bao nhiêu?",
        "21",
        "Tổng số $H^+$ bơm ra $= 6 \\times 10 + 4 \\times 6 = 60 + 24 = 84$ ion $H^+$. Số ATP thu được $= 84 / 4 = 21\\text{ ATP}$.",
        unit_hint="Nhập số nguyên")

    # SA-008
    add("cellbio", "hsg", "Động học Enzyme (Michaelis-Menten)",
        "Một enzyme xúc tác phản ứng tuân theo phương trình Michaelis-Menten ($V_0 = \\frac{V_{\\max} \\cdot [S]}{K_m + [S]}$) có tốc độ cực đại $V_{\\max} = 120\\text{ \\mu mol/phút}$ và hằng số Michaelis $K_m = 4\\text{ mM}$. Tại nồng độ cơ chất $[S] = 12\\text{ mM}$, tốc độ phản ứng ban đầu $V_0$ đo được là bao nhiêu **$\\text{\\mu mol/phút}$**?",
        "90",
        "Thay vào công thức: $V_0 = \\frac{120 \\times 12}{4 + 12} = \\frac{1440}{16} = 90\\text{ \\mu mol/phút}$.",
        unit_hint="Nhập số nguyên")

    # SA-009
    add("cellbio", "adv", "Vận chuyển Chủ động Bơm Na+/K+",
        "Mỗi chu kỳ hoạt động của bơm $Na^+/K^+\\text{-ATPase}$ trên màng sinh chất tế bào động vật sử dụng $1$ phân tử $ATP$ để bơm $3$ ion $Na^+$ ra ngoài và $2$ ion $K^+$ vào trong tế bào. Khi bơm đẩy được $1800$ ion $Na^+$ từ trong ra ngoài tế bào, đồng thời đã có bao nhiêu ion **$K^+$** được bơm vận chuyển chủ động vào bên trong tế bào?",
        "1200",
        "Số chu kỳ hoạt động của bơm $= 1800 / 3 = 600$ chu kỳ (tiêu tốn $600\\text{ ATP}$). Ở mỗi chu kỳ đưa vào $2\\text{ K}^+$, nên tổng số ion $K^+$ được bơm vào $= 600 \\times 2 = 1200$ ion.",
        unit_hint="Nhập số nguyên")

    # SA-010
    add("cellbio", "basic", "Cấu trúc Protein Bậc 1",
        "Phân tử Hemoglobin $HbA$ trưởng thành ở người là một protein bậc 4 cấu tạo gồm $2$ chuỗi polipeptit $\\alpha$ (mỗi chuỗi dài $141$ axit amin) và $2$ chuỗi polipeptit $\\beta$ (mỗi chuỗi dài $146$ axit amin). Tổng số liên kết peptit hiện diện trong toàn bộ phân tử $HbA$ hoàn chỉnh đó là bao nhiêu?",
        "570",
        "Mỗi chuỗi có $N - 1$ liên kết peptit: tổng số liên kết $= 2 \\times (141 - 1) + 2 \\times (146 - 1) = 280 + 290 = 570$ liên kết peptit.",
        unit_hint="Nhập số nguyên")

    # SA-011
    add("cellbio", "basic", "Tỷ lệ Diện tích Bề mặt / Thể tích",
        "Xét hai tế bào mô hình dạng hình lập phương: Tế bào nhỏ A có kích thước cạnh $a = 2\\text{ \\mu m}$ và Tế bào lớn B có kích thước cạnh $b = 10\\text{ \\mu m}$. Tỷ số $\\frac{\\text{Diện tích bề mặt}}{\\text{Thể tích}}$ ($S/V$) của tế bào nhỏ A lớn gấp bao nhiêu lần so với tế bào B?",
        "5",
        "Với hình lập phương cạnh $x$: $S/V = \\frac{6x^2}{x^3} = \\frac{6}{x}$. Suy ra tỷ lệ $\\frac{(S/V)_A}{(S/V)_B} = \\frac{b}{a} = \\frac{10}{2} = 5$ lần.",
        unit_hint="Nhập số nguyên")

    # SA-012
    add("cellbio", "adv", "Sinh hóa Lipit Màng & Dự trữ",
        "Để tổng hợp sinh học hoàn chỉnh $50$ phân tử chất béo trung tính (triglixerit) và $20$ phân tử photpholipit màng sinh chất (mỗi photpholipit gồm $1$ glixerol liên kết với $2$ axit béo và $1$ đầu photphat), tế bào cần huy động tổng cộng bao nhiêu phân tử axit béo tự do?",
        "190",
        "Mỗi triglixerit cần $3$ axit béo, mỗi photpholipit cần $2$ axit béo: tổng số $= 50 \\times 3 + 20 \\times 2 = 150 + 40 = 190$ phân tử axit béo.",
        unit_hint="Nhập số nguyên")

    # SA-013
    add("cellbio", "adv", "Định lượng Lên men Etanol",
        "Quá trình lên men rượu từ $360\\text{ gam}$ đường Glucose ($M = 180\\text{ g/mol}$) theo phương trình $C_6H_{12}O_6 \\rightarrow 2 C_2H_5OH + 2 CO_2$ chỉ đạt hiệu suất thực tế bằng $75\\%$. Tổng khối lượng khí $CO_2$ ($M = 44\\text{ g/mol}$) thu được bằng bao nhiêu **gam**?",
        "132",
        "$n_{\\text{glucose}} = 360 / 180 = 2\\text{ mol} \\Rightarrow$ số mol $CO_2$ thực tế $= 2 \\times 2 \\times 75\\% = 3\\text{ mol} \\Rightarrow m_{CO_2} = 3 \\times 44 = 132\\text{ gam}$.",
        unit_hint="Nhập số nguyên (đơn vị: gam)")

    # SA-014
    add("cellbio", "hsg", "Chu trình Tan của Thể Thực khuẩn",
        "Có $10^4$ hạt phage $T_4$ ban đầu gây nhiễm đồng thời vào một lượng rất lớn tế bào vi khuẩn *E. coli* đang sinh trưởng dư thừa vật chủ ($100\\%$ hạt phage đều bám nhiễm thành công tạo tế bào chủ mới ở mỗi chu kỳ). Giả sử mỗi tế bào bị ly giải sau $30\\text{ phút}$ lại phóng thích $100$ hạt phage mới có khả năng gây nhiễm ngay tiếp. Sau đúng $60\\text{ phút}$ ($2$ chu kỳ ly giải trọn vẹn), tổng số hạt phage mới được giải phóng ở thế hệ thứ $2$ là bao nhiêu **triệu hạt**?",
        "100",
        "Sau $30\\text{ phút}$ (vòng 1): $10^4 \\times 100 = 10^6$ phage. Sau $60\\text{ phút}$ (vòng 2): $10^6 \\times 100 = 10^8 = 100$ triệu hạt phage.",
        unit_hint="Nhập số nguyên (đơn vị: triệu hạt)")

    # SA-015
    add("cellbio", "adv", "Năng lượng Pha tối Quang hợp $C_4$",
        "Ở tế bào thực vật $C_4$, chi phí để cố định mỗi $1\\text{ mmol}$ khí $CO_2$ vào chu trình quang hợp là $5\\text{ mmol ATP}$ và $2\\text{ mmol NADPH}$ (bỏ qua hô hấp sáng). Để lá cây tổng hợp ròng được $180\\text{ mg}$ đường Glucose ($C_6H_{12}O_6$, khối lượng mol $180\\text{ g/mol}$), pha tối cần tiêu tốn bao nhiêu **mmol ATP**?",
        "30",
        "$180\\text{ mg}$ Glucose tương đương $1\\text{ mmol}$ Glucose, cần cố định $6\\text{ mmol } CO_2$. Tổng lượng ATP $= 6 \\times 5 = 30\\text{ mmol ATP}$.",
        unit_hint="Nhập số nguyên (đơn vị: mmol)")

    # ==================== TOPIC 2: MOLECULAR (SA-016 .. SA-030) ====================
    # SA-016
    add("molecular", "basic", "Cấu trúc ADN & Liên kết Hiđrô",
        "Một gen có chiều dài $5100\\text{ \\AA}$ và chứa tổng cộng $3900$ liên kết hiđrô giữa hai mạch đơn. Số lượng nucleotit loại Guanin ($G$) của gen này là bao nhiêu?",
        "900",
        "Tổng nu $N = \\frac{2 \\times 5100}{3.4} = 3000$. Hệ phương trình $2A + 2G = 3000$ và $2A + 3G = 3900 \\Rightarrow G = 3900 - 3000 = 900$.",
        unit_hint="Nhập số nguyên")

    # SA-017
    add("molecular", "basic", "Mạch Đơn Bổ sung ADN",
        "Trên mạch $1$ của một đoạn gen mạch kép có số lượng từng loại nucleotit là $A_1 = 150$, $T_1 = 350$, $G_1 = 400$, $C_1 = 600$. Tổng số liên kết hiđrô của đoạn gen mạch kép này bằng bao nhiêu?",
        "4000",
        "$A = A_1 + T_1 = 150 + 350 = 500$; $G = G_1 + C_1 = 400 + 600 = 1000$. Tổng liên kết hiđrô $H = 2A + 3G = 2(500) + 3(1000) = 4000$.",
        unit_hint="Nhập số nguyên")

    # SA-018
    add("molecular", "adv", "Nhân đôi ADN & Nhu cầu Môi trường",
        "Một phân tử ADN mạch kép gồm $2400$ nucleotit, trong đó số nucleotit loại $A$ bằng $600$. Khi cho phân tử ADN này tái bản liên tiếp $4$ lần bình thường, tổng số nucleotit tự do loại Guanin ($G$) mà môi trường nội bào phải cung cấp bằng bao nhiêu?",
        "9000",
        "$G_{\\text{ban đầu}} = \\frac{2400}{2} - 600 = 600$. Sau $4$ lần nhân đôi, môi trường cung cấp $G_{\\text{mt}} = 600 \\times (2^4 - 1) = 600 \\times 15 = 9000$.",
        unit_hint="Nhập số nguyên")

    # SA-019
    add("molecular", "adv", "Đồng vị Phóng xạ Nhân đôi ADN",
        "Nuôi cấy $3$ phân tử ADN hoàn toàn mang đồng vị nitơ nặng ($^{15}N$) chuyển sang môi trường chỉ chứa hoàn toàn đồng vị nitơ nhẹ ($^{14}N$). Sau khi cho $3$ phân tử này đồng loạt nhân đôi liên tiếp $4$ lần, sẽ thu được bao nhiêu phân tử ADN chỉ chứa toàn $^{14}N$ (không mang mạch $^{15}N$ nào)?",
        "42",
        "Tổng số phân tử ADN tạo thành $= 3 \\times 2^4 = 48$. Vì luôn giữ đúng $3 \\times 2 = 6$ phân tử lai mang mạch gốc $^{15}N$, số phân tử thuần $^{14}N = 48 - 6 = 42$.",
        unit_hint="Nhập số nguyên")

    # SA-020
    add("molecular", "hsg", "Đoạn mồi ARN tại Chạc chữ Y",
        "Một phân tử ADN mạch vòng ở vi khuẩn chỉ có $1$ điểm khởi đầu tái bản tạo $2$ chạc tái bản chữ Y mở rộng ngược chiều nhau. Khi kết thúc một lần nhân đôi hoàn chỉnh, thống kê được trên mạch ra chậm ở chạc thứ $1$ có $18$ đoạn Okazaki và ở chạc thứ $2$ có $22$ đoạn Okazaki. Tổng số đoạn mồi ARN đã phải tổng hợp trong cả lần nhân đôi này là bao nhiêu?",
        "42",
        "Mỗi đoạn Okazaki cần $1$ đoạn mồi ($18 + 22 = 40$ mồi), và mỗi mạch ra sớm (liên tục) tại $2$ chạc tái bản cần thêm $1$ đoạn mồi mở đầu ($2$ mồi). Tổng $= 40 + 2 = 42$ đoạn mồi.",
        unit_hint="Nhập số nguyên")

    # SA-021
    add("molecular", "basic", "Quá trình Phiên mã",
        "Một gen dài $4080\\text{ \\AA}$ tiến hành phiên mã liên tiếp $5$ lần để tạo $5$ phân tử $mARN$. Trên mạch khuôn ($3' \\rightarrow 5'$) của gen có số lượng nucleotit từng loại là $A = 200$, $T = 300$, $G = 400$, $C = 300$. Tổng số ribonucleotit tự do loại Uracil ($U$) mà môi trường nội bào cần cung cấp là bao nhiêu?",
        "1000",
        "Theo nguyên tắc bổ sung khi phiên mã: $U_{\\text{mARN}} = A_{\\text{khuôn}} = 200$. Qua $5$ lần phiên mã, môi trường cung cấp $5 \\times 200 = 1000$ ribonucleotit loại $U$.",
        unit_hint="Nhập số nguyên")

    # SA-022
    add("molecular", "adv", "Cắt ghép Exon - Intron (Splicing)",
        "Phân tử tiền-$mARN$ của một gen nhân thực gồm $4$ đoạn Exon có chiều dài lần lượt là $120, 210, 180, 153$ nucleotit, xen kẽ bởi $3$ đoạn Intron dài $300, 450, 240$ nucleotit. Sau khi cắt bỏ toàn bộ intron và ghép nối liên tiếp $4$ exon tạo khung đọc mở hoàn chỉnh từ codon mở đầu đến codon kết thúc, chuỗi polipeptit hoàn chỉnh (sau khi cắt bỏ axit amin mở đầu) dài bao nhiêu **axit amin**?",
        "219",
        "Tổng ribonucleotit các exon $= 120 + 210 + 180 + 153 = 663$ nu $\\Rightarrow 663 / 3 = 221$ bộ ba (gồm $1$ mở đầu và $1$ kết thúc). Số axit amin chuỗi hoàn chỉnh (trừ bộ ba kết thúc và axit amin mở đầu bị cắt) $= 221 - 2 = 219$ axit amin.",
        unit_hint="Nhập số nguyên")

    # SA-023
    add("molecular", "adv", "Polysome & Liên kết Peptit",
        "Một phân tử $mARN$ trưởng thành vùng mã hóa dài $1530\\text{ \\AA}$ tham gia dịch mã đồng thời với $6$ ribosome trượt qua đúng $1$ lần tạo $6$ chuỗi polipeptit giống hệt nhau. Tính tổng số **liên kết peptit** đã được hình thành trong quá trình dịch mã tổng hợp $6$ chuỗi polipeptit sơ khai nói trên.",
        "888",
        "Số nu trên vùng mã hóa $mARN = 1530 / 3.4 = 450$ nu $= 150$ codon $\\Rightarrow$ mỗi chuỗi sơ khai có $150 - 1 = 149$ axit amin, chứa $149 - 1 = 148$ liên kết peptit. Với $6$ chuỗi: $6 \\times 148 = 888$ liên kết peptit.",
        unit_hint="Nhập số nguyên")

    # SA-024
    add("molecular", "hsg", "Xác suất Bộ ba Nhân tạo",
        "Trong thí nghiệm giải mã di truyền, người ta tổng hợp nhân tạo ngẫu nhiên một chuỗi $mARN$ từ hỗn hợp chỉ gồm hai loại đơn phân tự do là $U$ ($40\\%$) và $G$ ($60\\%$). Theo lý thuyết, tỷ lệ phần trăm (%) xuất hiện bộ ba `5'-UGG-3'` (mã hóa Tryptophan) khi đọc liên tiếp không chồng lấn trên phân tử $mARN$ đó là bao nhiêu?",
        "14.4",
        "Xác suất xuất hiện ngẫu nhiên một bộ ba độc lập `U-G-G` bằng $0.4 \\times 0.6 \\times 0.6 = 0.144 = 14.4\\%$.",
        tolerance=0.05,
        unit_hint="Nhập số phần trăm (bỏ ký hiệu %, ví dụ: 14.4)")

    # SA-025
    add("molecular", "hsg", "Đột biến Mất đoạn nhỏ trong Gen",
        "Một gen cấu trúc dài $3060\\text{ \\AA}$ bị đột biến mất một đoạn nhỏ hoàn toàn nằm bên trong vùng mã hóa (không liên quan mã mở đầu hay kết thúc), làm gen mới giảm đi $21$ liên kết hiđrô và chuỗi polipeptit tương ứng tổng hợp bị mất đi $3$ axit amin so với bình thường. Số lượng nucleotit loại Adenin ($A$) có trong đoạn gen bị mất là bao nhiêu?",
        "6",
        "Giảm $3$ axit amin $\\Rightarrow$ mất $3 \\times 3 = 9$ cặp nucleotit ($x$ cặp $A-T$ và $y$ cặp $G-C$ với $x + y = 9$). Giảm $21$ liên kết hiđrô $\\Rightarrow 2x + 3y = 21$. Giải hệ được $y = 3, x = 6$, tức mất $6$ nucleotit loại $A$.",
        unit_hint="Nhập số nguyên")

    # SA-026
    add("molecular", "basic", "Khuếch đại ADN bằng PCR",
        "Từ mẫu bệnh phẩm ban đầu chiết tách được $16$ bản sao phân tử ADN mạch kép tinh sạch, kỹ thuật viên chạy phản ứng PCR qua $n$ chu kỳ nhiệt hoàn chỉnh (giả sử hiệu suất nhân đôi lý thuyết $100\\%$ ở mọi chu kỳ) và thu được $16\\,384$ bản sao phân tử ADN đoạn đích. Số chu kỳ nhiệt $n$ đã chạy là bao nhiêu?",
        "10",
        "Ta có $16 \\times 2^n = 16\\,384 \\Rightarrow 2^n = \\frac{16\\,384}{16} = 1024 = 2^{10} \\Rightarrow n = 10$ chu kỳ.",
        unit_hint="Nhập số nguyên")

    # SA-027
    add("molecular", "adv", "Enzyme Cắt giới hạn ADN Thẳng",
        "Một phân tử ADN mạch thẳng kích thước $25\\text{ kb}$ mang $3$ vị trí cắt đặc hiệu của enzyme $EcoRI$ và $4$ vị trí cắt đặc hiệu hoàn toàn khác của enzyme $HindIII$ (không trùng vị trí với $EcoRI$). Nếu ủ phân tử ADN mạch thẳng này đồng thời với cả hai enzyme trên để cắt hoàn toàn rồi chạy điện di, tối đa thu được bao nhiêu **băng ADN rời nhau** (giả sử các đoạn đều khác kích thước)?",
        "8",
        "Trên một đoạn ADN mạch thẳng có tổng cộng $3 + 4 = 7$ điểm cắt tách biệt sẽ chia đoạn thẳng đó thành $7 + 1 = 8$ phân đoạn rời nhau.",
        unit_hint="Nhập số nguyên")

    # SA-028
    add("molecular", "adv", "Biểu sinh & Thể Barr",
        "Hiện tượng bất hoạt biểu sinh nhiễm sắc thể X đảm bảo trong mỗi tế bào sinh dưỡng bình thường chỉ duy trì đúng $1$ NST X hoạt động (các NST X dư thừa còn lại bị dị nhiễm sắc hóa nén chặt thành thể Barr). Một người có bất thường bộ NST giới tính cực hiếm là $49, XXXXY$. Trong nhân tế bào niêm mạc miệng của người này quan sát thấy bao nhiêu **thể Barr**?",
        "3",
        "Số thể Barr luôn bằng $\\text{số NST X} - 1$. Với $4$ chiếc NST X ($XXXXY$), số thể Barr bằng $4 - 1 = 3$.",
        unit_hint="Nhập số nguyên")

    # SA-029
    add("molecular", "hsg", "Điều hòa Operon Lac (F' Merozygote)",
        "Ở vi khuẩn *E. coli* lưỡng bội một phần mang kiểu gen $F'\\, lacI^+\\, lacO^c\\, lacZ^-\\, lacY^+ \\,/\\, lacI^-\\, lacO^+\\, lacZ^+\\, lacY^-$, người ta nuôi tế bào trong môi trường hoàn toàn **KHÔNG CÓ đường Lactose** (chỉ có Glucose). Có bao nhiêu loại trong $2$ loại enzyme có hoạt tính chức năng bình thường là $\\beta$-galactosidase (do $lacZ^+$ mã hóa) và Permease (do $lacY^+$ mã hóa) vẫn được tế bào tổng hợp mạnh mẽ?",
        "1",
        "Protein ức chế từ $lacI^+$ tác động *trans* khóa chặt vùng vận hành $lacO^+$ trên nhiễm sắc thể (làm tắt $lacZ^+ lacY^-$ khi không có Lactose). Ngược lại trên plasmid $F'$ có vùng $lacO^c$ đột biến không gắn được repressor nên vẫn bật thường xuyên $lacZ^-$ (mất chức năng) và $lacY^+$ (sinh **Permease** có chức năng). Do vậy chỉ có $1$ loại enzyme hoạt động được tạo thành.",
        unit_hint="Nhập số nguyên")

    # SA-030
    add("molecular", "hsg", "Tổ hợp Mã Di truyền",
        "Từ $3$ loại đơn phân ribonucleotit khác nhau là $A$, $U$ và $G$ dùng để tổng hợp các bộ ba trên $mARN$ (đọc từ $5' \\rightarrow 3'$), có thể lập được tối đa bao nhiêu **loại bộ ba** vừa chứa đủ CẢ $3$ loại ribonucleotit trên ($A, U, G$), vừa có khả năng mã hóa cho một axit amin (không phải bộ ba kết thúc)?",
        "4",
        "Tổng số hoán vị chứa cả $3$ nu khác nhau là $3! = 6$ bộ ba (`AUG`, `AGU`, `GAU`, `GUA`, `UAG`, `UGA`). Loại trừ $2$ mã kết thúc là `UAG` và `UGA`, còn lại đúng $4$ bộ ba mã hóa axit amin.",
        unit_hint="Nhập số nguyên")

    # ==================== TOPIC 3: CELLULAR (SA-031 .. SA-045) ====================
    # SA-031
    add("cellular", "basic", "Nguyên phân & Đếm NST",
        "Theo dõi $10$ tế bào xôma của cây cà chua ($2n = 24$) đồng loạt tiến hành nguyên phân bình thường. Tại thời điểm toàn bộ $10$ tế bào đang ở **kỳ sau** của nguyên phân (mỗi NST kép đã tách ở tâm động, chưa phân chia tế bào chất), tổng số NST đơn có trong cả $10$ tế bào là bao nhiêu?",
        "480",
        "Ở kỳ sau nguyên phân, mỗi tế bào chứa $4n = 48$ NST đơn. Tổng số NST trong $10$ tế bào $= 10 \\times 48 = 480$.",
        unit_hint="Nhập số nguyên")

    # SA-032
    add("cellular", "basic", "Nguyên liệu NST qua Nguyên phân",
        "Có $4$ hợp tử bình thường của cùng một loài có bộ NST $2n = 16$ đều tiến hành nguyên phân liên tiếp $5$ đợt với tốc độ ngang nhau. Tổng số NST đơn hoàn toàn mới do môi trường nội bào phải cung cấp cho toàn bộ quá trình phân bào của $4$ hợp tử là bao nhiêu?",
        "1984",
        "Áp dụng công thức $a \\times 2n \\times (2^k - 1) = 4 \\times 16 \\times (2^5 - 1) = 64 \\times 31 = 1984$ NST đơn.",
        unit_hint="Nhập số nguyên")

    # SA-033
    add("cellular", "adv", "Số loại Giao tử có Trao đổi chéo",
        "Xét một cá thể động vật đực có bộ NST $2n = 12$ ($6$ cặp NST tương đồng). Khi giảm phân bình thường, có $3$ cặp NST xảy ra trao đổi chéo tại một điểm trên mỗi cặp ở một số tế bào, $2$ cặp NST khác có cấu trúc dị hợp không có trao đổi chéo, và cặp NST còn lại đồng hợp tử hoàn toàn. Về lý thuyết, cá thể đực này tạo ra tối đa bao nhiêu loại tinh trùng khác nhau?",
        "256",
        "Mỗi cặp trao đổi chéo đơn tạo tối đa $4$ loại tổ hợp ($4^3 = 64$); $2$ cặp dị hợp không HVG tạo $2^2 = 4$; $1$ cặp đồng hợp tạo $1$. Tổng số loại $= 64 \\times 4 \\times 1 = 256$ loại.",
        unit_hint="Nhập số nguyên")

    # SA-034
    add("cellular", "adv", "Hiệu suất Thụ tinh Giao tử",
        "Ở lợn ($2n = 38$), hiệu suất thụ tinh của tinh trùng đạt $5\\%$. Để tạo được $12$ hợp tử lưỡng bội bình thường trong một lứa đẻ, số lượng **tế bào sinh tinh** tối thiểu của lợn đực đã tham gia giảm phân bình thường là bao nhiêu?",
        "60",
        "$12$ hợp tử đòi hỏi $12$ tinh trùng thụ tinh $\\Rightarrow$ tổng tinh trùng tạo ra $= 12 / 0.05 = 240$ tinh trùng. Vì $1$ tế bào sinh tinh tạo $4$ tinh trùng $\\Rightarrow$ số tế bào sinh tinh $= 240 / 4 = 60$.",
        unit_hint="Nhập số nguyên")

    # SA-035
    add("cellular", "adv", "Vật chất Di truyền Bất thụ trong Thụ tinh",
        "Tại một loài thực vật có bộ NST $2n = 14$, người ta thu được đúng $100$ hợp tử bình thường qua thụ tinh chéo. Biết hiệu suất thụ tinh của noãn (trứng) đạt $25\\%$ và hiệu suất thụ tinh của hạt phấn (tinh tử) đạt $10\\%$. Tổng số lượng nhiễm sắc thể đơn chứa trong TẤT CẢ các tế bào trứng và tinh tử KHÔNG được thụ tinh (bị thoái hóa) là bao nhiêu?",
        "8400",
        "Tổng số trứng sinh ra $= 100 / 0.25 = 400$ (thoái hóa $300$ trứng). Tổng số tinh tử $= 100 / 0.10 = 1000$ (thoái hóa $900$ tinh tử). Tổng cộng $1200$ giao tử đơn bội ($n = 7$) không thụ tinh $\\Rightarrow 1200 \\times 7 = 8400$ NST đơn.",
        unit_hint="Nhập số nguyên")

    # SA-036
    add("cellular", "hsg", "Loại Giao tử khi Rối loạn Giảm phân I",
        "Một cá thể động vật có bộ NST $2n = 8$ ($4$ cặp NST tương đồng đều có cấu trúc dị hợp và không xảy ra trao đổi chéo). Trong quá trình giảm phân tạo tinh trùng, có một tỉ lệ tế bào sinh tinh bị không phân ly cặp NST số $1$ ở lần giảm phân I (các cặp khác và GP II bình thường), phần lớn các tế bào sinh tinh còn lại giảm phân bình thường. Tổng số loại giao tử tối đa (gồm cả bình thường lẫn lệch bội $n+1, n-1$) mà cá thể đó tạo được là bao nhiêu?",
        "32",
        "Nhóm bình thường tạo $2^4 = 16$ loại giao tử ($n$). Nhóm rối loạn GP I ở cặp 1 tạo $2$ trạng thái cặp $1$ (cả hai chiếc hoặc khuyết $0$) nhân $2^3$ tổ hợp của $3$ cặp kia $= 16$ loại lệch bội ($8$ loại $n+1$ và $8$ loại $n-1$). Tổng tối đa $16 + 16 = 32$ loại.",
        unit_hint="Nhập số nguyên")

    # SA-037
    add("cellular", "basic", "Đếm Dạng Thể Lệch bội",
        "Một loài thực vật có bộ NST lưỡng bội $2n = 20$ ($10$ cặp NST tương đồng có cấu trúc hoàn toàn khác nhau). Theo lý thuyết tổ hợp, ở loài này có thể hình thành tối đa bao nhiêu dạng **thể ba kép** ($2n + 1 + 1$) phân biệt?",
        "45",
        "Mỗi thể ba kép thừa đồng thời $2$ NST ở $2$ cặp khác nhau trong tổng số $10$ cặp. Số dạng tối đa $= C_{10}^2 = \\frac{10 \\times 9}{2} = 45$ dạng.",
        unit_hint="Nhập số nguyên")

    # SA-038
    add("cellular", "hsg", "Phép lai Thể Ba ($2n+1$) có Chống Hạt phấn Lệch bội",
        "Ở cà độc dược ($2n = 24$), alen $A$ (quả có gai) trội hoàn toàn so với $a$ (quả không gai). Một cây thể ba có kiểu gen $AAa$ thực hiện tự thụ phấn ($♀ AAa \\times ♂ AAa$). Biết noãn $n$ và $n+1$ đều hữu thụ bình thường, nhưng ở giới đực hạt phấn $n+1$ hoàn toàn mất sức sống (chỉ hạt phấn $n$ thụ tinh được). Tỉ lệ phần trăm (%) cây quả KHÔNG GAI ($aa$ và $aaa$) thu được ở đời con $F_1$ là bao nhiêu? (làm tròn 2 chữ số thập phân).",
        "5.56",
        "Noãn từ $AAa$ gồm $\\frac{1}{6} AA : \\frac{2}{6} Aa : \\frac{2}{6} A : \\frac{1}{6} a$. Hạt phấn hữu thụ $n$ chỉ gồm $\\frac{2}{3} A : \\frac{1}{3} a$. Tổ hợp duy nhất tạo quả không gai là $\\frac{1}{6}a(\\text{mẹ}) \\times \\frac{1}{3}a(\\text{bố}) = \\frac{1}{18} aa \\approx 5.56\\%$.",
        tolerance=0.03,
        unit_hint="Nhập số % làm tròn 2 chữ số (ví dụ: 5.56)")

    # SA-039
    add("cellular", "hsg", "Tỉ lệ Kiểu gen Thể Tứ bội ($4n$)",
        "Ở thực vật tứ bội ($4n$), các cây giảm phân tạo giao tử $2n$ hữu thụ bình thường. Cho cây tứ bội có kiểu gen $AAaa$ tự thụ phấn thu được đời con $F_1$. Trong số các cây mang kiểu hình TRỘI ($A---$) ở $F_1$, tỉ lệ phần trăm (%) cây mang kiểu gen $AAAa$ chiếm bao nhiêu (làm tròn 2 chữ số thập phân)?",
        "22.86",
        "$AAaa$ tạo $\\frac{1}{6}AA : \\frac{4}{6}Aa : \\frac{1}{6}aa$. Tỉ lệ kiểu hình trội $A--- = 1 - \\frac{1}{36} = \\frac{35}{36}$; tỉ lệ $AAAa = 2 \\times \\frac{1}{6} \\times \\frac{4}{6} = \\frac{8}{36}$. Trong nhóm trội, $AAAa$ chiếm $\\frac{8}{35} \\approx 22.86\\%$.",
        tolerance=0.05,
        unit_hint="Nhập số % làm tròn 2 chữ số (ví dụ: 22.86)")

    # SA-040
    add("cellular", "hsg", "Tác động Cônsixin lên Hợp tử Nguyên phân",
        "Có $10$ hợp tử mang kiểu gen $Aa$ ($2n$) bước vào quá trình nguyên phân: ngay tại lần phân bào thứ $1$, hóa chất cônsixin làm ức chế hình thành thoi vô sắc ở $20\\%$ số hợp tử (tạo tế bào $4n$), các hợp tử còn lại phân chia bình thường. Sau đó rửa sạch cônsixin, tất cả các tế bào tiếp tục nguyên phân thêm $2$ lần hoàn toàn bình thường. Tỉ lệ phần trăm (%) tế bào tứ bội ($4n$) ở thế hệ cuối cùng là bao nhiêu (làm tròn 2 chữ số thập phân)?",
        "11.11",
        "Nhóm $2$ hợp tử bị đa bội hóa ở lần 1 thành $2$ tế bào $4n$, nguyên phân tiếp $2$ lần tạo $2 \\times 2^2 = 8$ tế bào $4n$. Nhóm $8$ hợp tử bình thường qua $3$ lần nguyên phân tạo $8 \\times 2^3 = 64$ tế bào $2n$. Tỷ lệ $= \\frac{8}{8 + 64} = \\frac{1}{9} \\approx 11.11\\%$.",
        tolerance=0.05,
        unit_hint="Nhập số % làm tròn 2 chữ số (ví dụ: 11.11)")

    # SA-041
    add("cellular", "basic", "Thể Song Nhị bội (Dị đa bội)",
        "Lai xa giữa loài thực vật A ($2n = 18$) và loài B ($2n = 22$) thu được con lai bất thụ, sau đó đa bội hóa thành công tạo ra loài C mới hữu thụ. Tế bào rễ của loài C đang ở **kỳ sau của nguyên phân** có tổng cộng bao nhiêu nhiễm sắc thể đơn?",
        "80",
        "Bộ NST lưỡng bội của loài song nhị bội C là $2n_{\\text{mới}} = 18 + 22 = 40$ NST. Ở kỳ sau nguyên phân, mỗi NST kép tách thành $2$ NST đơn $\\Rightarrow 2 \\times 40 = 80$ NST đơn.",
        unit_hint="Nhập số nguyên")

    # SA-042
    add("cellular", "basic", "Đo Thời gian Pha Chu kỳ Tế bào",
        "Theo dõi $2000$ tế bào đang tăng sinh đồng đều thuộc cùng một dòng tế bào có chu kỳ tế bào kéo dài $15\\text{ giờ}$. Khi đếm trên tiêu bản nhuộm thấy có $600$ tế bào ở pha $G_1$, $800$ tế bào ở pha $S$, $400$ tế bào ở pha $G_2$ và $200$ tế bào đang ở pha nguyên phân ($M$). Thời gian diễn ra pha $S$ của tế bào này bằng bao nhiêu **giờ**?",
        "6",
        "Thời gian pha $S$ tỷ lệ thuận với tỉ lệ tế bào bắt gặp ở pha $S$: $t_S = \\frac{800}{2000} \\times 15 = 0.4 \\times 15 = 6\\text{ giờ}$.",
        accepted=["6", "6.0", "6,0"],
        unit_hint="Nhập số giờ")

    # SA-043
    add("cellular", "adv", "Đóng gói Nucleosome & Histon Lõi",
        "Một phân tử ADN nhân thực gồm $14\\,600$ cặp nucleotit được đóng gói đều đặn vào các đơn vị cấu trúc cơ bản có chu kỳ lặp mỗi đơn vị dài $200$ cặp nucleotit (gồm $146$ cặp nu quấn quanh $1$ lõi octamer $8$ phân tử histon và $54$ cặp nu đoạn nối linker). Tổng số phân tử **protein Histon lõi** (chỉ tính H2A, H2B, H3, H4 — bỏ qua H1) tham gia đóng gói đoạn ADN này là bao nhiêu?",
        "584",
        "Số hạt nucleosome $= 14\\,600 / 200 = 73$ hạt. Mỗi hạt cần $8$ phân tử histon lõi $\\Rightarrow 73 \\times 8 = 584$ phân tử histon lõi.",
        unit_hint="Nhập số nguyên")

    # SA-044
    add("cellular", "adv", "Số loại Tinh trùng Thực tế từ Ít Tế bào",
        "Ở một loài côn trùng ($2n = 16$, $8$ cặp NST đều có cấu trúc dị hợp), giảm phân không xảy ra hoán vị gen. Nếu chỉ lấy đúng $6$ tế bào sinh tinh của cá thể đực tiến hành giảm phân bình thường tạo tinh trùng, thì tổng số loại tinh trùng **tối đa** có thể thu được là bao nhiêu?",
        "12",
        "Tuy toàn cơ thể có thể tạo $2^8 = 256$ loại, nhưng $1$ tế bào sinh tinh không HVG chỉ sinh tối đa $2$ loại tinh trùng; nên $6$ tế bào sinh tinh sinh tối đa $6 \\times 2 = 12$ loại tinh trùng.",
        unit_hint="Nhập số nguyên")

    # SA-045
    add("cellular", "hsg", "Xác suất Hợp tử Hội chứng Down do Rối loạn GP II",
        "Ở người bố có $16\\%$ tế bào sinh tinh xảy ra rối loạn giảm phân tại cặp NST $21$: trong mỗi tế bào thuộc nhóm $16\\%$ này, giảm phân I bình thường tạo $2$ tế bào con, nhưng $1$ trong $2$ tế bào con đó lại bị không phân ly cặp NST $21$ ở **giảm phân II** (tạo $4$ tinh trùng gồm $1$ chiếc $n+1$, $1$ chiếc $n-1$ và $2$ chiếc $n$ bình thường); $84\\%$ tế bào sinh tinh còn lại và $100\\%$ tế bào sinh trứng của mẹ giảm phân bình thường. Xác suất (%) cặp vợ chồng này sinh ra đứa con mắc hội chứng Down ($3$ NST $21$) là bao nhiêu?",
        "4",
        "Tỉ lệ tinh trùng thừa NST $21$ ($n+1$) trong tổng tinh trùng của bố $= 16\\% \\times \\frac{1}{4} = 4\\%$. Vì mẹ luôn cho trứng bình thường mang $1$ NST $21$, xác suất sinh con Down $= 4\\% \\times 100\\% = 4\\%$.",
        accepted=["4", "4.0", "4,0"],
        unit_hint="Nhập số % (bỏ ký hiệu %, ví dụ: 4)")

    # ==================== TOPIC 4: MENDEL (SA-046 .. SA-060) ====================
    # SA-046
    add("mendel", "basic", "Số Loại Kiểu gen Đa cặp Độc lập",
        "Cho phép lai $P: AaBbDdEe \\times AabbDdee$ (các cặp gen phân ly độc lập, trội hoàn toàn). Số loại **kiểu gen** tối đa thu được ở đời con $F_1$ là bao nhiêu?",
        "36",
        "$Aa \\times Aa \\to 3$ KG; $Bb \\times bb \\to 2$ KG; $Dd \\times Dd \\to 3$ KG; $Ee \\times ee \\to 2$ KG. Tổng số KG $= 3 \\times 2 \\times 3 \\times 2 = 36$.",
        unit_hint="Nhập số nguyên")

    # SA-047
    add("mendel", "adv", "Tổ hợp Dị hợp Đúng $k$ cặp",
        "Cho cá thể có kiểu gen $AaBbDdEe$ tự thụ phấn ($4$ cặp gen phân ly độc lập). Trong tổng số các cá thể đời con $F_1$, tỉ lệ phần trăm (%) cá thể mang kiểu gen **dị hợp ĐÚNG $2$ cặp gen** và đồng hợp $2$ cặp gen còn lại bằng bao nhiêu?",
        "37.5",
        "Tại mỗi cặp $Aa \\times Aa$, xác suất dị hợp $= 0.5$ và đồng hợp $= 0.5$. Vậy xác suất đúng $2$ cặp dị hợp trong $4$ cặp $= C_4^2 \\times (0.5)^4 = 6/16 = 0.375 = 37.5\\%$.",
        tolerance=0.05,
        unit_hint="Nhập số % (ví dụ: 37.5)")

    # SA-048
    add("mendel", "adv", "Tương tác Bổ sung $9:7$",
        "Ở một loài thực vật, màu hoa đỏ ($A-B-$) và hoa trắng (các kiểu gen còn lại) do $2$ cặp gen phân ly độc lập tương tác bổ sung quy định. Cho cây hoa đỏ dị hợp $2$ cặp gen $AaBb$ tự thụ phấn thu được $F_1$. Trong số các cây **hoa ĐỎ** thu được ở $F_1$, tỉ lệ phần trăm (%) cây mang kiểu gen **không thuần chủng** (dị hợp ít nhất $1$ cặp gen) là bao nhiêu (làm tròn 2 chữ số thập phân)?",
        "88.89",
        "Trong $F_1$ có $9/16$ cây hoa đỏ ($A-B-$), trong đó chỉ duy nhất $1/16$ là thuần chủng $AABB$ và $8/16$ còn lại không thuần chủng. Vậy tỷ lệ cần tìm $= \\frac{8}{9} \\approx 88.89\\%$.",
        tolerance=0.05,
        unit_hint="Nhập số % làm tròn 2 chữ số (ví dụ: 88.89)")

    # SA-049
    add("mendel", "hsg", "Tương tác Cộng gộp $4$ Cặp Gen",
        "Chiều cao một loài thực vật do $4$ cặp gen phân ly độc lập ($A/a, B/b, C/c, D/d$) tương tác cộng gộp quy định: cây đồng hợp lặn $aabbccdd$ cao $80\\text{ cm}$, mỗi alen trội có mặt trong kiểu gen làm cây cao thêm $5\\text{ cm}$. Cho lai $P: AaBbCcDd \\times AaBbccDd$ thu được $F_1$. Tỉ lệ phần trăm (%) cây đạt chiều cao đúng $100\\text{ cm}$ ở $F_1$ là bao nhiêu (làm tròn 2 chữ số thập phân)?",
        "27.34",
        "Cây cao $100\\text{ cm}$ mang đúng $(100-80)/5 = 4$ alen trội. Ngoại trừ alen lặn $c$ từ $cc$ luôn góp $0$, có $7$ vị trí alen độc lập đều phân bố $50\\%$ trội : $50\\%$ lặn. Tỉ lệ $= \\frac{C_7^4}{2^7} = \\frac{35}{128} = 27.34375\\% \\approx 27.34\\%$.",
        tolerance=0.05,
        unit_hint="Nhập số % làm tròn 2 chữ số (ví dụ: 27.34)")

    # SA-050
    add("mendel", "basic", "Tương tác Át chế Trội $12:3:1$",
        "Ở bí ngô, alen $W$ (vỏ trắng) trội át chế hoàn toàn gen $Y/y$; khi đồng hợp $ww$ thì $Y-$ cho vỏ vàng và $yy$ cho vỏ xanh ($2$ cặp gen phân ly độc lập). Thực hiện phép lai $P: WwYy \\times wwYy$. Tỉ lệ phần trăm (%) cây con cho quả vỏ VÀNG thu được ở $F_1$ bằng bao nhiêu?",
        "37.5",
        "Bí quả vàng phải có kiểu gen $wwY-$: từ $Ww \\times ww$ cho $0.5 ww$; từ $Yy \\times Yy$ cho $0.75 Y-$. Tổng tỉ lệ $= 0.5 \\times 0.75 = 0.375 = 37.5\\%$.",
        tolerance=0.05,
        unit_hint="Nhập số % (ví dụ: 37.5)")

    # SA-051
    add("mendel", "adv", "Tìm Tần số Hoán vị Gen từ $F_1$",
        "Ở một loài thực vật, $A$ (hoa đỏ) trội hoàn toàn $a$ (hoa trắng), $B$ (hạt tròn) trội hoàn toàn $b$ (hạt dài). Cho một cây hoa đỏ, hạt tròn dị hợp $2$ cặp gen tự thụ phấn bình thường (hoán vị gen xảy ra ở $2$ giới với tần số như nhau) thu được $F_1$ có $59\\%$ số cây hoa đỏ, hạt tròn ($A-B-$). Tần số hoán vị gen ($f$, tính bằng %) của cây đem tự thụ là bao nhiêu?",
        "40",
        "$aabb = A-B- - 0.50 = 0.59 - 0.50 = 0.09 \\Rightarrow$ tỉ lệ giao tử $\\underline{ab} = \\sqrt{0.09} = 0.30 > 0.25$ (liên kết đều $\\frac{AB}{ab}$). Suy ra tần số hoán vị $f = (0.50 - 0.30) \\times 2 = 0.40 = 40\\%$.",
        unit_hint="Nhập số nguyên % (ví dụ: 40)")

    # SA-052
    add("mendel", "adv", "Hoán vị Gen 1 Giới (Ruồi giấm)",
        "Ở ruồi giấm ($2n = 8$, hoán vị gen CHỈ xảy ra ở con cái), $A$ (thân xám) trội $a$ (thân đen), $B$ (cánh dài) trội $b$ (cánh cụt). Thực hiện phép lai $P: ♀\\, \\frac{AB}{ab} \\text{ (}f = 24\\%\\text{)} \\times ♂\\, \\frac{AB}{ab}$. Tỉ lệ phần trăm (%) ruồi $F_1$ mang kiểu hình thân xám, cánh dài ($A-B-$) thu được là bao nhiêu?",
        "69",
        "Ruồi cái tạo giao tử hoán vị $0.12$ nên $\\underline{ab}_{\\text{cái}} = 0.38$; ruồi đực không hoán vị tạo $\\underline{ab}_{\\text{đực}} = 0.50$. Vậy $aabb = 0.38 \\times 0.50 = 0.19 = 19\\% \\Rightarrow A-B- = 50\\% + 19\\% = 69\\%$.",
        unit_hint="Nhập số nguyên % (ví dụ: 69)")

    # SA-053
    add("mendel", "hsg", "Phép lai Phối hợp $3$ Cặp Gen",
        "Cho cây tự thụ phấn có kiểu gen $Aa\\frac{BD}{bd}$ tiến hành tự thụ phấn bình thường thu được $F_1$. Biết hoán vị gen xảy ra ở cả hai giới với tần số $f = 20\\%$. Tỉ lệ phần trăm (%) cá thể mang kiểu gen đồng hợp lặn cả $3$ cặp gen ($aa\\frac{bd}{bd}$) ở $F_1$ là bao nhiêu?",
        "4",
        "Cặp $Aa \\times Aa \\to 0.25 aa$. Ở cặp liên kết $\\frac{BD}{bd}$ ($f=20\\%$), tỷ lệ $\\underline{bd} = 0.40 \\Rightarrow \\frac{bd}{bd} = 0.40^2 = 0.16$. Tổng tỉ lệ $= 0.25 \\times 0.16 = 0.04 = 4\\%$.",
        accepted=["4", "4.0", "4,0"],
        unit_hint="Nhập số % (bỏ ký hiệu %, ví dụ: 4)")

    # SA-054
    add("mendel", "hsg", "Bản đồ 3 Gen & Không Trao đổi chéo",
        "Trên một NST thường có $3$ gen liên kết sắp xếp theo thứ tự $A - B - D$, với khoảng cách di truyền $d(A-B) = 18\\text{ cM}$ và $d(B-D) = 8\\text{ cM}$ (không có nhiễu di truyền giữa 2 đoạn, tức $CoC = 1$). Đem cá thể dị hợp $\\frac{ABD}{abd}$ lai phân tích với $\\frac{abd}{abd}$. Về mặt lý thuyết, tổng tỉ lệ phần trăm (%) đời con mang kiểu gen giống bố mẹ (KHÔNG xảy ra bất kỳ trao đổi chéo nào ở cả 2 khoảng $A-B$ và $B-D$) là bao nhiêu (làm tròn 2 chữ số thập phân)?",
        "75.44",
        "Xác suất không trao đổi chéo đoạn 1 là $1 - 0.18 = 0.82$; ở đoạn 2 là $1 - 0.08 = 0.92$. Do độc lập không nhiễu ($CoC=1$), tỉ lệ giao tử liên kết gốc $\\underline{ABD} + \\underline{abd} = 0.82 \\times 0.92 = 0.7544 = 75.44\\%$.",
        tolerance=0.05,
        unit_hint="Nhập số % làm tròn 2 chữ số (ví dụ: 75.44)")

    # SA-055
    add("mendel", "adv", "Phối hợp NST Thường & NST Giới tính X",
        "Ở ruồi giấm, alen $B$ (thân xám) trội $b$ (đen) nằm trên NST thường; alen $A$ (mắt đỏ) trội $a$ (trắng) nằm trên vùng không tương đồng của NST X. Cho giao phối $P: Bb\\, X^A X^a \\times Bb\\, X^A Y$ thu được $F_1$. Tính theo tổng số toàn bộ đàn ruồi $F_1$? Khoan: trong riêng nhóm **ruồi ĐỰC** thu được ở $F_1$, tỉ lệ phần trăm (%) ruồi đực có kiểu hình thân xám, mắt đỏ ($B- X^A Y$) chiếm bao nhiêu?",
        "37.5",
        "Cặp $Bb \\times Bb \\to 75\\% B-$. Ở giới đực $F_1$, tỷ lệ mang $X^A Y$ vs $X^a Y$ là $1:1$ ($50\\% X^A Y$). Do đó trong số ruồi đực, ruồi xám-đỏ chiếm $0.75 \\times 0.50 = 0.375 = 37.5\\%$.",
        tolerance=0.05,
        unit_hint="Nhập số % (ví dụ: 37.5)")

    # SA-056
    add("mendel", "hsg", "Gen trên Vùng Tương đồng của X và Y",
        "Ở một loài động vật ($XX/XY$), gen quy định chiều cao nằm trên vùng tương đồng của NST X và Y ($A$ cao trội hoàn toàn so với $a$ thấp). Thực hiện phép lai $P: ♀\\, X^A X^a \\times ♂\\, X^a Y^a$ thu được $F_1$, sau đó cho toàn bộ đàn $F_1$ giao phối ngẫu nhiên với nhau thu được $F_2$. Tỉ lệ phần trăm (%) cá thể **CÁI thân thấp** ($X^a X^a$) tính trong tổng số toàn đàn $F_2$ là bao nhiêu?",
        "18.75",
        "$F_1$ cái gồm $\\frac{1}{2} X^A X^a : \\frac{1}{2} X^a X^a$ (cho trứng $0.25 X^A : 0.75 X^a$). $F_1$ đực gồm $\\frac{1}{2} X^A Y^a : \\frac{1}{2} X^a Y^a$ (cho tinh trùng $0.25 X^A : 0.25 X^a : 0.50 Y^a$). Tổ hợp $F_2$ tạo $X^a X^a = 0.75 \\times 0.25 = 0.1875 = 18.75\\%$.",
        tolerance=0.05,
        unit_hint="Nhập số % (ví dụ: 18.75)")

    # SA-057
    add("mendel", "hsg", "Xác định Tỉ lệ Kiểu gen Thể Tứ bội",
        "Ở thực vật tứ bội ($4n$), thực hiện phép lai giữa hai cây có kiểu gen $P: AAAa \\times AAaa$ (cả hai cây đều giảm phân bình thường tạo $100\\%$ giao tử lưỡng bội $2n$ hữu thụ). Tỉ lệ phần trăm (%) cá thể con ở $F_1$ có kiểu gen **$AAaa$** là bao nhiêu (làm tròn 2 chữ số thập phân)?",
        "41.67",
        "$AAAa$ tạo $\\frac{1}{2} AA : \\frac{1}{2} Aa$; $AAaa$ tạo $\\frac{1}{6} AA : \\frac{4}{6} Aa : \\frac{1}{6} aa$. Tỉ lệ $AAaa$ ở $F_1 = \\frac{1}{2} AA \\cdot \\frac{1}{6} aa + \\frac{1}{2} Aa \\cdot \\frac{4}{6} Aa = \\frac{1}{12} + \\frac{4}{12} = \\frac{5}{12} \\approx 41.67\\%$.",
        tolerance=0.05,
        unit_hint="Nhập số % làm tròn 2 chữ số (ví dụ: 41.67)")

    # SA-058
    add("mendel", "hsg", "Phả hệ Tính Xác suất Sinh Thêm Con",
        "Bệnh phenylketo niệu (PKU) do alen lặn $a$ trên NST thường quy định. Một cặp vợ chồng đều có kiểu hình bình thường nhưng đã sinh đứa con đầu lòng mắc bệnh PKU. Họ dự định sinh thêm đúng $2$ người con nữa. Xác suất (theo %, làm tròn 2 chữ số thập phân) để cả $2$ người con sinh thêm sau này đều KHÔNG mắc bệnh VÀ gồm đúng $1$ trai, $1$ gái là bao nhiêu?",
        "28.13",
        "Bố mẹ chắc chắn $Aa \\times Aa \\Rightarrow$ xác suất mỗi con không bệnh $= 3/4$. Xác suất $2$ con đều không bệnh $= (3/4)^2 = 9/16$. Xác suất gồm $1$ trai và $1$ gái (trai trước hoặc gái trước) $= 2 \\times 0.5 \\times 0.5 = 0.5$. Tích $= \\frac{9}{16} \\times \\frac{1}{2} = \\frac{9}{32} = 28.125\\% \\approx 28.13\\%$.",
        accepted=["28.13", "28.125", "28.12"],
        tolerance=0.05,
        unit_hint="Nhập số % làm tròn 2 chữ số (ví dụ: 28.13)")

    # SA-059
    add("mendel", "adv", "Số Kiểu gen Gen Đa alen Trên X và Y",
        "Xét một gen $A$ nằm trên vùng **không tương đồng** của NST X có $4$ alen ($A_1, A_2, A_3, A_4$), và một gen $B$ nằm trên vùng **không tương đồng** của NST Y có $3$ alen ($B_1, B_2, B_3$). Về mặt lý thuyết, trong quần thể có tối đa bao nhiêu loại kiểu gen khác nhau cùng lúc về cả $2$ gen nói trên?",
        "22",
        "Số kiểu gen ở giới cái ($XX$) $= \\frac{4(4+1)}{2} = 10$; số kiểu gen ở giới đực ($XY$) $= 4 \\times 3 = 12$. Tổng cộng $= 10 + 12 = 22$ kiểu gen.",
        unit_hint="Nhập số nguyên")

    # SA-060
    add("mendel", "adv", "Lai Phân tích Phối hợp Tương tác + HVG",
        "Ở một loài thực vật, màu hoa đỏ hình thành khi có đồng thời cả hai alen trội $A$ và $B$ ($A-B-$), thiếu một hoặc cả hai alen cho hoa trắng. Biết $2$ gen $A/a$ và $B/b$ cùng nằm trên một cặp NST thường cách nhau $30\\text{ cM}$. Cho cây dị hợp $\\frac{Ab}{aB}$ lai phân tích với cây $\\frac{ab}{ab}$. Tỉ lệ phần trăm (%) cây hoa ĐỎ thu được ở đời con là bao nhiêu?",
        "15",
        "Cây $\\frac{Ab}{aB}$ với $f = 30\\%$ tạo giao tử hoán vị $\\underline{AB} = f/2 = 15\\%$. Khi lai phân tích $\\times \\underline{ab}$, chỉ tổ hợp $\\frac{AB}{ab}$ mới biểu hiện hoa đỏ $\\Rightarrow 15\\%$.",
        unit_hint="Nhập số nguyên % (ví dụ: 15)")

    # ==================== TOPIC 5: POPULATION (SA-061 .. SA-075) ====================
    # SA-061
    add("population", "basic", "Tính Tần số Alen Quần thể",
        "Kiểm tra cấu trúc di truyền của một mẫu $500$ cây lúa thu được $180$ cây $AA$, $240$ cây $Aa$ và $80$ cây $aa$. Tần số alen trội $A$ ($p$) của quần thể này bằng bao nhiêu (viết dạng số thập phân)?",
        "0.6",
        "Ta có $p(A) = \\frac{180 + 240/2}{500} = \\frac{300}{500} = 0.60$.",
        accepted=["0.6", "0.60"],
        tolerance=0.01,
        unit_hint="Nhập số thập phân (ví dụ: 0.6)")

    # SA-062
    add("population", "basic", "Cân bằng Hardy-Weinberg",
        "Một quần thể động vật đang ở trạng thái cân bằng di truyền Hardy-Weinberg có tỉ lệ cá thể mang kiểu hình lặn ($aa$) chiếm $4\\%$. Tỉ lệ phần trăm (%) cá thể mang kiểu gen đồng hợp trội ($AA$) trong quần thể này là bao nhiêu?",
        "64",
        "Vì cân bằng: $q^2 = 0.04 \\Rightarrow q = 0.2 \\Rightarrow p = 0.8$. Suy ra $AA = p^2 = 0.8^2 = 0.64 = 64\\%$.",
        unit_hint="Nhập số nguyên % (ví dụ: 64)")

    # SA-063
    add("population", "basic", "Quần thể Tự thụ phấn",
        "Một quần thể thực vật tự thụ phấn có cấu trúc xuất phát ở $P$ là $0.24 AA + 0.64 Aa + 0.12 aa = 1$. Sau $4$ thế hệ tự thụ phấn liên tiếp ($F_4$), tỉ lệ phần trăm (%) cá thể dị hợp $Aa$ còn lại trong quần thể bằng bao nhiêu?",
        "4",
        "Sau $n = 4$ thế hệ tự thụ phấn: $f(Aa)_{F_4} = 64\\% \\times (\\frac{1}{2})^4 = \\frac{64\\%}{16} = 4\\%$.",
        accepted=["4", "4.0"],
        unit_hint="Nhập số % (ví dụ: 4)")

    # SA-064
    add("population", "adv", "Tự thụ phấn từ Cây Hoa đỏ",
        "Thế hệ $P$ của một quần thể cây đậu chỉ toàn gồm các cây hoa đỏ với tỷ lệ $0.40 AA + 0.60 Aa = 1$. Khi cho toàn bộ các cây này tự thụ phấn bắt buộc liên tiếp đến thế hệ $F_2$, tỉ lệ phần trăm (%) cây hoa trắng ($aa$) thu được ở $F_2$ là bao nhiêu?",
        "22.5",
        "Ở $F_2$: $Aa = 0.60 \\times (\\frac{1}{2})^2 = 0.15$. Tỉ lệ $aa = 0 + \\frac{0.60 - 0.15}{2} = 0.225 = 22.5\\%$.",
        tolerance=0.05,
        unit_hint="Nhập số % (ví dụ: 22.5)")

    # SA-065
    add("population", "hsg", "Chọn lọc chống $aa$ trong Ngẫu phối",
        "Một quần thể thực vật giao phấn ngẫu nhiên xuất phát ở giai đoạn hạt $P$ trưởng thành gồm $0.60 AA + 0.40 Aa = 1$ (trong môi trường mà MỌI hạt mang kiểu gen đồng hợp lặn $aa$ đều bị chết 100% không mọc thành cây sinh sản). Sau $2$ thế hệ giao phấn ngẫu nhiên, tỉ lệ phần trăm (%) hạt $aa$ bị chết ở hợp tử thế hệ $F_2$ bằng bao nhiêu (làm tròn 2 chữ số thập phân)?",
        "2.78",
        "$P$ trưởng thành có $q_0 = 0.2 \\Rightarrow$ tạo $F_1$ có $0.64 AA : 0.32 Aa : 0.04 aa$. Loại $0.04 aa$, cây $F_1$ trưởng thành gồm $\\frac{2}{3} AA + \\frac{1}{3} Aa \\Rightarrow q_1 = \\frac{1}{6}$. Ngẫu phối sinh hạt $F_2$ có $aa = (\\frac{1}{6})^2 = \\frac{1}{36} \\approx 2.78\\%$.",
        tolerance=0.03,
        unit_hint="Nhập số % làm tròn 2 chữ số (ví dụ: 2.78)")

    # SA-066
    add("population", "hsg", "Tự thụ phấn Loại bỏ Đồng hợp Lặn",
        "Một quần thể tự thụ phấn bắt buộc xuất phát $P$ gồm $0.25 AA + 0.75 Aa = 1$. Giả sử hạt mang kiểu gen $aa$ bị chết $100\\%$ ở giai đoạn nảy mầm trong tất cả mọi thế hệ. Tính tỉ lệ phần trăm (%) cây mang kiểu gen DỊ HỢP $Aa$ trong tổng số các cây trưởng thành sống sót ở thế hệ $F_2$ (làm tròn 2 chữ số thập phân).",
        "26.09",
        "Hợp tử $F_1$: $\\frac{7}{16} AA : \\frac{6}{16} Aa : \\frac{3}{16} aa \\Rightarrow$ cây $F_1$ sống: $\\frac{7}{13} AA + \\frac{6}{13} Aa$. Tự thụ sinh hợp tử $F_2$: $AA = \\frac{7}{13} + \\frac{6}{52} = \\frac{34}{52}$; $Aa = \\frac{12}{52}$; $aa = \\frac{6}{52}$. Bỏ $aa$, trong cây $F_2$ sống thì $Aa = \\frac{12}{34+12} = \\frac{6}{23} \\approx 26.09\\%$.",
        tolerance=0.05,
        unit_hint="Nhập số % làm tròn 2 chữ số (ví dụ: 26.09)")

    # SA-067
    add("population", "adv", "Quần thể 3 Alen Nhóm máu ABO",
        "Trong một quần thể người cân bằng Hardy-Weinberg về hệ nhóm máu ABO, thống kê thấy có $9\\%$ người mang nhóm máu O và $27\\%$ người mang nhóm máu A. Tỉ lệ phần trăm (%) người mang nhóm máu AB trong quần thể này là bao nhiêu?",
        "24",
        "Từ O ($r^2 = 0.09$) $\\Rightarrow r = 0.3$. Nhóm A + O $= (p+r)^2 = 0.27 + 0.09 = 0.36 \\Rightarrow p + r = 0.6 \\Rightarrow p = 0.3$. Suy ra $q(I^B) = 1 - 0.3 - 0.3 = 0.4$. Vậy nhóm AB $= 2pq = 2(0.3)(0.4) = 0.24 = 24\\%$.",
        unit_hint="Nhập số nguyên % (ví dụ: 24)")

    # SA-068
    add("population", "hsg", "Cân bằng Quần thể Gen trên NST X",
        "Một quần thể động vật ($XX/XY$, tỉ lệ đực:cái bằng $1:1$) ở thế hệ xuất phát $P$ có tần số alen $A$ (nằm trên vùng không tương đồng của NST X) ở giới cái là $0.50$ và ở giới đực là $0.80$. Khi quần thể giao phối ngẫu nhiên qua rất nhiều thế hệ tới lúc đạt cân bằng, tần số alen $A$ của quần thể ổn định tại giá trị bao nhiêu (dạng số thập phân)?",
        "0.6",
        "Áp dụng công thức cân bằng trên X: $p^* = \\frac{2 p_{\\text{cái}} + p_{\\text{đực}}}{3} = \\frac{2(0.50) + 0.80}{3} = \\frac{1.80}{3} = 0.60$.",
        accepted=["0.6", "0.60"],
        tolerance=0.01,
        unit_hint="Nhập số thập phân (ví dụ: 0.6)")

    # SA-069
    add("population", "adv", "Kích thước Hiệu quả $N_e$",
        "Trong một khu bảo tồn linh trưởng có đúng $30$ cá thể đực và $70$ cá thể cái trưởng thành tham gia sinh sản ngẫu nhiên (tổng $N = 100$). Kích thước hiệu quả ($N_e = \\frac{4 N_m N_f}{N_m + N_f}$) của quần thể này là bao nhiêu cá thể?",
        "84",
        "Thay vào công thức: $N_e = \\frac{4 \\times 30 \\times 70}{30 + 70} = \\frac{8400}{100} = 84$ cá thể.",
        unit_hint="Nhập số nguyên")

    # SA-070
    add("population", "hsg", "Dòng Nhập cư (Di-nhập gen)",
        "Quần thể bản địa trên đảo X có tần số alen $p_0(A) = 0.90$. Mỗi thế hệ, có một lượng cá thể nhập cư từ đất liền (nơi duy trì cố định tần số $p_m(A) = 0.10$) bay tới hòa nhập tạo nên tỷ trọng $m = 20\\%$ ($0.2$) trong đàn sinh sản của đảo. Ngay sau $2$ thế hệ chịu dòng nhập cư đều đặn này (giả sử không có nhân tố nào khác làm đổi $p$), tần số alen $A$ trên đảo X bằng bao nhiêu (viết chính xác số thập phân)?",
        "0.612",
        "Thế hệ 1: $p_1 = 0.8(0.90) + 0.2(0.10) = 0.74$. Thế hệ 2: $p_2 = 0.8(0.74) + 0.2(0.10) = 0.592 + 0.02 = 0.612$.",
        tolerance=0.002,
        unit_hint="Nhập số thập phân (ví dụ: 0.612)")

    # SA-071
    add("population", "hsg", "Ưu thế Dị hợp tử & Điểm Cân bằng",
        "Ở một loài bướm, giá trị thích nghi của $3$ kiểu gen lần lượt là $W_{AA} = 0.70$, $W_{Aa} = 1.00$ và $W_{aa} = 0.40$. Khi chọn lọc tự nhiên cân bằng ổn định trong quần thể ngẫu phối lớn, tần số alen lặn $a$ ($\\hat{q}$) duy trì ở giá trị bằng bao nhiêu (làm tròn 2 chữ số thập phân)?",
        "0.33",
        "Hệ số chọn lọc $s_1 = 1 - 0.7 = 0.3$; $s_2 = 1 - 0.4 = 0.6$. Tần số cân bằng $\\hat{q} = \\frac{s_1}{s_1 + s_2} = \\frac{0.3}{0.3 + 0.6} = \\frac{1}{3} \\approx 0.33$.",
        tolerance=0.01,
        unit_hint="Nhập số thập phân làm tròn 2 chữ số (ví dụ: 0.33)")

    # SA-072
    add("population", "adv", "Hệ số Nội phối $F$",
        "Một quần thể động vật có tần số alen $p(A) = 0.50$, $q(a) = 0.50$. Do bị cô lập sinh cảnh, quần thể có sự giao phối cận huyết một phần với hệ số nội phối chung $F = 0.30$. Áp dụng công thức $f(AA) = p^2 + pqF$, tần số kiểu gen đồng hợp trội $AA$ trong quần thể là bao nhiêu?",
        "0.325",
        "$f(AA) = 0.50^2 + (0.50)(0.50)(0.30) = 0.25 + 0.075 = 0.325$.",
        tolerance=0.005,
        unit_hint="Nhập số thập phân (ví dụ: 0.325)")

    # SA-073
    add("population", "adv", "Độ Đa dạng Di truyền $H_e$",
        "Tại một locus đa alen trên NST thường của quần thể cá hồi đang cân bằng ngẫu phối có $3$ alen với tần số tương ứng là $0.50$, $0.30$ và $0.20$. Tính chỉ số dị hợp tử kỳ vọng ($H_e = 1 - \\sum p_i^2$) của quần thể ở locus này (dạng số thập phân).",
        "0.62",
        "Tổng tỉ lệ đồng hợp $= 0.5^2 + 0.3^2 + 0.2^2 = 0.25 + 0.09 + 0.04 = 0.38$. Suy ra $H_e = 1 - 0.38 = 0.62$.",
        tolerance=0.01,
        unit_hint="Nhập số thập phân (ví dụ: 0.62)")

    # SA-074
    add("population", "hsg", "Phả hệ Kết hợp Quần thể",
        "Trong một quần thể người cân bằng di truyền, bệnh bạch tạng (gen lặn $a$ trên NST thường) xuất hiện với tần suất $1/400$ ($0.25\\%$). Một người đàn ông bị bệnh bạch tạng ($aa$) kết hôn với một người phụ nữ có da bình thường ngẫu nhiên trong quần thể. Xác suất (%) đứa con đầu lòng của họ mắc bệnh bạch tạng là bao nhiêu (làm tròn 2 chữ số thập phân)?",
        "4.76",
        "$q^2 = 1/400 \\Rightarrow q = 0.05, p = 0.95$. Trong nhóm người bình thường ($0.9025 AA + 0.095 Aa$), người vợ mang dị hợp $Aa$ với xác suất $\\frac{2q}{1+q} = \\frac{0.10}{1.05} = \\frac{2}{21}$. Chồng $aa$ luôn cho $a$, con mắc bệnh nếu vợ cho $a = \\frac{1}{2} \\times \\frac{2}{21} = \\frac{1}{21} \\approx 4.76\\%$.",
        tolerance=0.04,
        unit_hint="Nhập số % làm tròn 2 chữ số (ví dụ: 4.76)")

    # SA-075
    add("population", "adv", "Đồng hồ Phân tử",
        "Theo dữ liệu đồng hồ phân tử của một gen tiến hóa trung tính dài $2000$ cặp bazơ, tốc độ tích lũy sai khác giữa hai nhánh loài tách rời nhau bằng $2$ cặp nucleotit khác biệt trên mỗi $1000$ cặp bazơ cho mỗi $1$ triệu năm phân ly. Khi giải trình tự so sánh chính đoạn gen $2000\\text{ bp}$ đó giữa loài X và loài Y, người ta đếm được $60$ vị trí nucleotit sai khác nhau. Theo mô hình đồng hồ phân tử tuyến tính, tổ tiên chung gần nhất của X và Y tách nhánh cách đây bao nhiêu **triệu năm**?",
        "15",
        "Trên đoạn dài $2000\\text{ bp}$, tốc độ tích lũy sai khác $= 2 \\times 2 = 4$ nucleotit mỗi triệu năm. Vậy thời gian phân ly $= \\frac{60}{4} = 15$ triệu năm.",
        unit_hint="Nhập số nguyên (đơn vị: triệu năm)")

    # ==================== TOPIC 6: PHYSIOLOGY (SA-076 .. SA-090) ====================
    # SA-076
    add("physiology", "basic", "Thế nước Tế bào Thực vật",
        "Một tế bào nhu mô lá có thế chất tan $\\Psi_s = -1.35\\text{ MPa}$ được ngâm trong dung dịch đường cân bằng đẳng trương có thế nước ngoài $\\Psi_{\\text{ng}} = -0.85\\text{ MPa}$ (không đổi thể tích). Áp suất trương nước ($\\Psi_p$) của tế bào này ở trạng thái cân bằng bằng bao nhiêu **MPa**?",
        "0.5",
        "Khi cân bằng: $\\Psi_{\\text{tb}} = \\Psi_{\\text{ng}} = -0.85\\text{ MPa}$. Mà $\\Psi_{\\text{tb}} = \\Psi_s + \\Psi_p \\Rightarrow \\Psi_p = -0.85 - (-1.35) = +0.50\\text{ MPa}$.",
        accepted=["0.5", "0.50"],
        tolerance=0.01,
        unit_hint="Nhập số thập phân (đơn vị MPa)")

    # SA-077
    add("physiology", "basic", "Chi phí Năng lượng Pha tối $C_3$",
        "Trong chu trình Calvin của thực vật $C_3$ (bỏ qua hô hấp sáng), để cố định $CO_2$ tổng hợp được ròng $4$ phân tử đường Glucose ($C_6H_{12}O_6$), pha tối cần tiêu thụ tổng cộng bao nhiêu phân tử **ATP**?",
        "72",
        "Mỗi phân tử Glucose ở thực vật $C_3$ tiêu tốn $18\\text{ ATP}$ và $12\\text{ NADPH}$. Với $4$ phân tử Glucose cần $4 \\times 18 = 72\\text{ ATP}$.",
        unit_hint="Nhập số nguyên")

    # SA-078
    add("physiology", "adv", "Thương số Hô hấp (RQ)",
        "Khi hạt cây họ Dầu nảy mầm hô hấp hiếu khí phân giải hoàn toàn phân tử axit béo không no axit oleic ($C_{18}H_{34}O_2$) theo phương trình $C_{18}H_{34}O_2 + 25.5\\, O_2 \\rightarrow 18\\, CO_2 + 17\\, H_2O$. Thương số hô hấp ($RQ$) của phản ứng trên bằng bao nhiêu (làm tròn 2 chữ số thập phân)?",
        "0.71",
        "Áp dụng $RQ = \\frac{CO_2}{O_2} = \\frac{18}{25.5} \\approx 0.7059 \\approx 0.71$ (đặc trưng cho nguyên liệu giàu lipit).",
        tolerance=0.01,
        unit_hint="Nhập số thập phân làm tròn 2 chữ số (ví dụ: 0.71)")

    # SA-079
    add("physiology", "basic", "Chu kỳ Hoạt động của Tim",
        "Một người khi đang chạy nhanh có tần số nhịp tim tăng lên mức $120\\text{ nhịp/phút}$ (thời gian $1$ chu kỳ tim là $0.50\\text{ s}$). Biết thời gian tâm thất co ở người này gần như giữ ở mức $0.28\\text{ s}$, thời gian tâm nhĩ co và dãn chung co ngắn lại tương ứng. Trong mỗi chu kỳ tim lúc này, khoảng thời gian tâm thất được dãn nghỉ kéo dài bao nhiêu **giây**?",
        "0.22",
        "Trong một chu kỳ $0.50\\text{ s}$, tâm thất chỉ co $0.28\\text{ s}$, suy ra thời gian tâm thất dãn nghỉ $= 0.50 - 0.28 = 0.22\\text{ s}$.",
        tolerance=0.01,
        unit_hint="Nhập số thập phân (đơn vị: giây)")

    # SA-080
    add("physiology", "adv", "Cung lượng Tim ($CO$)",
        "Một vận động viên khi thi đấu đỉnh cao có nhịp tim $150\\text{ lần/phút}$, thể tích máu trong mỗi tâm thất ở cuối tâm trương là $EDV = 160\\text{ ml}$ và còn lại ở cuối tâm thu là $ESV = 40\\text{ ml}$. Cung lượng tim của vận động viên này đạt bao nhiêu **lít/phút**?",
        "18",
        "Thể tích tâm thu $SV = 160 - 40 = 120\\text{ ml}$. Cung lượng tim $CO = HR \\times SV = 150 \\times 120 = 18\\,000\\text{ ml/phút} = 18\\text{ lít/phút}$.",
        accepted=["18", "18.0"],
        unit_hint="Nhập số lít/phút (ví dụ: 18)")

    # SA-081
    add("physiology", "adv", "Thông khí Phế nang Phổi",
        "Một người trưởng thành hô hấp đều đặn với tần số $f = 16\\text{ nhịp/phút}$, thể tích khí lưu thông mỗi nhịp $V_T = 500\\text{ ml}$ và thể tích khoảng chết giải phẫu đường dẫn khí là $V_D = 150\\text{ ml}$. Lưu lượng thông khí phế nang thực sự ($V_A$) của người này đạt bao nhiêu **lít/phút**?",
        "5.6",
        "Áp dụng $V_A = (V_T - V_D) \\times f = (500 - 150) \\times 16 = 350 \\times 16 = 5600\\text{ ml/phút} = 5.6\\text{ lít/phút}$.",
        tolerance=0.05,
        unit_hint="Nhập số lít/phút (ví dụ: 5.6)")

    # SA-082
    add("physiology", "hsg", "Năng lực Vận chuyển Oxy của Máu",
        "Trung bình $1\\text{ gam}$ Hemoglobin ($Hb$) bão hòa $100\\%$ gắn kết tối đa được $1.34\\text{ ml}$ khí $O_2$. Một vận động viên có nồng độ $Hb = 15\\text{ g/100 ml}$ máu (bão hòa $100\\%$ ở phổi, bỏ qua $O_2$ hòa tan vật lý) và cung lượng tim $5.0\\text{ lít/phút}$. Tổng thể tích khí $O_2$ gắn Hemoglobin được tim bơm vận chuyển qua động mạch chủ trong mỗi phút bằng bao nhiêu **ml/phút**?",
        "1005",
        "$100\\text{ ml}$ máu chở được $15 \\times 1.34 = 20.1\\text{ ml } O_2$. Trong $5.0\\text{ lít} = 5000\\text{ ml}$ ($50$ phần $100\\text{ ml}$), tổng lượng $O_2 = 20.1 \\times 50 = 1005\\text{ ml/phút}$.",
        unit_hint="Nhập số nguyên (đơn vị: ml/phút)")

    # SA-083
    add("physiology", "hsg", "Sinh lý Thận - Ngưỡng Bài xuất Glucose",
        "Một bệnh nhân đái tháo đường có tốc độ lọc cầu thận $GFR = 120\\text{ ml/phút}$ và nồng độ glucose huyết tương tăng lên mức $3.0\\text{ mg/ml}$ ($300\\text{ mg/dL}$). Biết ngưỡng vận chuyển tái hấp thu tối đa ($T_m$) glucose tại ống lượn gần của thận là $300\\text{ mg/phút}$ (lượng lọc vượt quá $T_m$ sẽ bị đào thải toàn bộ ra nước tiểu). Mỗi phút có bao nhiêu **miligam (mg)** glucose bị bài xuất ra nước tiểu?",
        "60",
        "Tốc độ lọc glucose ở cầu thận $= GFR \\times P_{\\text{glucose}} = 120 \\times 3.0 = 360\\text{ mg/phút}$. Vì vượt khả năng tái hấp thu tối đa $300\\text{ mg/phút}$, lượng thải ra nước tiểu $= 360 - 300 = 60\\text{ mg/phút}$.",
        unit_hint="Nhập số nguyên (đơn vị: mg)")

    # SA-084
    add("physiology", "hsg", "Điện thế Cân bằng Nernst của $Na^+$",
        "Áp dụng phương trình Nernst ở $37^\\circ\\text{C}$ cho ion đơn hóa trị $Na^+$ ($z = +1$): $E_{Na} = \\frac{61}{z} \\log_{10} \\frac{[Na^+]_{\\text{ngoài}}}{[Na^+]_{\\text{trong}}}\\text{ mV}$. Với một tế bào thần kinh có $[Na^+]_{\\text{ngoài}} = 145\\text{ mM}$ và $[Na^+]_{\\text{trong}} = 14.5\\text{ mM}$, điện thế cân bằng $E_{Na}$ của màng tế bào là bao nhiêu **mV**?",
        "61",
        "$E_{Na} = \\frac{61}{1} \\log_{10} \\frac{145}{14.5} = 61 \\times \\log_{10}(10) = +61\\text{ mV}$.",
        accepted=["61", "+61"],
        unit_hint="Nhập số nguyên (đơn vị: mV)")

    # SA-085
    add("physiology", "adv", "Tích hợp Điện thế sau Xinap",
        "Một nơron thần kinh đang duy trì điện thế nghỉ ở $-70\\text{ mV}$ nhận tín hiệu truyền tới đồng thời từ $4$ xinap kích thích (mỗi xinap tạo điện thế sau xinap kích thích $EPSP = +6\\text{ mV}$) và $2$ xinap ức chế (mỗi xinap tạo điện thế sau xinap ức chế $IPSP = -4\\text{ mV}$). Giá trị điện thế màng tổng hợp tại gò sợi trục khi cộng gộp không gian lúc đó là bao nhiêu **mV**?",
        "-54",
        "Điện thế màng $= -70 + 4 \\times (+6) + 2 \\times (-4) = -70 + 24 - 8 = -54\\text{ mV}$ (đã vượt ngưỡng $-55\\text{ mV}$ để phát điện thế hoạt động!).",
        unit_hint="Nhập số nguyên (ghi rõ dấu - phía trước)")

    # SA-086
    add("physiology", "basic", "Ước lượng Kích thước Quần thể Sinh thái",
        "Để ước tính tổng số cá chép trong một hồ nước, nhóm nghiên cứu đánh bắt lần thứ $1$ được $80$ con, bấm khuyên đánh dấu vây rồi thả toàn bộ lại hồ. Một tuần sau bắt lại ngẫu nhiên lần thứ $2$ được $100$ con, trong đó đếm được $16$ con có đánh dấu từ lần trước. Áp dụng công thức Lincoln-Petersen ($N = \\frac{M \\cdot C}{R}$), kích thước ước tính của quần thể cá trong hồ là bao nhiêu con?",
        "500",
        "$N = \\frac{80 \\times 100}{16} = \\frac{8000}{16} = 500$ cá thể.",
        unit_hint="Nhập số nguyên")

    # SA-087
    add("physiology", "adv", "Mô hình Tăng trưởng Logistic",
        "Quần thể thỏ rừng tăng trưởng theo mô hình Logistic $\\frac{dN}{dt} = r N \\left(\\frac{K - N}{K}\\right)$ trong môi trường có sức chứa tối đa $K = 4000$ cá thể và tốc độ tăng trưởng nội tại tối đa $r = 0.5\\text{ /năm}$. Tốc độ tăng trưởng số lượng cá thể cực đại ($(\\frac{dN}{dt})_{\\max}$, đơn vị **cá thể/năm**) mà quần thể có thể đạt được bằng bao nhiêu?",
        "500",
        "Tốc độ tăng trưởng đạt cực đại tại $N = K/2 = 2000$ cá thể: $(\\frac{dN}{dt})_{\\max} = \\frac{rK}{4} = \\frac{0.5 \\times 4000}{4} = 500$ cá thể/năm.",
        unit_hint="Nhập số nguyên")

    # SA-088
    add("physiology", "basic", "Hiệu suất Sinh thái Bậc Dinh dưỡng",
        "Trong một hệ sinh thái rừng, sinh vật sản xuất tích lũy $1.2 \\times 10^6\\text{ kcal}$. Hiệu suất sinh thái chuyển lên sinh vật tiêu thụ bậc $1$ là $8\\%$, tiếp lên bậc $2$ là $10\\%$, và từ bậc $2$ lên bậc $3$ là $12.5\\%$. Năng lượng tích lũy được ở sinh vật tiêu thụ bậc $3$ bằng bao nhiêu **kcal**?",
        "1200",
        "$E_1 = 1.2 \\times 10^6 \\times 0.08 = 96\\,000$; $E_2 = 96\\,000 \\times 0.10 = 9600$; $E_3 = 9600 \\times 0.125 = 1200\\text{ kcal}$.",
        unit_hint="Nhập số nguyên (đơn vị: kcal)")

    # SA-089
    add("physiology", "hsg", "Chỉ số Đa dạng Simpson ($1 - D$)",
        "Khảo sát một quần xã thực vật với mẫu $100$ cá thể gồm $4$ loài có số lượng cá thể lần lượt là: Loài A ($60$ cây), Loài B ($20$ cây), Loài C ($10$ cây) và Loài D ($10$ cây). Áp dụng chỉ số đa dạng Simpson $1 - D = 1 - \\sum_{i=1}^S p_i^2$, giá trị chỉ số đa dạng của quần xã này là bao nhiêu?",
        "0.58",
        "Các tỷ lệ $p_i$: $0.6, 0.2, 0.1, 0.1$. Ta có $\\sum p_i^2 = 0.6^2 + 0.2^2 + 0.1^2 + 0.1^2 = 0.36 + 0.04 + 0.01 + 0.01 = 0.42 \\Rightarrow 1 - D = 1 - 0.42 = 0.58$.",
        tolerance=0.01,
        unit_hint="Nhập số thập phân (ví dụ: 0.58)")

    # SA-090
    add("physiology", "adv", "Ngân sách Năng lượng Sinh vật",
        "Một con chuột đồng ăn vào lượng thức ăn hạt chứa $500\\text{ kJ}$ năng lượng. Sau quá trình tiêu hóa, $150\\text{ kJ}$ bị thải ra trong phân và nước tiểu; phần năng lượng đồng hóa được ($A$) sử dụng $90\\%$ cho hô hấp giữ thân nhiệt ($R$) và $10\\%$ còn lại tích lũy vào tăng trưởng sinh khối mới ($P$). Lượng năng lượng tích lũy cho tăng trưởng ($P$) bằng bao nhiêu **kJ**?",
        "35",
        "Năng lượng đồng hóa $A = 500 - 150 = 350\\text{ kJ}$. Phần tích lũy sinh trưởng $P = 10\\% \\times 350 = 35\\text{ kJ}$.",
        unit_hint="Nhập số nguyên (đơn vị: kJ)")

    assert len(items) == 90, f"Expected 90 SA items, got {len(items)}"
    validate_question_list(items, kind="SA")
    write_js_module("bank_sa.js", "SA_BANK", items)
    return items


if __name__ == "__main__":
    res = build_sa_bank()
    print("Total SA:", len(res))
    print("By topic:", Counter(x["topic"] for x in res))
    print("By level:", Counter(x["level"] for x in res))
