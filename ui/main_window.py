"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : ui/main_window.py
Açıklama   : Ana Pencere
Yazar      : Yunus Durnagöl
Sürüm      : 2.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QStackedWidget,
    QStatusBar,
    QLabel,
)

from ui.widgets.sidebar import Sidebar
from ui.widgets.header import Header

from ui.pages.dashboard_page import DashboardPage
from ui.pages.personel_page import PersonelPage


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "Personel ve Bakım Yönetim Sistemi"
        )

        self.resize(
            1800,
            950,
        )

        self.showMaximized()

        self.create_ui()

    # =====================================================
    # UI
    # =====================================================

    def create_ui(self):

        self.central = QWidget()

        self.setCentralWidget(
            self.central,
        )

        self.main_layout = QHBoxLayout(
            self.central,
        )

        self.main_layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        self.main_layout.setSpacing(0)

        ####################################################
        # SOL MENÜ
        ####################################################

        self.sidebar = Sidebar()

        self.main_layout.addWidget(
            self.sidebar,
        )

        ####################################################
        # SAĞ TARAF
        ####################################################

        right_widget = QWidget()

        right_layout = QVBoxLayout(
            right_widget,
        )

        right_layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        right_layout.setSpacing(0)

        ####################################################
        # HEADER
        ####################################################

        self.header = Header()

        right_layout.addWidget(
            self.header,
        )

        ####################################################
        # STACKED WIDGET
        ####################################################

        self.pages = QStackedWidget()

        right_layout.addWidget(
            self.pages,
        )

        self.main_layout.addWidget(
            right_widget,
        )

        ####################################################
        # SAYFALAR
        ####################################################

        self.dashboard_page = DashboardPage()

        self.personel_page = PersonelPage()

        self.pages.addWidget(
            self.dashboard_page,
        )

        self.pages.addWidget(
            self.personel_page,
        )

        ####################################################
        # STATUSBAR
        ####################################################

        self.create_statusbar()

        ####################################################
        # MENÜ BAĞLANTISI
        ####################################################

        self.sidebar.tree.currentItemChanged.connect(
            self.change_page,
        )

    # =====================================================
    # STATUSBAR
    # =====================================================

    def create_statusbar(self):

        status = QStatusBar()

        self.setStatusBar(
            status,
        )

        self.lbl_status = QLabel(
            "Hazır"
        )

        status.addPermanentWidget(
            self.lbl_status,
        )

    # =====================================================
    # SAYFA DEĞİŞTİR
    # =====================================================

    def change_page(
        self,
        current,
        previous,
    ):

        if current is None:
            return

        text = current.text(0)

        ################################################

        if "Dashboard" in text:

            self.pages.setCurrentWidget(
                self.dashboard_page,
            )

            self.header.set_page_title(
                "🏠 Dashboard",
            )

            self.lbl_status.setText(
                "Dashboard Açıldı",
            )

        ################################################

        elif "Personel Listesi" in text:

            self.pages.setCurrentWidget(
                self.personel_page,
            )

            self.header.set_page_title(
                "👨 Personeller",
            )

            self.lbl_status.setText(
                "Personel Listesi",
            )