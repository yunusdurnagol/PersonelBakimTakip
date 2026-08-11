"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : ui/pages/dashboard_page.py
Açıklama   : Dashboard Sayfası
Yazar      : Yunus Durnagöl
Sürüm      : 2.0.0
---------------------------------------------------------
"""
 
 
from PySide6.QtGui import QColor
from PySide6.QtGui import QFont
 
 
 

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QFrame,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QGraphicsDropShadowEffect,
)

class DashboardCard(QFrame):

    def __init__(
        self,
        icon: str,
        title: str,
        value: str,
        color: str,
        
    ):
        
        super().__init__()
         
        self.setObjectName("DashboardCard")

        self.setStyleSheet(
            f"""
            QFrame#DashboardCard{{
                background:{color};
                border-radius:12px;
            }}

            QLabel{{
                color:white;
            }}
            """
        )

        self.setFixedHeight(110)

        shadow = QGraphicsDropShadowEffect()

        shadow.setBlurRadius(30)
        shadow.setOffset(0, 5)
        shadow.setColor(QColor(0, 0, 0, 60))

        self.setGraphicsEffect(shadow)

        layout = QVBoxLayout(self)

        layout.setContentsMargins(18, 15, 18, 15)

        lbl_icon = QLabel(icon)
        lbl_icon.setFont(QFont("Segoe UI Emoji", 26))

        lbl_title = QLabel(title)
        lbl_title.setFont(QFont("Segoe UI", 10))

        lbl_value = QLabel(value)
        lbl_value.setFont(QFont("Segoe UI", 22, QFont.Bold))

        layout.addWidget(lbl_icon)
        layout.addWidget(lbl_title)
        layout.addStretch()
        layout.addWidget(lbl_value)

class DashboardPage(QWidget):

    def __init__(
        self,
        dashboard_service,
    ):

        super().__init__()

        self.dashboard_service = dashboard_service

        self.create_ui()

        self.load_tables()
    

    # =====================================================

    def create_ui(self):

        main = QVBoxLayout(self)

        main.setContentsMargins(25, 20, 25, 20)

        ####################################################

        header = QHBoxLayout()

        title = QLabel("🏠 Dashboard")

        title.setFont(
            QFont(
                "Segoe UI",
                20,
                QFont.Bold,
            )
        )

        header.addWidget(title)
        header.addStretch()

        main.addLayout(header)

        ####################################################

        cards = QGridLayout()
        kartlar = self.dashboard_service.kart_verileri()


        self.lbl_personel = DashboardCard(
            "👨",
            "Personeller",
            str(kartlar["personel"]),
            "#3B82F6",
        )

        self.lbl_makine = DashboardCard(
            "🏭",
            "Makineler",
            str(kartlar["makine"]),
            "#10B981",
        )

        self.lbl_parca = DashboardCard(
            "📦",
            "Parçalar",
            str(kartlar["parca"]),
            "#F59E0B",
        )

        self.lbl_tedarikci = DashboardCard(
            "🚚",
            "Tedarikçiler",
            str(kartlar["tedarikci"]),
            "#EF4444",
        )

        cards.addWidget(self.lbl_personel, 0, 0)
        cards.addWidget(self.lbl_makine, 0, 1)
        cards.addWidget(self.lbl_parca, 0, 2)
        cards.addWidget(self.lbl_tedarikci, 0, 3)

        main.addLayout(cards)

        ####################################################
        # Alt Tablolar
        ####################################################

        bottom = QHBoxLayout()
        
        self.personel_frame, self.tbl_personeller = self.create_table(
            "Son Eklenen Personeller",
            [
                "Sicil",
                "Ad Soyad",
                "Pozisyon",
            ],
        )

        
        self.hareket_frame, self.tbl_hareket = self.create_table(
            "Son Parça Hareketleri",
            [
                "Tarih",
                "Parça",
                "Adet",
                "Tedarikçi",
            ],
        )

        bottom.addWidget(self.personel_frame)
        bottom.addWidget(self.hareket_frame)

        main.addLayout(bottom)
         
    # =====================================================

    def create_table(
        self,
        title,
        headers,
    ):

        frame = QFrame()

        frame.setStyleSheet(
            """
            QFrame{
                background:white;
                border-radius:10px;
            }
            """
        )

        shadow = QGraphicsDropShadowEffect()

        shadow.setBlurRadius(20)
        shadow.setOffset(0, 3)

        frame.setGraphicsEffect(shadow)

        layout = QVBoxLayout(frame)

        lbl = QLabel(title)

        lbl.setFont(
            QFont(
                "Segoe UI",
                11,
                QFont.Bold,
            )
        )

        table = QTableWidget()

        table.setColumnCount(len(headers))
        table.setHorizontalHeaderLabels(headers)

        table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        table.verticalHeader().hide()

        table.setAlternatingRowColors(True)

        table.setStyleSheet(
            """
            QTableWidget{
                border:none;
                alternate-background-color:#f8f8f8;
                gridline-color:#dddddd;
            }

            QHeaderView::section{
                background:#ECECEC;
                padding:6px;
                font-weight:bold;
            }

            QTableWidget::item:hover{
                background:#D6EAF8;
            }
            """
        )

        layout.addWidget(lbl)
        layout.addWidget(table)

        return frame, table

    # =====================================================

     

    def load_tables(self):

        # ----------------------------------
        # Son 10 Personel
        # ----------------------------------

        personeller = self.dashboard_service.son_personeller()

        self.tbl_personeller.setRowCount(len(personeller))

        for row, personel in enumerate(personeller):

            self.tbl_personeller.setItem(
                row,
                0,
                QTableWidgetItem(personel.sicil_no),
            )

            self.tbl_personeller.setItem(
                row,
                1,
                QTableWidgetItem(
                    f"{personel.ad} {personel.soyad}"
                ),
            )

            pozisyon = ""

            if personel.pozisyon:
                pozisyon = personel.pozisyon.ad

            self.tbl_personeller.setItem(
                row,
                2,
                QTableWidgetItem(pozisyon),
            )

        # ----------------------------------
        # Son 10 Parça Hareketi
        # ----------------------------------

        hareketler = self.dashboard_service.son_hareketler()

        self.tbl_hareket.setRowCount(len(hareketler))

        for row, hareket in enumerate(hareketler):

            self.tbl_hareket.setItem(
                row,
                0,
                QTableWidgetItem(
                    hareket.alis_tarihi.strftime("%d.%m.%Y")
                ),
            )

            self.tbl_hareket.setItem(
                row,
                1,
                QTableWidgetItem(
                    hareket.parca.parca_adi
                ),
            )

            self.tbl_hareket.setItem(
                row,
                2,
                QTableWidgetItem(
                    str(hareket.adet)
                ),
            )

            self.tbl_hareket.setItem(
                row,
                3,
                QTableWidgetItem(
                    hareket.tedarikci.firma_adi
                ),
            )   