# -*- coding: utf-8 -*-
"""
Block B of True/False bank: 45 TF questions (15 mendel + 15 population + 15 physiology).
"""
from common import make_tf


def get_block_b(start_idx=46):
    items = []
    idx = start_idx

    def add(topic, level, subtopic, stem, stmts, sexp=""):
        nonlocal idx
        qid = f"TF-{idx:03d}"
        items.append(make_tf(qid, topic, level, subtopic, stem, stmts, sexp))
        idx += 1

    # ==================== TOPIC 4: MENDEL (TF-046 .. TF-060) ====================
    # TF-046
    add("mendel", "basic", "Quy luật Phân ly độc lập",
        "Ở một loài thực vật giao phấn, alen $A$ quy định thân cao trội hoàn toàn so với $a$ thân thấp; $B$ quy định hoa đỏ trội hoàn toàn so với $b$ hoa trắng; $D$ quy định hạt vàng trội hoàn toàn so với $d$ hạt xanh. Các cặp gen nằm trên các cặp NST tương đồng khác nhau. Cho phép lai $P: AaBbDd \\times AaBbdd$. Xét đời con $F_1$ thu được:",
        [("Số loại kiểu gen tối đa thu được ở đời con $F_1$ bằng $18$ và số loại kiểu hình tối đa bằng $8$.",
          True, "$Aa \\times Aa \\to 3\\text{ KG}, 2\\text{ KH}$; $Bb \\times Bb \\to 3\\text{ KG}, 2\\text{ KH}$; $Dd \\times dd \\to 2\\text{ KG}, 2\\text{ KH}$. Tổng $= 3\\times 3\\times 2 = 18$ KG và $2\\times 2\\times 2 = 8$ KH."),
         ("Tỉ lệ cây thân cao, hoa đỏ, hạt vàng thuần chủng ($AABBDD$) ở $F_1$ bằng $0$.",
          True, "Bố mẹ có $dd$ nên mọi giao tử của bố mẹ đó đều mang $d$, không thể tạo được kiểu gen $DD$ ở $F_1$."),
         ("Tỉ lệ cây có kiểu hình mang ĐÚNG $2$ tính trạng trội và $1$ tính trạng lặn ở $F_1$ chiếm $\\frac{9}{32}$ ($28.125\\%$).",
          False, "Các kiểu $2$ trội $+ 1$ lặn: $A-B-dd = \\frac{3}{4}\\cdot\\frac{3}{4}\\cdot\\frac{1}{2} = \\frac{9}{32}$; $A-bbD- = \\frac{3}{4}\\cdot\\frac{1}{4}\\cdot\\frac{1}{2} = \\frac{3}{32}$; $aaB-D- = \\frac{1}{4}\\cdot\\frac{3}{4}\\cdot\\frac{1}{2} = \\frac{3}{32}$. Tổng cộng $= \\frac{15}{32} = 46.875\\%$!"),
         ("Tỉ lệ cá thể dị hợp về ÍT NHẤT $1$ cặp gen ở đời con $F_1$ là $\\frac{7}{8}$ ($87.5\\%$).",
          True, "Tỉ lệ cá thể ĐỒNG HỢP tất cả các cặp ($AA/aa$ và $BB/bb$ và $dd$) $= \\frac{1}{2} \\times \\frac{1}{2} \\times \\frac{1}{2} = \\frac{1}{8}$. Lấy $1 - \\frac{1}{8} = \\frac{7}{8}$ có ít nhất $1$ cặp dị hợp.")])

    # TF-047
    add("mendel", "adv", "Tương tác Gen Bổ sung ($9:7$ và $9:6:1$)",
        "Ở một loài cây trồng, màu sắc hoa do $2$ cặp gen không alen phân ly độc lập $A/a$ và $B/b$ cùng chi phối theo kiểu tương tác bổ sung: kiểu gen chứa đồng thời cả alen $A$ và alen $B$ ($A-B-$) cho hoa ĐỎ; các kiểu gen còn lại ($A-bb, aaB-, aabb$) đều cho hoa TRẮNG. Cho giao phấn $P: AaBb \\text{ (hoa đỏ)} \\times Aabb \\text{ (hoa trắng)}$ thu được $F_1$. Xét các nhận định sau:",
        [("Ở thế hệ $F_1$ thu được tỉ lệ phân ly kiểu hình là $3$ cây hoa đỏ : $5$ cây hoa trắng.",
          True, "Từ $Aa \\times Aa \\to \\frac{3}{4}A-$, từ $Bb \\times bb \\to \\frac{1}{2}B-$. Vậy hoa đỏ $A-B- = \\frac{3}{4} \\times \\frac{1}{2} = \\frac{3}{8}$, còn lại $\\frac{5}{8}$ hoa trắng ($3:5$)."),
         ("Nếu cho các cây hoa TRẮNG ở $F_1$ tự thụ phấn riêng rẽ, chắc chắn sẽ xuất hiện một số cây con $F_2$ cho hoa màu ĐỎ.",
          False, "Các cây hoa trắng ở $F_1$ gồm $A-bb$, $aaBb$ và $aabb$ đều thiếu hoàn toàn ít nhất $1$ trong $2$ alen trội $A$ hoặc $B$ nên khi tự thụ phấn không bao giờ tổ hợp lại được $A-B-$ (ra $100\\%$ trắng)."),
         ("Trong số các cây hoa ĐỎ thu được ở $F_1$, tỉ lệ cây có kiểu gen đồng hợp về cặp gen $A$ ($AABb$) chiếm $\\frac{1}{3}$.",
          True, "Các cây hoa đỏ $F_1$ chỉ có $2$ kiểu gen là $\\frac{1}{3} AABb$ và $\\frac{2}{3} AaBb$ (vì từ $Aa\\times Aa$ trong nhóm $A-$ thì $AA=1/3, Aa=2/3$; còn $Bb$ luôn $100\\%$)."),
         ("Nếu cũng vẫn $2$ kiểu gen $AaBb \\times Aabb$ đó nhưng xét tính trạng hình dạng quả di truyền theo tương tác bổ sung $9:6:1$ ($A-B-$ dẹt; $A-bb + aaB-$ tròn; $aabb$ dài) thì đời con thu được $3$ dẹt : $4$ tròn : $1$ dài.",
          True, "Dẹt $= \\frac{3}{8}$; dài $aabb = \\frac{1}{4} \\times \\frac{1}{2} = \\frac{1}{8}$; còn lại tròn $= \\frac{4}{8} \\Rightarrow 3:4:1$.")])

    # TF-048
    add("mendel", "adv", "Tương tác Cộng gộp (Di truyền Đa gen)",
        "Ở một loài thực vật, chiều cao cây do $3$ cặp gen phân ly độc lập ($A/a, B/b, D/d$) tương tác cộng gộp quy định: cây mang toàn alen lặn ($aabbdd$) cao $100\\text{ cm}$, mỗi alen trội có mặt trong kiểu gen làm cây cao thêm $5\\text{ cm}$. Tiến hành phép lai $P: AaBbDd \\times AaBbdd$ thu được $F_1$. Xét các nhận định sau:",
        [("Chiều cao các cây ở đời con $F_1$ phân bố thành $6$ nhóm kiểu hình khác nhau trải từ mức thấp nhất $100\\text{ cm}$ đến cao nhất $125\\text{ cm}$.",
          True, "Số alen trội ở con tối thiểu là $0$ ($aabbdd \\to 100\\text{ cm}$) và tối đa là $5$ ($AABBDd \\to 125\\text{ cm}$) $\\Rightarrow 6$ mức chiều cao ($100, 105, 110, 115, 120, 125\\text{ cm}$)."),
         ("Trong số các cây thu được ở $F_1$, tỉ lệ cây có chiều cao đúng $115\\text{ cm}$ (mang $3$ alen trội) bằng $\\frac{5}{16}$ ($31.25\\%$).",
          True, "Xét phân bố số alen trội của $AaBbDd \\times AaBbdd$ là khai triển $(\\frac{1}{2}A + \\frac{1}{2}a)^4 (\\frac{1}{2}D + \\frac{1}{2}d)^1 = (\\frac{1}{2} + \\frac{1}{2})^5$: xác suất đúng $3$ alen trội $= \\binom{5}{3} (\\frac{1}{2})^5 = \\frac{10}{32} = \\frac{5}{16}$."),
         ("Cây mang chiều cao trung bình $115\\text{ cm}$ ở $F_1$ chỉ có duy nhất $1$ kiểu gen là $AaBbDd$.",
          False, "Tất cả mọi kiểu gen có tổng cộng $3$ alen trội (như $AABbdd, AaBBdd, AABbDd$...) đều cao $115\\text{ cm}$: cụ thể $AaBbDd$ chiếm $\\frac{1}{8}$ nhưng tổng nhóm $115\\text{ cm}$ tới $\\frac{5}{16}$, có tới nhiều kiểu gen khác nhau."),
         ("Khi lấy ngẫu nhiên các cây $125\\text{ cm}$ ($AABBDd$) ở $F_1$ cho giao phấn ngẫu nhiên với nhau thì $100\\%$ đời $F_2$ thu được sẽ có chiều cao đồng nhất $125\\text{ cm}$.",
          False, "$AABBDd \\times AABBDd$ phân ly cặp $Dd$ tạo $AABBDD$ ($130\\text{ cm}$), $AABBDd$ ($125\\text{ cm}$) và $AABBdd$ ($120\\text{ cm}$) theo tỉ lệ $1:2:1$.")])

    # TF-049
    add("mendel", "adv", "Hoán vị gen ở Hai giới (Thực vật)",
        "Ở một loài cây trồng tự thụ phấn, alen $A$ (thân cao) trội hoàn toàn so với $a$ (thân thấp), alen $B$ (quả tròn) trội hoàn toàn so với $b$ (quả dài). Hai gen cùng nằm trên một cặp NST thường cách nhau $20\\text{ cM}$ (hoán vị gen xảy ra ở cả hai giới với tần số $f = 20\\%$). Cho một cây thân cao, quả tròn dị hợp đối $\\frac{Ab}{aB}$ tự thụ phấn thu được $F_1$. Xét các nhận định sau:",
        [("Cây $\\frac{Ab}{aB}$ tạo ra $4$ loại giao tử với tỉ lệ bằng $\\underline{Ab} = \\underline{aB} = 40\\%$ và $\\underline{AB} = \\underline{ab} = 10\\%$.",
          True, "Với $f = 20\\%$, mỗi loại giao tử hoán vị chiếm $f/2 = 10\\%$ ($\\underline{AB}, \\underline{ab}$) và giao tử liên kết chiếm $50\\% - 10\\% = 40\\%$ ($\\underline{Ab}, \\underline{aB}$)."),
         ("Tỉ lệ cây thân thấp, quả dài ($\\frac{ab}{ab}$) thu được ở thế hệ $F_1$ là $1\\%$ ($0.01$).",
          True, "$f(\\frac{ab}{ab}) = 0.10 \\times 0.10 = 0.01 = 1\\%$."),
         ("Tỉ lệ cây thân cao, quả dài thuần chủng ($\\frac{Ab}{Ab}$) ở $F_1$ chiếm $24\\%$.",
          False, "$A-bb = 0.25 - 0.01 = 24\\%$, nhưng trong đó gồm $2$ kiểu gen $\\frac{Ab}{Ab}$ ($0.4^2 = 16\\%$) và $\\frac{Ab}{ab}$ ($2\\times 0.4\\times 0.1 = 8\\%$); vậy kiểu gen thuần chủng $\\frac{Ab}{Ab}$ chỉ chiếm $16\\%$!"),
         ("Trong tổng số các cây thân cao, quả tròn ($A-B-$) ở $F_1$, số cây mang kiểu gen đồng hợp $2$ cặp gen ($\\frac{AB}{AB}$) chỉ chiếm tỉ lệ $\\frac{1}{51}$.",
          True, "$A-B- = 0.50 + 0.01 = 51\\%$, trong đó $\\frac{AB}{AB} = 0.10^2 = 1\\% \\Rightarrow$ tỷ lệ $= \\frac{1}{51}$!")])

    # TF-050
    add("mendel", "hsg", "Ruồi giấm - Hoán vị gen Một giới",
        "Ở ruồi giấm (*Drosophila melanogaster*), tính trạng thân xám ($A$) trội hoàn toàn so với thân đen ($a$); cánh dài ($B$) trội hoàn toàn so với cánh cụt ($b$), hai gen cùng nằm trên NST thường số II cách nhau $20\\text{ cM}$. Đặc trưng sinh học của ruồi giấm là hoán vị gen CHỈ xảy ra ở con CÁI (con đực liên kết hoàn toàn $f=0$). Cho ruồi cái $\\frac{Ab}{aB}$ giao phối với ruồi đực $\\frac{Ab}{aB}$ thu được $F_1$. Xét các nhận định sau:",
        [("Vì cả bố và mẹ đều có kiểu gen dị hợp chéo $\\frac{Ab}{aB}$ nên chắc chắn xuất hiện kiểu hình ruồi thân đen, cánh cụt ($\\frac{ab}{ab}$) ở $F_1$ với tỉ lệ $1\\%$.",
          False, "Ruồi đực $\\frac{Ab}{aB}$ không hoán vị nên chỉ tạo $\\frac{1}{2}\\underline{Ab} : \\frac{1}{2}\\underline{aB}$ (hoàn toàn KHÔNG tạo giao tử $\\underline{ab}$!), do đó tỉ lệ $\\frac{ab}{ab}$ ở $F_1$ bằng $0\\%$!"),
         ("Số loại kiểu gen tối đa thu được ở thế hệ $F_1$ của phép lai này là $7$ kiểu gen và tỉ lệ kiểu hình $F_1$ là $2$ xám-dài : $1$ xám-cụt : $1$ đen-dài.",
          True, "Từ cái ($0.4\\underline{Ab}, 0.4\\underline{aB}, 0.1\\underline{AB}, 0.1\\underline{ab}$) $\\times$ đực ($0.5\\underline{Ab}, 0.5\\underline{aB}$): tạo $7$ KG ($\\frac{AB}{Ab}, \\frac{AB}{aB}, \\frac{Ab}{Ab}, \\frac{Ab}{aB}, \\frac{aB}{aB}, \\frac{Ab}{ab}, \\frac{aB}{ab}$), kiểu hình luôn là $50\\%$ $A-B-$ : $25\\%$ $A-bb$ : $25\\%$ $aaB-$ ($2:1:1$)."),
         ("Tỉ lệ ruồi thân xám, cánh dài ($A-B-$) có kiểu gen dị hợp $2$ cặp gen $\\frac{Ab}{aB}$ ở $F_1$ bằng $40\\%$ tính trên tổng toàn bộ đàn con.",
          True, "$f(\\frac{Ab}{aB}) = 0.4(\\underline{Ab}) \\times 0.5(\\underline{aB}) + 0.4(\\underline{aB}) \\times 0.5(\\underline{Ab}) = 0.20 + 0.20 = 40\\%$."),
         ("Thú vị hơn, cho ruồi cái dị hợp ĐỀU $\\frac{AB}{ab}$ (hoán vị $f=20\\%$) lai với ruồi đực dị hợp ĐỀU $\\frac{AB}{ab}$ ($f=0\\%$) cũng vẫn thu được $7$ kiểu gen nhưng tỉ lệ đồng hợp lặn $\\frac{ab}{ab}$ khi đó sẽ bằng $20\\%$.",
          True, "Từ cái ($0.4\\underline{ab}$) $\\times$ đực ($0.5\\underline{ab}$) thu được $\\frac{ab}{ab} = 0.4 \\times 0.5 = 0.20 = 20\\%$, khi đó tỉ lệ KH là $70\\%$ $A-B-$ : $5\\%$ $A-bb$ : $5\\%$ $aaB-$ : $20\\%$ $aabb$.")])

    # TF-051
    add("mendel", "basic", "Di truyền Liên kết Giới tính trên NST X",
        "Trong thí nghiệm nổi tiếng năm 1910 của T.H. Morgan trên ruồi giấm về gen quy định màu mắt nằm trên vùng không tương đồng của NST X ($W$: mắt đỏ trội hoàn toàn so với $w$: mắt trắng). Xét hai phép lai thuận và nghịch thuần chủng: Phép lai thuận: $\\text{Cái mắt đỏ } X^W X^W \\times \\text{Đực mắt trắng } X^w Y$; Phép lai nghịch: $\\text{Cái mắt trắng } X^w X^w \\times \\text{Đực mắt đỏ } X^W Y$. Xét các nhận định sau:",
        [("Ở $F_1$ của phép lai thuận, toàn bộ $100\\%$ ruồi đực và cái đều đồng loạt biểu hiện mắt đỏ, nhưng nếu cho $F_1$ giao phối tạo $F_2$ thì tất cả ruồi mắt trắng đều tập trung ở giới ĐỰC.",
          True, "$F_1$: $X^W X^w \\times X^W Y \\rightarrow F_2$: $1 X^W X^W : 1 X^W X^w : 1 X^W Y : 1 X^w Y$ (toàn bộ ruồi cái mắt đỏ, một nửa ruồi đực mắt trắng)."),
         ("Ở ngay thế hệ $F_1$ của phép lai nghịch, kết quả phân ly kiểu hình khác nhau giữa 2 giới: $100\\%$ ruồi cái mắt ĐỎ ($X^W X^w$) và $100\\%$ ruồi đực mắt TRẮNG ($X^w Y$) — biểu hiện quy luật di truyền chéo.",
          True, "Con đực nhận X trực tiếp từ mẹ trắng ($X^w$) còn con cái nhận X từ bố đỏ ($X^W$)."),
         ("Nếu cho ruồi mắt trắng $X^w Y$ giao phối với ruồi cái $F_1$ của phép lai thuận ($X^W X^w$) thì tỉ lệ ruồi ĐỰC mắt trắng trong tổng số cá thể đời con chỉ chiếm $50\\%$.",
          False, "$X^W X^w \\times X^w Y \\rightarrow \\frac{1}{4} X^W X^w : \\frac{1}{4} X^w X^w : \\frac{1}{4} X^W Y : \\frac{1}{4} X^w Y$. Do đó ruồi đực mắt trắng chiếm $25\\%$ tổng số đời con (chiếm $50\\%$ trong riêng nhóm con đực)."),
         ("Trong tự nhiên ở chim, bướm và cá, hệ NST giới tính có cặp đồng giao ở con đực ($ZZ$) và dị giao ở con cái ($ZW$), nên gen lặn trên Z sẽ biểu hiện di truyền chéo theo chiều mẹ $Z^a W$ truyền cho con trống và bố truyền cho con mái.",
          True, "Quy luật di truyền chéo trên Z luôn đi từ $Z$ của bố $\\rightarrow$ con mái $ZW$, còn $Z$ của mẹ chỉ đi về con trống $ZZ$.")])

    # TF-052
    add("mendel", "hsg", "Phối hợp Tương tác Gen & Liên kết NST Z",
        "Ở gà ($ZZ$ là trống, $ZW$ là mái), tính trạng màu lông do $2$ gen tương tác bổ sung quy định: kiểu gen có đồng thời cả alen $A$ và $B$ ($A-B-$) quy định lông màu XÁM, các kiểu gen còn lại cho lông TRẮNG. Trong đó gen $A/a$ nằm trên NST thường; gen $B/b$ nằm trên vùng không tương đồng của NST giới tính Z. Thực hiện phép lai $P: Aa Z^B Z^b \\text{ (trống xám)} \\times Aa Z^b W \\text{ (mái trắng)}$ thu được $F_1$. Xét các phân tích sau:",
        [("Số loại kiểu gen tối đa có thể xuất hiện ở đàn gà con $F_1$ bằng $12$ kiểu gen ($3 \\times 4$).",
          True, "$Aa \\times Aa \\to 3\\text{ KG}$; $Z^B Z^b \\times Z^b W \\to 4\\text{ KG}$ ($Z^B Z^b, Z^b Z^b, Z^B W, Z^b W$). Tổng $3 \\times 4 = 12\\text{ KG}$."),
         ("Tổng tỉ lệ gà con có bộ lông màu XÁM thu được ở thế hệ $F_1$ chiếm $37.5\\%$ ($\\frac{3}{8}$), trong đó chia đều bằng nhau giữa gà trống xám và gà mái xám.",
          True, "$A- = \\frac{3}{4}$; ở cặp Z thu $\\frac{1}{4} Z^B Z^b$ (trống $B-$) và $\\frac{1}{4} Z^B W$ (mái $B-$). Vậy trống xám $= \\frac{3}{16}$, mái xám $= \\frac{3}{16}$, tổng xám $= \\frac{6}{16} = \\frac{3}{8} = 37.5\\%$."),
         ("Tỉ lệ gà con lông TRẮNG thu được ở $F_1$ chiếm $\\frac{5}{8}$ và tất cả các gà lông trắng này chỉ có thể là gà mái.",
          False, "Cả trống và mái đều có thể có lông trắng (như $aa Z^B Z^b$ hay $AA Z^b Z^b$), trong đó trống trắng chiếm $\\frac{5}{16}$ và mái trắng cũng chiếm $\\frac{5}{16}$."),
         ("Nếu cho tất cả gà trống lông xám và gà mái lông xám ở $F_1$ giao phối ngẫu nhiên tạo $F_2$, tỉ lệ gà con lông TRẮNG ở $F_2$ thu được bằng $\\frac{1}{3}$ ($\\approx 33.33\\%$).",
          True, "Nhóm xám $F_1$ gồm $(\\frac{1}{3}AA : \\frac{2}{3}Aa) Z^B Z^b \\times (\\frac{1}{3}AA : \\frac{2}{3}Aa) Z^B W$. Tỉ lệ $A- = 1 - (\\frac{1}{3})^2 = \\frac{8}{9}$; tỉ lệ $B- = \\frac{3}{4}$. Vậy xám $F_2 = \\frac{8}{9} \\times \\frac{3}{4} = \\frac{2}{3} \\Rightarrow$ lông trắng $F_2 = 1 - \\frac{2}{3} = \\frac{1}{3}$!")])

    # TF-053
    add("mendel", "adv", "Di truyền Ngoài nhân (Tế bào chất)",
        "Phân tích đặc điểm di truyền của các gen nằm trong ty thể và lục lạp thông qua thí nghiệm lai thuận nghịch trên cây hoa phấn (*Mirabilis jalapa*) của C. Correns và bệnh động kinh rung giật cơ (MERRF) do đột biến ADN ty thể ở người:",
        [("Ở cây hoa phấn, khi lấy hạt phấn từ cành lá ĐỐM thụ phấn cho hoa trên cành lá XANH hoàn toàn, đời con thu được có $50\\%$ lá xanh và $50\\%$ lá đốm.",
          False, "Di truyền ngoài nhân tuân theo dòng MẸ: tế bào hạt phấn gần như không đóng góp bào tương (lục lạp) cho hợp tử; khi mẹ lá xanh nhận phấn bất kể cành nào thì $100\\%$ cây con đều lá XANH."),
         ("Nếu cho hạt phấn từ hoa lá xanh thụ phấn cho nhụy trên cành lá KHẢM (chứa hỗn hợp lục lạp xanh bình thường và lục lạp trắng đột biến trong bào tương noãn), đời con có thể xuất hiện đồng thời cả cây lá xanh, cây lá trắng và cây lá khảm với tỉ lệ không cố định.",
          True, "Sự phân chia tế bào chất không đồng đều trong nguyên phân/giảm phân hình thành noãn trên cành khảm tạo ra $3$ loại tế bào trứng chứa toàn lạp xanh, toàn lạp trắng hoặc hỗn hợp lạp xanh-trắng."),
         ("Ở người, một người đàn ông mắc bệnh di truyền do đột biến gen ty thể ($mtADN$) kết hôn với người phụ nữ có ty thể hoàn toàn bình thường sẽ truyền alen bệnh cho $100\\%$ các con gái của anh ta.",
          False, "Người đàn ông mang ty thể bệnh KHÔNG truyền ty thể cho các con (duy nhất trứng của người mẹ cung cấp ty thể cho phôi hợp tử; đuôi tinh trùng mang ty thể hầu hết bị phá hủy khi thụ tinh)."),
         ("Mọi người con của một người mẹ mang hoàn toàn ty thể đồng hợp đột biến gây bệnh teo dây thần kinh thị giác Leber (LHON) đều thừa hưởng các phân tử ty thể đột biến từ mẹ bất kể giới tính nam hay nữ.",
          True, "Ty thể di truyền thẳng theo dòng mẹ (maternal inheritance) cho cả con trai lẫn con gái.")])

    # TF-054
    add("mendel", "basic", "Mức phản ứng & Ảnh hưởng Môi trường",
        "Mối quan hệ tương tác giữa kiểu gen, môi trường và kiểu hình được thể hiện rõ ở hai hiện tượng sinh học quen thuộc: (1) Cây hoa cẩm tú cầu (*Hydrangea macrophylla*) có cùng kiểu gen nhưng trồng ở đất chua giàu $Al^{3+}$ ra hoa xanh lam còn trồng ở đất kiềm ra hoa hồng; (2) Thỏ Himalaya thuần chủng có lông trắng toàn thân nhưng chóp tai, chóp mũi, bàn chân và đuôi lại đen tuyền. Xét các nhận định sau:",
        [("Tập hợp tất cả các màu hoa khác nhau mà cùng một kiểu gen hoa cẩm tú cầu có thể biểu hiện ra tương ứng với các độ pH đất khác nhau gọi là mức phản ứng của kiểu gen đó.",
          True, "Mức phản ứng là tập hợp các kiểu hình của CÙNG MỘT KIỂU GEN tương ứng với các điều kiện môi trường khác nhau."),
         ("Ở thỏ Himalaya, sở dĩ các vùng đầu mút như tai, mũi, bàn chân có màu lông đen là do nhiệt độ ngoại vi ở các vùng này mát lạnh hơn thân mình ($< 33^\\circ\\text{C}$), cho phép enzyme tổng hợp sắc tố melanin hoạt động.",
          True, "Enzyme tyrosinase ở giống thỏ này mang đột biến nhạy nhiệt: mất hoạt tính ở thân ấm ($\\sim 37^\\circ\\text{C}$) nhưng hoạt động bình thường ở vùng mút lạnh ($\\sim 25-32^\\circ\\text{C}$)."),
         ("Nếu cạo sạch lông trắng trên lưng một con thỏ Himalaya rồi chườm túi nước đá lạnh liên tục lên vùng da vừa cạo cho tới khi lông mọc lại, lông mọc lên vẫn hoàn toàn giữ màu trắng vì kiểu gen quy định vùng lưng không bao giờ đen được.",
          False, "Chính kiểu gen nhạy nhiệt phản ứng với nhiệt độ thấp tại vùng lưng được chườm lạnh sẽ kích hoạt enzyme tổng hợp melanin làm vùng lông mọc mới ở lưng có màu ĐEN!"),
         ("Bố mẹ không truyền trực tiếp các kiểu hình đã hình thành sẵn (như vết sẹo hay màu hoa xanh do pH) cho con, mà truyền cho con một kiểu gen quy định giới hạn mức phản ứng trước môi trường.",
          True, "Tính trạng chất lượng thường có mức phản ứng hẹp, tính trạng số lượng (năng suất, cân nặng) thường có mức phản ứng rộng.")])

    # TF-055
    add("mendel", "hsg", "Lập Bản đồ 3 Điểm Gen (Three-point Cross)",
        "Một cá thể dị hợp $3$ cặp gen ($A/a, B/b, C/c$) nằm trên cùng $1$ cặp NST thường được lai phân tích thu được $1000$ cá thể đời con $F_a$ gồm $8$ tổ hợp giao tử: $ABC = 420$; $abc = 424$; $aBC = 48$; $Abc = 48$; $ABc = 28$; $abC = 28$; $AbC = 2$; $aBc = 2$. Xét các kết luận sau:",
        [("Hai lớp giao tử bố mẹ ban đầu (không có trao đổi chéo) là $\\underline{ABC}$ và $\\underline{abc}$, tương ứng kiểu gen dị hợp đều $\\frac{ABC}{abc}$.",
          True, "$420 + 424 = 844$ ($84.4\\%$) chiếm đa số tuyệt đối nên là giao tử liên kết ban đầu."),
         ("Từ hai lớp trao đổi chéo kép ít nhất ($AbC = 2, aBc = 2$) suy ra trật tự sắp xếp của $3$ gen trên nhiễm sắc thể là $B - A - C$ (tức $A$ nằm giữa).",
          False, "So với lớp bố mẹ $\\underline{ABC}$, tổ hợp chéo kép $\\underline{AbC}$ chỉ đảo một mình alen $b$ (còn $A$ và $C$ giữ nguyên vị trí tương đối), chứng tỏ **$B$** nằm chính giữa: trật tự đúng là $A - B - C$."),
         ("Khoảng cách di truyền giữa $A$ và $B$ bằng $10.0\\text{ cM}$ và khoảng cách giữa $B$ và $C$ bằng $6.0\\text{ cM}$.",
          True, "$d(A-B) = \\frac{48+48+2+2}{1000}\\times 100 = 10.0\\text{ cM}$; $d(B-C) = \\frac{28+28+2+2}{1000}\\times 100 = 6.0\\text{ cM}$."),
         ("Số lượng cá thể trao đổi chéo kép KỲ VỌNG (nếu hai đoạn trao đổi chéo hoàn toàn độc lập) là $6$ cá thể, nhưng thực tế chỉ quan sát được $4$ cá thể, chứng tỏ có hiện tượng nhiễu dương với $CoC = \\frac{2}{3}$ và hệ số nhiễu $I = \\frac{1}{3}$.",
          True, "Kỳ vọng $= 0.10 \\times 0.06 \\times 1000 = 6$; $CoC = \\frac{4}{6} = \\frac{2}{3}$ và nhiễu $I = 1 - CoC = \\frac{1}{3} \\approx 33.3\\%$.")])

    # TF-056
    add("mendel", "adv", "Gen Đa hiệu & Tương tác Át chế",
        "Xét hai hiện tượng di truyền quan trọng: (1) Một gen đột biến $Hb^S$ ở người gây đồng thời hồng cầu hình liềm, tắc nghẽn vi mạch, tổn thương lách và suy thận; (2) Màu lông ở chó Labrador Retriever do $2$ gen độc lập: gen $B/b$ quy định sắc tố đen ($B-$) hay nâu ($bb$), nhưng gen $E/e$ kiểm soát khả năng lắng đọng sắc tố lên lông ($ee$ ngăn tất cả sắc tố gắn vào lông tạo lông vàng bất kể $B$ hay $b$). Xét các nhận định sau:",
        [("Hiện tượng đột biến ở một gen $Hb^S$ ảnh hưởng hàng loạt tới nhiều tính trạng và cơ quan khác nhau trong cơ thể được gọi là tác động đa hiệu của gen (Pleiotropy).",
          True, "Sản phẩm của một gen tham gia con đường chuyển hóa hoặc cấu trúc thiết yếu sẽ dẫn tới chuỗi tác động hệ quả đa cơ quan."),
         ("Khi cho lai hai con chó Labrador đều dị hợp $2$ cặp gen lông đen ($BbEe \\times BbEe$), đời con phân ly kiểu hình theo tỉ lệ $9$ đen : $3$ nâu : $4$ vàng.",
          True, "$9 B-E-$ (đen) : $3 bbE-$ (nâu) : $(3 B-ee + 1 bbee)$ (vàng) $= 9:3:4$ — kiểu tương tác át chế lặn ($ee$ át chế locus $B/b$)."),
         ("Khi lai chó Labrador lông VÀNG ($BBee$) với chó lông VÀNG ($bbee$), đời con chắc chắn thu được $100\\%$ chó con lông NÂU hoặc ĐEN nhờ hiện tượng bổ sung phục hồi màu tối.",
          False, "$BBee \\times bbee \\rightarrow 100\\% Bbee$ mang $ee$ nên vẫn $100\\%$ lông VÀNG; chỉ khi lai $BBee$ với $bbEE$ (hoặc $bbEe$) mới ra được $BbEe$ lông ĐEN."),
         ("Kiểu gen gây hội chứng Marfan ở người (đột biến gen *FBN1* mã hóa fibrillin-1 gây chân tay dài bất thường, trật thủy tinh thể mắt và phình vỡ động mạch chủ) cũng tuân theo quy luật tương tác $2$ cặp gen bổ sung hoàn toàn không liên quan đa hiệu.",
          False, "Hội chứng Marfan cũng là ví dụ điển hình cho TÍNH ĐA HIỆU của một gen đột biến trội đơn lẻ (*FBN1*) gây khiếm khuyết mô liên kết toàn cơ thể.")])

    # TF-057
    add("mendel", "hsg", "Phối hợp Độc lập & Hoán vị Gen",
        "Ở một loài thực vật giao phấn, $3$ cặp gen quy định $3$ tính trạng trội hoàn toàn ($A>a$, $B>b$, $D>d$). Phép lai $P: Aa \\frac{BD}{bd} \\times Aa \\frac{Bd}{bD}$ thu được $F_1$. Biết hoán vị gen xảy ra ở cả hai giới với tần số $f = 40\\%$. Xét các tính toán ở đời con $F_1$:",
        [("Số loại kiểu gen tối đa có thể xuất hiện ở đời con $F_1$ là $3 \\times 9 = 27$ kiểu gen.",
          False, "Cặp $Aa \\times Aa$ cho $3$ kiểu gen; cặp liên kết hoán vị ở cả $2$ giới $\\frac{BD}{bd} \\times \\frac{Bd}{bD}$ tạo tối đa $10$ kiểu gen trên cặp NST đó. Tổng số KG $= 3 \\times 10 = 30$ kiểu gen!"),
         ("Tỉ lệ kiểu gen mang đồng thời cả $3$ cặp gen đồng hợp lặn ($aa \\frac{bd}{bd}$) ở $F_1$ chiếm $1.5\\%$ ($0.015$).",
          True, "Cặp $Aa \\times Aa \\to 0.25 aa$. Ở cặp liên kết: $\\frac{BD}{bd}$ tạo $0.30 \\underline{bd}$; $\\frac{Bd}{bD}$ tạo $0.20 \\underline{bd} \\Rightarrow \\frac{bd}{bd} = 0.30 \\times 0.20 = 0.06$. Vậy $aa \\frac{bd}{bd} = 0.25 \\times 0.06 = 0.015 = 1.5\\%$."),
         ("Tỉ lệ cá thể ở $F_1$ mang kiểu hình lặn về cặp $A$ nhưng trội về cả hai tính trạng $B$ và $D$ ($aa B-D-$) bằng $14.0\\%$.",
          True, "Từ $\\frac{bd}{bd} = 0.06$, áp dụng hệ thức $B-D- = 0.50 + \\frac{bd}{bd} = 0.56$. Nhân $0.25 aa \\times 0.56 = 0.14 = 14.0\\%$!"),
         ("Tỉ lệ kiểu hình mang ĐÚNG $1$ tính trạng trội và $2$ tính trạng lặn ở $F_1$ là $24.5\\%$.",
          False, "Tính chính xác: từ $\\frac{bd}{bd}=0.06 \\Rightarrow B-dd = bbD- = 0.25 - 0.06 = 0.19$. Các trường hợp $1$ trội $2$ lặn: $A-bbdd = 0.75\\times 0.06 = 0.045$; $aa B-dd = 0.25\\times 0.19 = 0.0475$; $aa bbD- = 0.25\\times 0.19 = 0.0475$. Tổng $= 0.045 + 0.095 = 0.14 = 14.0\\%$, không phải $24.5\\%$!")])

    # TF-058
    add("mendel", "adv", "Alen Gây chết (Lethal Alleles)",
        "Ở chuột, gen quy định màu lông gồm alen trội $A^Y$ (lông vàng) và alen lặn $A$ (lông xám/nâu kiểu dại). Tuy nhiên, alen $A^Y$ đồng thời gây chết giai đoạn phôi ở trạng thái đồng hợp $A^Y A^Y$ (biến tính gen thiết yếu lân cận). Khi cho lai các con chuột lông vàng với nhau ($P: A^Y A \\times A^Y A$), xét đàn chuột con sinh ra còn sống ở $F_1$:",
        [("Tỉ lệ phân ly kiểu hình của các con chuột con SỐNG SÓT sinh ra ở $F_1$ là $2$ lông vàng : $1$ lông xám (thay vì $3:1$).",
          True, "Tổ hợp hợp tử $1 A^Y A^Y \\text{ (chết)} : 2 A^Y A \\text{ (vàng)} : 1 AA \\text{ (xám)}$, do đó trong số con sống sót luôn phân ly $2$ vàng : $1$ xám."),
         ("Mọi con chuột lông vàng trưởng thành đang sống trong đàn thực chất đều mang kiểu gen DỊ HỢP tử ($A^Y A$), không bao giờ tồn tại dòng chuột lông vàng thuần chủng.",
          True, "Do $A^Y A^Y$ chết ngay từ giai đoạn phôi sớm nên bất kỳ cá thể vàng nào sống được đều là $A^Y A$."),
         ("Nếu cho một con chuột lông vàng ($A^Y A$) giao phối với một con chuột lông xám ($AA$), tỉ lệ chuột chết phôi vẫn là $25\\%$ và đời con sống phân ly $2:1$.",
          False, "$A^Y A \\times AA \\to \\frac{1}{2} A^Y A \\text{ (vàng)} : \\frac{1}{2} AA \\text{ (xám)}$; không hề xuất hiện đồng hợp $A^Y A^Y$ nên tỷ lệ phôi chết do alen này bằng $0\\%$ và tỉ lệ phân ly là $1:1$."),
         ("Hiện tượng mất đi một tổ hợp kiểu gen đồng hợp ở đời con là một ví dụ cho thấy yếu tố sức sống / chọn lọc phôi có thể làm biến đổi tỉ lệ kiểu hình lý thuyết kinh điển của Mendel.",
          True, "Các gen gây chết lặn hoặc trội có hiệu ứng gây chết lặn ở đồng hợp tử đều biến đổi tỷ lệ $3:1$ kinh điển thành $2:1$.")])

    # TF-059
    add("mendel", "hsg", "Suy luận Kiểu gen & Tần số Hoán vị ngược từ $F_2$",
        "Ở một loài thực vật, xét $2$ cặp gen cùng nằm trên $1$ cặp NST thường: $A$ (quả đỏ) trội hoàn toàn $a$ (quả vàng); $B$ (quả ngọt) trội hoàn toàn $b$ (quả chua). Hai phép lai tự thụ phấn độc lập (tần số hoán vị bằng nhau ở 2 giới): Ở thí nghiệm $1$, cây dị hợp $2$ cặp gen $X$ tự thụ cho $F_2$ có $16\\%$ $aabb$; Ở thí nghiệm $2$, cây dị hợp $2$ cặp gen $Y$ tự thụ cho $F_2$ có $4\\%$ $aabb$. Xét các suy luận sau:",
        [("Kiểu gen của cây $X$ là dị hợp đều $\\frac{AB}{ab}$ với tần số hoán vị gen $f = 20\\%$.",
          True, "$aabb = 0.16 \\Rightarrow \\underline{ab} = 0.40 > 0.25$ nên là giao tử liên kết $\\frac{AB}{ab}$, $f = 2(0.5 - 0.4) = 20\\%$."),
         ("Kiểu gen của cây $Y$ cũng là dị hợp đều $\\frac{AB}{ab}$ nhưng với tần số hoán vị gen $f = 10\\%$.",
          False, "Do $\\underline{ab} = \\sqrt{0.04} = 0.20 < 0.25$, cây $Y$ có kiểu gen dị hợp chéo $\\frac{Ab}{aB}$ với $f = 2 \\times 0.20 = 40\\%$."),
         ("Ở $F_2$ của thí nghiệm $1$, tỉ lệ cây quả đỏ, quả ngọt ($A-B-$) chiếm $66\\%$ tổng số cây thu được.",
          True, "$A-B- = 0.50 + 0.16 = 0.66 = 66\\%$."),
         ("Ở $F_2$ của thí nghiệm $2$, tổng tỉ lệ các cây dị hợp $2$ cặp gen (cả $\\frac{AB}{ab}$ và $\\frac{Ab}{aB}$) bằng đúng $26\\%$.",
          True, "Cây $Y$ tạo $0.3\\underline{Ab} : 0.3\\underline{aB} : 0.2\\underline{AB} : 0.2\\underline{ab}$. Tự thụ tạo $\\frac{Ab}{aB} = 2(0.3)(0.3) = 18\\%$ và $\\frac{AB}{ab} = 2(0.2)(0.2) = 8\\%$. Tổng cộng $18\\% + 8\\% = 26\\%$!")])

    # TF-060
    add("mendel", "basic", "Liên kết Gen Hoàn toàn vs Hoán vị Gen",
        "So sánh phép lai giữa hai cây dị hợp $2$ cặp gen $P: \\frac{AB}{ab} \\times \\frac{AB}{ab}$ trong $3$ kịch bản độc lập khác nhau về diễn biến giảm phân của $2$ gen $A/a$ và $B/b$ cùng nằm trên một cặp NST:",
        [("Nếu cả bố và mẹ đều có $f = 0\\%$ (liên kết hoàn toàn), đời con $F_1$ thu được tối đa $10$ loại kiểu gen và $4$ loại kiểu hình.",
          False, "Nếu liên kết hoàn toàn cả 2 bên: $0.5\\underline{AB}, 0.5\\underline{ab} \\times 0.5\\underline{AB}, 0.5\\underline{ab}$ chỉ tạo $3$ kiểu gen ($1 \\frac{AB}{AB} : 2 \\frac{AB}{ab} : 1 \\frac{ab}{ab}$) và $2$ kiểu hình ($3:1$)."),
         ("Nếu chỉ một bên xảy ra hoán vị gen (tạo $4$ loại giao tử) và bên kia liên kết hoàn toàn (tạo $2$ loại giao tử), đời con $F_1$ thu được tối đa $7$ loại kiểu gen.",
          True, "Phép nhân $(4 \\text{ loại}) \\times (2 \\text{ loại})$ giao tử liên kết-hoán vị sinh đúng $7$ kiểu gen phân biệt (chỉ trùng $\\frac{AB}{ab}$)."),
         ("Nếu hoán vị gen xảy ra ở cả hai bên bố và mẹ đều tạo $4$ loại giao tử, số loại kiểu gen tối đa ở $F_1$ tăng lên thành $10$ loại (với $2$ kiểu dị hợp hai cặp là $\\frac{AB}{ab}$ và $\\frac{Ab}{aB}$).",
          True, "Bảng $4\\times 4$ tổ hợp với $2$ kiểu dị hợp kép phân biệt cho $\\frac{4(4+1)}{2} = 10$ kiểu gen."),
         ("Hiện tượng liên kết hoàn toàn làm hạn chế sự xuất hiện các biến dị tổ hợp, góp phần bảo tồn ổn định các nhóm gen quý thường xuyên di truyền cùng nhau.",
          True, "Đây là ý nghĩa di truyền và chọn giống quan trọng của hiện tượng liên kết gen do Morgan phát hiện.")])

    # ==================== TOPIC 5: POPULATION (TF-061 .. TF-075) ====================
    # TF-061
    add("population", "basic", "Cấu trúc Quần thể Tự thụ phấn",
        "Một quần thể thực vật lưỡng bội tự thụ phấn bắt buộc có cấu trúc di truyền ở thế hệ xuất phát $P$ là: $0.20 AA + 0.60 Aa + 0.20 aa = 1$ (không có đột biến, không chọn lọc, sức sống mọi kiểu gen bằng nhau). Xét các nhận định sau về các thế hệ con cháu:",
        [("Tần số tương đối của alen $A$ và alen $a$ tại thế hệ xuất phát $P$ đều bằng nhau ($p(A) = q(a) = 0.50$) và vẫn bảo toàn ở mức $0.50$ tại thế hệ $F_5$.",
          True, "Tự thụ phấn không làm thay đổi tần số alen: $p(A) = 0.20 + 0.60/2 = 0.50$."),
         ("Ở thế hệ $F_1$, thành phần kiểu gen của quần thể là $0.35 AA + 0.30 Aa + 0.35 aa = 1$.",
          True, "$Aa$ giảm một nửa còn $0.30$; lượng giảm $0.30$ chia đều cho $AA$ và $aa$ mỗi bên $+0.15$ thành $0.35 AA$ và $0.35 aa$."),
         ("Ở thế hệ $F_2$, tỉ lệ cây mang kiểu hình trội ($A-$) trong quần thể giảm xuống còn $57.5\\%$ ($0.575$).",
          True, "Ở $F_2$: $Aa = 0.6 \\times (0.5)^2 = 0.15$; $AA = 0.2 + \\frac{0.6 - 0.15}{2} = 0.425$; $aa = 0.425$. Tổng kiểu hình trội $A- = 0.425 + 0.15 = 0.575 = 57.5\\%$ (hoặc $1 - 0.425 = 0.575$)."),
         ("Sau $3$ thế hệ tự thụ phấn ($F_3$), quần thể đạt ngay trạng thái cân bằng Hardy-Weinberg với $2pq = 0.50 Aa$.",
          False, "Tự thụ phấn càng kéo dài thì tỉ lệ dị hợp $Aa$ càng tiến về $0$ ($F_3$ còn $0.075 Aa$), không bao giờ chuyển thành $0.50 Aa$ của ngẫu phối.")])

    # TF-062
    add("population", "adv", "Kiểm định Cân bằng Hardy-Weinberg",
        "Khảo sát một quần thể động vật sinh sản hữu tính (gen trên NST thường gồm $2$ alen $A, a$) tại thế hệ xuất phát $P$: Giới cái ($50\\%$) có cấu trúc $0.5 AA + 0.4 Aa + 0.1 aa = 1$; Giới đực ($50\\%$) có cấu trúc $0.1 AA + 0.4 Aa + 0.5 aa = 1$. Cho quần thể này giao phối ngẫu nhiên tự do qua các thế hệ (không chọn lọc, không đột biến, không di-nhập gen). Xét các phân tích sau:",
        [("Tần số alen $A$ ở giới cái là $p_f = 0.70$, còn ở giới đực là $p_m = 0.30$.",
          True, "Giới cái: $p_f = 0.5 + 0.2 = 0.7$; giới đực: $p_m = 0.1 + 0.2 = 0.3$."),
         ("Ngay sau $1$ thế hệ ngẫu phối ($F_1$), quần thể đã đạt trạng thái cân bằng di truyền Hardy-Weinberg với $0.25 AA + 0.50 Aa + 0.25 aa$.",
          False, "Do $p_f \\neq p_m$ ở $P$, $F_1$ thu được có: $AA = 0.7\\times 0.3 = 0.21$; $aa = 0.3\\times 0.7 = 0.21$; $Aa = 0.7(0.7)+0.3(0.3) = 0.58$ ($0.21 AA + 0.58 Aa + 0.21 aa$, CHƯA cân bằng!). Phải sang **$F_2$** mới đạt cân bằng $0.25:0.50:0.25$!"),
         ("Ở thế hệ $F_1$, tần số alen $A$ đã đồng nhất ở cả con đực và con cái bằng $0.50$, và tỉ lệ kiểu gen dị hợp $Aa$ tại $F_1$ chiếm tới $58\\%$.",
          True, "Mỗi con $F_1$ nhận ngẫu nhiên $1$ NST thường từ mẹ ($0.7 A$) và $1$ từ bố ($0.3 A$), nên $p(F_1) = 0.50$ đều cả 2 giới, còn $Aa = 0.58 > 0.50$."),
         ("Từ thế hệ $F_2$ trở đi, nếu các nhân tố tiến hóa vẫn không tác động, cấu trúc di truyền quần thể ổn định vĩnh viễn ở $0.25 AA + 0.50 Aa + 0.25 aa = 1$.",
          True, "Từ $F_1$ đồng nhất 2 giới ($p=0.5$), sang $F_2$ đạt ngay định luật Hardy-Weinberg $0.25:0.50:0.25$.")])

    # TF-063
    add("population", "adv", "Quần thể Gen Liên kết Giới tính X",
        "Trong một quần thể người lớn đạt trạng thái cân bằng di truyền Hardy-Weinberg (tỉ lệ nam:nữ là $1:1$), bệnh máu khó đông (Hemophilia) do một alen lặn $h$ nằm trên vùng không tương đồng của NST X quy định ($H$ bình thường trội hoàn toàn). Khảo sát ghi nhận tần số nam giới mắc bệnh trong nhóm nam là $5\\%$ ($q(X^h) = 0.05$). Xét các nhận định sau:",
        [("Tỉ lệ phụ nữ mắc bệnh máu khó đông ($X^h X^h$) trong tổng số nữ giới là $0.25\\%$ ($0.0025$), thấp hơn $20$ lần so với tỉ lệ mắc bệnh ở nam giới.",
          True, "Nữ mắc bệnh có tần số $q^2 = 0.05^2 = 0.0025 = 0.25\\%$. Tỷ lệ so với nam $= 0.05 / 0.0025 = 20$ lần."),
         ("Tỉ lệ phụ nữ có kiểu hình bình thường nhưng mang alen gây bệnh ($X^H X^h$) trong nhóm nữ giới chiếm $9.5\\%$ ($0.095$).",
          True, "Trong giới nữ: $2pq = 2 \\times 0.95 \\times 0.05 = 0.095 = 9.5\\%$."),
         ("Nếu chọn ngẫu nhiên một cặp vợ chồng đều KHÔNG mắc bệnh trong quần thể này, xác suất để đứa con trai đầu lòng của họ mắc bệnh máu khó đông bằng $5\\%$.",
          False, "Bố bình thường luôn là $X^H Y$ nên không ảnh hưởng bệnh con trai (chỉ truyền Y cho con trai). Mẹ bình thường có xác suất mang $X^H X^h = \\frac{2pq}{p^2+2pq} = \\frac{2q}{1+q} = \\frac{0.10}{1.05} = \\frac{2}{21}$. Khi xét NẾU đã sinh con trai, xác suất con trai nhận $X^h$ từ mẹ $= \\frac{1}{2} \\times \\frac{2}{21} = \\frac{1}{21} \\approx 4.76\\%$ (nếu xét xác suất vừa là con trai vừa bị bệnh thì còn chia thêm $1/2$ thành $\\frac{1}{42} \\approx 2.38\\%$, trong mọi cách hiểu đều không bằng $5\\%$!)."),
         ("Tần số alen $h$ ở giới nữ ($XX$) và ở giới nam ($XY$) trong quần thể đang cân bằng là hoàn toàn khác nhau ($q_{\\text{nữ}} = 2 q_{\\text{nam}}$).",
          False, "Khi quần thể đạt cân bằng di truyền trên NST X, tần số alen lặn ở cả $2$ giới đã hội tụ bằng nhau: $q_{\\text{nữ}} = q_{\\text{nam}} = q = 0.05$.")])

    # TF-064
    add("population", "hsg", "Chọn lọc Loại bỏ Đồng hợp Lặn trong Ngẫu phối",
        "Một quần thể thực vật giao phấn ngẫu nhiên có thành phần kiểu gen ở giai đoạn hạt nảy mầm thế hệ $P$ là $0.16 AA + 0.48 Aa + 0.36 aa = 1$. Do sâu ăn lá đặc hiệu chỉ phá hủy làm chết $100\\%$ các cây non mang kiểu gen $aa$ trước độ tuổi ra hoa ở MỌI thế hệ; các cây sống sót giao phấn ngẫu nhiên bình thường. Xét các nhận định sau:",
        [("Tỉ lệ cá thể sống sót ra hoa ở thế hệ $P$ là $0.64$, trong đó tỉ lệ kiểu gen của các cây trưởng thành $P$ tham gia sinh sản là $0.25 AA + 0.75 Aa$.",
          True, "Loại $0.36 aa$, phần còn lại $0.64$: $AA = \\frac{0.16}{0.64} = \\frac{1}{4} = 0.25$ và $Aa = \\frac{0.48}{0.64} = \\frac{3}{4} = 0.75$."),
         ("Từ các cây sống sót thế hệ $P$, tần số alen $a$ truyền qua giao tử bằng $0.375$ ($\\frac{3}{8}$), và khi giao phấn ngẫu nhiên tạo thế hệ hạt $F_1$ sẽ cho tỉ lệ hạt $aa$ chiếm $\\frac{9}{64}$ ($\\approx 14.06\\%$).",
          True, "$q_0' = \\frac{0.75}{2} = \\frac{3}{8} = 0.375 \\Rightarrow$ hạt $F_1$ có $aa = (\\frac{3}{8})^2 = \\frac{9}{64}$."),
         ("Sau khi cây $aa$ ở $F_1$ lại tiếp tục bị chết hết, tần số alen $a$ ở các cây trưởng thành $F_1$ còn lại bằng $\\frac{3}{11}$, suy ra tỉ lệ hạt $aa$ bị chết ở thế hệ $F_2$ là $\\frac{9}{100}$ ($9\\%$).",
          False, "$q_1' = \\frac{3/8}{1 + 3/8} = \\frac{3}{11}$, nên ở $F_2$ tỉ lệ hạt $aa = (\\frac{3}{11})^2 = \\frac{9}{121}$ ($\\approx 7.44\\%$), không phải $\\frac{9}{100}$!"),
         ("Theo công thức lặp chuẩn $q_n = \\frac{q_0'}{1 + n \\cdot q_0'}$, tốc độ làm giảm tần số alen $a$ diễn ra rất nhanh ở các thế hệ đầu nhưng chậm dần về sau và rất khó tiệt trừ alen $a$ về $0$ tuyệt đối sau hữu hạn thế hệ.",
          True, "Vì khi $q$ nhỏ, phần lớn alen $a$ nằm ẩn trong kiểu gen dị hợp $Aa$ sống sót nên tốc độ chọn lọc $\\Delta q \\approx -s q^2 (1-q)$ giảm theo bình phương của $q$.")])

    # TF-065
    add("population", "hsg", "Phả hệ Kết hợp Di truyền Quần thể",
        "Ở người, bệnh xơ nang (Cystic Fibrosis) do một alen lặn $a$ nằm trên NST thường quy định (alen trội $A$ bình thường). Trong một quần thể người cân bằng Hardy-Weinberg có tỉ lệ người mắc bệnh xơ nang là $1\\%$ ($0.01$). Anh Minh có kiểu hình bình thường nhưng có em ruột bị mắc bệnh xơ nang; bố mẹ anh Minh đều bình thường. Anh Minh kết hôn với chị Lan — một người phụ nữ bình thường được chọn ngẫu nhiên từ quần thể trên (gia đình bên ngoại không rõ tiền sử bệnh). Xét các nhận định sau:",
        [("Tần số alen lặn $a$ trong quần thể là $q = 0.10$ và tần số alen trội $A$ là $p = 0.90$.",
          True, "$q^2 = 0.01 \\Rightarrow q = 0.10$, $p = 0.90$."),
         ("Xác suất anh Minh mang kiểu gen dị hợp ($Aa$) bằng $\\frac{2}{3}$, còn xác suất chị Lan mang kiểu gen dị hợp ($Aa$) bằng $\\frac{2}{11}$ ($\\approx 18.18\\%$).",
          True, "Bố mẹ Minh đều $Aa \\Rightarrow$ Minh bình thường có $\\frac{2}{3} Aa$. Chị Lan trong nhóm bình thường quần thể ($0.81 AA : 0.18 Aa$) có $\\frac{0.18}{0.99} = \\frac{2}{11} Aa$."),
         ("Xác suất để đứa con đầu lòng của cặp vợ chồng anh Minh - chị Lan là CON GÁI VÀ BỊ BỆNH xơ nang bằng $\\frac{1}{33}$.",
          False, "Xác suất đứa con đầu lòng mắc bệnh ($aa$) $= \\frac{2}{3} \\times \\frac{2}{11} \\times \\frac{1}{4} = \\frac{1}{33}$. Do có thêm điều kiện là CON GÁI (xác suất $\\frac{1}{2}$ độc lập), nên xác suất cần tìm $= \\frac{1}{33} \\times \\frac{1}{2} = \\frac{1}{66}$!"),
         ("Nếu đứa con đầu lòng của anh Minh và chị Lan thực tế sinh ra bị mắc bệnh xơ nang ($aa$), thì xác suất để đứa con thứ hai của họ KHÔNG bị mắc bệnh (bình thường) tăng lên? Không: bằng đúng $\\frac{3}{4}$ ($75\\%$).",
          True, "Khi đã sinh con đầu $aa$, ta biết CHẮC CHẮN $100\\%$ cả anh Minh và chị Lan đều mang kiểu gen $Aa \\times Aa$; do đó xác suất đứa thứ hai bình thường ($A-$) bằng đúng $3/4 = 75\\%$.")])

    # TF-066
    add("population", "adv", "Quần thể Đa alen - Hệ Nhóm máu ABO",
        "Khảo sát một quần thể người lớn đang cân bằng di truyền về hệ nhóm máu ABO ($I^A, I^B$ đồng trội và trội hoàn toàn so với $I^O$). Kết quả thống kê ghi nhận tần số các alen là $p(I^A) = 0.4$, $q(I^B) = 0.2$ và $r(I^O) = 0.4$. Xét các nhận định sau:",
        [("Tỉ lệ phân bố $4$ nhóm máu trong quần thể này lần lượt là: Nhóm A chiếm $48\\%$; Nhóm B chiếm $20\\%$; Nhóm AB chiếm $16\\%$ và Nhóm O chiếm $16\\%$.",
          True, "O $= 0.4^2 = 16\\%$; AB $= 2(0.4)(0.2) = 16\\%$; A $= 0.4^2 + 2(0.4)(0.4) = 0.16 + 0.32 = 48\\%$; B $= 0.2^2 + 2(0.2)(0.4) = 0.04 + 0.16 = 20\\%$. (Tổng $100\\%$)."),
         ("Trong số những người mang nhóm máu A của quần thể, tỉ lệ người có kiểu gen thuần chủng ($I^A I^A$) chiếm tới $50\\%$.",
          False, "Trong $48\\%$ nhóm máu A gồm $16\\% I^A I^A$ và $32\\% I^A I^O$; vậy người thuần chủng $I^A I^A$ chiếm $\\frac{16}{48} = \\frac{1}{3}$ ($\\approx 33.33\\%$), còn dị hợp $I^A I^O$ chiếm $\\frac{2}{3}$."),
         ("Nếu một cặp vợ chồng ngẫu nhiên trong quần thể đều có nhóm máu B kết hôn với nhau, xác suất họ sinh được đứa con đầu lòng mang nhóm máu O ($I^O I^O$) bằng $\\frac{16}{100} = 16\\%$.",
          True, "Trong nhóm B ($4\\% I^B I^B + 16\\% I^B I^O = 20\\%$), tỉ lệ mang dị hợp $I^B I^O$ là $\\frac{16}{20} = \\frac{4}{5}$. Xác suất hai vợ chồng B sinh con O $= \\frac{4}{5} \\times \\frac{4}{5} \\times \\frac{1}{4} = \\frac{16}{100} = 16\\%$!"),
         ("Xác suất chọn ngẫu nhiên được một người có kiểu gen ĐỒNG HỢP (tính chung cho cả $I^A I^A, I^B I^B$ và $I^O I^O$) trong quần thể này bằng $36\\%$.",
          True, "Tổng tỉ lệ đồng hợp $= p^2 + q^2 + r^2 = 0.16 + 0.04 + 0.16 = 0.36 = 36\\%$.")])

    # TF-067
    add("population", "basic", "Vai trò các Nhân tố Tiến hóa",
        "Theo thuyết tiến hóa tổng hợp hiện đại, $5$ nhân tố tiến hóa cơ bản tác động làm biến đổi cấu trúc di truyền của quần thể là: Đột biến, Di-nhập gen, Chọn lọc tự nhiên, Các yếu tố ngẫu nhiên và Giao phối không ngẫu nhiên. Xét bảng đối chiếu tính chất của các nhân tố này:",
        [("Chỉ có duy nhất $2$ nhân tố là Đột biến và Di-nhập gen có khả năng làm giàu thêm vốn gen của quần thể bằng cách trực tiếp bổ sung các alen hoàn toàn mới.",
          True, "Đột biến phát sinh alen mới từ trong quần thể; di-nhập gen đưa alen mới từ quần thể khác tới."),
         ("Cả Chọn lọc tự nhiên và Các yếu tố ngẫu nhiên (phiêu bạt di truyền) đều có khả năng làm nghèo vốn gen và giảm sự đa dạng di truyền của quần thể.",
          True, "CLTN loại bỏ alen kém thích nghi; phiêu bạt ngẫu nhiên làm mất ngẫu nhiên các alen (đặc biệt alen hiếm) khỏi quần thể nhỏ."),
         ("Giao phối không ngẫu nhiên vừa trực tiếp làm tăng tỉ lệ đồng hợp tử vừa làm biến đổi mạnh tần số tương đối của các alen theo hướng tăng dần alen trội.",
          False, "Giao phối không ngẫu nhiên KHÔNG làm thay đổi tần số alen của quần thể (chỉ làm giảm dị hợp tử và tăng đồng hợp tử)."),
         ("Các yếu tố ngẫu nhiên (thiên tai, lũ lụt, dịch bệnh bất ngờ) tác động càng mạnh mẽ nhất lên những quần thể có kích thước càng lớn (hàng triệu cá thể).",
          False, "Ngược lại: sai số ngẫu nhiên tác động CỰC MẠNH ở những quần thể có kích thước NHỎ; quần thể càng lớn thì biến động ngẫu nhiên càng yếu.")])

    # TF-068
    add("population", "adv", "Các Hình thức Chọn lọc Tự nhiên",
        "Trong sinh học tiến hóa, chọn lọc tự nhiên tác động lên các tính trạng phân bố liên tục (như kích thước, khối lượng, màu sắc) theo $3$ hình thức chính: Chọn lọc ổn định, Chọn lọc vận động (định hướng) và Chọn lọc phân hóa. Xét các nhận định phân biệt $3$ hình thức này:",
        [("Chọn lọc ổn định xảy ra khi điều kiện môi trường ít thay đổi trong thời gian dài, không làm thay đổi giá trị trung bình của quần thể mà lại mở rộng biên độ phương sai ra gấp đôi.",
          False, "Chọn lọc ổn định thu hẹp biên độ biến dị (GIẢM phương sai) do đào thải hai cực, giữ chặt kiểu hình trung bình tối ưu."),
         ("Chọn lọc vận động (định hướng) làm dịch chuyển giá trị trung bình của tính trạng về một phía thích nghi hơn, ví dụ sự phát triển chiều cao hươu cao cổ hay tính kháng thuốc trừ sâu ở muỗi theo thời gian.",
          True, "Khi môi trường biến đổi theo một xu hướng mới, một cực của dãy phân bố có giá trị thích nghi cao hơn sẽ dần thay thế trạng thái trung bình cũ."),
         ("Chọn lọc phân hóa ưu tiên giữ lại các cá thể mang giá trị tính trạng ở CẢ HAI CỰC ĐOAN (ví dụ chim sẻ mỏ rất to ăn hạt cứng và mỏ rất nhỏ ăn hạt mềm) và đào thải nhóm trung gian, có thể làm phân chia quần thể thành hai nhóm riêng biệt.",
          True, "Chọn lọc phân hóa làm tăng phương sai, tạo phân bố hai đỉnh và có thể khởi phát hình thành loài cùng khu nếu kết hợp chọn bạn tình đồng hình."),
         ("Ở động vật đẻ trứng (như chim sáo đá đẻ số trứng mỗi lứa dao động từ $1$ đến $9$), những ổ có số trứng trung bình ($4-5$ trứng) cho tỉ lệ con non sống sót tới trưởng thành cao nhất là ví dụ của chọn lọc ổn định.",
          True, "Đẻ quá ít không hiệu quả sinh sản, đẻ quá nhiều bố mẹ không đủ mồi nuôi khiến con còi cọc chết nhiều $\\rightarrow$ chọn lọc ổn định quanh $4-5$ trứng.")])

    # TF-069
    add("population", "adv", "Con đường Hình thành Loài mới",
        "Quá trình hình thành loài mới (tiến hóa nhỏ kết thúc khi xuất hiện cách ly sinh sản) diễn ra qua các con đường khác nhau: Cách ly địa lý, Cách ly sinh thái (cùng khu) và Lai xa kết hợp đa bội hóa. Xét các nhận định sau:",
        [("Hình thành loài bằng con đường cách ly địa lý thường diễn ra rất chậm chạp qua nhiều giai đoạn trung gian và rất dễ xảy ra ở những loài động vật có khả năng phát tán, di cư mở rộng khu phân bố.",
          True, "Cách ly địa lý chia cắt quần thể thành nhiều quần thể nhỏ tách biệt dòng gen trong thời gian dài để thích nghi với điều kiện địa phương khác nhau."),
         ("Trong con đường cách ly địa lý, điều kiện địa lý khác nhau đóng vai trò trực tiếp gây ra các đột biến định hướng giống nhau giúp cách ly sinh sản ngay lập tức.",
          False, "Điều kiện địa lý và ngoại cảnh KHÔNG tạo ra đột biến có hướng sẵn, mà đóng vai trò tác nhân chọn lọc tự nhiên giữ lại các biến dị thích nghi khác nhau ở mỗi khu vực."),
         ("Loài ruồi ăn táo Bắc Mỹ (*Rhagoletis pomonella*) vốn sống trên cây táo gai bản địa đã tách thành hai dòng quần thể sinh sản lệch mùa trên cây táo gai và cây táo trồng châu Âu ngay trong cùng một khu vườn địa lý là ví dụ của hình thành loài cùng khu (cách ly sinh thái / tập tính).",
          True, "Chuyển đổi vật chủ kết hợp giao phối trên cây ký chủ có mùa chín quả khác nhau làm suy giảm dòng gen xuống vài phần trăm giữa hai nòi sinh thái."),
         ("Bằng con đường lai xa và đa bội hóa, loài mới (thể song nhị bội) hình thành RẤT NHANH chỉ qua vài thế hệ ngay trong cùng khu phân bố mà không cần cách ly địa lý kéo dài.",
          True, "Thể song nhị bội ($2n_A + 2n_B$) cách ly sinh sản tức thì với cả hai loài bố mẹ nhờ sai khác bộ NST khi lai ngược trở lại.")])

    # TF-070
    add("population", "adv", "Học thuyết Darwin & Thuyết Tiến hóa Trung tính",
        "Đối chiếu học thuyết Chọn lọc tự nhiên của Charles Darwin (1859), Thuyết tiến hóa tổng hợp hiện đại và Thuyết tiến hóa trung tính ở cấp độ phân tử của Motoo Kimura (1968). Xét các nhận định sau:",
        [("Ưu điểm lớn của Darwin là đã chỉ ra đúng vai trò trung tâm của chọn lọc tự nhiên và biến dị cá thể, song hạn chế lịch sử của ông là chưa hiểu được nguyên nhân phát sinh biến dị và cơ chế di truyền biến dị (do thời đó chưa có di truyền học Mendel).",
          True, "Sự ra đời của di truyền học quần thể vào đầu thế kỷ 20 đã kết hợp di truyền học Mendel với chọn lọc Darwin thành thuyết tiến hóa tổng hợp."),
         ("Theo thuyết tiến hóa trung tính của Kimura, phần lớn các thay thế nucleotit ở mức độ phân tử không ảnh hưởng đến giá trị thích nghi (biến dị trung tính) và do đó sự cố định chúng chỉ do Chọn lọc tự nhiên định hướng chứ không liên quan yếu tố ngẫu nhiên.",
          False, "Ngược lại: đối với các alen TRUNG TÍNH ($s = 0$), Chọn lọc tự nhiên không tác động tới chúng; số phận cố định hay biến mất của các đột biến trung tính hoàn toàn do **phiêu bạt di truyền ngẫu nhiên** quyết định!"),
         ("Tốc độ thay thế cố định các đột biến trung tính mới phát sinh trong quần thể theo thời gian đúng bằng tốc độ đột biến trung tính $u$ của mỗi giao tử và hoàn toàn ĐỘC LẬP với kích thước quần thể $N_e$.",
          True, "Kỳ vọng phát sinh đột biến trung tính mới toàn quần thể mỗi thế hệ là $2N u$, nhân xác suất cố định $1/(2N)$ bằng đúng $u$! Đây là cơ sở toán học của 'đồng hồ phân tử'."),
         ("Các đoạn trình tự ADN không mã hóa, intron hoặc vị trí nucleotit thứ ba đồng nghĩa trong codon thường tích lũy đột biến nhanh hơn hẳn vùng trung tâm hoạt động của enzyme vì ít chịu sức ép của chọn lọc ổn định.",
          True, "Vùng thiết yếu có bảo thủ tiến hóa cao do mọi đột biến sai hỏng ở đó đều bị chọn lọc loại bỏ ngay.")])

    # TF-071
    add("population", "basic", "Bằng chứng Tiến hóa Gián tiếp & Trực tiếp",
        "Xét bảng tổng hợp các bằng chứng tiến hóa giúp tái dựng lịch sử phát sinh các loài từ tổ tiên chung:",
        [("Chi trước của người (cầm nắm), cánh chim (bay), chi trước cá voi (bơi) và chi trước chuột chũi (đào đất) có khung xương cấu tạo đồng nhất gồm xương cánh, xương quay-trụ, cổ-bàn-ngón tay là bằng chứng về cơ quan tương đồng phản ánh tiến hóa phân ly.",
          True, "Cùng bắt nguồn từ chi $5$ ngón của tổ tiên động vật $4$ chân cổ đại nhưng biến đổi phục vụ chức năng sinh thái khác nhau."),
         ("Nhờ phương pháp xác định tuổi đồng vị phóng xạ (như $^{14}C$ cho hóa thạch trẻ $< 50\\,000$ năm hoặc $^{40}K/^{40}Ar$, $^{238}U$ cho đá cổ hàng trăm triệu năm), nhà cổ sinh vật học định tuổi chính xác các lớp hóa thạch chuyển tiếp như *Archaeopteryx* hay *Tiktaalik*.",
          True, "*Tiktaalik* là hóa thạch chuyển tiếp nối giữa cá vây thùy và lưỡng cư 4 chân; *Archaeopteryx* mang đặc điểm trung gian khủng long có lông vũ và chim."),
         ("Gai xương rồng (biến dạng từ lá) và gai hoa hồng (biến dạng từ biểu bì thân) có cùng nguồn gốc phôi sinh nên là cơ quan tương đồng.",
          False, "Khác nguồn gốc phát sinh cơ quan (lá vs biểu bì thân) nhưng thực hiện chung chức năng tự vệ với hình thái nhọn giống nhau $\\rightarrow$ cơ quan TƯƠNG TỰ."),
         ("Chuỗi axit amin của protein Cytochrome c ở hai loài càng sai khác nhiều chứng tỏ hai loài đó tách ra từ tổ tiên chung càng GẦN đây.",
          False, "Sai khác phân tử càng ÍT thì phân ly càng GẦN; sai khác càng NHIỀU chứng tỏ hai nhánh đã tiến hóa độc lập tách rời từ rất XA nhau trong quá khứ.")])

    # TF-072
    add("population", "hsg", "Thắt cổ chai & Hiệu ứng Kẻ Sáng lập (Báo săn Cheetah)",
        "Loài báo săn châu Phi (*Acinonyx jubatus*) nổi tiếng với mức độ đồng hợp tử di truyền cực kỳ cao (tương đương động vật cận huyết phòng thí nghiệm nhiều thế hệ: thậm chí hai cá thể báo săn không cùng họ hàng ghép mảnh da cho nhau cũng gần như không bị đào thải miễn dịch mạnh ở các locus MHC), dẫn tới tỉ lệ tinh trùng dị dạng cao và dễ bị diệt vong hàng loạt trước một virus mới. Xét các nhận định tiến hóa bảo tồn sau:",
        [("Nguyên nhân sâu xa khiến báo săn có độ đa dạng di truyền cực thấp là do chúng đang có kích thước quần thể khổng lồ hàng chục triệu con trải khắp các châu lục.",
          False, "Báo săn từng trải qua ít nhất một hoặc hai sự kiện THẮT CỔ CHAI (genetic bottleneck) khốc liệt cuối kỷ Băng hà ($\\approx 10\\,000$ năm trước), tụt xuống chỉ còn vài cá thể sống sót."),
         ("Sự thiếu hụt đa dạng tại cụm gen hòa hợp mô chính (MHC) ở báo săn khiến quần thể thiếu kho kháng nguyên trình diện phong phú, làm giảm khả năng chống chịu tập thể trước các chủng virus đột biến mới.",
          True, "Đa dạng MHC cao giúp trong quần thể luôn có những cá thể nhận diện và sống sót trước các mầm bệnh mới xuất hiện."),
         ("Trong bảo tồn sinh học, việc nuôi nhốt hoặc phân mảnh sinh cảnh thành các khu bảo tồn nhỏ biệt lập mà không có hành lang di cư nhân tạo có nguy cơ làm tăng tốc vòng xoáy tuyệt chủng (Extinction vortex) do giao phối cận huyết và phiêu bạt di truyền.",
          True, "Quần thể nhỏ bị tách rời mất dòng gen làm $N_e$ giảm mạnh $\\to$ nội phối tăng $\\to$ suy thoái giống $\\to$ giảm sinh sản $\\to$ kích thước càng thu nhỏ thêm."),
         ("Giải pháp phục hồi di truyền khả thi nhất cho quần thể nhỏ suy thoái cận huyết là cấm tuyệt đối mọi sự trao đổi cá thể giữa các khu bảo tồn để giữ 'độ thuần' tối đa.",
          False, "Trái lại: 'giải cứu di truyền' (Genetic rescue — đưa một vài cá thể từ quần thể lân cận cùng loài tới giao phối) giúp đưa alen mới vào xóa bỏ trạng thái đồng hợp lặn có hại và nâng cao sức sống quần thể.")])

    # TF-073
    add("population", "hsg", "Kích thước Hiệu quả $N_e$ & Hệ số Nội phối $F$",
        "Trong một chương trình bảo tồn loài hươu sao quý hiếm có $N = 100$ cá thể trưởng thành tham gia sinh sản: Trại A nuôi $50$ đực và $50$ cái; Trại B nuôi $5$ đực và $95$ cái. Biết kích thước hiệu quả tính theo công thức $N_e = \\frac{4 N_m N_f}{N_m + N_f}$ và tỷ lệ mất dị hợp tử mỗi thế hệ do phiêu bạt di truyền là $\\Delta F = \\frac{1}{2 N_e}$. Xét các phân tích định lượng sau:",
        [("Kích thước hiệu quả $N_e$ của Trại A bằng đúng $100$ cá thể, còn $N_e$ của Trại B chỉ còn xấp xỉ $19$ cá thể ($19.0$).",
          True, "Trại A: $\\frac{4\\times 50\\times 50}{100} = 100$. Trại B: $\\frac{4\\times 5\\times 95}{100} = \\frac{1900}{100} = 19.0$!"),
         ("Mặc dù cả hai trại đều nuôi tổng cộng $100$ cá thể, nhưng tốc độ mất đa dạng di truyền (gia tăng hệ số nội phối $\\Delta F$) mỗi thế hệ ở Trại B diễn ra nhanh gấp hơn $5$ lần so với Trại A.",
          True, "Trại A mất $\\frac{1}{200} = 0.5\\%$/thế hệ; Trại B mất $\\frac{1}{38} \\approx 2.63\\%$/thế hệ (tỷ số $100/19 \\approx 5.26$ lần)."),
         ("Nếu trong Trại A, người ta chọn từ nguồn ban đầu có $p = q = 0.50$ và thực hiện giao phối cận huyết đạt hệ số nội phối $F = 0.40$, thì cấu trúc di truyền hiện tại sẽ là $0.35 AA + 0.30 Aa + 0.35 aa = 1$.",
          True, "$Aa = 2pq(1-F) = 0.50 \\times (1 - 0.40) = 0.30$; $AA = p^2 + pqF = 0.25 + 0.25(0.4) = 0.35$; $aa = 0.35$."),
         ("Sự sụt giảm mạnh kích thước hiệu quả $N_e$ ở Trại B là do khi có ít con đực tham gia phối giống thì tần số alen $A$ tự động tăng vọt lên $1.0$ ngay sau $1$ thế hệ ở mọi gen.",
          False, "Ít con đực làm tăng biến động ngẫu nhiên (phương sai $\\frac{pq}{2N_e}$) chứ KHÔNG định hướng luôn đẩy alen trội lên $1.0$ ngay trong $1$ thế hệ.")])

    # TF-074
    add("population", "adv", "Hiệu ứng Wahlund & Hòa nhập Quần thể",
        "Giả sử có $2$ quần thể thực vật lớn kích thước BẰNG NHAU cùng loài nhưng tách biệt: Quần thể $1$ cân bằng ở $p_1(A) = 0.90, q_1(a) = 0.10$; Quần thể $2$ cân bằng ở $p_2(A) = 0.10, q_2(a) = 0.90$. Lấy tỷ lệ $50\\%$ hạt từ quần thể $1$ trộn đều với $50\\%$ hạt từ quần thể $2$ trồng chung tạo lô $P_{\\text{hỗn hợp}}$, rồi cho giao phấn ngẫu nhiên tự do. Xét các nhận định sau:",
        [("Ngay tại lô cây $P_{\\text{hỗn hợp}}$ trước khi giao phấn, tỉ lệ cây có kiểu gen dị hợp $Aa$ bằng $18\\%$, còn tỉ lệ đồng hợp $AA$ và $aa$ đều bằng $41\\%$.",
          True, "QT1: $0.81 AA + 0.18 Aa + 0.01 aa$; QT2: $0.01 AA + 0.18 Aa + 0.81 aa$. Trung bình hỗn hợp: $0.41 AA + 0.18 Aa + 0.41 aa$."),
         ("Sự thiếu hụt thể dị hợp ($18\\%$ thực tế so với $50\\%$ lý thuyết tại $\\bar{p} = 0.50$) khi gộp $2$ quần thể phân hóa tần số alen gọi là hiệu ứng Wahlund.",
          True, "Độ thiếu hụt dị hợp đúng bằng $2 \\text{Var}(p) = 2 \\times 0.4^2 = 0.32$ ($50\\% - 18\\% = 32\\%$)."),
         ("Sau khi cho lô $P_{\\text{hỗn hợp}}$ giao phấn ngẫu nhiên tự do qua $1$ thế hệ ($F_1$), tỉ lệ cây dị hợp $Aa$ vẫn bị giữ cố định ở mức $18\\%$ mà không tăng lên được.",
          False, "Vì cả hạt phấn và noãn hỗn hợp đều mang $\\bar{p} = 0.5, \\bar{q} = 0.5$, ngay ở $F_1$ tỉ lệ dị hợp nhảy vọt từ $18\\%$ lên $50\\%$ (đạt cân bằng $0.25 AA : 0.50 Aa : 0.25 aa$)."),
         ("Quá trình hòa nhập ngẫu phối giữa $2$ quần thể trên làm tăng tần số alen $A$ từ $0.50$ lên $0.81$ chỉ nhờ tác động trộn gen.",
          False, "Giao phấn ngẫu nhiên hoàn toàn bảo toàn tần số alen chung $\\bar{p}(A) = 0.50$ và $\\bar{q}(a) = 0.50$.")])

    # TF-075
    add("population", "basic", "Phát sinh Sự sống & Các Đại Địa chất",
        "Dựa trên bằng chứng địa chất, hóa thạch và thực nghiệm sinh hóa học về nguồn gốc sự sống và tiến trình phát triển sinh giới qua các đại địa chất trên Trái Đất:",
        [("Trong giai đoạn tiến hóa hóa học ở Trái Đất nguyên thủy, khí quyển giàu oxy phân tử ($O_2$) đóng vai trò chất xúc tác chính tổng hợp nên các hợp chất hữu cơ đơn giản như axit amin từ chất vô cơ.",
          False, "Khí quyển nguyên thủy có tính KHỬ (hầu như KHÔNG có $O_2$ tự do, gồm $CH_4, NH_3, H_2, H_2O, CO_2...$) — chính sự vắng mặt của $O_2$ giúp các hợp chất hữu cơ mới sinh không bị oxy hóa phá hủy ngay."),
         ("Khi khí quyển tích lũy đủ $O_2$ từ quang hợp của vi khuẩn lam hình thành tầng ozon ($O_3$) chắn tia tử ngoại ở đại Cổ sinh (kỷ Silur), thực vật và động vật chân khớp bắt đầu di cư lên sống trên cạn.",
          True, "Kỷ Silur chứng kiến thực vật mạch đầu tiên (như Quyết trần) và chân khớp tiến lên chinh phục đất liền."),
         ("Đại Trung sinh (gồm các kỷ Tam điệp, Jura, Phấn trắng) được mệnh danh là kỷ nguyên ngự trị của Bò sát khổng lồ (khủng long) và thực vật Hạt trần, đồng thời chứng kiến sự xuất hiện của Chim, Thú cổ và Thực vật có hoa (Hạt kín).",
          True, "Cuối đại Trung sinh (kỷ Phấn trắng), thiên thạch rơi cộng hoạt động núi lửa làm tuyệt chủng khủng long phi điểu, mở đường cho đại Tân sinh."),
         ("Trong đại Tân sinh (cách nay $\\sim 66$ triệu năm đến hiện tại), các loài Thực vật Hạt kín, Côn trùng, Chim và Động vật có vú phát triển phân hóa bùng nổ, đỉnh cao là sự xuất hiện chi *Homo* và loài người *Homo sapiens* ở kỷ Đệ tứ.",
          True, "Quá trình phát sinh loài người trải qua nhánh vượn người cổ, chi *Australopithecus*, *Homo habilis*, *Homo erectus* đến *Homo sapiens*.")])

    # ==================== TOPIC 6: PHYSIOLOGY (TF-076 .. TF-090) ====================
    # TF-076
    add("physiology", "adv", "Vận chuyển Nước & Thoát hơi nước",
        "Thực vật trên cạn hấp thụ một lượng nước khổng lồ mỗi ngày qua rễ, đẩy theo mạch gỗ (Xylem) lên đỉnh tán cây cao tới cả trăm mét và thoát phần lớn qua lá. Xét các nhận định sinh lý về dòng mạch gỗ:",
        [("Động lực đẩy dòng nước từ dưới lên nhờ áp suất rễ có thể quan sát trực tiếp qua hiện tượng rỉ nhựa khi cắt ngang thân hoặc hiện tượng ứ giọt ở mép lá vào sáng sớm độ ẩm không khí bão hòa.",
          True, "Khi thoát hơi nước ngừng vào đêm ẩm, áp suất rễ (chủ yếu do bơm ion vào mạch gỗ kéo nước theo thẩm thấu) đẩy nước thoát qua thủy khổng mép lá."),
         ("Cột nước liên tục trong mạch gỗ không bị đứt gãy ngay cả ở đỉnh cây gỗ cao hàng chục mét nhờ $2$ lực: lực liên kết giữa các phân tử nước với nhau (lực cố kết nhờ liên kết hiđrô) và lực bám dính giữa phân tử nước với thành mạch gỗ xenlulôzơ ưa nước.",
          True, "Lực hút kéo từ sự thoát hơi nước tại lá tạo sức căng âm truyền suốt cột nước liên tục xuống tận lông hút rễ (thuyết sức căng - cố kết)."),
         ("Vào buổi trưa nắng gắt khi cây bị thiếu nước nghiêm trọng, thoát hơi nước qua bề mặt tầng cutin chiếm tới trên $90\\%$ tổng lượng nước bay hơi trong khi qua khí khổng dưới $10\\%$.",
          False, "Khi khí khổng mở bình thường, thoát hơi nước qua KHÍ KHỔNG chiếm chủ yếu ($\\approx 90\\%$); chỉ khi cây đóng chặt khí khổng chống hạn thì lượng nhỏ qua cutin mới còn tồn tại (tầng cutin cản thấm rất mạnh, càng dày mất nước càng ít)."),
         ("Mạch gỗ cấu tạo từ hai loại tế bào chết (quản bào và mạch ống) có thành tế bào thấm lignin cực bền giúp ống dẫn không bị bẹp xẹp dưới áp suất âm lớn của dòng hút kéo.",
          True, "Khác với mạch rây gồm tế bào sống (ống rây và tế bào kèm), tế bào mạch gỗ hóa gỗ chết rỗng hoàn toàn giúp giảm tối đa lực cản dòng nước.")])

    # TF-077
    add("physiology", "adv", "Quang hợp Thực vật $C_3$, $C_4$ và $CAM$",
        "So sánh hiệu quả và cơ chế đồng hóa $CO_2$ pha tối của $3$ nhóm thực vật thích nghi với các điều kiện khí hậu khác nhau: lúa ($C_3$), mía ($C_4$) và dứa ($CAM$). Xét các nhận định sau:",
        [("Chất nhận $CO_2$ đầu tiên của thực vật $C_3$ là đường photphat $5$ cacbon ($RuBP$), còn chất nhận $CO_2$ đầu tiên cố định khí trời ở cả $C_4$ và $CAM$ đều là axit photphoenolpyruvic ($PEP$, $3$ cacbon).",
          True, "Chu trình Calvin ở $C_3$ bắt đầu bằng RuBisCO gắn $CO_2$ vào $RuBP$; cả $C_4$ và $CAM$ đều bước đầu cố định nhờ enzyme PEP-carboxylase gắn $CO_2$ vào $PEP$ tạo $OAA$ ($4C$)."),
         ("Trong thực vật $C_4$, hai giai đoạn cố định $CO_2$ sơ cấp và chu trình Calvin xảy ra ở HAI THỜI ĐIỂM KHÁC NHAU (đêm và ngày) ngay trong cùng một loại tế bào mô giậu.",
          False, "Đặc điểm tách biệt theo **THỜI GIAN** (đêm cố định qua PEPcase, ngày chạy Calvin) trong cùng tế bào là của thực vật **$CAM$**; còn thực vật **$C_4$** diễn ra cùng ban ngày nhưng tách biệt theo **KHÔNG GIAN** tại $2$ loại tế bào (tế bào mô giậu và tế bào bao bó mạch)!"),
         ("Do có cơ chế bơm $CO_2$ tập trung quanh RuBisCO nên nhóm $C_4$ hầu như triệt tiêu được hô hấp sáng, nhưng phải trả giá tốn thêm năng lượng ($\\approx 2\\text{ ATP}$ phụ cho mỗi phân tử $CO_2$ cố định để tái sinh $PEP$).",
          True, "Vì tốn thêm $2\\text{ ATP}$ nên ở môi trường mát ẩm ít hô hấp sáng thì cây $C_3$ cạnh tranh tốt hơn, còn ở vùng nhiệt đới nắng nóng thì $C_4$ vượt trội hẳn."),
         ("Cả $3$ nhóm thực vật $C_3$, $C_4$ và $CAM$ cuối cùng đều BẮT BUỘC phải sử dụng chu trình Calvin (với enzyme RuBisCO) để tổng hợp nên đường glucozơ.",
          True, "Mọi sinh vật quang hợp giải phóng oxy bậc cao đều dùng chu trình Calvin làm con đường tổng hợp cacbohiđrat thuần.")])

    # TF-078
    add("physiology", "basic", "Dinh dưỡng Nitơ & Chuyển hóa Khoáng",
        "Thực vật không sử dụng được trực tiếp khí $N_2$ chiếm $78\\%$ khí quyển nếu không có quá trình cố định đạm sinh học hoặc lý-hóa, và trong mô cây nitơ đồng hóa thành axit amin theo những con đường chặt chẽ. Xét các nhận định sau:",
        [("Trong đất tơi xốp thoáng khí, nhóm vi khuẩn nitrat hóa (*Nitrosomonas* và *Nitrobacter*) oxy hóa lần lượt $NH_4^+ \\rightarrow NO_2^- \\rightarrow NO_3^-$ tạo dạng đạm dễ hấp thụ cho cây trồng.",
          True, "Vi khuẩn hóa tự dưỡng thu năng lượng từ sự oxy hóa amôni và nitrit để cố định cacbon."),
         ("Sau khi rễ cây hấp thụ ion $NO_3^-$ vào tế bào, cây có thể gắn trực tiếp ngay gốc nitrat ($-NO_3$) vào khung cacbon axit hữu cơ để biến thẳng thành axit amin mà không cần khử thành $NH_4^+$.",
          False, "Cây BẮT BUỘC phải thực hiện quá trình khử $NO_3^- \\xrightarrow{\\text{nitrat reductase}} NO_2^- \\xrightarrow{\\text{nitrit reductase}} NH_4^+$ rồi mới thực hiện amin hóa gắn $NH_4^+$ vào $\\alpha$-xêtôglutaric tạo axit amin."),
         ("Khi bổ sung dư thừa ion $NH_4^+$ trong tế bào thực vật, cây giải độc amoni bằng cách gắn vào axit amin dicarboxylic (tạo thành amit như Asparagin hoặc Glutamin) giúp dự trữ nitơ an toàn.",
          True, "Hình thành amit vừa khử độc $NH_3$ vừa là kho dự trữ đạm cơ động cho nhu cầu sinh tổng hợp protein."),
         ("Các loài thực vật ăn sâu bọ (như cây nắp ấm, cây gọng vó sống ở đầm lầy đất chua nghèo khoáng) tiêu hóa côn trùng nhằm lấy chất hữu cơ thay thế hoàn toàn chức năng quang hợp.",
          False, "Các loài cây này vẫn có diệp lục quang hợp tự tạo chất hữu cơ từ $CO_2$ bình thường; chúng bắt côn trùng chủ yếu để bổ sung nguồn **Nitơ (đạm) và Phốt pho** thiếu hụt trong đất ngập lầy.")])

    # TF-079
    add("physiology", "hsg", "Điều hòa Hormone & Nảy mầm / Ra hoa Thực vật",
        "Trong nông nghiệp và công nghệ sinh học thực vật, việc hiểu rõ cơ chế tác động đối kháng hay hiệp đồng của các nhóm phytohormone giúp điều khiển quá trình nảy mầm hạt, ra rễ giâm cành, tạo quả không hạt và ra hoa trái vụ. Xét các nhận định sau:",
        [("Ở hạt đại mạch đang nảy mầm, khi phôi hút nước đủ sẽ tổng hợp hormone $ABA$ để kích thích lớp tế bào alơrôn tiết mạnh enzyme $\\alpha$-amylase thủy phân tinh bột trong nội nhũ.",
          False, "Hormone kích thích lớp alơrôn sản sinh $\\alpha$-amylase phá ngủ kích thích nảy mầm là **Gibberellin ($GA$)**; ngược lại $ABA$ là hormone gây ngủ nghỉ và ức chế nảy mầm!"),
         ("Cắt bỏ chồi ngọn ở cây thân thảo (như tỉa ngọn chè, bông, cà phê) làm mất nguồn sản sinh Auxin từ đỉnh sinh trưởng, từ đó giải phóng ức chế ưu thế ngọn giúp các chồi nách bật mọc mạnh tạo tán xum xuê.",
          True, "Tỉ lệ Auxin cao từ đỉnh kìm hãm chồi nách; khi bấm ngọn, Cytokinin từ rễ thắng thế kích thích chồi bên phát triển."),
         ("Đối với cây ngày DÀI cần thời gian sáng trên $14\\text{ giờ}$ để ra hoa (tối tới hạn $< 10\\text{ giờ}$), trong điều kiện mùa đông đêm dài $13\\text{ giờ}$, nhà vườn thắp đèn ánh sáng đỏ ($660\\text{ nm}$) ngắt quãng giữa đêm khoảng $15$ phút sẽ thúc đẩy cây ra hoa trái vụ.",
          True, "Một lóe ánh sáng đỏ giữa đêm chuyển phytochrome $P_r \\to P_{fr}$, chia đôi đêm dài $13\\text{ h}$ thành hai nửa $6.5\\text{ h} < 10\\text{ h}$ khiến cây ngày dài cảm nhận như đêm ngắn và ra hoa."),
         ("Phun dung dịch Auxin hoặc Gibberellin nồng độ thích hợp lên hoa cái chưa thụ phấn của cà chua hoặc nho có thể kích thích bầu nhụy phát triển thành quả không hạt (tạo quả đơn tính).",
          True, "Thay thế nguồn hormone tự nhiên vốn do phôi hạt sinh ra sau thụ tinh bằng hormone ngoại sinh giúp bầu quả phình lớn mà không tạo hạt.")])

    # TF-080
    add("physiology", "adv", "Sinh lý Tiêu hóa Hóa học ở Người",
        "Theo dõi quá trình tiêu hóa hóa học các đại phân tử thức ăn (tinh bột, protein, lipid) khi đi dọc qua khoang miệng, dạ dày và tá tràng của ống tiêu hóa người:",
        [("Enzyme Amylase trong nước bọt bắt đầu thủy phân tinh bột chín thành đường đôi mantozơ ở khoang miệng (pH $\\approx 6.5 - 7.0$), nhưng khi xuống tới dịch vị dạ dày có $pH \\approx 1.5 - 2.0$ thì enzyme amylase nước bọt nhanh chóng bị bất hoạt.",
          True, "pH axit mạnh của HCl làm biến tính mất hoạt tính amylase nước bọt, đồng thời diệt hầu hết vi khuẩn theo thức ăn."),
         ("Trong dạ dày, tế bào chính tiết tiền enzyme $Pepsinogen$ không hoạt động (tránh tự tiêu hóa tuyến dạ dày); khi tiếp xúc axit $HCl$, $Pepsinogen$ được cắt thành enzyme $Pepsin$ hoạt động thủy phân protein thành các chuỗi polipeptit ngắn.",
          True, "Ngoài cơ chế tiết tiền chất bất hoạt (zymogen), lớp chất nhầy bicarbonat phủ niêm mạc bảo vệ dạ dày khỏi tự tiêu."),
         ("Tại tá tràng, enzyme $Trypsinogen$ do tuyến tụy tiết ra được hoạt hóa thành $Trypsin$ bởi enzyme Enterokinase bám trên vi nhung mao thành ruột non, sau đó chính $Trypsin$ lại tự hoạt hóa các zymogen tụy khác (như Chymotrypsinogen).",
          True, "Cơ chế hoạt hóa dây chuyền chỉ khởi động ngay trong lòng ruột non giúp bảo vệ mô tuyến tụy khỏi viêm tụy cấp tự tiêu."),
         ("Muối mật do tế bào gan tiết ra và dự trữ ở túi mật chứa một loại enzyme Lipase rất mạnh trực tiếp cắt đứt các liên kết este trong phân tử triglixerit thành axit béo tự do.",
          False, "Dịch mật HOÀN TOÀN KHÔNG chứa enzyme tiêu hóa! Muối mật chỉ đóng vai trò nhũ tương hóa cơ học chia giọt mỡ lớn thành hạt nhỏ để tăng diện tích tiếp xúc cho enzyme **Lipase của dịch tụy** cắt phân tử chất béo.")])

    # TF-081
    add("physiology", "adv", "Sinh lý Tim & Huyết động học",
        "Xét hoạt động cơ học và điều hòa của tim trong một chu kỳ chuẩn ($0.8\\text{ s}$) ở một người trưởng thành khỏe mạnh khi nghỉ ngơi (nhịp tim $75\\text{ nhịp/phút}$, $EDV = 120\\text{ ml}$, $ESV = 50\\text{ ml}$). Mỗi nhận định sau Đúng hay Sai?",
        [("Thể tích tâm thu của mỗi tâm thất ở người này bằng $70\\text{ ml}$ và cung lượng tim đạt $5.25\\text{ lít/phút}$.",
          True, "$SV = 120 - 50 = 70\\text{ ml}$; $CO = 75 \\times 70 = 5250\\text{ ml/phút} = 5.25\\text{ lít/phút}$."),
         ("Tiếng tim thứ nhất ($T_1$ - 'bùm') xuất hiện do van động mạch chủ và phổi đóng lại, còn tiếng tim thứ hai ($T_2$ - 'tặc') xuất hiện do đóng van hai lá và ba lá.",
          False, "Ngược lại: Tiếng $T_1$ do đóng **van nhĩ-thất** (hai lá và ba lá) khi bắt đầu thì tâm thất co; tiếng $T_2$ do đóng **van tổ chim/bán nguyệt** (động mạch chủ và động mạch phổi) khi bắt đầu thì tâm thất dãn."),
         ("Theo định luật Frank - Starling của tim, trong giới hạn sinh lý, máu tĩnh mạch đổ về tâm thất làm căng sợi cơ tim cuối tâm trương ($EDV$) càng lớn thì lực co bóp của tâm thất tăng tương ứng để tống lượng máu lớn hơn vào động mạch.",
          True, "Kéo dãn sarcomer tới chiều dài tối ưu làm tăng độ nhạy với $Ca^{2+}$ và tăng số cầu nối actin-myosin giúp tự động cân bằng lượng máu tống ra với máu trở về."),
         ("Khi vận động thể lực mạnh, hệ thần kinh giao cảm giải phóng Noradrenalin gắn thụ thể $\\beta_1$ trên nút xoang nhĩ và cơ tim làm TĂNG cả tần số phát nhịp lẫn lực co bóp cơ tim giúp cung lượng tim có thể tăng lên $3-4$ lần.",
          True, "Cơ chế giao cảm tăng cAMP mở kênh ion funny ($I_f$) đẩy nhanh khử cực tự phát nút xoang và tăng bơm $Ca^{2+}$ vào cơ tim.")])

    # TF-082
    add("physiology", "adv", "Vận chuyển Khí & Hiệu ứng Bohr",
        "Phân tích đường cong phân ly Oxyhemoglobin ($Hb-O_2$) biểu diễn mối quan hệ giữa phần trăm bão hòa $O_2$ của Hemoglobin ($Y\\%$) theo phân áp $O_2$ ($pO_2$, $\\text{mmHg}$). Xét các nhận định sau trong trạng thái sinh lý bình thường và khi cơ vân chạy cường độ cao:",
        [("Đường cong phân ly $Hb-O_2$ có dạng hình chữ $S$ (sigmoid) do cấu trúc tứ phân của phân tử Hemoglobin biểu hiện tính gắn hợp tác dương tính: khi tiểu phần thứ nhất gắn $O_2$ làm thay đổi cấu hình không gian giúp $3$ tiểu phần còn lại gắn $O_2$ dễ dàng hơn nhiều.",
          True, "Chính tính chất hình chữ $S$ giúp $Hb$ bão hòa gần $98\\%$ ở phổi ($pO_2 \\approx 100\\text{ mmHg}$) nhưng chỉ cần $pO_2$ mô giảm xuống $40 \\to 20\\text{ mmHg}$ đã giải phóng nhanh lượng lớn $O_2$."),
         ("Tại mô cơ bắp đang chạy nước rút mạnh tạo ra nhiều axit lactic (làm $pH$ giảm), nồng độ $CO_2$ tăng và nhiệt độ cơ tăng cao, tất cả các yếu tố này đồng loạt làm dịch chuyển đường cong phân ly $Hb-O_2$ sang PHẢI (hiệu ứng Bohr), làm giảm ái lực với $O_2$ để nhả $O_2$ dồi dào hơn cho cơ.",
          True, "Đây là cơ chế thích nghi tối ưu đưa $O_2$ đúng đến những mô đang chuyển hóa mạnh cần oxy nhất."),
         ("Chất $2,3$-BPG ($2,3$-bisphosphoglycerate) do hồng cầu tổng hợp tăng lên khi người leo núi cao giúp đường cong phân ly $Hb-O_2$ dịch chuyển mạnh sang TRÁI làm $Hb$ khóa chặt oxy không bao giờ nhả ra cho mô.",
          False, "$2,3$-BPG gắn ổn định trạng thái T (deoxy-Hb), làm đường cong dịch sang PHẢI (giảm ái lực nhẹ ở mô) giúp giải phóng $O_2$ cho tế bào mô dễ dàng hơn ở độ cao trung bình."),
         ("Ở động mạch phổi đưa máu từ tim lên phổi có phân áp $O_2$ cao ($100\\text{ mmHg}$) hơn hẳn ở động mạch chủ đi nuôi cơ thể ($40\\text{ mmHg}$).",
          False, "Động mạch phổi mang máu NGHÈO $O_2$ từ tâm thất phải lên phổi ($pO_2 \\approx 40\\text{ mmHg}$); chỉ sau khi trao đổi khí ở mao mạch phế nang thì máu tĩnh mạch phổi và động mạch chủ mới đạt $pO_2 \\approx 95 - 100\\text{ mmHg}$.")])

    # TF-083
    add("physiology", "hsg", "Sinh lý Thận & Điều hòa Thể tích Dịch cơ thể",
        "Đơn vị chức năng thận (Nephron) thực hiện $3$ quá trình chính là Lọc ở cầu thận, Tái hấp thu và Bài tiết thêm tại hệ thống ống thận để tạo nước tiểu và duy trì cân bằng nội môi. Xét các nhận định sau:",
        [("Ở người bình thường khỏe mạnh, toàn bộ $100\\%$ lượng glucose và protein albumin huyết tương đều được lọc tự do qua màng lọc cầu thận rồi sau đó tái hấp thu hết ở ống lượn gần.",
          False, "Glucose lọc tự do và được tái hấp thu $100\\%$ qua đồng vận chuyển $Na^+$-glucose tại ống lượn gần; nhưng các đại phân tử protein huyết tương như Albumin gần như KHÔNG đi qua được khe lọc cầu thận do kích thước lớn và màng đáy tích điện âm đẩy lại!"),
         ("Hormone Aldosterone tiết ra từ lớp cầu vỏ tuyến thượng thận (kích hoạt qua hệ Renin - Angiotensin - Aldosterone khi huyết áp hoặc $Na^+$ giảm) kích thích tế bào chính ở ống lượn xa và ống góp tăng TÁI HẤP THU $Na^+$ kèm nước và tăng BÀI TIẾT $K^+$.",
          True, "Do tái hấp thu $Na^+$ kéo nước theo thẩm thấu, Aldosterone giúp nâng thể tích máu và huyết áp."),
         ("Peptide lợi niệu tâm nhĩ ($ANP$) do tế bào cơ tâm nhĩ tiết ra khi huyết áp và thể tích máu tăng căng quá mức có tác dụng đối kháng với hệ RAAS: gây giãn tiểu động mạch đến cầu thận tăng lọc và tăng thải trừ $Na^+$ cùng nước qua nước tiểu.",
          True, "Hệ RAAS/ADH (giữ muối, nước, tăng áp) đối trọng cân bằng tinh vi với ANP (thải muối, nước, hạ áp)."),
         ("Nếu thuốc lợi tiểu Furosemide ức chế đồng vận chuyển $Na^+-K^+-2Cl^-$ ở nhánh lên dày quai Henle, độ ưu trương của dịch kẽ vùng tủy thận sẽ giảm mạnh, kéo theo mất khả năng cô đặc nước tiểu và tăng lượng nước tiểu thải ra.",
          True, "Làm giảm gradient thẩm thấu tủy thận khiến nước không thể tái hấp thu thụ động tại nhánh xuống và ống góp dù có $ADH$.")])

    # TF-084
    add("physiology", "adv", "Xinap Hóa học vs Điện học & Xử lý Thông tin",
        "So sánh cơ chế truyền tin qua Xinap hóa học và Xinap điện học, cũng như cách một nơron trung gian tích hợp đồng thời nhiều tín hiệu đến:",
        [("Tại xinap hóa học, xung thần kinh chỉ truyền một chiều từ màng trước xinap sang màng sau xinap vì chỉ chùy xinap mới chứa bóng chất dẫn truyền thần kinh và chỉ màng sau xinap mới có thụ thể tiếp nhận tương ứng.",
          True, "Tính chất một chiều và hiện tượng 'chậm xinap' ($\\approx 0.5-1\\text{ ms}$) giúp định hướng luồng thông tin thần kinh chính xác."),
         ("Chất dẫn truyền thần kinh ức chế như $GABA$ hoặc Glycine khi gắn vào thụ thể kênh ở màng sau xinap thường làm mở kênh $Cl^-$ (cho $Cl^-$ đi vào) hoặc mở kênh $K^+$ (cho $K^+$ đi ra), gây tăng phân cực màng (điện thế sau xinap ức chế $IPSP$).",
          True, "Làm điện thế trong màng âm hơn nữa (ví dụ từ $-70\\text{ mV}$ xuống $-75\\text{ mV}$), đẩy màng ra xa ngưỡng kích thích $-55\\text{ mV}$."),
         ("Khác với xinap hóa học, xinap điện học nối hai tế bào trực tiếp qua các kênh liên kết khe (Gap junction), cho phép dòng ion truyền trực tiếp cực nhanh hầu như không có độ trễ xinap.",
          True, "Xinap điện học có mặt phổ biến ở tế bào cơ tim (giúp tim đồng bộ hóa co bóp thành khối) và các phản xạ thoát hiểm siêu nhanh ở cá/giáp xác."),
         ("Sau khi chất dẫn truyền kích thích Acetylcholine bám vào màng sau xinap gây mở kênh ion, nó sẽ bám chặt vĩnh viễn tại thụ thể đó suốt đời để cơ bắp luôn giữ trạng thái co cứng liên tục.",
          False, "Ngay sau vài phần nghìn giây, Acetylcholinesterase thủy phân Acetylcholine thành choline và axetat để kết thúc kích thích (chất truyền tin khác như serotonin/dopamine được tái hấp thu lại màng trước xinap).")])

    # TF-085
    add("physiology", "basic", "Hệ Miễn dịch Động vật có vú",
        "Cơ thể người tự vệ trước vi khuẩn, virus và ký sinh trùng thông qua hai tuyến phòng thủ phối hợp: Miễn dịch không đặc hiệu (bẩm sinh) và Miễn dịch đặc hiệu (thích nghi). Xét các nhận định sau:",
        [("Lớp biểu bì da, chất nhầy niêm mạc, axit $HCl$ dịch vị, enzyme lysozyme nước mắt, tế bào thực bào và tế bào giết tự nhiên ($NK$) đều thuộc tuyến miễn dịch bẩm sinh (không đặc hiệu).",
          True, "Tuyến miễn dịch bẩm sinh phản ứng nhanh ngay từ giờ đầu không cần ghi nhớ tiếp xúc trước."),
         ("Cả hai dòng tế bào miễn dịch đặc hiệu chính là Lympho B và Lympho T đều được sản sinh tại tủy xương và đồng loạt di cư tới tuyến ức (Thymus) để biệt hóa trưởng thành hoàn toàn.",
          False, "Chỉ có tế bào **Lympho T** di cư tới **tuyến ức (Thymus)** để trưởng thành và chọn lọc âm-dương; còn tế bào **Lympho B** ở động vật có vú trưởng thành ngay tại **tủy xương (Bone marrow)**!"),
         ("Tế bào bị nhiễm virus thường tiết ra protein tín hiệu **Interferon** kích thích các tế bào lành lân cận sản sinh các enzyme phong tỏa sự nhân lên của virus.",
          True, "Interferon loại I ($IFN-\\alpha, IFN-\\beta$) tạo trạng thái kháng virus cấp tính cho mô xung quanh và hoạt hóa tế bào NK."),
         ("Dị ứng quá mẫn tức thì (như sốc phản vệ hay dị ứng phấn hoa, hải sản) xảy ra khi dị nguyên gắn chéo các kháng thể $IgE$ bám sẵn trên bề mặt tế bào Mast (tế bào phì) làm vỡ hạt giải phóng ồ ạt **Histamine**.",
          True, "Histamine gây giãn mạch nhanh, tăng tính thấm thành mạch, co thắt cơ trơn phế quản và nổi mề đay.")])

    # TF-086
    add("physiology", "adv", "Điều hòa Nội tiết & Cơ chế Ngược âm tính",
        "Xét sự điều hòa hoạt động nội tiết theo trục Hạ đồi (dưới đồi) $\\rightarrow$ Tuyến yên $\\rightarrow$ Tuyến giáp và cơ chế cân bằng đường huyết quanh mức sinh lý ($\\sim 0.8 - 1.2\\text{ g/L}$ hay $\\sim 4.4 - 6.1\\text{ mmol/L}$) ở người:",
        [("Khi trời lạnh kéo dài, vùng dưới đồi tăng tiết $TRH$ kích thích thùy trước tuyến yên tiết $TSH$, thúc đẩy tuyến giáp giải phóng $T_3, T_4$ nhằm tăng cường chuyển hóa cơ bản và sinh nhiệt duy trì thân nhiệt.",
          True, "Hormone tuyến giáp làm tăng biểu hiện bơm $Na^+/K^+$ ATPase và tiêu thụ $O_2$ sinh nhiệt (calorigenic effect)."),
         ("Nồng độ hormone tuyến giáp $T_3, T_4$ trong máu tăng cao sẽ quay ngược lại kích thích dương tính dồn dập lên vùng dưới đồi và tuyến yên tiết thêm nhiều $TRH$ và $TSH$ lên vô hạn.",
          False, "Đó là cơ chế điều hòa ngược **ÂM TÍNH** (Negative feedback): $T_3, T_4$ cao tự động ức chế lại thùy trước tuyến yên và vùng dưới đồi giảm tiết $TSH, TRH$ để giữ nồng độ ổn định."),
         ("Trong trường hợp người bị thiếu hụt hoàn toàn nguyên tố Iốt trong khẩu phần ăn kéo dài, tuyến giáp không tổng hợp đủ $T_3, T_4$ làm mất lực ức chế ngược lên tuyến yên khiến $TSH$ tăng tiết liên tục, kích thích mô tuyến giáp phì đại gây bệnh bướu cổ đơn thuần.",
          True, "Thiếu nguyên liệu iốt dẫn tới $T_3/T_4$ thấp $\\rightarrow$ tăng $TSH$ kéo dài $\\rightarrow$ phì đại bù trừ nang giáp."),
         ("Khi đói xa bữa ăn đường huyết hạ xuống thấp, tế bào $\\alpha$ đảo tụy giảm tiết Glucagon đồng thời tế bào $\\beta$ tăng mạnh tiết Insulin để đẩy glucose từ máu vào tế bào mỡ.",
          False, "Khi đường huyết GIẢM, tế bào **$\\alpha$** tăng tiết **Glucagon** kích thích gan phân giải glycogen tạo glucose giải phóng vào máu; ngược lại **Insulin** (tế bào $\\beta$) giảm tiết tối đa.")])

    # TF-087
    add("physiology", "hsg", "Nội tiết Chu kỳ Kinh nguyệt & Thai kỳ",
        "Theo dõi diễn biến nồng độ của $5$ hormone ($GnRH, FSH, LH, Estrogen, Progesterone$) ở phụ nữ trong chu kỳ kinh nguyệt bình thường $28$ ngày (rụng trứng ngày $14$) và khi có sự thụ tinh thành công:",
        [("Ở giai đoạn đầu chu kỳ (pha nang trứng), hormone $FSH$ từ tuyến yên kích thích nang trứng phát triển, và các tế bào hạt của nang trứng tăng cường bài tiết Progesterone ở mức cực đại gây bong niêm mạc.",
          False, "Trong pha nang trứng (ngày $1-14$), nang trứng tiết chủ yếu **Estrogen** để tái tạo làm dày niêm mạc tử cung; **Progesterone** chỉ tăng vọt chủ yếu ở pha thể vàng SAU khi rụng trứng."),
         ("Sự tăng cao đột ngột nồng độ Estrogen vào cuối pha nang trứng chuyển tác động sang điều hòa ngược dương tính lên vùng dưới đồi-tuyến yên gây ra đỉnh $LH$ làm vỡ nang chín phóng thích noãn bào II.",
          True, "Nồng độ Estrogen duy trì ngưỡng cao $> 200\\text{ pg/ml}$ trong $\\ge 50$ giờ kích hoạt đỉnh $LH$ phóng noãn."),
         ("Nếu không có sự thụ tinh xảy ra, thể vàng thoái hóa sau $\\sim 12 - 14$ ngày làm tụt giảm đột ngột nồng độ Progesterone và Estrogen, kéo theo co thắt tiểu động mạch xoắn gây bong tróc lớp chức năng niêm mạc tử cung (hành kinh).",
          True, "Sự sụt giảm đột ngột hormone buồng trứng là tín hiệu trực tiếp khởi phát chu kỳ kinh mới."),
         ("Nếu trứng được thụ tinh và làm tổ tại niêm mạc tử cung, các tế bào lá nuôi của phôi sớm tiết ra hormone **$hCG$** (Human Chorionic Gonadotropin) giúp duy trì thể vàng tiếp tục sống và tiết Progesterone trong suốt giai đoạn đầu thai kỳ.",
          True, "Que thử thai phát hiện nhanh sự có mặt của hormone $hCG$ (có cấu trúc tương tự $LH$) bài tiết ra trong nước tiểu mẹ sớm.")])

    # TF-088
    add("physiology", "adv", "Diễn thế Sinh thái & Độ Đa dạng Quần xã",
        "So sánh diễn biến cấu trúc của một quần xã sinh vật trong suốt tiến trình diễn thế nguyên sinh (khởi đầu từ bãi tro tàn núi lửa đá trần không đất) tới giai đoạn quần xã đỉnh cực (rừng ôn đới/nhiệt đới trưởng thành), và cách đo độ đa dạng loài:",
        [("Trong tiến trình diễn thế từ quần xã tiên phong (địa y, rêu) hướng tới quần xã đỉnh cực, tổng sinh khối tích lũy, số lượng loài, độ phức tạp lưới thức ăn và khả năng tự điều chỉnh ổn định nhìn chung tăng dần theo thời gian.",
          True, "Quá trình hình thành đất mùn dày dần kéo theo sự đa dạng hóa cấu trúc tầng tán và nhiều ổ sinh thái mới."),
         ("Nếu khu rừng đỉnh cực bị cháy rừng hoàn toàn hoặc chặt trắng nhưng lớp đất mùn, rễ cây và ngân hàng hạt giống dưới đất vẫn còn tồn tại, quá trình phục hồi sau đó diễn ra chậm hơn diễn thế nguyên sinh rất nhiều lần.",
          False, "Đó là diễn thế THỨ SINH — vì đã có sẵn nền đất giàu dinh dưỡng và nguồn hạt mầm sống sót nên diễn thế thứ sinh diễn ra NHANH hơn rất nhiều so với diễn thế nguyên sinh trên đá trần."),
         ("Hai quần xã cùng có đúng $4$ loài cây ($S = 4$) nhưng Quần xã $1$ phân bố đồng đều ($25\\%, 25\\%, 25\\%, 25\\%$) sẽ có chỉ số đa dạng loài (theo cả Shannon-Wiener và Simpson) cao hơn hẳn Quần xã $2$ có $1$ loài chiếm tới $97\\%$ cá thể ($97\\%, 1\\%, 1\\%, 1\\%$).",
          True, "Độ đa dạng loài là hàm kết hợp của cả Độ giàu loài (Species richness) và Độ đồng đều tương đối (Relative abundance / Evenness)."),
         ("Theo giả thuyết 'nhiễu loạn trung bình' (Intermediate Disturbance Hypothesis), mức độ xáo trộn môi trường ở cường độ và tần suất vừa phải thường duy trì độ đa dạng loài CAO hơn so với khi môi trường hoàn toàn yên tĩnh hoặc bị tàn phá quá khắc nghiệt liên tục.",
          True, "Nhiễu loạn trung bình ngăn loài cạnh tranh ưu thế loại trừ sạch các loài khác nhưng vẫn đủ thời gian cho nhiều loài tái định cư.")])

    # TF-089
    add("physiology", "hsg", "Dòng Năng lượng & Ngân sách Sinh học Hệ Sinh thái",
        "Nghiên cứu dòng năng lượng chảy qua một hệ sinh thái rừng rụng lá ôn đới trong $1$ năm thu được số liệu thống kê tính trên $1\\text{ m}^2$: Tổng năng lượng bức xạ mặt trời chiếu tới là $1.5 \\times 10^6\\text{ kcal}$; Sinh vật sản xuất cố định được sản lượng sơ cấp thô $GPP = 24\\,000\\text{ kcal}$, trong đó thực vật tự hô hấp mất $R_a = 14\\,000\\text{ kcal}$. Động vật ăn cỏ (SVTT bậc $1$) ăn tiêu thụ $20\\%$ sản lượng $NPP$, phần còn lại rơi rụng vào lưới thức ăn mùn bã hoặc tích lũy trong thân gỗ. Xét các tính toán sau:",
        [("Sản lượng sơ cấp tinh ($NPP$) do hệ thực vật tích lũy thành chất hữu cơ mới trong năm bằng $10\\,000\\text{ kcal/m}^2\\text{/năm}$.",
          True, "$NPP = GPP - R_a = 24\\,000 - 14\\,000 = 10\\,000\\text{ kcal/m}^2\\text{/năm}$."),
         ("Hiệu suất sử dụng năng lượng bức xạ mặt trời tính theo sản lượng sơ cấp thô ($GPP$) của thảm thực vật rừng là $1.6\\%$ và theo sản lượng tinh ($NPP$) là $6.67\\%$.",
          False, "Hiệu suất theo $GPP$: $\\frac{24\\,000}{1\\,500\\,000} = 1.6\\%$ (ĐÚNG); nhưng hiệu suất theo $NPP$: $\\frac{10\\,000}{1\\,500\\,000} = 0.67\\%$ (gần $0.667\\%$), không phải $6.67\\%$!"),
         ("Tổng lượng năng lượng chứa trong thức ăn mà động vật ăn cỏ đã ăn vào ($I$) bằng $2000\\text{ kcal/m}^2\\text{/năm}$; giả sử $50\\%$ lượng đó mất qua phân ($F$) và $40\\%$ lượng đã ăn được dùng cho hô hấp tế bào ($R$), thì phần sinh trưởng tích lũy ($P$) của động vật ăn cỏ chỉ là $200\\text{ kcal/m}^2\\text{/năm}$.",
          True, "$I = 20\\% \\times 10\\,000 = 2000\\text{ kcal}$. $F = 1000\\text{ kcal}$, $R = 800\\text{ kcal} \\Rightarrow P = 2000 - 1000 - 800 = 200\\text{ kcal}$. (Hiệu suất sinh thái truyền $200/10\\,000 = 2\\%$ tính từ tổng NPP hoặc $10\\%$ tính trên lượng ăn vào)."),
         ("Trong hầu hết các hệ sinh thái rừng trên cạn trưởng thành, lượng cacbon và năng lượng từ phần rụng lá rơi vào chuỗi thức ăn phế liệu (sinh vật ăn mùn bã và phân giải) thường lớn hơn nhiều so với luồng bị động vật ăn cỏ ăn sống trực tiếp.",
          True, "Ở rừng ôn đới/nhiệt đới, $> 70-80\\%$ $NPP$ là gỗ và lá rụng đi trực tiếp vào hệ phân giải trong đất thay vì đi qua chuỗi gặm cỏ.")])

    # TF-090
    add("physiology", "adv", "Sinh thái học Bảo tồn & Biến đổi Khí hậu",
        "Trước thách thức suy giảm đa dạng sinh học toàn cầu do mất sinh cảnh và biến đổi khí hậu từ hoạt động con người, sinh thái học bảo tồn đưa ra các phân tích và giải pháp khoa học sau:",
        [("Khi một khu rừng nguyên sinh rộng lớn bị chia cắt thành hàng chục mảnh rừng nhỏ tách rời bởi đường cao tốc và nương rẫy, tổng diện tích 'vùng biên' (Edge effect) sẽ GIẢM đi đáng kể giúp các loài sống sâu trong lõi rừng phát triển mạnh hơn.",
          False, "Phân mảnh sinh cảnh làm TĂNG vọt tỷ lệ chu vi/diện tích, mở rộng mạnh vùng biên chịu gió lốc, ánh sáng gắt và loài xâm lấn, thu hẹp nghiêm trọng vùng lõi bên trong khiến các loài đặc hữu vùng lõi suy thoái nhanh."),
         ("Xây dựng các hành lang sinh thái nối liền các khu bảo tồn bị tách rời giúp duy trì dòng di-nhập gen tự nhiên giữa các quần thể, giảm giao phối cận huyết và tăng khả năng sống sót khi loài phải dịch chuyển tránh biến đổi khí hậu.",
          True, "Tuy nhiên cũng cần kiểm soát hành lang sinh thái cẩn thận để hạn chế phát tán mầm bệnh hoặc loài ngoại lai xâm hại."),
         ("Nồng độ $CO_2$ khí quyển tăng cao hòa tan nhiều vào đại dương tạo thành axit cacbonic ($H_2CO_3$) làm giảm độ pH nước biển (axit hóa đại dương) và làm giảm mạnh nồng độ ion cacbonat ($CO_3^{2-}$), đe dọa trực tiếp sự tạo bộ khung $CaCO_3$ của rạn san hô và động vật thân mềm.",
          True, "$CO_2 + H_2O \\rightarrow H_2CO_3 \\rightarrow H^+ + HCO_3^-$; các ion $H^+$ dư kết hợp với $CO_3^{2-}$ thành $HCO_3^-$, làm cạn kiệt nguồn $CO_3^{2-}$ cho quá trình vôi hóa."),
         ("Hiện tượng nóng lên toàn cầu làm mất cân bằng nhịp sinh học (Phenological mismatch) giữa thực vật có hoa và côn trùng thụ phấn hoặc giữa thời điểm nở hoa-sâu non với mùa sinh sản của chim di cư ăn sâu.",
          True, "Do một số loài phản ứng theo nhiệt độ (nở hoa/sâu nở sớm hơn) trong khi chim di cư lại định hướng thời điểm bay dựa trên quang chu kỳ (độ dài ngày cố định theo vĩ độ) dẫn đến lệch pha nguồn thức ăn.")])

    assert len(items) == 45, f"Expected 45 TF items in Block B, got {len(items)}"
    return items, idx
