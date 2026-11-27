# -*- coding: utf-8 -*-
"""
Block A of True/False bank: 45 TF questions (15 cellbio + 15 molecular + 15 cellular).
"""
from common import make_tf


def get_block_a():
    items = []
    idx = 1

    def add(topic, level, subtopic, stem, stmts, sexp=""):
        nonlocal idx
        qid = f"TF-{idx:03d}"
        items.append(make_tf(qid, topic, level, subtopic, stem, stmts, sexp))
        idx += 1

    # ==================== TOPIC 1: CELLBIO (TF-001 .. TF-015) ====================
    # TF-001
    add("cellbio", "basic", "Nước & Hóa học Tế bào",
        "Nước chiếm khoảng $70 - 90\\%$ khối lượng tế bào sống và đóng vai trò dung môi vạn năng nhờ tính phân cực cùng mạng lưới liên kết hiđrô giữa các phân tử. Khi phân tích các đặc tính lý-hóa của nước trong sinh học tế bào, mỗi nhận định sau đây Đúng hay Sai?",
        [("Liên kết hiđrô giữa các phân tử nước là liên kết yếu hình thành giữa nguyên tử hiđrô mang một phần điện tích dương ($\\delta^+$) của phân tử này với nguyên tử oxi mang một phần điện tích âm ($\\delta^-$) của phân tử khác.",
          True, "Tính phân cực của liên kết cộng hóa trị O-H tạo lực hút tĩnh điện yếu gọi là liên kết hiđrô giữa các phân tử nước lân cận."),
         ("Nhờ hệ thống liên kết hiđrô dày đặc, nước có nhiệt dung riêng rất cao giúp tế bào và cơ thể sinh vật tránh được sự biến động nhiệt độ đột ngột.",
          True, "Cần lượng nhiệt lớn để phá vỡ mạng liên kết hiđrô trước khi làm tăng động năng phân tử nước, giúp ổn định thân nhiệt và môi trường nước."),
         ("Ở trạng thái rắn (nước đá), các phân tử nước xếp xít nhau hơn trạng thái lỏng nên khối lượng riêng của băng lớn hơn nước lỏng và chìm xuống đáy ao hồ vào mùa đông.",
          False, "Khi đóng băng ($0^\\circ\\text{C}$), các liên kết hiđrô cố định thành mạng tinh thể tứ diện thưa rỗng làm thể tích tăng, tỷ trọng nhẹ hơn nước lỏng nên băng nổi lên trên cách nhiệt cho thủy sinh vật."),
         ("Nước là môi trường trực tiếp cho các phản ứng thủy phân (như thủy phân tinh bột, protein) cũng như tham gia trực tiếp làm chất cho electron trong quang phân ly nước.",
          True, "Nước vừa là dung môi vừa là chất tham gia trực tiếp các phản ứng sinh hóa thiết yếu của tế bào.")])

    # TF-002
    add("cellbio", "adv", "Cấu trúc Màng sinh chất",
        "Theo mô hình khảm động (Fluid Mosaic Model) của Singer và Nicolson (1972), màng sinh chất cấu tạo chủ yếu từ lớp kép photpholipit và các phân tử protein cùng cacbohiđrat, cholesterol. Xét các nhận định sau về cấu trúc và tính chất màng tế bào động vật:",
        [("Các phân tử photpholipit có đầu ưa nước hướng ra ngoài tiếp xúc môi trường nước và hai đuôi axit béo kỵ nước quay vào trong lõi màng.",
          True, "Tính chất lưỡng cực của photpholipit khiến chúng tự lắp ráp thành lớp kép kín bền vững trong môi trường nước."),
         ("Các phân tử cholesterol xen kẽ giữa lớp kép photpholipit giúp ổn định tính lỏng của màng: hạn chế chuyển động quá mức khi nhiệt độ cao và ngăn màng đông cứng kết tinh khi nhiệt độ hạ thấp.",
          True, "Cholesterol đóng vai trò chất đệm điều hòa độ linh động màng sinh chất ở tế bào động vật."),
         ("Ở tế bào nhân thực, tất cả các protein xuyên màng chỉ bám hờ trên bề mặt ngoài bằng lực hút tĩnh điện yếu chứ không xuyên qua vùng lõi kỵ nước của lớp kép.",
          False, "Protein xuyên màng (protein tích hợp) có vùng kỵ nước nằm lọt sâu trong lõi axit béo xuyên suốt lớp kép photpholipit để làm kênh, chất mang hoặc thụ thể."),
         ("Khi thả tế bào hồng cầu người bình thường vào dung dịch muối $NaCl$ nồng độ $1.8\\%$ (ưu trương), nước sẽ đi từ trong tế bào ra ngoài khiến hồng cầu bị co rút nhăn nheo.",
          True, "Nước muối sinh lý đẳng trương là $0.9\\%$; dung dịch $1.8\\%$ là ưu trương nên nước thẩm thấu ra ngoài làm hồng cầu teo lại.")])

    # TF-003
    add("cellbio", "basic", "Hệ thống Bào quan Tế bào nhân thực",
        "Một nhà sinh học tế bào theo dõi con đường tổng hợp và tiết một loại enzyme tiêu hóa protein ngoại bào (như Pepsinogen ở tế bào tuyến dạ dày) bằng phương pháp đánh dấu đồng vị phóng xạ $^{3}H$-Leucine (axit amin). Xét các nhận định sau:",
        [("Chuỗi polipeptit sơ khai của enzyme tiết được tổng hợp bởi các ribosome bám trên bề mặt mạng lưới nội chất hạt (RER).",
          True, "Protein xuất bào, protein màng và enzyme lizôxôm được dịch mã tại ribosome trên lưới nội chất hạt rồi đẩy vào xoang RER."),
         ("Mạng lưới nội chất trơn (SER) chịu trách nhiệm tổng hợp chuỗi mARN để truyền ra tế bào chất dịch mã tạo enzyme protein tiết.",
          False, "mARN được tổng hợp trong nhân tế bào; SER không có ribosome mà chuyên tổng hợp lipid, phospholipid, hormone steroid và khử độc."),
         ("Từ lưới nội chất hạt, protein được gói trong túi vận chuyển chuyển tới bộ máy Golgi để hoàn thiện cấu trúc (như gắn nhóm đường), phân loại và đóng gói vào túi tiết.",
          True, "Bộ máy Golgi nhận túi từ mặt cis, sửa đổi hóa học và xuất túi tiết ở mặt trans đưa đến màng sinh chất."),
         ("Quá trình giải phóng enzyme ra khỏi màng tế bào theo cơ chế xuất bào (exocytosis) cần tiêu tốn năng lượng ATP và sự trợ giúp của khung xương tế bào.",
          True, "Xuất bào là hình thức vận chuyển tích cực khối lớn sử dụng ATP và vi ống khung xương tế bào.")])

    # TF-004
    add("cellbio", "adv", "Thuyết Nội cộng sinh - Ty thể & Lục lạp",
        "Thuyết nội cộng sinh (Endosymbiosis) giải thích nguồn gốc của ty thể và lục lạp ở tế bào nhân thực hiện đại là hậu quả của việc tế bào nhân thực cổ đại thực bào các vi khuẩn hiếu khí và vi khuẩn lam quang hợp nhưng không tiêu hóa chúng. Những bằng chứng nào sau đây ủng hộ thuyết này?",
        [("Cả ty thể và lục lạp đều chứa phân tử ADN dạng vòng kép trần (không liên kết với protein histon) tương tự nhiễm sắc thể của vi khuẩn.",
          True, "Hệ gen riêng dạng vòng trần là đặc điểm di truyền cổ điển có nguồn gốc vi khuẩn."),
         ("Ribosome bên trong chất nền ty thể và stroma lục lạp thuộc loại $70S$, nhạy cảm với một số kháng sinh ức chế vi khuẩn như chloramphenicol giống ribosome sinh vật nhân sơ.",
          True, "Tế bào chất nhân thực dùng ribosome $80S$, nhưng ty thể/lục lạp dùng ribosome $70S$ đặc trưng của vi khuẩn."),
         ("Màng ngoài của ty thể hoàn toàn không chứa photpholipit, còn màng trong hoàn toàn phẳng không gấp nếp mà chứa thành phần peptidoglycan dày giống vi khuẩn Gram dương.",
          False, "Cả 2 màng ty thể đều là màng photpholipit; màng trong gấp nếp thành mào (cristae) chứa nhiều cardiolipin (giống màng vi khuẩn) và không có lớp peptidoglycan dày."),
         ("Ty thể và lục lạp tự phân chia bên trong tế bào bằng nguyên phân có hình thành thoi vô sắc từ trung thể của nhân tế bào.",
          False, "Hai bào quan này tự nhân đôi độc lập bằng cách phân đôi giống vi khuẩn chứ không dùng thoi vô sắc hay phụ thuộc kỳ nguyên phân.")])

    # TF-005
    add("cellbio", "hsg", "Động học Enzyme & Chất ức chế",
        "Một nhà sinh hóa học đo tốc độ ban đầu ($V_0$) của một enzyme tuân theo phương trình Michaelis-Menten theo nồng độ cơ chất $[S]$ ở 3 nghiệm thức: (I) Không có chất ức chế ($V_{\\max} = 100\\text{ \\mu mol/phút}$, $K_m = 2\\text{ mM}$); (II) Bổ sung chất ức chế X; (III) Bổ sung chất ức chế Y. Kết quả thu được cho thấy chất X làm $V_{\\max}$ vẫn bằng $100$ nhưng $K_m^{\\text{app}} = 6\\text{ mM}$; chất Y làm $V_{\\max}^{\\text{app}} = 50$ nhưng $K_m$ vẫn bằng $2\\text{ mM}$. Mỗi phân tích sau Đúng hay Sai?",
        [("Chất X là chất ức chế cạnh tranh thuận nghịch, có cấu trúc tương tự cơ chất và cạnh tranh trực tiếp vào trung tâm hoạt động của enzyme.",
          True, "Chất ức chế cạnh tranh có thể bị đẩy lùi nếu tăng nồng độ $[S]$ rất cao nên $V_{\\max}$ giữ nguyên ($100$), nhưng cần nồng độ cơ chất cao hơn nên $K_m$ biểu kiến tăng ($2 \\to 6\\text{ mM}$)."),
         ("Khi tăng nồng độ cơ chất $[S]$ lên thật cao (ví dụ $500\\text{ mM}$), tác động ức chế của chất Y sẽ bị loại bỏ hoàn toàn đưa tốc độ phản ứng chạm mức $100\\text{ \\mu mol/phút}$.",
          False, "Chất Y là chất ức chế KHÔNG cạnh tranh (gắn vào vị trí ngoài trung tâm hoạt động làm biến dạng không gian TTHĐ nên giảm $V_{\\max}$ còn $50$ bất kể $[S]$ cao cỡ nào)."),
         ("Trong trường hợp bổ sung chất ức chế X, nếu giữ nồng độ cơ chất đúng bằng $6\\text{ mM}$ thì tốc độ phản ứng đo được là $50\\text{ \\mu mol/phút}$.",
          True, "Theo định nghĩa, $K_m^{\\text{app}}$ chính là nồng độ cơ chất để vận tốc đạt $\\frac{1}{2} V_{\\max} = 50\\text{ \\mu mol/phút}$."),
         ("Cơ chế điều hòa hoạt động enzyme bằng phân tử hiệu ứng dị lập thể không cạnh tranh gắn ở vùng điều hòa hoàn toàn không làm thay đổi cấu hình không gian ba chiều của phân tử enzyme.",
          False, "Chất ức chế/hoạt hóa dị lập thể hoạt động đúng bằng cách gây biến đổi cấu hình không gian (allosteric transition) của toàn bộ phân tử enzyme.")])

    # TF-006
    add("cellbio", "adv", "Điều hòa Con đường Chuyển hóa",
        "Xét con đường chuyển hóa phân nhánh trong vi khuẩn: $A \\xrightarrow{E_1} B \\xrightarrow{E_2} C$, sau đó tại $C$ chia hai nhánh: $C \\xrightarrow{E_3} D \\xrightarrow{E_4} X$ (sản phẩm $X$) và $C \\xrightarrow{E_5} F \\xrightarrow{E_6} Y$ (sản phẩm $Y$). Khi nồng độ sản phẩm cuối $X$ tích tụ dư thừa trong tế bào, phân tích logic điều hòa ức chế ngược sau đây Đúng hay Sai?",
        [("Để tối ưu hóa năng lượng, sản phẩm $X$ dư thừa sẽ trực tiếp ức chế hoàn toàn enzyme $E_1$ khiến cả sản phẩm $Y$ cũng ngừng tổng hợp hoàn toàn dù tế bào đang thiếu $Y$.",
          False, "Ở con đường phân nhánh, sản phẩm cuối $X$ chủ yếu ức chế ngược đặc hiệu enzyme đứng ngay đầu nhánh riêng ($E_3$) để $C$ chuyển hướng tạo $Y$ chứ không cắt $E_1$ làm thiếu hụt $Y$."),
         ("Sự tăng cao nồng độ $X$ gây ức chế ngược enzyme $E_3$ giúp ngăn lãng phí $C$ tạo thêm $X$ và đồng thời tạo điều kiện đẩy dòng cơ chất $C$ đi qua nhánh $E_5$ tạo $Y$.",
          True, "Cơ chế phản hồi đặc hiệu nhánh giúp điều phối thông lượng chuyển hóa cân bằng giữa hai sản phẩm cuối."),
         ("Nếu tế bào bị dư thừa đồng thời CẢ hai sản phẩm $X$ và $Y$, sự phối hợp ức chế ngược của cả $X$ và $Y$ lên $E_1$ (hoặc lên 2 isozyme của $E_1$) sẽ làm dừng chuỗi từ đầu chất $A$.",
          True, "Khi cả hai nhánh đều bão hòa, ức chế phối hợp tại bước cam kết đầu tiên $E_1$ giúp tiết kiệm cơ chất $A$ tối đa."),
         ("Nếu đột biến làm hỏng trung tâm dị lập thể của enzyme $E_3$ khiến $X$ không thể bám ức chế $E_3$, vi khuẩn có thể sản xuất liên tục quá mức sản phẩm $X$ ngay cả khi $X$ đã dư thừa.",
          True, "Mất khả năng ức chế ngược (feedback-resistant mutant) chính là nguyên lý kỹ thuật sinh học tạo các chủng vi khuẩn tăng sản xuất axit amin công nghiệp như Lysine, Glutamate.")])

    # TF-007
    add("cellbio", "adv", "Hô hấp Hiếu khí Tế bào",
        "Xét toàn bộ quá trình phân giải hoàn toàn $1$ phân tử Glucose ($C_6H_{12}O_6$) trong hô hấp hiếu khí ở tế bào nhân thực bình thường (không có chất độc ức chế chuỗi truyền điện tử). Mỗi nhận định sau Đúng hay Sai?",
        [("Giai đoạn đường phân diễn ra tại bào tương, phân cắt $1$ phân tử glucose tạo ra $2$ axit pyruvic, tích lũy ròng $2\\text{ ATP}$ (phosphoryl hóa mức cơ chất) và $2\\text{ NADH}$.",
          True, "Đường phân tiêu tốn $2\\text{ ATP}$ pha đầu tư và thu $4\\text{ ATP}$ pha thu hoạch $\\rightarrow$ ròng $2\\text{ ATP}$, kèm $2\\text{ NADH}$ và $2$ pyruvat."),
         ("Toàn bộ lượng khí $CO_2$ giải phóng từ $6$ nguyên tử cacbon của phân tử glucose đều được thải ra ở bước chuyển hóa Pyruvat $\\rightarrow$ Acetyl-CoA và Chu trình Krebs bên trong chất nền ty thể.",
          True, "$2$ $CO_2$ thoát ở phản ứng khử cacboxyl oxy hóa pyruvat thành acetyl-CoA và $4$ $CO_2$ thoát ra trong 2 vòng Krebs ($2 + 4 = 6$ cacbon)."),
         ("Trong chuỗi truyền electron ở màng trong ty thể, chất nhận điện tử cuối cùng trực tiếp từ phức hệ IV (Cytochrome c oxidase) là phân tử $CO_2$ để biến thành glucozơ.",
          False, "Chất nhận điện tử cuối cùng có độ âm điện rất cao là khí oxi phân tử ($O_2$); nhận $4e^-$ và $4H^+$ tạo thành nước $H_2O$."),
         ("Nếu bổ sung chất DNP (2,4-dinitrophenol — chất làm màng trong ty thể bị rò rỉ cho proton $H^+$ đi xuyên tự do qua lớp kép photpholipit không qua ATP synthase), tốc độ tiêu thụ $O_2$ và sinh nhiệt tăng mạnh nhưng sản lượng ATP giảm tụt nghiêm trọng.",
          True, "DNP tháo khớp (uncoupler) phá hủy chênh lệch gradient proton ($\\Delta pH$), khiến năng lượng chuỗi chuyền electron giải phóng hết thành nhiệt thay vì tổng hợp ATP.")])

    # TF-008
    add("cellbio", "basic", "Lên men & Hô hấp kị khí",
        "Hai nhóm vi sinh vật thực hiện quá trình phân giải kị khí đường glucose (không có $O_2$): Nấm men bia (*Saccharomyces cerevisiae*) thực hiện lên men rượu và Vi khuẩn sữa (*Lactobacillus*) thực hiện lên men lactic. Xét các nhận định sau:",
        [("Điểm chung thiết yếu của cả hai loại lên men là đều bắt đầu bằng giai đoạn đường phân tạo $2\\text{ ATP}$ ròng và dùng chất hữu cơ nội sinh làm chất nhận điện tử để tái sinh $NAD^+$ từ $NADH$.",
          True, "Nếu không tái oxy hóa $NADH \\rightarrow NAD^+$, đường phân cũng sẽ lập tức đình trệ do cạn nguồn $NAD^+$."),
         ("Quá trình lên men ở nấm men có bước khử cacboxyl loại đi $1$ phân tử $CO_2$ trên mỗi axit pyruvic để biến thành acetaldehyd trước khi khử thành etanol, giúp bánh mì nở phồng.",
          True, "Bọt khí $CO_2$ thoát ra làm phồng bột mì và sủi bọt khi lên men rượu bia."),
         ("Lên men lactic đồng hình ở *Lactobacillus* tạo ra lượng $CO_2$ nhiều gấp đôi so với lên men etanol ở nấm men cho mỗi mol glucose.",
          False, "Lên men lactic khử trực tiếp axit pyruvic ($C_3H_4O_3$) thành axit lactic ($C_3H_6O_3$) nhờ $NADH$ nên KHÔNG giải phóng $CO_2$."),
         ("Trong cơ xương người khi chạy nước rút cường độ tối đa thiếu oxy, tế bào cơ chuyển sang lên men etanol tạo cồn tích tụ gây mỏi cơ.",
          False, "Tế bào cơ người lên men LACTIC tạo axit lactic (sau đó gan thu hồi theo chu trình Cori chuyển ngược thành glucose), chứ không tạo etanol.")])

    # TF-009
    add("cellbio", "adv", "Pha sáng Quang hợp trên Tilacoit",
        "Nghiên cứu phức hệ màng tilacoit trong lục lạp thực vật bậc cao đang được chiếu ánh sáng trắng bình thường ở môi trường đủ nước. Xét các nhận định sau về chuỗi truyền điện tử và hóa thẩm trong pha sáng:",
        [("Electron bị bật ra khỏi cặp diệp lục a ở trung tâm phản ứng $P_{680}$ (PS II) được bù đắp trực tiếp bằng electron tách ra từ sự quang phân ly phân tử nước.",
          True, "Hệ oxy hóa nước gắn với PS II giúp $P_{680}^+$ có thế oxi hóa khử cực dương lấy lại electron từ $H_2O$ và giải phóng $O_2$."),
         ("Khi dòng electron đi qua phức hệ cytochrome $b_6 f$, các ion $H^+$ được bơm tích cực từ lòng xoang tilacoit ra ngoài chất nền stroma làm pH trong xoang tilacoit tăng cao hơn hẳn pH ở stroma.",
          False, "Ngược lại: $H^+$ được bơm từ STROMA VÀO XOANG TILACOIT (cộng thêm $H^+$ từ quang phân ly nước sinh ra ngay trong xoang) làm xoang tilacoit có pH axit ($\\approx 5$) THẤP hơn stroma ($\\approx 8$)."),
         ("Sự khuếch tán xuôi chiều gradient điện hóa của ion $H^+$ từ xoang tilacoit đi xuyên qua phức hệ kênh $ATP\\text{ synthase}$ ($CF_0 - CF_1$) quay về stroma xúc tác gắn $P_i$ vào $ADP$ tạo thành $ATP$.",
          True, "Đây là cơ chế photphoryl hóa quang hợp theo thuyết hóa thẩm của Peter Mitchell."),
         ("Nếu dùng thuốc diệt cỏ DCMU ngăn chặn sự truyền electron từ $Q_A$ sang $Q_B$ tại PS II, quá trình giải phóng khí $O_2$ từ lục lạp lập tức bị ức chế mạnh.",
          True, "Khi $Q_B$ bị khóa, PS II không giải phóng được electron nên $P_{680}$ kẹt ở trạng thái khử, ngừng nhận electron từ nước $\\rightarrow$ ngừng tạo $O_2$.")])

    # TF-010
    add("cellbio", "basic", "Cấu trúc Đại phân tử Sinh học",
        "Xét $4$ nhóm đại phân tử hữu cơ chính cấu tạo nên mọi tế bào sống: Cacbohiđrat, Lipit, Protein và Axit nucleic. Mỗi phát biểu sau đây Đúng hay Sai?",
        [("Tinh bột, glycogen và xenlulôzơ đều là các chuỗi polixaccarit cấu tạo từ cùng một loại đơn phân duy nhất là $\\alpha$ hoặc $\\beta$-glucose liên kết với nhau qua liên kết glicôzit.",
          True, "Tinh bột và glycogen ghép từ $\\alpha$-glucose dễ thủy phân dự trữ năng lượng; xenlulôzơ ghép thẳng từ $\\beta$-glucose (liên kết $\\beta$-1,4) tạo sợi bền chắc làm thành tế bào thực vật."),
         ("Protein có chức năng xúc tác sinh học cực kỳ đa dạng nhờ được tạo nên từ $20$ loại đơn phân axit amin khác nhau về nhóm gốc $R$, xếp theo trình tự đặc thù và cuộn xoắn thành cấu trúc bậc 3 không gian chính xác.",
          True, "Trình tự axit amin (bậc 1) quyết định tương tác gấp cuộn thành cấu hình không gian bậc 3, 4 quyết định chức năng sinh học."),
         ("Trong tế bào chất có nhiệt độ tăng lên tới $90^\\circ\\text{C}$, mọi protein enzyme thông thường bị biến tính làm đứt gãy sạch toàn bộ liên kết peptit trong mạch chính bậc 1.",
          False, "Biến tính do nhiệt phá vỡ các liên kết yếu (liên kết hiđrô, tương tác kỵ nước, cầu ion) làm hỏng cấu trúc bậc 2, 3, 4 nhưng KHÔNG đủ năng lượng phá vỡ liên kết peptit cộng hóa trị ở mạch bậc 1."),
         ("Lipit (như triglixerit, photpholipit, steroid) đều không có cấu tạo theo nguyên tắc đa phân từ một đơn phân giống nhau lặp lại như protein hay axit nucleic, nhưng chúng có chung tính chất kỵ nước cao.",
          True, "Lipit không phải là polymer thực thụ có đơn phân lặp lại mà là nhóm phân tử đa dạng chung đặc tính không tan trong nước.")])

    # TF-011
    add("cellbio", "adv", "Vận chuyển các chất qua Màng sinh chất",
        "Tại biểu mô ruột non người, tế bào biểu mô hấp thụ đường Glucose từ lòng ruột (nơi nồng độ Glucose có thể thấp hơn bên trong tế bào biểu mô) bằng protein đồng vận chuyển SGLT1 phụ thuộc vào chênh lệch nồng độ $Na^+$, được duy trì nhờ bơm $Na^+/K^+$ đặt ở màng đáy-bên. Xét các nhận định sau:",
        [("Glucose được đưa từ lòng ruột vào tế bào biểu mô ruột theo phương thức khuếch tán thụ động đơn thuần không hề tiêu tốn gián tiếp ATP.",
          False, "Đi ngược chiều nồng độ glucose bằng đồng vận chuyển dựa trên gradient $Na^+$ là vận chuyển chủ động THỨ CẤP, gián tiếp tiêu tốn ATP ở bơm $Na^+/K^+$ ATPase."),
         ("Protein SGLT1 cho phép $Na^+$ khuếch tán xuôi dốc điện hóa từ lòng ruột vào trong tế bào đồng thời kéo theo Glucose đi cùng chiều vào tế bào (cơ chế symport).",
          True, "Năng lượng từ dòng chảy xuôi chiều $Na^+$ giải phóng ra làm động lực đưa glucose ngược dốc vào tế bào."),
         ("Nếu nhỏ chất Ouabain ức chế đặc hiệu bơm $Na^+/K^+$ ATPase ở mặt đáy-bên tế bào biểu mô ruột, quá trình hấp thụ chủ động glucose ở mặt đỉnh qua SGLT1 cũng sẽ sớm bị đình trệ.",
          True, "Khi bơm $Na^+/K^+$ ngừng chạy, nồng độ $Na^+$ nội bào tăng lên xóa mất gradient $Na^+$ qua màng đỉnh khiến SGLT1 hết động lực hoạt động."),
         ("Thụ thể LDL trên màng tế bào gan bắt giữ hạt lipoprotein kích thước lớn bằng phương thức nhập bào qua trung gian thụ thể (Receptor-mediated endocytosis).",
          True, "Hạt LDL mang cholesterol quá lớn không qua được kênh màng nên được thu nhận đặc hiệu qua hố phủ clathrin.")])

    # TF-012
    add("cellbio", "adv", "Truyền tin Tế bào",
        "Hormone Adrenalin (tan trong nước, không tự đi qua được lớp kép photpholipit) gắn vào thụ thể $\\beta$-adrenergic trên màng tế bào gan kích hoạt con đường truyền tin nội bào gây phân giải glycogen thành glucose giải phóng vào máu. Xét các nhận định sau về chuỗi truyền tin này:",
        [("Thụ thể $\\beta$-adrenergic là một loại thụ thể kết cặp protein G (GPCR); khi Adrenalin gắn vào, protein $G_s$ giải phóng GDP để gắn GTP và hoạt hóa enzyme màng Adenylyl cyclase.",
          True, "Đây là cơ chế kinh điển của họ thụ thể GPCR xuyên màng 7 lần."),
         ("Enzyme Adenylyl cyclase chuyển hóa ATP nội bào thành chất truyền tin thứ hai là cAMP (AMP vòng); chỉ một phân tử hormone gắn vào có thể kích hoạt tạo ra hàng nghìn phân tử cAMP giúp khuếch đại tín hiệu mạnh mẽ.",
          True, "Mỗi bước hoạt hóa enzyme dây chuyền (GPCR $\\to$ Adenylyl cyclase $\\to$ PKA $\\to$ Phosphorylase kinase) nhân bội số lượng phân tử phản ứng."),
         ("Hormone sinh dục Testosterone và Estrogen bản chất steroid tan trong dầu cũng bắt buộc phải sử dụng thụ thể GPCR trên màng ngoài và cAMP do không thể chui qua lớp kép photpholipit.",
          False, "Ngược lại: hormone steroid nhỏ và ưa lipit (kỵ nước) khuếch tán dễ dàng xuyên qua lõi kỵ nước của màng sinh chất để gắn vào THỤ THỂ NỘI BÀO trong bào tương hoặc nhân."),
         ("Sau khi kết thúc kích thích, enzyme Phosphodiesterase nhanh chóng thủy phân cAMP thành AMP mất hoạt tính để tắt tín hiệu tế bào kịp thời.",
          True, "Hệ thống ngắt tín hiệu (cùng với tính tự thủy phân GTP của protein G) đảm bảo tế bào sẵn sàng đáp ứng tín hiệu mới.")])

    # TF-013
    add("cellbio", "basic", "Vi sinh vật - Cấu trúc Tế bào Nhân sơ",
        "Khi tiến hành nhuộm Gram hai chủng vi khuẩn phân lập được (*Staphylococcus aureus* bắt màu tím đặc trưng và *Escherichia coli* bắt màu hồng đỏ), phân tích sự khác biệt cấu trúc thành tế bào giải thích cho kết quả này:",
        [("Chủng *S. aureus* là vi khuẩn Gram dương có lớp thành peptidoglycan rất dày nằm bên ngoài cùng, giữ chặt phức hợp tím kết tinh – iod trong bước tẩy cồn.",
          True, "Lưới peptidoglycan dày co lại khi rửa cồn giữ phức hợp màu tím crystal violet - iod."),
         ("Chủng *E. coli* là vi khuẩn Gram âm không hề chứa thành phần peptidoglycan nào trong thành tế bào.",
          False, "Vi khuẩn Gram âm vẫn CÓ lớp peptidoglycan nhưng rất mỏng nằm trong khoang chu chất bên dưới lớp màng ngoài lipopolysaccharide (LPS)."),
         ("Thành phần Lipopolysaccharide (LPS) nằm ở lớp màng ngoài của vi khuẩn Gram âm chứa phần Lipid A có thể hoạt động như nội độc tố gây sốt và sốc nhiễm khuẩn ở người.",
          True, "LPS vừa bảo vệ vi khuẩn Gram âm khỏi thuốc nhuộm, lysozyme, một số kháng sinh (như penicillin G) vừa là nội độc tố đặc trưng."),
         ("Kháng sinh Penicillin ức chế enzyme nối chéo peptidoglycan nên phát huy hiệu quả diệt khuẩn rõ rệt nhất trên vi khuẩn đang sinh trưởng phân chia mạnh.",
          True, "Vi khuẩn đang tăng trưởng cần tổng hợp liên tục vách peptidoglycan mới; khi bị khóa nối chéo vách trở nên yếu ớt dẫn tới ly giải thẩm thấu.")])

    # TF-014
    add("cellbio", "adv", "Sinh trưởng Quần thể Vi sinh vật",
        "Nuôi cấy $10^3$ tế bào vi khuẩn *E. coli* vào bình tam giác chứa $100\\text{ ml}$ môi trường dinh dưỡng tổng hợp kín không bổ sung thêm chất dinh dưỡng mới (nuôi cấy không liên tục) chứa đồng thời hỗn hợp đường Glucose và Lactose. Quan sát đồ thị sinh trưởng của quần thể vi khuẩn:",
        [("Ở pha tiềm phát (pha lag), số lượng tế bào vi khuẩn chưa tăng rõ rệt vì chúng đang thích nghi môi trường và tổng hợp các enzyme cần thiết cho trao đổi chất.",
          True, "Pha lag là thời kỳ tổng hợp ARN, protein, enzyme chuẩn bị cho bước phân bào nhanh."),
         ("Trong giai đoạn sinh trưởng kép (diauxic), vi khuẩn tiêu thụ hết Lactose trước rồi tạm nghỉ để tổng hợp enzyme tiêu hóa Glucose vì đường đôi luôn ưu tiên hơn đường đơn.",
          False, "Vi khuẩn ưu tiên sử dụng GLUCOSE trước (đường đơn dễ chuyển hóa, gây ức chế cảm ứng operon Lac); khi cạn sạch Glucose mới có pha nghỉ thứ 2 để bật operon Lac dùng Lactose."),
         ("Giả sử trong pha lũy thừa có thời gian thế hệ $g = 20\\text{ phút}$, sau đúng $2$ giờ kể từ đầu pha lũy thừa, một dòng tế bào khởi điểm gồm $10^3$ tế bào sẽ nhân lên thành $6.4 \\times 10^4$ tế bào.",
          True, "$2\\text{ giờ} = 120\\text{ phút} \\Rightarrow n = 120 / 20 = 6$ lần phân chia. Số tế bào $N_t = 10^3 \\times 2^6 = 64 \\times 10^3 = 6.4 \\times 10^4$."),
         ("Ở pha cân bằng của nuôi cấy không liên tục, quá trình phân bào ở mọi vi khuẩn đã dừng hẳn bằng $0$ tuyệt đối và không có bất kỳ tế bào nào chết.",
          False, "Ở pha cân bằng tốc độ sinh mới bằng tốc độ chết đi ($\\approx$ nhau) nên số tế bào sống đạt cực đại ổn định trước khi chuyển sang pha suy vong.")])

    # TF-015
    add("cellbio", "hsg", "Sinh học Virus & Phage",
        "So sánh chu trình nhân lên của $3$ loại virus khác nhau: Phage $T_4$ (chỉ có chu trình tan), Phage $\\lambda$ (có chu trình tan và tiềm tan) và Retrovirus HIV (gây suy giảm miễn dịch ở người). Xét các nhận định sau:",
        [("Khi phage $\\lambda$ đi vào chu trình tiềm tan, toàn bộ axit nucleic của phage được dịch mã ngay tạo hàng trăm vỏ capsid làm vỡ tan tế bào chủ *E. coli* chỉ sau $30$ phút.",
          False, "Trong chu trình tiềm tan, ADN của phage $\\lambda$ gắn xen vào nhiễm sắc thể tế bào chủ ở trạng thái tiền phage (prophage) lặng lẽ nhân đôi cùng tế bào chủ nhiều thế hệ mà chưa làm tan tế bào."),
         ("Vật chất di truyền của virus HIV gồm $2$ phân tử ARN mạch đơn dương và được đóng gói sẵn enzyme phiên mã ngược (Reverse Transcriptase) trong lõi hạt virus.",
          True, "Tế bào người không có enzyme phiên mã ngược nên HIV buộc phải mang sẵn enzyme này trong capsid để tổng hợp cDNA mạch kép từ khuôn ARN ngay sau khi xâm nhập."),
         ("Phage $T_4$ bơm phân tử ADN vào tế bào vi khuẩn chủ còn giữ lớp vỏ protein rỗng bên ngoài, trong khi virus HIV có màng bao ngoài dung hợp với màng sinh chất để đưa cả lõi nucleocapsid vào tế bào $CD4^+$.",
          True, "Virus có gai gp120/gp41 gắn đồng thụ thể $CD4/CCR5$ rồi hòa màng; ngược lại phage bơm axit nucleic xuyên thành peptidoglycan."),
         ("Sử dụng thuốc AZT (chất tương tự thymidin thiếu nhóm $3'-OH$) có thể ức chế chọn lọc quá trình tổng hợp sợi ADN mới của HIV nhờ chặn kéo dài mạch ở enzyme phiên mã ngược.",
          True, "AZT là chất ức chế phiên mã ngược tương tự nucleoside (NRTI) làm dừng tổng hợp proviral cDNA sớm.")])

    # ==================== TOPIC 2: MOLECULAR (TF-016 .. TF-030) ====================
    # TF-016
    add("molecular", "basic", "Cấu trúc Hóa học ADN",
        "Một đoạn phân tử ADN mạch kép tuyến tính theo mô hình Watson - Crick gồm $3000$ cặp nucleotit, trong đó số nucleotit loại Guanin ($G$) chiếm $30\\%$ tổng số nucleotit của cả phân tử. Xét các nhận định định lượng và cấu trúc sau:",
        [("Tổng số nucleotit của đoạn ADN là $6000$ với chiều dài bằng $10200\\text{ \\AA}$ ($1.02\\text{ \\mu m}$).",
          True, "Tổng $N = 3000 \\times 2 = 6000$ nu; chiều dài $L = 3000 \\times 3.4 = 10200\\text{ \\AA}$."),
         ("Số nucleotit loại Adenin ($A$) trong đoạn ADN này bằng $1200$ và tổng số liên kết hiđrô giữa hai mạch đơn bằng $7800$.",
          True, "$G = 30\\% \\Rightarrow A = 20\\% = 0.2 \\times 6000 = 1200$; $G = 1800$. Số liên kết hiđrô $H = 2A + 3G = 2(1200) + 3(1800) = 2400 + 5400 = 7800$."),
         ("Khi tăng nhiệt độ dung dịch chứa đoạn ADN trên để tách biến tính $2$ mạch đơn, phân tử nào có tỷ lệ $\\frac{A+T}{G+C}$ càng cao thì nhiệt độ nóng chảy $T_m$ càng cao.",
          False, "Cặp $G \\equiv C$ có $3$ liên kết hiđrô bền vững hơn cặp $A = T$ ($2$ liên kết), nên hàm lượng $G+C$ càng cao thì $T_m$ càng cao (tỷ lệ $(A+T)/(G+C)$ cao làm $T_m$ THẤP xuống)."),
         ("Hai mạch polinucleotit của đoạn ADN chạy song song ngược chiều nhau (một mạch $5' \\rightarrow 3'$, mạch bổ sung $3' \\rightarrow 5'$), liên kết với nhau bằng lực hiđrô đặc hiệu $A=T, G \\equiv C$.",
          True, "Tính đối song và nguyên tắc bổ sung là nền tảng giúp tái bản ADN chính xác.")])

    # TF-017
    add("molecular", "adv", "Cơ chế Tái bản ADN (Sơ vs Thực)",
        "Quan sát chạc chữ Y tái bản (Replication fork) của quá trình nhân đôi phân tử ADN ở tế bào vi khuẩn *E. coli* và ở tế bào người. Mỗi nhận định sau đây Đúng hay Sai?",
        [("Ở cả sinh vật nhân sơ và nhân thực, enzyme $ADN\\text{ polymerase}$ chỉ có thể lắp ráp nucleotit tự do theo chiều $5' \\rightarrow 3'$ và bắt buộc phải có sẵn đầu $3'-OH$ tự do từ một đoạn mồi ARN ngắn.",
          True, "Đặc tính bất biến của tất cả các enzyme ADN polymerase được biết đến trên sinh giới là xúc tác tổng hợp chiều $5' \\rightarrow 3'$ cần nhóm $3'-OH$ mồi."),
         ("Trên mạch khuôn có chiều $3' \\rightarrow 5'$ (tính theo hướng mở chạc chữ Y), mạch mới được tổng hợp gián đoạn thành từng đoạn Okazaki nhờ hàng loạt đoạn mồi ARN.",
          False, "Trên mạch khuôn $3' \\rightarrow 5'$ theo hướng di chuyển của chạc chữ Y, mạch mới được tổng hợp LIÊN TỤC theo chiều $5' \\rightarrow 3'$ (mạch ra chậm mới tổng hợp gián đoạn trên khuôn $5' \\rightarrow 3'$)."),
         ("Ở sinh vật nhân sơ *E. coli*, enzyme $ADN\\text{ polymerase I}$ vừa cắt bỏ các đoạn mồi ARN bằng hoạt tính exonuclease $5' \\rightarrow 3'$ vừa lấp đầy khoảng trống bằng deoxyribonucleotit.",
          True, "Sau khi ADN pol III tổng hợp đoạn Okazaki, ADN pol I thay mồi bằng ADN và Ligase nối khe hở photphodieste cuối cùng."),
         ("Trong mọi tế bào sinh dưỡng (xôma) đã biệt hóa của cơ thể người trưởng thành, enzyme Telomerase hoạt động cực mạnh giúp các đầu mút NST kéo dài mãi mãi không bao giờ bị ngắn đi.",
          False, "Ở tế bào xôma trưởng thành, gen Telomerase bị tắt nên telomere ngắn dần sau mỗi lần phân bào (liên quan lão hóa tế bào); telomerase chỉ hoạt động mạnh ở tế bào mầm sinh dục, tế bào gốc và $>85\\%$ tế bào ung thư.")])

    # TF-018
    add("molecular", "hsg", "Thí nghiệm Meselson - Stahl",
        "Trong thí nghiệm kinh điển chứng minh nguyên tắc bán bảo toàn của tái bản ADN: người ta nuôi vi khuẩn *E. coli* qua nhiều thế hệ trong môi trường chứa đồng vị nitơ nặng $^{15}N$ để toàn bộ ADN ban đầu đều là băng nặng ($^{15}N - ^{15}N$). Sau đó rửa sạch rồi chuyển vi khuẩn sang môi trường chỉ chứa đồng vị nhẹ $^{14}N$ và cho phân chia đồng bộ qua $3$ thế hệ liên tiếp (thu được $8$ lần số lượng phân tử ADN ban đầu). Mỗi nhận định sau Đúng hay Sai?",
        [("Sau $1$ thế hệ nhân đôi trong môi trường $^{14}N$, ly tâm phân tách ADN thu được hai băng rõ rệt bằng nhau gồm $50\\%$ ADN băng nặng ($^{15}N - ^{15}N$) và $50\\%$ ADN băng nhẹ ($^{14}N - ^{14}N$).",
          False, "Sau thế hệ $1$, tất cả $100\\%$ phân tử ADN con đều là băng LAI trung bình ($^{15}N - ^{14}N$), loại bỏ thuyết bảo toàn."),
         ("Sau $2$ thế hệ nhân đôi trong môi trường $^{14}N$, tỷ lệ phân tử ADN mang cấu trúc lai ($^{15}N - ^{14}N$) chiếm $50\\%$ tổng số phân tử ADN tạo thành.",
          True, "Trong $4$ phân tử ADN ở $F_2$: $2$ phân tử vẫn giữ $2$ mạch gốc $^{15}N$ nên ở dạng lai $^{15}N-^{14}N$ ($50\\%$), và $2$ phân tử hoàn toàn nhẹ $^{14}N-^{14}N$ ($50\\%$)."),
         ("Sau $3$ thế hệ nhân đôi trong môi trường $^{14}N$, trong tổng số mạch đơn polinucleotit của tất cả các phân tử ADN thu được, số mạch đơn chỉ chứa $^{15}N$ chiếm $25\\%$.",
          False, "Tổng số phân tử ADN $= 2^3 = 8$ phân tử $= 16$ mạch đơn, trong đó chỉ có đúng $2$ mạch đơn ban đầu chứa $^{15}N$ $\\Rightarrow$ tỷ lệ mạch đơn chứa $^{15}N = \\frac{2}{16} = 12.5\\%$ (còn tỷ lệ PHÂN TỬ ADN lai mới là $2/8 = 25\\%$)."),
         ("Nếu tiếp tục nhân đôi đến thế hệ thứ $5$ trong môi trường $^{14}N$, tổng số phân tử ADN hoàn toàn chỉ chứa $^{14}N$ (băng nhẹ) gấp $15$ lần số phân tử ADN lai ($^{15}N - ^{14}N$).",
          True, "Tại thế hệ $5$: có $2^5 = 32$ phân tử, trong đó $2$ phân tử lai và $32 - 2 = 30$ phân tử nhẹ hoàn toàn. Tỷ số $30 / 2 = 15$ lần!")])

    # TF-019
    add("molecular", "adv", "Sửa sai ADN & Bệnh di truyền Sửa sai",
        "Độ chính xác cực cao của sao chép ADN ($\\sim 10^{-9}$ sai sót mỗi cặp bazơ) là nhờ hệ thống kiểm sửa nhiều lớp của tế bào. Xét các nhận định sau về cơ chế sửa sai ADN:",
        [("Khi $ADN\\text{ polymerase}$ đang tổng hợp mạch mới chiều $5' \\rightarrow 3'$ vô tình gắn nhầm một nucleotit không đúng cặp bổ sung, enzyme có thể lùi lại cắt bỏ nucleotit sai bằng hoạt tính exonuclease $3' \\rightarrow 5'$ (đọc sửa ngay lập tức).",
          True, "Hoạt tính đọc sửa (proofreading $3' \\to 5'$) giảm tỷ lệ sai sót từ $\\sim 10^{-5}$ xuống còn $\\sim 10^{-7}$ ngay tại chạc nhân đôi."),
         ("Hệ thống sửa chữa bắt cặp sai (Mismatch Repair - MMR) hoạt động sau khi nhân đôi xong, phân biệt mạch mới tổng hợp để sửa lại theo khuôn mạch cũ nhằm tránh biến sai sót thành đột biến cố định.",
          True, "Ở *E. coli*, MMR dựa vào dấu methyl hóa gốc A ở trình tự `GATC` của mạch khuôn mẹ (mạch mới vừa tổng hợp chưa bị methyl hóa ngay) để nhận diện mạch mới."),
         ("Tia cực tím (UV) từ ánh sáng mặt trời thường gây đột biến tạo liên kết cộng hóa trị giữa hai bazơ nitơ Timin đứng cạnh nhau trên cùng một mạch (Dimer Timin); tế bào người sửa sai tổn thương cồng kềnh này bằng cơ chế cắt bỏ nucleotit (NER).",
          True, "Thiếu hụt hệ enzyme NER di truyền gây bệnh khô da sắc tố (*Xeroderma pigmentosum*), bệnh nhân cực nhạy cảm tia UV và dễ ung thư da sớm."),
         ("Các bazơ nitơ bị hỏng trong ADN luôn bắt buộc phải cắt bỏ toàn bộ chiều dài cả một nhiễm sắc thể rồi mới gắn ghép lại từng nucleotit.",
          False, "Cơ chế sửa cắt bỏ bazơ (BER) hoặc NER chỉ cắt bỏ $1$ bazơ hỏng hoặc đoạn ngắn khoảng $12 - 30$ nucleotit chứa tổn thương và dùng mạch đối diện làm khuôn tổng hợp bù.")])

    # TF-020
    add("molecular", "basic", "Phiên mã & Chế biến mARN Nhân thực",
        "Quá trình phiên mã tổng hợp $mARN$ trưởng thành ở tế bào nhân thực khác biệt sâu sắc về không gian và các bước biến đổi sau phiên mã so với vi khuẩn. Xét các nhận định sau:",
        [("Ở tế bào nhân thực, quá trình phiên mã và dịch mã xảy ra đồng thời tại một chỗ vì phân tử tiền-$mARN$ ngay khi đang phiên mã dở trong nhân đã được ribosome trong nhân bám vào dịch mã.",
          False, "Tế bào nhân thực có màng nhân ngăn cách: phiên mã và chế biến $mARN$ xảy ra trong nhân, sau đó $mARN$ trưởng thành mới đi qua lỗ màng nhân ra tế bào chất dịch mã (khác nhân sơ ghép đôi đồng thời)."),
         ("Đầu $5'$ của tiền-$mARN$ do $ARN\\text{ polymerase II}$ tổng hợp được gắn một mũ 7-metylguanozin giúp bảo vệ $mARN$ khỏi enzyme phân giải và hỗ trợ tiểu phần nhỏ ribosome nhận diện khởi đầu dịch mã.",
          True, "Mũ $5'$-cap được gắn rất sớm ngay khi chuỗi ARN vừa vươn dài vài chục nucleotit."),
         ("Đuôi $3'$-polyA gồm khoảng $50 - 250$ nucleotit loại Adenin được gắn sau phiên mã bởi enzyme Poly(A) polymerase mà không cần có trình tự dT tương ứng trên mạch khuôn ADN.",
          True, "Đuôi polyA tăng độ bền của $mARN$ trong bào tương và tạo thuận lợi cho xuất bào qua màng nhân."),
         ("Nhờ cơ chế cắt ghép thay thế (Alternative Splicing) tổ hợp lại các đoạn exon khác nhau từ cùng một phân tử tiền-$mARN$, một gen nhân thực có thể tạo ra nhiều chuỗi polipeptit có chức năng biến đổi khác nhau ở các mô.",
          True, "Splicing thay thế giải thích vì sao hệ gen người chỉ có $\\approx 20\\,000$ gen mã hóa protein nhưng lại tạo ra hàng trăm nghìn loại protein khác nhau.")])

    # TF-021
    add("molecular", "basic", "Mã Di truyền",
        "Phân tích đặc điểm và cấu trúc bảng mã di truyền chuẩn trên phân tử $mARN$ của sinh giới:",
        [("Mã di truyền có tính thoái hóa, tức là nhiều bộ ba khác nhau có thể cùng mã hóa cho một loại axit amin (ngoại trừ $AUG$ cho Methionine và $UGG$ cho Tryptophan mỗi chất chỉ có duy nhất $1$ codon).",
          True, "Trong $61$ codon mã hóa cho $20$ axit amin, phần lớn axit amin được mã hóa bởi $2, 3, 4$ hoặc $6$ bộ ba đồng nghĩa."),
         ("Bộ ba $AUG$ vừa là mã mở đầu quy định Methionine (hay formylmethionine ở sinh vật nhân sơ), vừa có thể xuất hiện ở giữa gen để mã hóa thêm các phân tử Methionine nội chuỗi.",
          True, "$AUG$ đầu khung đọc được tARN khởi đầu đặc hiệu nhận diện; $AUG$ phía trong được tARN mang Met nội chuỗi kéo dài nhận diện."),
         ("Cả $64$ bộ ba trên $mARN$ đều tương ứng với ít nhất $1$ phân tử $tARN$ mang axit amin trong tế bào sống bình thường.",
          False, "Có $3$ bộ ba kết thúc (`5'-UAA-3'`, `5'-UAG-3'`, `5'-UGA-3'`) không mã hóa axit amin và không có $tARN$ bình thường tương ứng mà được các yếu tố giải phóng (Release factor) nhận diện."),
         ("Mã di truyền có tính đặc hiệu tuyệt đối nghĩa là một loại axit amin chỉ có thể do duy nhất một codon quy định trên toàn hệ gen.",
          False, "Đó là nhầm khái niệm 'tính thoái hóa' với 'tính đặc hiệu': tính đặc hiệu nghĩa là $1$ bộ ba chỉ mã hóa cho $1$ loại axit amin (không nhập nhằng), chứ $1$ axit amin có thể có nhiều bộ ba.")])

    # TF-022
    add("molecular", "adv", "Cơ chế Dịch mã & Ribosome",
        "Xét hoạt động của phức hệ ribosome trong giai đoạn dịch mã tổng hợp chuỗi polipeptit trên $mARN$ của tế bào sống:",
        [("Trên khung cấu trúc $3$ vị trí của ribosome theo thứ tự đi qua của $tARN$, $tARN$ mới mang axit amin tiến vào vị trí **A**, tạo liên kết peptit rồi trượt sang vị trí **P**, và thoát ra qua vị trí **E**.",
          True, "Trình tự chuẩn tại ribosome trong bước kéo dài là A (Aminoacyl) $\\rightarrow$ P (Peptidyl) $\\rightarrow$ E (Exit)."),
         ("Liên kết giữa bộ ba đối mã (anticodon) trên $tARN$ và bộ ba mã sao (codon) trên $mARN$ tuân theo nguyên tắc bổ sung đối song; ví dụ codon `5'-GCA-3'` khớp với anticodon `3'-CGU-5'`.",
          True, "$mARN$ đọc theo chiều $5' \\rightarrow 3'$, còn $tARN$ áp sát đối song theo chiều $3' \\rightarrow 5'$."),
         ("Hoạt tính enzyme Peptidyl transferase xúc tác hình thành liên kết peptit nối các axit amin trong tiểu phần lớn ribosome thực chất do phân tử **$rARN$** (ribozyme) chứ không phải do protein ribosome đảm nhiệm.",
          True, "Khám phá cấu trúc tinh thể khẳng định trung tâm peptidyl transferase là lõi $rARN$ ($23S$ ở nhân sơ, $28S$ ở nhân thực) — bằng chứng lớn ủng hộ Thế giới ARN."),
         ("Trên một phân tử $mARN$, nhiều ribosome trượt nối tiếp nhau thành chuỗi Polysome để từ $1$ khuôn $mARN$ tổng hợp ra đồng thời nhiều loại protein hoàn toàn khác hẳn trình tự nhau.",
          False, "Polysome giúp tăng năng suất tổng hợp CÙNG MỘT LOẠI chuỗi polipeptit giống hệt nhau trên một bản sao $mARN$ trong thời gian ngắn.")])

    # TF-023
    add("molecular", "hsg", "Điều hòa Hoạt động Gen - Operon Lac",
        "Xét cơ chế điều hòa cảm ứng dương và âm tính của Operon Lac ở vi khuẩn *E. coli* (gồm vùng khởi động $P$, vùng vận hành $O$, các gen cấu trúc $lacZ, lacY, lacA$, cùng gen điều hòa $lacI$ nằm gần đó). Xét các kịch bản đột biến và môi trường sau:",
        [("Gen điều hòa $lacI$ nằm ngoài operon nhưng sản phẩm protein ức chế do nó mã hóa gắn vào vùng vận hành $O$ khi môi trường KHÔNG có đường Lactose, ngăn cản $ARN\\text{ polymerase}$ trượt qua phiên mã.",
          True, "Không có chất cảm ứng allolactose, protein ức chế liên kết bền chặt vào operator $O$ khóa chặt operon ở trạng thái tắt."),
         ("Khi môi trường không có cả Glucose lẫn Lactose, nồng độ cAMP nội bào tăng vọt giúp phức hệ $cAMP-CAP$ bám vào vùng $P$, đủ sức làm các gen $lacZ, lacY, lacA$ phiên mã rầm rộ ngay cả khi vắng mặt Lactose.",
          False, "Dù $cAMP-CAP$ gắn vào $P$ để hoạt hóa dương, nhưng vì KHÔNG CÓ Lactose nên protein ức chế $LacI$ vẫn đang bám chặt chẹn ngang vùng $O$ khiến phiên mã vẫn bị khóa chặt!"),
         ("Nếu vi khuẩn mang đột biến mất hoàn toàn khả năng gắn protein ức chế ở vùng vận hành ($lacO^c$ — đột biến vận hành cơ định), operon Lac sẽ luôn bật phiên mã liên tục cả khi môi trường có hay không có Lactose.",
          True, "$O^c$ là đột biến tác động cis (chỉ tác động lên operon nằm cùng phân tử ADN đó), mất điểm bám repressor nên biểu hiện liên tục."),
         ("Khi có đột biến vô nghĩa ở gen $lacZ$ tạo bộ ba kết thúc sớm, gen $lacZ$ không tạo được $\\beta$-galactosidase có hoạt tính nhưng các gen phía sau ($lacY, lacA$) vẫn được phiên mã thành một $mARN$ polycistronic khi có Lactose (nếu không xét hiệu ứng phân cực nặng).",
          True, "Operon Lac phiên mã chung $1$ phân tử $mARN$ cho cả $lacZ-lacY-lacA$, nên khi dịch mã ribosome tới mã dừng sớm ở $lacZ$ sẽ rụng xuống nhưng vẫn khởi đầu dịch mã được độc lập tại $AUG$ đầu gen $lacY$ và $lacA$.")])

    # TF-024
    add("molecular", "basic", "Đột biến Điểm Gen cấu trúc",
        "Phân tích hậu quả phân tử của các dạng đột biến điểm (liên quan $1$ cặp nucleotit) xảy ra trong vùng mã hóa exon của một gen quy định chuỗi polipeptit:",
        [("Mọi đột biến thay thế một cặp nucleotit đều làm thay đổi toàn bộ trình tự axit amin kể từ vị trí đột biến trở về sau cho đến tận cuối chuỗi polipeptit.",
          False, "Thay thế $1$ cặp nu chỉ tác động tối đa lên $1$ bộ ba (có thể gây đột biến đồng nghĩa không đổi aa, nhầm nghĩa đổi $1$ aa, hoặc vô nghĩa); chỉ mất/thêm không chia hết cho $3$ mới gây dịch khung toàn phần sau đó."),
         ("Đột biến thay thế `A-T` thành `T-A` ở codon thứ $6$ của gen $\\beta$-globin người làm đổi bộ ba `GAG` (Glutamate) thành `GUG` (Valine), gây bệnh thiếu máu hồng cầu hình liềm.",
          True, "Đây là ví dụ kinh điển của đột biến nhầm nghĩa (missense mutation) gây biến đổi sâu sắc tính tan của hemoglobin khi thiếu oxy."),
         ("Đột biến vô nghĩa (Nonsense mutation) biến một bộ ba mã hóa axit amin ở giữa gen thành bộ ba kết thúc (`UAA`, `UAG`, `UGA`), tạo ra chuỗi polipeptit ngắn bất thường và thường mất chức năng.",
          True, "Càng xuất hiện mã dừng sớm gần đầu $5'$, chuỗi polipeptit bị cắt cụt càng nhiều và thường bị thoái biến nhanh."),
         ("Nếu thêm $1$ cặp nucleotit vào ngay sau codon khởi đầu `AUG` và mất $1$ cặp nucleotit cách đó $6$ nucleotit về phía $3'$, khung đọc đoạn phía sau cả hai vị trí sẽ được phục hồi nguyên vẹn.",
          True, "Tổng cộng thêm $1$ và mất $1$ ($+1 - 1 = 0$) nên chỉ làm xáo trộn $2-3$ axit amin nằm giữa hai điểm đột biến, còn toàn bộ phần đuôi gen giữ nguyên khung đọc cũ.")])

    # TF-025
    add("molecular", "hsg", "Biểu sinh học (Epigenetics)",
        "Di truyền biểu sinh nghiên cứu các biến đổi di truyền được qua phân bào nhưng KHÔNG làm thay đổi trình tự nucleotit trong phân tử ADN, chủ yếu thông qua methyl hóa ADN và biến đổi hóa học đuôi protein histon. Xét các nhận định sau:",
        [("Sự methyl hóa dày đặc các bazơ Cytosine tại đảo `CpG` trong vùng promoter của gen nhân thực thường thu hút phức hệ nén chất nhiễm sắc và làm TẮT phiên mã gen đó.",
          True, "Hypermethyl hóa promoter là cơ chế khóa gen dài hạn (ví dụ tắt gen ức chế khối u trong tế bào ung thư hoặc bất hoạt NST X)."),
         ("Acetyl hóa các gốc axit amin Lysine trên đuôi protein Histon (nhờ enzyme HAT) làm trung hòa điện tích dương của histon, làm lực hút với ADN (mang điện âm) lỏng lẻo hơn, tạo chất nhiễm sắc thưa dãn thuận lợi cho phiên mã.",
          True, "Euchromatin (nhiễm sắc chất hoạt động phiên mã) giàu nhóm acetyl trên đuôi histon hơn heterochromatin."),
         ("Hiện tượng bất hoạt một nhiễm sắc thể X ở tế bào sinh dưỡng động vật có vú cái (hình thành thể Barr) khiến cả hai NST X trong mỗi tế bào đều hoạt động tăng công suất gấp đôi so với nam giới $XY$.",
          False, "Chỉ CÓ MỘT NST X hoạt động trong mỗi tế bào xôma cái, còn một NST X bị đóng xoắn bất hoạt biểu sinh thành thể Barr để cân bằng liều lượng gen giữa $XX$ và $XY$."),
         ("Các dấu ấn biểu sinh (như trong hiện tượng in dấu hệ gen - Genomic Imprinting ở chuột với gen *Igf2*) được thiết lập khác nhau tùy vào giao tử có nguồn gốc từ bố hay mẹ và được duy trì ổn định suốt đời cá thể con.",
          True, "Ở động vật có vú, alen *Igf2* nhận từ bố mới được biểu hiện còn bản sao từ mẹ bị im lặng biểu sinh do khác biệt methyl hóa vùng kiểm soát ICR.")])

    # TF-026
    add("molecular", "adv", "Can thiệp ARN (RNAi - siRNA/miRNA)",
        "Cơ chế can thiệp ARN (RNA interference - RNAi, phát hiện giúp Fire và Mello đoạt giải Nobel Y học 2006) đóng vai trò trung tâm trong điều hòa biểu hiện gen sau phiên mã và bảo vệ tế bào chống virus chứa ARN mạch kép. Xét các nhận định sau:",
        [("Enzyme Dicer trong tế bào chất cắt phân tử ARN mạch kép (dsRNA) dài thành các đoạn ARN can thiệp nhỏ ($siRNA$) hay $miRNA$ dài khoảng $21-23$ cặp nucleotit.",
          True, "Dicer thuộc họ ribonuclease III cắt chính xác các đoạn dsRNA thành duplex ngắn $21-23\\text{ bp}$ có đầu lồi $2$ nu ở $3'$."),
         ("Mạch dẫn đường (guide strand) của $siRNA$ hoặc $miRNA$ gắn vào phức hệ protein Argonaute tạo phức hệ RISC, sau đó bám bổ sung vào phân tử $mARN$ mục tiêu để cắt phân hủy $mARN$ hoặc chặn ribosome dịch mã.",
          True, "Nếu khớp bổ sung hoàn hảo thường dẫn đến cắt đứt $mARN$; nếu khớp một phần vùng $3'-UTR$ (thường gặp ở $miRNA$ động vật) sẽ kìm hãm dịch mã và làm mất ổn định $mARN$."),
         ("Cơ chế RNAi tác động trực tiếp làm cắt đứt trình tự phân tử ADN hai mạch bên trong nhân trước khi phiên mã xảy ra.",
          False, "RNAi chủ yếu tác động ở giai đoạn SAU PHIÊN MÃ (post-transcriptional) nhắm vào các phân tử $mARN$ đích trong bào tương chứ không cắt ADN mạch kép."),
         ("Tất cả phân tử $miRNA$ đều được vi khuẩn tổng hợp từ các operon nhỏ và không hề có mặt ở động vật hay thực vật đa bào.",
          False, "miRNA cực kỳ phổ biến và thiết yếu ở cả thực vật và động vật bậc cao (người có hàng nghìn gen mã hóa miRNA tham gia phát triển phôi và bệnh lý).")])

    # TF-027
    add("molecular", "adv", "Kỹ thuật PCR & Điện di Gel",
        "Một phòng xét nghiệm sử dụng kỹ thuật phản ứng chuỗi trùng hợp (PCR) để khuếch đại một đoạn gen đặc trưng dài $600\\text{ bp}$ từ mẫu ADN ban đầu chỉ có $10$ bản sao mạch kép tinh sạch, chạy $30$ chu kỳ nhiệt hoàn chỉnh. Sau đó sản phẩm được nạp lên giếng gel agarose $1.5\\%$ để điện di kiểm tra. Xét các nhận định sau:",
        [("Mỗi chu kỳ nhiệt của phản ứng PCR chuẩn gồm 3 bước theo thứ tự: Biến tính tách mạch ở $\\approx 94-95^\\circ\\text{C}$ $\\rightarrow$ Bắt cặp mồi đặc hiệu ở $\\approx 50-65^\\circ\\text{C}$ $\\rightarrow$ Kéo dài mạch mới ở $\\approx 72^\\circ\\text{C}$.",
          True, "Nhiệt độ tối ưu của enzyme chịu nhiệt $Taq\\text{ polymerase}$ phân lập từ suối nước nóng *Thermus aquaticus* là khoảng $72^\\circ\\text{C}$."),
         ("Sau $30$ chu kỳ PCR lý thuyết, hỗn hợp phản ứng chỉ chứa tối đa $10 \\times 30 = 300$ phân tử ADN đoạn đích.",
          False, "Số bản sao ADN tăng theo cấp số nhân $N_0 \\times 2^n$: với $n=30$ chu kỳ, số lượng đạt cỡ $10 \\times 2^{30} \\approx 1.07 \\times 10^{10}$ bản sao!"),
         ("Khi chạy điện di trong điện trường một chiều, phân tử ADN mang điện tích âm (do các nhóm photphat $PO_4^{3-}$ trên khung đường-photphat) nên sẽ di chuyển từ cực ÂM về phía cực DƯƠNG.",
          True, "Mật độ điện tích âm trên đơn vị độ dài của ADN gần như đồng nhất nên tốc độ di chuyển chỉ phụ thuộc kích thước mảnh ADN và nồng độ gel."),
         ("Nếu trong cùng một giếng có trộn cả mảnh $600\\text{ bp}$ và một mảnh nhiễu dài $2400\\text{ bp}$, mảnh $600\\text{ bp}$ xuyên qua các lỗ mạng agarose nhanh hơn nên tạo băng nằm gần cực DƯƠNG hơn so với mảnh $2400\\text{ bp}$.",
          True, "Phân tử ngắn hơn ít bị mạng lưới gel cản trở nên chạy nhanh và xa hơn về phía cực dương.")])

    # TF-028
    add("molecular", "hsg", "Enzyme Cắt giới hạn & Bản đồ Plasmid",
        "Một phân tử ADN **plasmid dạng vòng** tinh sạch dài $10\\text{ kb}$ được xử lý cắt hoàn toàn bằng các enzyme giới hạn (Restriction Enzymes) $EcoRI$ và $BamHI$, sau đó điện di xác định kích thước mảnh thu được: (1) Cắt chỉ với $EcoRI$ thu $2$ băng kích thước $3\\text{ kb}$ và $7\\text{ kb}$; (2) Cắt chỉ với $BamHI$ thu $1$ băng duy nhất kích thước $10\\text{ kb}$; (3) Cắt đồng thời cả $EcoRI$ và $BamHI$ thu $3$ băng kích thước $1\\text{ kb}$, $3\\text{ kb}$ và $6\\text{ kb}$. Xét các kết luận sau:",
        [("Plasmid vòng ban đầu sở hữu đúng $2$ vị trí cắt của $EcoRI$ và đúng $1$ vị trí cắt của $BamHI$.",
          True, "Với ADN vòng, $k$ vị trí cắt tạo đúng $k$ mảnh: $EcoRI$ cho $2$ mảnh ($2$ điểm cắt cách nhau $3$ và $7\\text{ kb}$); $BamHI$ cho $1$ mảnh thẳng $10\\text{ kb}$ ($1$ điểm cắt)."),
         ("Vị trí cắt của $BamHI$ nằm ngay trên mảnh $7\\text{ kb}$ (tạo bởi $EcoRI$), chia mảnh $7\\text{ kb}$ này thành hai đoạn $1\\text{ kb}$ và $6\\text{ kb}$ còn giữ nguyên mảnh $3\\text{ kb}$.",
          True, "Khi cắt chung cho $1, 3, 6\\text{ kb}$ (tổng vẫn $= 10\\text{ kb}$), dễ thấy $3\\text{ kb}$ giữ nguyên và $7\\text{ kb}$ bị chẻ thành $1 + 6\\text{ kb}$."),
         ("Enzyme cắt giới hạn nhận diện các trình tự ADN hoàn toàn ngẫu nhiên không có tính đối xứng hai chiều nên không bao giờ tạo được đầu dính bổ sung.",
          False, "Các enzyme giới hạn loại II nhận diện trình tự đối xứng gương (Palindrome, ví dụ EcoRI `5'-GAATTC-3'`) và thường cắt lệch tạo đầu dính (sticky ends) giúp dễ dàng nối chéo với gen lạ."),
         ("Nếu cắt một đoạn ADN **mạch thẳng** dài $10\\text{ kb}$ bằng một enzyme có $2$ vị trí nhận diện trên đoạn đó thì sẽ thu được tối đa $3$ mảnh ADN rời nhau.",
          True, "Với phân tử thẳng, $k$ vị trí cắt chia thành $k + 1 = 3$ đoạn.")])

    # TF-029
    add("molecular", "adv", "Công nghệ ADN Tái tổ hợp",
        "Để sản xuất hàng loạt hormone Insulin người quy mô công nghiệp bằng vi khuẩn *E. coli* biến đổi gen, các nhà khoa học không lấy trực tiếp đoạn ADN gen gốc từ nhân tế bào tuyến tụy để ghép vào plasmid biểu hiện, mà tách $mARN$ trưởng thành của Insulin từ tế bào $\\beta$ đảo tụy rồi phiên mã ngược tạo bản sao $cADN$ đưa vào vector plasmid mang gen chỉ thị kháng ampicillin ($amp^R$) và gen $lacZ$. Xét các nhận định sau:",
        [("Có thể dùng trực tiếp đoạn ADN nhân tế bào người chèn nguyên vẹn vào plasmid *E. coli* mà vi khuẩn vẫn tự cắt bỏ các intron chính xác để dịch mã ra đúng chuỗi Insulin người.",
          False, "Vi khuẩn *E. coli* là sinh vật nhân sơ KHÔNG có bộ máy spliceosome để cắt bỏ các đoạn intron của gen nhân thực, dẫn tới dịch mã sai hoàn toàn nếu dùng ADN gốc; do đó phải dùng $cADN$ vốn đã loại bỏ sẵn intron."),
         ("Quá trình tổng hợp $cADN$ (ADN bổ sung) từ khuôn $mARN$ trưởng thành trong ống nghiệm cần sự xúc tác của enzyme phiên mã ngược Reverse Transcriptase.",
          True, "Reverse Transcriptase phiên mã ngược $mARN$ thành mạch $cADN$ đơn, sau đó dùng ADN polymerase tổng hợp thành sợi kép chèn vào vector."),
         ("Trong thí nghiệm sàng lọc xanh-trắng trên đĩa thạch chứa Ampicillin và chất X-gal (cơ chất đổi màu xanh dương dưới tác dụng của enzyme từ gen $lacZ$), những khuẩn lạc có màu TRẮNG thường là các dòng vi khuẩn mang plasmid tái tổ hợp (chèn thành công gen mục tiêu vào giữa vùng đa điểm cắt nằm trong gen $lacZ$).",
          True, "Chèn đoạn $cADN$ làm gián đoạn bất hoạt gen $lacZ$ (tạo $\\beta$-galactosidase hỏng không chuyển X-gal thành xanh nên khuẩn lạc giữ màu trắng), trong khi gen $amp^R$ vẫn bảo toàn giúp tế bào sống trên đĩa Ampicillin."),
         ("Vì vi khuẩn phát triển thành dòng khuẩn lạc màu XANH DƯƠNG trên đĩa thạch trên là những vi khuẩn đã chết hết không mang plasmid kháng ampicillin.",
          False, "Khuẩn lạc màu XANH DƯƠNG vẫn sống trên Ampicillin tức là đã tiếp nhận plasmid khép vòng rỗng (có $amp^R$ và gen $lacZ$ còn nguyên vẹn chưa bị chèn gen lạ).")])

    # TF-030
    add("molecular", "hsg", "Công nghệ Chỉnh sửa Gen CRISPR-Cas9",
        "Hệ thống chỉnh sửa hệ gen CRISPR-Cas9 có nguồn gốc từ hệ miễn dịch thích nghi của vi khuẩn chống lại thể thực khuẩn, hiện được cải tiến gồm 2 thành phần chính đưa vào tế bào nhân thực: enzyme nuclease $Cas9$ và một phân tử ARN dẫn đường tổng hợp ($sgRNA$). Xét các nhận định sau:",
        [("Enzyme $Cas9$ có thể cắt đứt $2$ mạch ADN tại bất kỳ vị trí nào khớp bổ sung với $sgRNA$ mà không cần bất kỳ điều kiện trình tự đặc biệt nào liền kề trên bộ gen đích.",
          False, "$Cas9$ (ví dụ *SpCas9*) BẮT BUỘC phải nhận diện trình tự ngắn gọi là motif PAM (ví dụ `5'-NGG-3'`) nằm ngay sát đầu $3'$ của đoạn DNA đích để mở xoắn và cắt."),
         ("Phân tử $sgRNA$ chứa vùng trình tự khoảng $20$ nucleotit thiết kế bổ sung đặc hiệu với đoạn gen mục tiêu giúp định hướng chính xác enzyme $Cas9$ tới đúng một vị trí mong muốn trong hàng tỷ cặp bazơ.",
          True, "Khả năng lập trình lại mục tiêu dễ dàng chỉ bằng thay đoạn $20\\text{ nt}$ của $sgRNA$ giúp CRISPR vượt trội hoàn toàn so với ZFN hay TALEN."),
         ("Sau khi $Cas9$ tạo vết cắt đứt gãy mạch kép ($DSB$) tại đích, nếu tế bào sửa chữa theo con đường nối đầu không tương đồng (NHEJ) thường phát sinh lỗi thêm/mất vài nucleotit gây đột biến dịch khung làm bất hoạt (knockout) gen đó.",
          True, "NHEJ hoạt động nhanh nhưng dễ sai sót (indels), được tận dụng để tắt gen mục tiêu hiệu quả."),
         ("Nếu cung cấp đồng thời một mạch khuôn ADN sửa đổi có hai đầu tương đồng với vùng cắt, tế bào có thể dùng cơ chế sửa chữa tái tổ hợp tương đồng (HDR) để gắn chèn chính xác trình tự mới thay thế alen bệnh.",
          True, "Con đường HDR sửa sai chính xác cao (nổi trội ở pha $S/G_2$) cho phép sửa chữa đột biến điểm hoặc chèn đoạn gen định vị (knock-in).")])

    # ==================== TOPIC 3: CELLULAR (TF-031 .. TF-045) ====================
    # TF-031
    add("cellular", "adv", "Chu kỳ Tế bào & Điểm Kiểm soát",
        "Chu kỳ phân chia của một tế bào nhân thực động vật có vú được giám sát nghiêm ngặt bởi các điểm kiểm soát (Checkpoints) và phức hệ enzyme $Cyclin - Cdk$. Xét các nhận định sau:",
        [("Tại điểm kiểm soát $G_1$ (điểm giới hạn ở cuối $G_1$), nếu ADN bị đứt gãy nghiêm trọng do tia X, protein ức chế khối u $p53$ tích tụ kích hoạt gen $p21$ ức chế $Cdk$, làm tế bào tạm dừng ở $G_1$ để sửa sai ADN hoặc kích hoạt tự chết theo chương trình (Apoptosis).",
          True, "$p53$ được mệnh danh là 'người bảo vệ hệ gen', ngăn không cho tế bào mang ADN hỏng bước vào pha $S$ nhân đôi."),
         ("Phức hệ MPF (Cyclin B - Cdk1) đạt nồng độ hoạt tính đỉnh cao ở cuối pha $G_2$ để thúc đẩy tế bào bước vào pha $M$ (nguyên phân: tan màng nhân, co xoắn NST và hình thành thoi phân bào).",
          True, "Đến cuối kỳ giữa/đầu kỳ sau, phức hệ APC/C đánh dấu ubiquitin phân hủy Cyclin B khiến Cdk1 tắt hoạt tính để tế bào thoát khỏi nguyên phân."),
         ("Hầu hết các tế bào thần kinh trưởng thành trong não người duy trì ở trạng thái biệt hóa sâu không còn phân chia, được xếp vào pha nghỉ $G_0$ (tách khỏi chu kỳ tế bào ở điểm kiểm soát $G_1$).",
          True, "Tế bào vào $G_0$ vẫn chuyển hóa và truyền xung điện mạnh mẽ nhưng ngừng nhân đôi ADN và phân bào."),
         ("Điểm kiểm soát $M$ (kỳ giữa $\\rightarrow$ kỳ sau) đảm bảo nhân đôi xong mọi ty thể, còn nếu có một NST kép chưa kịp bám vào tơ vô sắc thì NST đó sẽ lập tức bị tách ngay ra đẩy bừa về hai cực.",
          False, "Điểm kiểm soát thoi vô sắc (kỳ giữa-kỳ sau) giữ chặt các crômatit bằng cách ức chế $APC/C$ nếu thậm chí chỉ MỘT tâm động chưa gắn vi ống hai cực đúng cách, ngăn ngừa lệch bội.")])

    # TF-032
    add("cellular", "basic", "Nguyên phân & Hàm lượng ADN",
        "Theo dõi $1$ tế bào lưỡng bội bình thường của ruồi giấm ($2n = 8$) có hàm lượng ADN nhân ở pha $G_1$ quy ước là $2c$ tiến hành $1$ lần nguyên phân chuẩn. Xét các nhận định sau về số NST, số crômatit và hàm lượng ADN qua các kỳ:",
        [("Ở pha $G_2$ (ngay sau khi hoàn tất nhân đôi ở pha $S$), nhân tế bào vẫn có $8$ NST nhưng mỗi NST ở trạng thái KÉP gồm $2$ crômatit chị em dính nhau ở tâm động, tổng là $16$ crômatit và hàm lượng ADN bằng $4c$.",
          True, "Nhân đôi ADN ở pha $S$ nhân đôi hàm lượng ADN ($2c \\to 4c$) và chuyển $8$ NST đơn thành $8$ NST kép."),
         ("Tại kỳ giữa nguyên phân, tất cả $8$ NST kép co xoắn cực đại và xếp thành HAI hàng song song đối xứng nhau trên mặt phẳng xích đạo của thoi phân bào.",
          False, "Trong NGUYÊN PHÂN, các NST kép xếp thành MỘT hàng trên mặt phẳng xích đạo ở kỳ giữa (xếp HAI hàng kép của từng cặp tương đồng chỉ xảy ra ở kỳ giữa GIẢM PHÂN I!)."),
         ("Tại kỳ sau nguyên phân, mỗi cặp crômatit chị em tách rời hoàn toàn ở tâm động để tiến về 2 cực: khi đó trong một tế bào đang chia có $16$ NST đơn, $0$ crômatit và tổng ADN vẫn là $4c$.",
          True, "Khi 2 crômatit tách nhau ở kỳ sau, mỗi chiếc lập tức được tính là $1$ NST đơn độc lập nên số lượng trong 1 tế bào chưa cắt tế bào chất là $4n = 16$ NST đơn."),
         ("Kết thúc nguyên phân (sau phân chia tế bào chất), mỗi trong $2$ tế bào con nhận được đúng $8$ NST đơn và hàm lượng ADN phục hồi về $2c$ y hệt tế bào mẹ ban đầu.",
          True, "Nguyên phân bảo toàn nguyên vẹn bộ NST $2n$ qua các thế hệ tế bào sinh dưỡng.")])

    # TF-033
    add("cellular", "adv", "Giảm phân & Trao đổi chéo",
        "Xét $1$ tế bào sinh dục chín có bộ NST $2n = 14$ (với $7$ cặp tương đồng) tiến hành giảm phân bình thường tạo giao tử. Hàm lượng ADN nhân ở pha $G_1$ trước giảm phân là $2c$. Xét các nhận định sau:",
        [("Ở kỳ đầu của giảm phân I, các cặp NST kép tương đồng tiếp hợp theo từng cặp tạo bộ bốn crômatit (tetrad) và có thể trao đổi chéo những đoạn tương ứng giữa các crômatit KHÔNG chị em.",
          True, "Trao đổi chéo tại các điểm bắt chéo (chiasmata) tạo biến dị tổ hợp hoán vị gen và giữ cặp tương đồng dính nhau để định hướng chính xác."),
         ("Khi kết thúc lần phân bào giảm phân I (tạo $2$ tế bào con ở kỳ cuối I), mỗi tế bào con chứa $n = 7$ NST KÉP ($14$ crômatit) và mang hàm lượng ADN bằng $2c$.",
          True, "Giảm phân I làm giảm một nửa số NST ($2n$ kép $\\to n$ kép), nên hàm lượng ADN từ $4c$ về $2c$."),
         ("Tại kỳ sau giảm phân I, xảy ra hiện tượng tách dọc tâm động của mỗi NST kép khiến các crômatit chị em chia làm hai nửa đi về hai cực tế bào.",
          False, "Ở kỳ sau I, các tâm động KHÔNG tách; hai NST kép trong cặp tương đồng trượt tách nhau đi về 2 cực. Chỉ đến kỳ sau II tâm động mới tách đôi!"),
         ("Kết thúc toàn bộ quá trình giảm phân II, từ $1$ tế bào sinh tinh ban đầu thu được $4$ tế bào con đơn bội, mỗi tế bào có $n = 7$ NST đơn và hàm lượng ADN bằng $0.5c$.",
          False, "Mỗi tế bào con giảm phân II nhận $n = 7$ NST đơn và hàm lượng ADN bằng $1c$ (một nửa so với mức $2c$ của tế bào $G_1$ ban đầu, không phải $0.5c$).")])

    # TF-034
    add("cellular", "adv", "Số loại Giao tử & Quá trình Tạo Trứng - Tinh trùng",
        "Xét một cá thể động vật đực và một cá thể cái cùng loài có kiểu gen $Aa Bb Dd \\frac{EG}{eg}$ ($3$ cặp đầu phân ly độc lập, cặp NST thứ $4$ mang $2$ gen liên kết $E/e$ và $G/g$; bộ NST chung $2n = 8$). Xét các nhận định định lượng sau:",
        [("Khi xét trên phạm vi TOÀN CƠ THỂ cá thể đực, nếu giảm phân bình thường và chỉ xảy ra trao đổi chéo giữa $E$ và $G$ ở một tỷ lệ tế bào sinh tinh, số loại tinh trùng TỐI ĐA có thể tạo thành là $2^3 \\times 2 = 16$ loại.",
          False, "Mỗi cặp $Aa, Bb, Dd$ độc lập cho $2$ loại $\\Rightarrow 2^3 = 8$; cặp $EG/eg$ có hoán vị cho $4$ loại giao tử (`EG, eg, Eg, eG`), do đó tổng số loại $= 8 \\times 4 = 32$ loại giao tử tối đa!"),
         ("Nếu chỉ xét **MỘT tế bào sinh tinh** duy nhất có kiểu gen trên giảm phân có hoán vị gen tại cặp $EG/eg$, số loại tinh trùng thực tế thu được từ $1$ tế bào đó chỉ tối đa là $4$ loại (với tỉ lệ $1:1:1:1$).",
          True, "$1$ tế bào sinh tinh chỉ tạo $4$ tinh trùng sau giảm phân II; nếu có hoán vị ở 1 cặp và các cặp kia phân ly độc lập theo một cách cố định, 4 sản phẩm tối đa mang $4$ tổ hợp giao tử."),
         ("Từ **MỘT tế bào sinh trứng** duy nhất của cá thể cái có kiểu gen trên giảm phân bình thường tạo giao tử, dù có hoán vị gen xảy ra ở bao nhiêu điểm đi nữa, kết quả vẫn chỉ thu được DUY NHẤT $1$ loại tế bào trứng (kèm $3$ thể cực thoái biến).",
          True, "Phân bào chất không đều trong giảm phân tạo noãn dồn toàn bộ bào tương về $1$ tế bào trứng duy nhất $\\Rightarrow 1$ kiểu gen trứng duy nhất từ $1$ tế bào sinh trứng."),
         ("Giả sử $500$ tế bào sinh tinh của cá thể đực tiến hành giảm phân hoàn chỉnh thì thu được tất cả $2000$ tinh trùng có khả năng tham gia thụ tinh; còn $500$ tế bào sinh trứng giảm phân chỉ thu được $500$ tế bào trứng.",
          True, "Tỷ lệ hiệu suất $1$ tế bào sinh dục chín $\\rightarrow 4$ tinh trùng vs $1$ trứng.")])

    # TF-035
    add("cellular", "hsg", "Rối loạn Phân ly NST (GP I vs GP II)",
        "Ở người, bệnh mù màu đỏ-lục do gen lặn $m$ trên vùng không tương đồng của NST X quy định (mắt nhìn màu bình thường do alen trội $M$). Một cặp vợ chồng có mắt nhìn màu BÌNH THƯỜNG (chồng $X^M Y$, vợ mang kiểu gen dị hợp $X^M X^m$) sinh ra một người con trai bị **hội chứng Klinefelter ($XXY$) VÀ mắc bệnh mù màu**. Biết không có đột biến gen phát sinh mới và không có hoán vị vùng chứa gen. Xét các suy luận về cơ chế gây rối loạn sau:",
        [("Người con trai mắc đồng thời Klinefelter và mù màu bắt buộc phải mang kiểu gen là $X^m X^m Y$.",
          True, "Là con trai Klinefelter có $2$ NST X và $1$ Y; để biểu hiện tính trạng lặn mù màu thì cả $2$ NST X đều phải mang alen lặn $X^m$ (vì bố $X^M Y$ không có $X^m$)."),
         ("Cặp NST $X^m X^m$ trong hợp tử chắc chắn có nguồn gốc từ trứng bất thường ($n+1$) của người MẸ do rối loạn không phân ly ở lần phân bào **giảm phân II** (tại cặp crômatit $X^m X^m$).",
          True, "Mẹ $X^M X^m$ chỉ tạo được trứng mang hai bản sao giống hệt $X^m X^m$ khi xảy ra không phân ly $2$ crômatit chị em ở GP II (còn nếu hỏng ở GP I, trứng $n+1$ sẽ là $X^M X^m$, kết hợp với $Y$ tạo $X^M X^m Y$ nhìn màu bình thường!)."),
         ("Nếu người mẹ bị rối loạn không phân ly ở **giảm phân I** (còn bố hoàn toàn bình thường), giao tử trứng chứa $2$ NST X đó kết hợp tinh trùng $Y$ có thể sinh ra con trai Klinefelter $X^m X^m Y$ mù màu.",
          False, "Hỏng GP I ở mẹ $X^M X^m$ tạo trứng mang $X^M X^m$ nên con $X^M X^m Y$ sẽ KHÔNG bị mù màu nhờ có $X^M$ trội."),
         ("Sự không phân ly cặp NST giới tính trong giảm phân II ở người BỐ ($X^M Y$) có thể tạo ra tinh trùng chứa hai chiếc $Y$ ($YY$), khi thụ tinh với trứng bình thường tạo hợp tử $XYY$ (hội chứng Jacobs).",
          True, "Chỉ có rối loạn GP II ở bố (không tách 2 crômatit Y) mới tạo được giao tử $YY$ (và $XX$ hoặc $O$).")])

    # TF-036
    add("cellular", "adv", "Đột biến Cấu trúc: Mất đoạn & Lặp đoạn",
        "Nghiên cứu hai dạng đột biến cấu trúc nhiễm sắc thể làm thay đổi số lượng gen trên mỗi NST là Mất đoạn và Lặp đoạn. Xét các nhận định sau:",
        [("Cơ chế phổ biến hàng đầu làm phát sinh ĐỒNG THỜI một NST bị lặp đoạn và một NST bị mất đoạn trong giảm phân là sự tiếp hợp lệch và trao đổi chéo KHÔNG CÂN giữa $2$ crômatit khác nguồn gốc trong cặp tương đồng.",
          True, "Khi trượt lệch các trình tự lặp tương đồng trên 2 crômatit rồi trao đổi chéo, một chiếc nhận thêm đoạn thành lặp đoạn còn chiếc kia mất đoạn tương ứng."),
         ("Ở người, đột biến mất một đoạn nhỏ trên vai ngắn của NST số $5$ ($5p-$) gây hội chứng tiếng mèo kêu (Cri-du-chat) với chậm phát triển trí tuệ nghiêm trọng.",
          True, "Đột biến mất đoạn làm mất các gen thiết yếu ở trạng thái đơn bội dẫn đến rối loạn phát triển nặng hoặc gây chết."),
         ("Đột biến lặp đoạn gen *Bar* trên NST X ở ruồi giấm làm tăng số lượng mặt đơn giúp mắt ruồi to gấp đôi mắt ruồi kiểu dại bình thường.",
          False, "Lặp đoạn $16A$ (gen *Bar*) ở ruồi giấm làm mắt DẸT NHỎ đi (giảm số mặt đơn); lặp càng nhiều mắt càng dẹt nhỏ."),
         ("Trong tiến hóa hệ gen lâu dài, lặp đoạn gen có ý nghĩa đặc biệt vì bản sao gen dư thừa có thể tích lũy đột biến phân hóa tạo thành gen mới mang chức năng mới mà bản sao gốc vẫn đảm nhiệm chức năng thiết yếu cũ.",
          True, "Lặp đoạn là động lực chủ yếu hình thành các họ đa gen (như họ gen globin $\\alpha, \\beta$ ở người).")])

    # TF-037
    add("cellular", "adv", "Đột biến Cấu trúc: Đảo đoạn & Chuyển đoạn",
        "Phân tích các dạng đột biến cấu trúc NST giữ nguyên hoặc thay đổi vị trí phân bố gen là Đảo đoạn và Chuyển đoạn NST:",
        [("Đột biến đảo đoạn làm xoay ngược $180^\\circ$ một đoạn NST thường không làm tăng hay giảm số lượng vật chất di truyền trên NST nhưng có thể làm thay đổi mức độ hoạt động của gen gần điểm đứt gãy (hiệu ứng vị trí).",
          True, "Đặt gen gần vùng dị nhiễm sắc hoặc tách khỏi enhancer cũ làm thay đổi biểu hiện gen; đồng thời giúp tạo biến dị hình thái khi lai."),
         ("Cá thể mang đột biến đảo đoạn dị hợp tử thường tạo được tỉ lệ lớn giao tử mất đoạn/lặp đoạn không sống sót nếu xảy ra trao đổi chéo bên trong vòng đảo khi giảm phân, góp phần cách ly sinh sản hình thành loài mới.",
          True, "Trao đổi chéo trong vòng đảo làm giảm khả năng sinh sản của con lai dị hợp đảo đoạn giữa các quần thể (cách ly sau hợp tử)."),
         ("Đột biến chuyển đoạn tương hỗ giữa NST số $9$ và NST số $22$ ở người hình thành nhiễm sắc thể Philadelphia gây bệnh bạch cầu tủy mạn (CML) là do thiếu vitamin C bẩm sinh trong khẩu phần ăn.",
          False, "NST Philadelphia $t(9;22)$ là đột biến chuyển đoạn tương hỗ tạo gen dung hợp *BCR-ABL* sinh enzyme tyrosine kinase hoạt động quá mức thúc đẩy tế bào tủy tăng sinh ác tính, không phải do thiếu vitamin C."),
         ("Một người mang chuyển đoạn hòa hợp tâm (Robertsonian) cân bằng giữa NST $14$ và $21$ tuy chỉ có $45$ NST trong tế bào xôma nhưng vẫn khỏe mạnh bình thường vì hầu như không mất gen thiết yếu, song lại có nguy cơ cao sinh con mắc hội chứng Down.",
          True, "Người mang $t(14;21)$ có thể truyền đồng thời NST hợp nhất $14/21$ cùng NST $21$ bình thường sang con tạo kiểu nhân $46$ NST với $3$ bản sao vùng gen $21q$ (Down do chuyển đoạn).")])

    # TF-038
    add("cellular", "basic", "Đột biến Số lượng NST - Lệch bội ở Người",
        "Nghiên cứu các hội chứng lệch bội thường gặp ở người (như Down, Turner, Klinefelter, Siêu nữ XXX). Xét các nhận định sau:",
        [("Hội chứng Down ($2n+1 = 47$ NST với $3$ NST số $21$) có tần suất xuất hiện tăng nhanh theo độ tuổi sinh con của người mẹ (đặc biệt trên $35$ tuổi) do noãn bào cấp I bị dừng kéo dài ở kỳ đầu I làm tăng nguy cơ rối loạn phân ly NST.",
          True, "Tế bào trứng người dừng ở kỳ đầu I từ giai đoạn phôi thai tới tận lúc rụng trứng hàng chục năm sau dễ hỏng phức hệ gắn kết crômatit (cohesin)."),
         ("Bệnh nhân mắc hội chứng Turner có kiểu nhân $45, XO$ là nữ giới thường có vóc dáng thấp, cổ bạnh, vô sinh và khi nhuộm nhân tế bào niêm mạc miệng hoàn toàn KHÔNG phát hiện thể Barr.",
          True, "Số thể Barr luôn bằng $\\text{số NST X} - 1$. Với $XO$, có $1 - 1 = 0$ thể Barr."),
         ("Trong tế bào xôma của người nam mắc hội chứng Klinefelter ($47, XXY$), khi xét nghiệm tiêu bản tế bào niêm mạc miệng cũng KHÔNG thấy xuất hiện thể Barr vì giới tính là nam có NST Y.",
          False, "Bệnh nhân $XXY$ mang $2$ NST X nên vẫn bất hoạt $1$ NST X tạo thành $1$ thể Barr giống nữ $XX$ bình thường!"),
         ("Ở người, các đột biến thể một ($2n-1$) trên nhiễm sắc thể thường hầu như đều bị đào thải gây sẩy thai sớm từ giai đoạn phôi, trong khi thể một trên NST giới tính X ($XO$) lại có thể sống sót tới tuổi trưởng thành.",
          True, "Cơ chế bất hoạt X (tế bào bình thường chỉ dùng liều $1$ NST X hoạt động) giải thích vì sao thiếu $1$ chiếc X ít gây chết phôi hơn thiếu $1$ NST thường.")])

    # TF-039
    add("cellular", "hsg", "Tính Xác suất Hợp tử Lệch bội",
        "Ở một loài động vật ($2n$), người bố bình thường có $20\\%$ tế bào sinh tinh bị rối loạn không phân ly cặp NST giới tính $XY$ ở giảm phân I (giảm phân II bình thường), các tế bào còn lại giảm phân bình thường. Người mẹ hoàn toàn bình thường giảm phân cho $100\\%$ trứng bình thường ($n$). Các giao tử đều có khả năng thụ tinh như nhau. Xét các xác suất hợp tử $F_1$ thu được:",
        [("Tỉ lệ loại tinh trùng bất thường mang cả hai NST giới tính ($XY$) do người bố tạo ra bằng $20\\%$ tổng số tinh trùng.",
          False, "$20\\%$ tế bào sinh tinh hỏng GP I tạo $50\\%$ tinh trùng $XY$ và $50\\%$ tinh trùng khuyết $O$ $\\Rightarrow$ tỷ lệ tinh trùng $XY = 20\\% \\times 0.5 = 10\\%$ (còn $O = 10\\%$, $X = 40\\%$, $Y = 40\\%$)."),
         ("Tỉ lệ tinh trùng bình thường mang $1$ NST $X$ trong tổng số tinh trùng của người bố chiếm đúng $40\\%$.",
          True, "$80\\%$ tế bào sinh tinh giảm phân bình thường tạo $40\\%$ tinh trùng $X$ và $40\\%$ tinh trùng $Y$."),
         ("Xác suất cặp bố mẹ này sinh được một hợp tử mang kiểu gen $XXY$ là $10\\%$, xác suất sinh hợp tử $XO$ cũng bằng $10\\%$.",
          True, "Vì $100\\%$ trứng mang $X$, kết hợp $10\\% XY \\to 10\\% XXY$ và kết hợp $10\\% O \\to 10\\% XO$."),
         ("Tỉ lệ hợp tử bình thường ($XX$ hoặc $XY$) ở đời con $F_1$ chỉ bằng $60\\%$ tổng số hợp tử.",
          False, "Tổng tinh trùng bình thường ($X + Y$) $= 40\\% + 40\\% = 80\\% \\Rightarrow$ xác suất sinh hợp tử bình thường bằng $80\\%$ (gồm $40\\% XX$ và $40\\% XY$).")])

    # TF-040
    add("cellular", "basic", "Đột biến Tự đa bội & Ứng dụng",
        "Trong chọn tạo giống cây trồng, hóa chất Cônsixin (Colchicine) được sử dụng phổ biến để gây đột biến tạo các dòng cây tự đa bội mang nhiều đặc tính nông học quý giá. Xét các nhận định sau:",
        [("Cơ chế tác động chính của Cônsixin là trực tiếp cắt đứt các gen quy định chiều cao thấp để nối thêm gen tăng năng suất vào ADN.",
          False, "Cônsixin gắn vào tiểu phần tubulin ức chế sự trùng hợp vi ống hình thành thoi phân bào, khiến bộ NST đã nhân đôi không thể phân ly về 2 cực $\\rightarrow$ tăng gấp bội số NST trong 1 nhân ($2n \\to 4n$)."),
         ("Khi lai cây dưa hấu tứ bội ($4n$) làm mẹ với cây dưa hấu lưỡng bội ($2n$) làm bố thu được cây dưa hấu tam bội ($3n$) phát triển thân lá lớn và tạo quả không hạt.",
          True, "Tế bào tam bội ($3n$) có 3 chiếc mỗi cặp NST không thể chia đều đồng bộ trong giảm phân I, sinh giao tử lệch bội hỏng hầu hết $\\rightarrow$ không hạt."),
         ("Thể tự đa bội thường gặp và có giá trị thực tế rất cao ở thực vật (rau ăn lá, củ, cây ăn quả) vì có kích thước cơ quan sinh dưỡng to lớn, tế bào rộng, tổng hợp chất hữu cơ mạnh mẽ.",
          True, "Tăng số bản sao hệ gen (nhân đa bội) tương ứng với tăng kích thước tế bào và năng suất sinh khối ở nhiều loài thực vật."),
         ("Để nhân giống nhanh và duy trì nguyên vẹn đặc điểm tốt của một cây chuối hay cây nho tam bội ($3n$) không hạt, người trồng trọt sử dụng các phương pháp sinh sản vô tính như nuôi cấy mô hoặc giâm/tách chồi.",
          True, "Do $3n$ bất thụ hữu tính, sinh sản sinh dưỡng giúp nhân rộng vô hạn bản sao di truyền $3n$ ưu việt.")])

    # TF-041
    add("cellular", "adv", "Thể Dị đa bội & Thí nghiệm Karpechenko",
        "Nhà di truyền học Liên Xô G.D. Karpechenko (1927) đã tiến hành lai xa giữa cây Củ cải (*Raphanus sativus*, $2n = 18R$) với cây Bắp cải (*Brassica oleracea*, $2n = 18B$). Cây lai $F_1$ thu được có $18$ NST ($9R + 9B$) sinh trưởng khỏe nhưng bị bất thụ hoàn toàn. Tuy nhiên, một số cây $F_1$ tự phát đa bội hóa bộ NST đã tạo thành loài thực vật mới hữu thụ đặt tên là *Raphanobrassica*. Xét các nhận định sau:",
        [("Nguyên nhân trực tiếp khiến cây lai $F_1$ ($9R + 9B$) bị bất thụ là do $9$ NST của củ cải không có $9$ NST tương đồng từ bắp cải để bắt cặp tiếp hợp bình thường ở kỳ đầu giảm phân I.",
          True, "Hai bộ NST khác loài không tương đồng khiến quá trình phân ly trong giảm phân rối loạn hoàn toàn, không tạo được giao tử sống."),
         ("Cây song nhị bội *Raphanobrassica* hữu thụ mang tổng cộng $36$ NST lưỡng bội của cả hai loài ($18R + 18B$), khi giảm phân bình thường sẽ tạo ra mỗi giao tử chứa đúng $9R + 9B = 18$ NST.",
          True, "Mỗi NST đều có bạn cặp tương đồng chính mình để tiếp hợp và phân ly chuẩn tạo giao tử lưỡng bội ghép $(n_R + n_B) = 18$."),
         ("Ở cây *Raphanobrassica* ($18R + 18B$), do số NST tổng cộng bằng $36$ nên bộ NST được xếp vào dạng tự tứ bội ($4n = 36$) thuộc cùng một loài củ cải ban đầu.",
          False, "*Raphanobrassica* là thể SONG NHỊ BỘI (dị đa bội $2n_1 + 2n_2$), mang hai bộ lưỡng bội của hai loài khác nhau, đã cách ly sinh sản với cả củ cải ($2n=18$) và bắp cải ($2n=18$) thành một loài mới."),
         ("Phương pháp lai xa kết hợp đa bội hóa (tạo thể song nhị bội) có vai trò cực kỳ quan trọng trong tiến hóa lịch sử của thực vật hạt kín (như nguồn gốc lúa mì hiện đại $6n = 42$).",
          True, "Đa số loài thực vật có hoa ngày nay (như lúa mì *Triticum aestivum*, bông vải, cải dầu) có lịch sử hình thành qua dị đa bội hóa.")])

    # TF-042
    add("cellular", "hsg", "Phép lai Thể Tứ bội ($4n$)",
        "Ở một loài thực vật tứ bội ($4n$), alen $A$ quy định thân cao trội hoàn toàn so với alen $a$ quy định thân thấp. Giả sử các cây tứ bội giảm phân bình thường chỉ tạo giao tử lưỡng bội ($2n$) hữu thụ hoàn toàn. Thực hiện phép lai $P: AAaa \\times Aaaa$. Mỗi nhận định sau Đúng hay Sai?",
        [("Cây có kiểu gen $AAaa$ khi giảm phân cho tỉ lệ các loại giao tử lưỡng bội là $\\frac{1}{6} AA : \\frac{4}{6} Aa : \\frac{1}{6} aa$.",
          True, "Áp dụng cách viết 6 cạnh của hình tứ diện/chữ nhật với 4 alen ($A, A, a, a$): $\\binom{4}{2} = 6$ cặp tạo $1 AA : 4 Aa : 1 aa$."),
         ("Cây có kiểu gen $Aaaa$ khi giảm phân chỉ tạo ra $2$ loại giao tử với tỉ lệ bằng nhau là $\\frac{1}{2} Aa : \\frac{1}{2} aa$.",
          True, "Cây có $1 A$ và $3 a$ ghép $2$ tạo $3 Aa : 3 aa = \\frac{1}{2} Aa : \\frac{1}{2} aa$."),
         ("Ở đời con $F_1$ của phép lai $AAaa \\times Aaaa$, tỉ lệ cây thân thấp ($aaaa$) thu được bằng $\\frac{1}{24}$.",
          False, "Tỉ lệ cây thân thấp $aaaa = \\frac{1}{6}(aa) \\times \\frac{1}{2}(aa) = \\frac{1}{12}$, suy ra tỉ lệ thân cao là $\\frac{11}{12}$."),
         ("Nếu cho các cây $F_1$ thân cao ở trên ($\\frac{1}{11} AAAa + \\frac{5}{11} AAaa + \\frac{5}{11} Aaaa$) lại tự tạo giao tử, tất cả các cây $F_1$ thân cao đều có thể tự thụ sinh ra toàn $100\\%$ thân cao ở $F_2$.",
          False, "Chỉ cây $AAAa$ ($F_1$) tạo toàn giao tử mang $A$ ($\\frac{1}{2}AA:\\frac{1}{2}Aa$) mới sinh $100\\%$ thân cao; các cây $AAaa$ và $Aaaa$ đều tạo được giao tử $aa$ nên khi tự thụ đều tạo thêm cây thân thấp $aaaa$.")])

    # TF-043
    add("cellular", "basic", "Cấu trúc Siêu hiển vi Nhiễm sắc thể",
        "Ở tế bào nhân thực, phân tử ADN rất dài (tổng chiều dài $\\approx 2\\text{ m}$ trong nhân người đường kính chỉ vài micromet) được đóng gói gọn gàng qua các bậc cấu trúc siêu hiển vi của nhiễm sắc thể. Xét các nhận định sau:",
        [("Đơn vị cấu trúc cơ bản đầu tiên của nhiễm sắc thể là Nucleosome, gồm một lõi $8$ phân tử protein Histon ($2$ bản sao mỗi loại $H2A, H2B, H3, H4$) được $1$ đoạn ADN dài khoảng $146-147$ cặp nucleotit quấn quanh $1.75$ vòng.",
          True, "Cấu trúc chuỗi hạt nucleosome làm đường kính sợi cơ bản đạt khoảng $10 - 11\\text{ nm}$."),
         ("Protein Histon giàu các axit amin mang điện tích ÂM như Glutamate và Aspartate nên đẩy mạnh phân tử ADN để tạo vùng giãn xoắn.",
          False, "Protein Histon rất giàu axit amin kiềm mang điện tích DƯƠNG (Lysine, Arginine) giúp liên kết tĩnh điện chặt chẽ với khung đường-photphat mang điện tích ÂM của phân tử ADN."),
         ("Sợi cơ bản ($11\\text{ nm}$) tiếp tục cuộn xoắn với sự tham gia của histon $H1$ thành sợi nhiễm sắc đường kính $30\\text{ nm}$, rồi vùng xếp cuộn $300\\text{ nm}$ và sợi crômatit $700\\text{ nm}$.",
          True, "Quá trình xoắn nhiều cấp giúp thu gọn chiều dài ADN tới hơn $10\\,000$ lần ở NST kỳ giữa."),
         ("Ở kỳ giữa của nguyên phân, NST co xoắn cực đại giúp quan sát rõ nhất hình thái, số lượng và kích thước đặc trưng cho loài (như lập bộ nhiễm sắc thể đồ - Karyotype).",
          True, "Co xoắn cực đại ở kỳ giữa vừa giúp phân ly không đứt rối NST về 2 cực vừa thuận lợi cho xét nghiệm di truyền tế bào.")])

    # TF-044
    add("cellular", "hsg", "Sinh học Ung thư & Gen Kiểm soát Chu kỳ",
        "Sự phát sinh ung thư là quá trình tích lũy nhiều đột biến liên tiếp tại hai nhóm gen chủ chốt kiểm soát chu kỳ tế bào: Tiền gen ung thư (Proto-oncogenes, như *Ras*, *Myc*) và Gen ức chế khối u (Tumor suppressor genes, như *Rb*, *p53*). Xét các nhận định sau:",
        [("Đột biến biến đổi một Tiền gen ung thư bình thường thành Gen ung thư hoạt động quá mức (Oncogene) thường có tính chất như một đột biến TRỘI ở cấp độ tế bào (chỉ cần $1$ trong $2$ alen bị đột biến tăng chức năng đã thúc đẩy tăng sinh).",
          True, "Ví dụ một bản sao *Ras* đột biến khóa ở trạng thái gắn GTP liên tục phát tín hiệu phân bào bất chấp không có yếu tố tăng trưởng."),
         ("Với gen ức chế khối u (như gen $Rb$ trong bệnh u nguyên bào võng mạc), ở người bình thường chỉ cần $1$ alen lành còn lại vẫn đủ tạo protein kìm hãm tăng sinh; theo giả thuyết 'hai cú đánh' của Knudson, tế bào thường chỉ mất kiểm soát khi CẢ HAI alen của gen ức chế khối u bị bất hoạt.",
          True, "Đây là lý do người thừa hưởng sẵn $1$ alen đột biến $Rb$ từ bố mẹ có nguy cơ ung thư võng mạc sớm rất cao (chỉ cần thêm $1$ đột biến xôma trên alen thứ hai)."),
         ("Tế bào ung thư chỉ cần tích lũy duy nhất $1$ đột biến tăng hoạt tính trên gen $p53$ là lập tức mọc thành khối u di căn xa toàn thân.",
          False, "Hình thành ung thư ác tính thường đòi hỏi nhiều bước tích lũy đột biến qua thời gian (kết hợp bật oncogene, mất gen ức chế khối u, bật telomerase và tăng sinh mạch máu di căn); bản thân *tăng* $p53$ lại chống ung thư, phải là *mất* chức năng $p53$."),
         ("Thuốc Imatinib (Gleevec) nhắm trúng đích ức chế đặc hiệu hoạt tính kinase của protein đột biến *BCR-ABL* mà không phá hủy hàng loạt tế bào lành như hóa trị kinh điển.",
          True, "Liệu pháp nhắm trúng đích (Targeted therapy) gắn vào khe bám ATP của tyrosine kinase đột biến mang lại hiệu quả điều trị vượt trội trong CML.")])

    # TF-045
    add("cellular", "hsg", "Phân tích Thực nghiệm Chu kỳ Tế bào",
        "Nuôi cấy đồng loạt một quần thể tế bào động vật có tổng thời gian một chu kỳ tế bào đúng bằng $24\\text{ giờ}$. Khi đếm ngẫu nhiên $1000$ tế bào trên tiêu bản cố định (tất cả đang phân chia tích cực, không đồng pha) thu được: $450$ tế bào đang ở pha $G_1$; $350$ tế bào ở pha $S$; $150$ tế bào ở pha $G_2$; và $50$ tế bào đang ở các kỳ của nguyên phân $M$ (trong đó có $15$ tế bào ở kỳ giữa). Xét các phân tích sau:",
        [("Tổng thời gian của kỳ trung gian ($G_1 + S + G_2$) trong mỗi chu kỳ tế bào chiếm thời lượng gấp đôi so với pha nguyên phân ($M$).",
          False, "Kỳ trung gian có $450 + 350 + 150 = 950$ tế bào ($95\\% = 22.8\\text{ giờ}$), còn pha $M$ có $50$ tế bào ($5\\% = 1.2\\text{ giờ}$), tức kỳ trung gian dài gấp $19$ lần pha $M$ chứ không phải gấp đôi."),
         ("Khoảng thời gian trung bình dành cho giai đoạn nhân đôi ADN (pha $S$) của tế bào này ước tính bằng $8.4\\text{ giờ}$.",
          True, "Thời gian pha tỷ lệ với phần trăm số tế bào đang ở pha đó: $t_S = \\frac{350}{1000} \\times 24 = 8.4\\text{ giờ}$."),
         ("Nếu bổ sung chất đánh dấu phóng xạ $^3H$-Thymidine trong một xung ngắn $15$ phút vào môi trường nuôi cấy, ngay lúc vừa kết thúc xung $15$ phút chỉ các tế bào đang nằm trong pha $S$ mới mang dấu phóng xạ trong nhân.",
          True, "Thymidine là đơn phân đặc thù của ADN (khác Uracil của ARN) nên chỉ gắn vào ADN khi tế bào đang sao chép ở pha $S$."),
         ("Từ dữ kiện tiêu bản, chỉ số phân bào (Mitotic index) của quần thể tế bào đang xét là $5.0\\%$ và thời gian kỳ giữa ước tính vào khoảng $21.6\\text{ phút}$.",
          True, "Chỉ số phân bào $= \\frac{50}{1000} = 5.0\\%$. Thời gian kỳ giữa $= \\frac{15}{1000} \\times 24\\text{ giờ} = 0.36\\text{ giờ} = 21.6\\text{ phút}$.")])

    return items, idx
