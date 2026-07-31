"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : ui/pages/personel_page.py
Açıklama   : Personel Sayfası
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from PySide6.QtGui import QStandardItem
from PySide6.QtGui import QStandardItemModel
from PySide6.QtWidgets import QMessageBox

from core.database import SessionLocal

from repositories.personel_repository import PersonelRepository
from services.personel_service import PersonelService

from ui.widgets.base_page import BasePage


class PersonelPage(BasePage):

    def __init__(self):

        super().__init__("Personeller")

        self.session = SessionLocal()

        self.repository = PersonelRepository(
            self.session
        )

        self.service = PersonelService(
            self.repository
        )

        self.model = QStandardItemModel()

        self.table.setModel(self.model)

        self.table.setSortingEnabled(True)

        self.load_personeller()

        self.btn_refresh.clicked.connect(
            self.load_personeller
        )

        self.txt_search.textChanged.connect(
            self.search
        )

    # =====================================================
    # DATA
    # =====================================================

    def load_personeller(self):

        self.model.clear()

        self.model.setHorizontalHeaderLabels(

            [

                "ID",

                "Sicil",

                "Ad",

                "Soyad",

                "Telefon",

                "Pozisyon",

            ]

        )

        personeller = self.service.get_all()

        for personel in personeller:

            self.model.appendRow(

                [

                    QStandardItem(str(personel.id)),

                    QStandardItem(personel.sicil_no),

                    QStandardItem(personel.ad),

                    QStandardItem(personel.soyad),

                    QStandardItem(
                        personel.telefon or ""
                    ),

                    QStandardItem(
                        personel.pozisyon.ad
                        if personel.pozisyon
                        else ""
                    ),

                ]

            )

        self.set_record_count(
            len(personeller)
        )

        self.table.resizeColumnsToContents()

    # =====================================================
    # SEARCH
    # =====================================================

    def search(
        self,
        text: str,
    ):

        if not text.strip():

            self.load_personeller()

            return

        self.model.removeRows(
            0,
            self.model.rowCount(),
        )

        personeller = self.service.search(
            text
        )

        for personel in personeller:

            self.model.appendRow(

                [

                    QStandardItem(str(personel.id)),

                    QStandardItem(personel.sicil_no),

                    QStandardItem(personel.ad),

                    QStandardItem(personel.soyad),

                    QStandardItem(
                        personel.telefon or ""
                    ),

                    QStandardItem(
                        personel.pozisyon.ad
                        if personel.pozisyon
                        else ""
                    ),

                ]

            )

        self.set_record_count(
            len(personeller)
        )

    # =====================================================
    # EVENTS
    # =====================================================

    def closeEvent(
        self,
        event,
    ):

        self.session.close()

        super().closeEvent(event)