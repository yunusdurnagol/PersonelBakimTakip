"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : ui/dialogs/personel_izin_dialog.py
Açıklama   : Personel izin listeleme dialogu
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from PySide6.QtGui import QStandardItem
from PySide6.QtGui import QStandardItemModel

from PySide6.QtWidgets import (
    QDialog,
    QHBoxLayout,
    QLabel,
    QMessageBox,
    QPushButton,
    QTableView,
    QVBoxLayout,
)

from ui.dialogs.personel_izin_ekle_dialog import (
    PersonelIzinEkleDialog,
)


class PersonelIzinDialog(QDialog):
    """
    Seçilen personelin izin kayıtlarını gösterir.

    Özellikler
    ----------
    - Personelin mevcut izinlerini listeler.
    - Yeni izin eklenmesini sağlar.
    - Mevcut izinleri düzenlemez.
    - Mevcut izinleri silmez.
    - İzin gün sayısını hesaplamaz.
    """

    # =====================================================
    # INIT
    # =====================================================

    def __init__(
        self,
        personel_izin_service,
        personel,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self.service = personel_izin_service
        self.personel = personel

        self.setWindowTitle(
            f"📅 İzinler - "
            f"{self.get_personel_adi()}"
        )

        self.resize(
            1100,
            650,
        )

        self.create_ui()
        self.create_connections()
        self.load_izinler()

    # =====================================================
    # UI
    # =====================================================

    def create_ui(self) -> None:

        main_layout = QVBoxLayout(self)

        main_layout.setContentsMargins(
            20,
            20,
            20,
            20,
        )

        main_layout.setSpacing(12)

        # =================================================
        # BAŞLIK
        # =================================================

        self.lbl_baslik = QLabel(
            f"📅 {self.get_personel_adi()}"
        )

        self.lbl_baslik.setStyleSheet(
            """
            QLabel {
                font-size: 15pt;
                font-weight: bold;
                color: #1E293B;
                padding: 5px;
            }
            """
        )

        main_layout.addWidget(
            self.lbl_baslik
        )

        # =================================================
        # TABLO
        # =================================================

        self.table = QTableView()

        self.table.setAlternatingRowColors(
            True
        )

        self.table.setSelectionBehavior(
            QTableView.SelectRows
        )

        self.table.setSelectionMode(
            QTableView.SingleSelection
        )

        self.table.setEditTriggers(
            QTableView.NoEditTriggers
        )

        self.table.verticalHeader().setVisible(
            False
        )

        self.model = QStandardItemModel()

        self.model.setHorizontalHeaderLabels(
            [
                "Başlangıç",
                "Bitiş",
                "Gün",
                "İzin Nedeni",
                "Açıklama",
            ]
        )

        self.table.setModel(
            self.model
        )

        self.table.setStyleSheet(
            """
            QTableView {
                background: white;
                border: 1px solid #E2E8F0;
                border-radius: 8px;
                gridline-color: #E2E8F0;
                font-size: 10pt;
            }

            QHeaderView::section {
                background: #F1F5F9;
                color: #334155;
                font-weight: 600;
                padding: 8px;
                border: none;
                border-bottom: 1px solid #CBD5E1;
            }

            QTableView::item {
                padding: 7px;
                border-bottom: 1px solid #F1F5F9;
            }

            QTableView::item:selected {
                background: #DBEAFE;
                color: #1E3A8A;
            }
            """
        )

        main_layout.addWidget(
            self.table,
            1,
        )

        # =================================================
        # ALT BUTONLAR
        # =================================================

        button_layout = QHBoxLayout()

        button_layout.setSpacing(8)

        button_layout.addStretch()

        # -------------------------------------------------
        # YENİ İZİN
        # -------------------------------------------------

        self.btn_yeni = QPushButton(
            "＋ Yeni İzin"
        )

        self.btn_yeni.setMinimumHeight(
            38
        )

        self.btn_yeni.setStyleSheet(
            """
            QPushButton {
                background: #10B981;
                color: white;
                border: none;
                border-radius: 7px;
                padding: 0 20px;
                font-weight: 600;
            }

            QPushButton:hover {
                background: #059669;
            }
            """
        )

        # -------------------------------------------------
        # KAPAT
        # -------------------------------------------------

        self.btn_kapat = QPushButton(
            "Kapat"
        )

        self.btn_kapat.setMinimumHeight(
            38
        )

        self.btn_kapat.setStyleSheet(
            """
            QPushButton {
                background: white;
                color: #334155;
                border: 1px solid #CBD5E1;
                border-radius: 7px;
                padding: 0 20px;
                font-weight: 600;
            }

            QPushButton:hover {
                background: #F1F5F9;
            }
            """
        )

        button_layout.addWidget(
            self.btn_yeni
        )

        button_layout.addWidget(
            self.btn_kapat
        )

        main_layout.addLayout(
            button_layout
        )

        # =================================================
        # GENEL DIALOG STYLE
        # =================================================

        self.setStyleSheet(
            """
            QDialog {
                background: #F8FAFC;
            }
            """
        )

    # =====================================================
    # CONNECTIONS
    # =====================================================

    def create_connections(self) -> None:

        self.btn_yeni.clicked.connect(
            self.yeni_izin
        )

        self.btn_kapat.clicked.connect(
            self.reject
        )

    # =====================================================
    # PERSONEL ADI
    # =====================================================

    def get_personel_adi(self) -> str:

        ad = getattr(
            self.personel,
            "ad",
            "",
        ) or ""

        soyad = getattr(
            self.personel,
            "soyad",
            "",
        ) or ""

        sicil_no = getattr(
            self.personel,
            "sicil_no",
            "",
        ) or ""

        return (
            f"{ad} {soyad} "
            f"({sicil_no})"
        ).strip()

    # =====================================================
    # İZİNLERİ YÜKLE
    # =====================================================

    def load_izinler(self) -> None:

        self.model.removeRows(
            0,
            self.model.rowCount(),
        )

        try:

            izinler = (
                self.service.get_by_personel(
                    self.personel.id
                )
            )

            for izin in izinler:

                row = [

                    QStandardItem(
                        self.format_date(
                            izin.izin_baslangic
                        )
                    ),

                    QStandardItem(
                        self.format_date(
                            izin.izin_bitis
                        )
                    ),

                    QStandardItem(
                        str(
                            izin.izin_gun_sayisi
                        )
                    ),

                    QStandardItem(
                        izin.izin_nedeni or ""
                    ),

                    QStandardItem(
                        izin.aciklama or ""
                    ),
                ]

                self.model.appendRow(
                    row
                )

            self.table.resizeColumnsToContents()

            # Açıklama sütunu
            self.table.setColumnWidth(
                4,
                400,
            )

            self.table.horizontalHeader().setStretchLastSection(
                True
            )

        except Exception as exc:

            QMessageBox.critical(
                self,
                "İzinler Yüklenemedi",
                str(exc),
            )

    # =====================================================
    # YENİ İZİN
    # =====================================================

    def yeni_izin(self) -> None:

        dialog = PersonelIzinEkleDialog(
            personel_izin_service=self.service,
            personel=self.personel,
            parent=self,
        )

        result = dialog.exec()

        if result == QDialog.Accepted:

            self.load_izinler()

    # =====================================================
    # TARİH FORMAT
    # =====================================================

    @staticmethod
    def format_date(
        value,
    ) -> str:

        if value is None:
            return ""

        return value.strftime(
            "%d.%m.%Y"
        )