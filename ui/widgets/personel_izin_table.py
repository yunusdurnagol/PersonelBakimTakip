"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : ui/widgets/personel_izin_table.py
Açıklama   : Personel İzin Listesi
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItem
from PySide6.QtGui import QStandardItemModel
from PySide6.QtWidgets import (
    QHBoxLayout,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from ui.dialogs.personel_izinler_dialog import (
    PersonelIzinDialog,
)
from ui.widgets.modern_table import ModernTable


class PersonelIzinTable(QWidget):
    """
    Seçili personele ait izin kayıtlarını gösterir.
    """

    def __init__(
        self,
        personel_izin_service,
        personel,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self.service = personel_izin_service
        self.personel = personel

        self.model = QStandardItemModel()

        self.create_ui()
        self.load_izinler()

    # =====================================================
    # UI
    # =====================================================

    def create_ui(self) -> None:

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        layout.setSpacing(10)

        # =================================================
        # TABLO
        # =================================================

        self.table = ModernTable(
            title="Personel İzinleri",
            icon="📅",
        )

        layout.addWidget(
            self.table
        )

        self.model.setHorizontalHeaderLabels(
            [
                "ID",
                "İzin Başlangıç",
                "İzin Bitiş",
                "Kullanılan İzin",
                "İzin Nedeni",
                "Açıklama",
            ]
        )

        self.table.set_model(
            self.model
        )

        self.table.hide_column(0)

        # =================================================
        # BUTON
        # =================================================

        button_layout = QHBoxLayout()

        self.btn_yeni = QPushButton(
            "＋ Yeni İzin"
        )

        self.btn_yeni.setObjectName(
            "btnYeniIzin"
        )

        self.btn_yeni.setStyleSheet(
            """
            QPushButton {
                min-height: 36px;
                padding: 0 16px;
                border-radius: 8px;
                border: none;
                background: #2563EB;
                color: white;
                font-weight: 600;
            }

            QPushButton:hover {
                background: #1D4ED8;
            }
            """
        )

        button_layout.addWidget(
            self.btn_yeni
        )

        button_layout.addStretch()

        layout.addLayout(
            button_layout
        )

        self.btn_yeni.clicked.connect(
            self.yeni_izin
        )

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
                        str(izin.id)
                    ),

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
                        f"{izin.izin_gun_sayisi} gün"
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

            self.table.resize_columns()
            self.table.update_footer()

        except Exception as exc:

            QMessageBox.critical(
                self,
                "İzinler Yüklenemedi",
                str(exc),
            )

    # =====================================================
    # TARİH
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

    # =====================================================
    # YENİ İZİN
    # =====================================================

    def yeni_izin(self) -> None:

        dialog = PersonelIzinDialog(
            personel_izin_service=self.service,
            personel=self.personel,
            parent=self,
        )

        result = dialog.exec()

        if result == dialog.Accepted:

            self.load_izinler()