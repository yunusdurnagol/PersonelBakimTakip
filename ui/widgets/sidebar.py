"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : ui/widgets/sidebar.py
Açıklama   : Modern Sol Menü
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
)


class Sidebar(QFrame):

    def __init__(self):

        super().__init__()

        self.setObjectName("Sidebar")

        self.setFixedWidth(270)

        self.setStyleSheet("""
#Sidebar{
    background:#FFFFFA;
    border-right:1px solid #E5E7EB;
}

QLabel{
    color:#1F2937;
    font-size:11pt;
    font-weight:600;
}

QTreeWidget{
    background:transparent;
    color:#334155;
    border:none;
    outline:none;
    font-size:11pt;
}

QTreeWidget::item{
    height:40px;
    padding-left:12px;
    border-radius:8px;
    margin:2px 6px;
}

QTreeWidget::item:hover{
    background:#EEF4FF;
    color:#2563EB;
}

QTreeWidget::item:selected{
    background:#2563EB;
    color:white;
    font-weight:600;
}

QTreeWidget::branch{
    background:transparent;
}

QScrollBar:vertical{
    width:8px;
    background:transparent;
}

QScrollBar::handle:vertical{
    background:#CBD5E1;
    border-radius:4px;
}

QScrollBar::handle:vertical:hover{
    background:#94A3B8;
}

QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical{
    height:0px;
}

QScrollBar::add-page:vertical,
QScrollBar::sub-page:vertical{
    background:transparent;
}
""")

        layout = QVBoxLayout(self)

        layout.setContentsMargins(15, 15, 15, 15)

        ################################################

        logo = QLabel("⚙")

        logo.setAlignment(Qt.AlignCenter)

        logo.setStyleSheet("""
            font-size:40px;
        """)

        title = QLabel(
            "Personel ve\nBakım Yönetim Sistemi"
        )

        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet("""
            font-size:13pt;
            font-weight:bold;
            padding-bottom:20px;
        """)

        layout.addWidget(logo)

        layout.addWidget(title)

        ################################################

        self.tree = QTreeWidget()

        self.tree.setHeaderHidden(True)

        layout.addWidget(self.tree)

        ################################################

        footer = QLabel("v1.0.0")

        footer.setAlignment(Qt.AlignCenter)

        footer.setStyleSheet("""
            color:#9CA3AF;
            padding-top:10px;
        """)

        layout.addWidget(footer)

        self.create_menu()

    ####################################################

    def create_menu(self):

        dashboard = QTreeWidgetItem(
            ["🏠 Dashboard"]
        )

        personel = QTreeWidgetItem(
            ["👨 Personeller"]
        )

        personel.addChild(
            QTreeWidgetItem(
                ["📋 Personel Listesi"]
            )
        )

        personel.addChild(
            QTreeWidgetItem(
                ["➕ Yeni Personel"]
            )
        )

        personel.addChild(
            QTreeWidgetItem(
                ["📅 İzinler"]
            )
        )

        personel.addChild(
            QTreeWidgetItem(
                ["📄 Evraklar"]
            )
        )

        makine = QTreeWidgetItem(
            ["🏭 Makineler"]
        )

        makine.addChild(
            QTreeWidgetItem(
                ["🏭 Makineler"]
            )
        )

        makine.addChild(
            QTreeWidgetItem(
                ["⚙ Bölümler"]
            )
        )

        parca = QTreeWidgetItem(
            ["📦 Parçalar"]
        )

        parca.addChild(
            QTreeWidgetItem(
                ["📦 Parçalar"]
            )
        )

        parca.addChild(
            QTreeWidgetItem(
                ["🔄 Hareketler"]
            )
        )

        parca.addChild(
            QTreeWidgetItem(
                ["🗂 Kategoriler"]
            )
        )

        parca.addChild(
            QTreeWidgetItem(
                ["🏷 Markalar"]
            )
        )

        tedarikci = QTreeWidgetItem(
            ["🚚 Tedarikçiler"]
        )

        ayarlar = QTreeWidgetItem(
            ["⚙ Ayarlar"]
        )

        self.tree.addTopLevelItem(dashboard)
        self.tree.addTopLevelItem(personel)
        self.tree.addTopLevelItem(makine)
        self.tree.addTopLevelItem(parca)
        self.tree.addTopLevelItem(tedarikci)
        self.tree.addTopLevelItem(ayarlar)

        personel.setExpanded(True)
        makine.setExpanded(True)
        parca.setExpanded(True)

        self.tree.setCurrentItem(dashboard)