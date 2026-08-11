"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : ui/widgets/sidebar.py
Açıklama   : Modern ERP Sidebar
Yazar      : Yunus Durnagöl
Sürüm      : 2.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from PySide6.QtCore import (
    Qt,
    QPropertyAnimation,
    QEasingCurve,
)

from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QTreeWidget,
    QVBoxLayout,
)
from PySide6.QtWidgets import QTreeWidgetItem

class Sidebar(QFrame):
    """
    Modern ERP Sidebar

    Özellikler

    - Açılır / Kapanır
    - Animasyonlu
    - Sadece ikon modu
    - Responsive
    """

    def __init__(self):

        super().__init__()

        ####################################################
        # WIDTH
        ####################################################

        self.expanded = True
         
        self.expanded_width = 240

        self.collapsed_width = 70

        self.animation = None

        ####################################################
        # STYLE
        ####################################################

        self.setObjectName("Sidebar")

        self.setMinimumWidth(
    self.collapsed_width
)

        self.setMaximumWidth(
            self.expanded_width
        )

        self.setStyleSheet(
            """
            QFrame#Sidebar{

                background:#FFFFFA;

                border-right:1px solid #E5E7EB;

            }

            QLabel{

                color:#1F2937;

            }

            QLabel#Logo{

                font-size:40px;

            }

            QLabel#Title{

                font-size:13pt;

                font-weight:bold;

            }

            QLabel#Footer{

                color:#9CA3AF;

                font-size:10pt;

            }

            QTreeWidget{

                border:none;

                background:transparent;

                outline:none;

                font-size:11pt;

                color:#334155;

            }

            QTreeWidget::item{

                height:40px;

                padding-left:12px;

                margin:2px 6px;

                border-radius:8px;

            }

            QTreeWidget::item:hover{

                background:#EEF4FF;

                color:#2563EB;

            }

            QTreeWidget::item:selected{

                background:#2563EB;

                color:white;

                font-weight:bold;

            }

            QScrollBar:vertical{

                width:8px;

                background:transparent;

            }

            QScrollBar::handle:vertical{

                background:#CBD5E1;

                border-radius:4px;

            }

            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical{

                height:0px;

            }

            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical{

                background:transparent;

            }
            """
        )

        ####################################################
        # LAYOUT
        ####################################################

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            15,
            15,
            15,
            15,
        )

        layout.setSpacing(10)

        ####################################################
        # LOGO
        ####################################################

        self.logo = QLabel("⚙")

        self.logo.setObjectName("Logo")

        self.logo.setAlignment(
            Qt.AlignCenter
        )

        layout.addWidget(
            self.logo
        )

        ####################################################
        # TITLE
        ####################################################

        self.title = QLabel(
            "Personel ve\nBakım Yönetim Sistemi"
        )

        self.title.setObjectName(
            "Title"
        )

        self.title.setAlignment(
            Qt.AlignCenter
        )

        layout.addWidget(
            self.title
        )

        ####################################################
        # TREE
        ####################################################

        self.tree = QTreeWidget()

        self.tree.setHeaderHidden(True)

        self.tree.setIndentation(18)

        layout.addWidget(
            self.tree,
            1,
        )

        ####################################################
        # FOOTER
        ####################################################

        self.footer = QLabel(
            "v1.0.0"
        )

        self.footer.setObjectName(
            "Footer"
        )

        self.footer.setAlignment(
            Qt.AlignCenter
        )

        layout.addWidget(
            self.footer
        )

        ####################################################
        # MENU
        ####################################################

        self.create_menu()

    # =====================================================
    # MENU
    # =====================================================

    def create_menu(self):

        self.dashboard_item = QTreeWidgetItem(
            ["🏠 Dashboard"]
        )

        self.personel_item = QTreeWidgetItem(
            ["👨 Personeller"]
        )

        self.personel_item.addChild(
            QTreeWidgetItem(
                ["📋 Personel Listesi"]
            )
        )

        

     

        self.personel_item.addChild(
            QTreeWidgetItem(
                ["📄 Evraklar"]
            )
        )

        self.makine_item = QTreeWidgetItem(
            ["🏭 Makineler"]
        )

        self.makine_item.addChild(
            QTreeWidgetItem(
                ["🏭 Makine Listesi"]
            )
        )

        self.parca_item = QTreeWidgetItem(
            ["📦 Parçalar"]
        )

        self.parca_item.addChild(
            QTreeWidgetItem(
                ["📦 Parçalar"]
            )
        )

        self.parca_item.addChild(
            QTreeWidgetItem(
                ["🔄 Hareketler"]
            )
        )

        self.parca_item.addChild(
            QTreeWidgetItem(
                ["🗂 Kategoriler"]
            )
        )

        self.parca_item.addChild(
            QTreeWidgetItem(
                ["🏷 Markalar"]
            )
        )

        self.tedarikci_item = QTreeWidgetItem(
            ["🚚 Tedarikçiler"]
        )

        self.ayarlar_item = QTreeWidgetItem(
            ["⚙ Ayarlar"]
        )

        self.tree.addTopLevelItem(
            self.dashboard_item
        )

        self.tree.addTopLevelItem(
            self.personel_item
        )

        self.tree.addTopLevelItem(
            self.makine_item
        )

        self.tree.addTopLevelItem(
            self.parca_item
        )

        self.tree.addTopLevelItem(
            self.tedarikci_item
        )

        self.tree.addTopLevelItem(
            self.ayarlar_item
        )

        self.personel_item.setExpanded(True)
        self.makine_item.setExpanded(True)
        self.parca_item.setExpanded(True)

        self.tree.setCurrentItem(
            self.dashboard_item
        )

        ####################################################
        # Menü isimleri
        ####################################################

        self.menu_titles = {

            self.dashboard_item:
                "🏠 Dashboard",

            self.personel_item:
                "👨 Personeller",

            self.makine_item:
                "🏭 Makineler",

            self.parca_item:
                "📦 Parçalar",

            self.tedarikci_item:
                "🚚 Tedarikçiler",

            self.ayarlar_item:
                "⚙ Ayarlar",

        }

    # =====================================================
    # TOGGLE
    # =====================================================
    def toggle(self):

        start = self.width()

        if self.expanded:

            end = self.collapsed_width

        else:

            end = self.expanded_width


        self.animation = QPropertyAnimation(
            self,
            b"maximumWidth"
        )

        self.animation.setDuration(
            250
        )

        self.animation.setStartValue(
            start
        )

        self.animation.setEndValue(
            end
        )

        self.animation.setEasingCurve(
            QEasingCurve.OutCubic
        )


        self.animation.finished.connect(
            self.toggle_finished
        )


        self.animation.start()
    # =====================================================
    # TOGGLE FINISHED
    # =====================================================

    def toggle_finished(self):


        self.expanded = not self.expanded


        if self.expanded:

            self.setMaximumWidth(
                self.expanded_width
            )

            self.title.show()

            self.footer.show()

            self.tree.setIndentation(
                18
            )


            for item, text in self.menu_titles.items():

                item.setText(
                    0,
                    text
                )


            self.personel_item.setExpanded(True)

            self.makine_item.setExpanded(True)

            self.parca_item.setExpanded(True)



        else:


            self.setMaximumWidth(
                self.collapsed_width
            )


            self.title.hide()

            self.footer.hide()

            self.tree.setIndentation(
                0
            )


            for item, text in self.menu_titles.items():

                icon = text.split()[0]

                item.setText(
                    0,
                    icon
                )


            self.personel_item.setExpanded(False)

            self.makine_item.setExpanded(False)

            self.parca_item.setExpanded(False)