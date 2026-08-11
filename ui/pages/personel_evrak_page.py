"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : ui/pages/personel_evrak_page.py
Açıklama   : Personele ait evrakların listelenmesi ve eklenmesi
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

import os

from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItem
from PySide6.QtGui import QStandardItemModel
from PySide6.QtWidgets import (
    QComboBox,
    QDialog,
    QHBoxLayout,
    QLabel,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from ui.dialogs.personel_evrak_dialog import PersonelEvrakDialog
from ui.widgets.modern_table import ModernTable


class PersonelEvrakPage(QWidget):
    """
    Personel evrak yönetim ekranı.

    UI
        ↓
    PersonelEvrakService
        ↓
    PersonelEvrakRepository
        ↓
    ORM
    """

    def __init__(
        self,
        personel_service,
        personel_evrak_service,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self.personel_service = personel_service
        self.evrak_service = personel_evrak_service

        self.model = QStandardItemModel()

        self.create_ui()
        self.create_connections()
        self.load_personeller()

    # =====================================================
    # UI
    # =====================================================

    def create_ui(self) -> None:

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            15,
            15,
            15,
            15,
        )

        layout.setSpacing(10)

        # -------------------------------------------------
        # ÜST BİLGİ
        # -------------------------------------------------

        top_layout = QHBoxLayout()

        self.lbl_personel = QLabel(
            "Personel:"
        )

        self.combo_personel = QComboBox()

        self.combo_personel.setMinimumWidth(
            300
        )

        self.btn_yeni = QPushButton(
            "＋ Yeni Evrak"
        )

        self.btn_yeni.setObjectName(
            "btnYeniEvrak"
        )

        self.set_button_style()

        top_layout.addWidget(
            self.lbl_personel
        )

        top_layout.addWidget(
            self.combo_personel
        )

        top_layout.addWidget(
            self.btn_yeni
        )

        top_layout.addStretch()

        layout.addLayout(
            top_layout
        )

        # -------------------------------------------------
        # TABLO
        # -------------------------------------------------

        self.table = ModernTable(
            title="Personel Evrakları",
            icon="📄",
        )

        layout.addWidget(
            self.table
        )

        # -------------------------------------------------
        # MODEL
        # -------------------------------------------------

        self.model.setHorizontalHeaderLabels(
            [
                "ID",
                "Evrak Adı",
                "Dosya Adı",
                "Belge Tarihi",
                "Açıklama",
                "Dosya Yolu",
            ]
        )

        self.table.set_model(
            self.model
        )

        # ID gizle
        self.table.hide_column(0)

        # Dosya yolunu da gizleyelim.
        # Dosyayı açarken modelden kullanacağız.
        self.table.hide_column(5)

    # =====================================================
    # CONNECTIONS
    # =====================================================

    def create_connections(self) -> None:

        self.combo_personel.currentIndexChanged.connect(
            self.personel_changed
        )

        self.btn_yeni.clicked.connect(
            self.yeni_evrak
        )

        self.table.refreshRequested.connect(
            self.load_evraklar
        )

        self.table.rowDoubleClicked.connect(
            self.evrak_double_clicked
        )

    # =====================================================
    # BUTON STİLİ
    # =====================================================

    def set_button_style(self) -> None:

        self.setStyleSheet(
            """
            QPushButton {
                min-height: 36px;
                padding: 0 16px;
                border-radius: 8px;
                border: none;
                background: #2563EB;
                color: white;
                font-size: 10pt;
                font-weight: 600;
            }

            QPushButton:hover {
                background: #1D4ED8;
            }
            """
        )

    # =====================================================
    # PERSONELLERİ YÜKLE
    # =====================================================

    def load_personeller(self) -> None:

        self.combo_personel.blockSignals(True)

        self.combo_personel.clear()

        try:

            personeller = (
                self.personel_service.get_tum_personeller()
            )

            for personel in personeller:

                ad_soyad = (
                    f"{personel.ad} "
                    f"{personel.soyad}"
                )

                self.combo_personel.addItem(
                    ad_soyad,
                    personel.id,
                )

        except Exception as exc:

            QMessageBox.critical(
                self,
                "Personeller Yüklenemedi",
                str(exc),
            )

        finally:

            self.combo_personel.blockSignals(
                False
            )

        if self.combo_personel.count() > 0:

            self.combo_personel.setCurrentIndex(0)

            self.load_evraklar()

    # =====================================================
    # PERSONEL DEĞİŞTİ
    # =====================================================

    def personel_changed(
        self,
        index: int,
    ) -> None:

        if index < 0:

            self.model.removeRows(
                0,
                self.model.rowCount(),
            )

            return

        self.load_evraklar()

    # =====================================================
    # SEÇİLİ PERSONEL ID
    # =====================================================

    def selected_personel_id(self) -> int | None:

        value = (
            self.combo_personel.currentData()
        )

        if value is None:

            return None

        return int(value)

    # =====================================================
    # EVRAKLARI YÜKLE
    # =====================================================

    def load_evraklar(self) -> None:

        self.model.removeRows(
            0,
            self.model.rowCount(),
        )

        personel_id = (
            self.selected_personel_id()
        )

        if personel_id is None:

            self.table.update_footer()

            return

        try:

            evraklar = (
                self.evrak_service.get_by_personel(
                    personel_id
                )
            )

            for evrak in evraklar:

                row = [

                    QStandardItem(
                        str(evrak.id)
                    ),

                    QStandardItem(
                        evrak.evrak_adi or ""
                    ),

                    QStandardItem(
                        evrak.dosya_adi or ""
                    ),

                    QStandardItem(
                        self.format_date(
                            evrak.belge_tarihi
                        )
                    ),

                    QStandardItem(
                        evrak.aciklama or ""
                    ),

                    QStandardItem(
                        evrak.dosya_yolu or ""
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
                "Evraklar Yüklenemedi",
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
    # YENİ EVRAK
    # =====================================================

    def yeni_evrak(self) -> None:

        personel_id = (
            self.selected_personel_id()
        )

        if personel_id is None:

            QMessageBox.information(
                self,
                "Personel Seçilmedi",
                "Lütfen önce bir personel seçin.",
            )

            return

        dialog = PersonelEvrakDialog(
            personel_id=personel_id,
            personel_evrak_service=self.evrak_service,
            parent=self,
        )

        result = dialog.exec()

        if result == QDialog.Accepted:

            self.load_evraklar()

    # =====================================================
    # ÇİFT TIK
    # =====================================================

    def evrak_double_clicked(
        self,
        row: int,
    ) -> None:

        item = self.model.item(
            row,
            5,
        )

        if item is None:

            return

        dosya_yolu = item.text()

        if not dosya_yolu:

            return

        if not os.path.exists(
            dosya_yolu
        ):

            QMessageBox.warning(
                self,
                "Dosya Bulunamadı",
                (
                    "Evrak dosyası bulunamadı:\n\n"
                    f"{dosya_yolu}"
                ),
            )

            return

        try:

            os.startfile(
                dosya_yolu
            )

        except Exception as exc:

            QMessageBox.critical(
                self,
                "Dosya Açma Hatası",
                str(exc),
            )

    # =====================================================
    # REFRESH
    # =====================================================

    def refresh(self) -> None:

        self.load_personeller()