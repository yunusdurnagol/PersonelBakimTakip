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
from ui.pages.personel_evrak_page import PersonelEvrakPage
class MainWindow(QMainWindow):

    def __init__(
        self,
        container,
    ):

        super().__init__()

        self.container = container

        self.setWindowTitle(
            "Personel ve Bakım Yönetim Sistemi"
        )

        self.resize(
            1800,
            950,
        )

        self.showMaximized()

        self.create_ui()
        self.create_connections()

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

        self.dashboard_page = DashboardPage(
            self.container.dashboard_service
        )

        self.personel_page = PersonelPage(
            self.container.personel_service,
            self.container.pozisyon_service,
            self.container.personel_evrak_service,
            self.container.personel_izin_service,
        )
        self.personel_evrak_page = PersonelEvrakPage(
            self.container.personel_service,
            self.container.personel_evrak_service,
        )
       
        self.pages.addWidget(
            self.dashboard_page,
        )

        self.pages.addWidget(
            self.personel_page,
        )
        self.pages.addWidget(
            self.personel_evrak_page,
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

        self.header.toggleMenuRequested.connect(
        self.sidebar.toggle
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

        # =================================================
        # DASHBOARD
        # =================================================

        if "Dashboard" in text:

            self.pages.setCurrentWidget(
                self.dashboard_page
            )

            self.header.set_page_title(
                "🏠 Dashboard"
            )

            self.lbl_status.setText(
                "Dashboard Açıldı"
            )

            return

        # =================================================
        # PERSONELLER
        # =================================================

        if "Personeller" in text:

            # Alt menüyü aç
            self.sidebar.personel_item.setExpanded(
                True
            )

            # Personel listesini göster
            self.pages.setCurrentWidget(
                self.personel_page
            )

            self.header.set_page_title(
                "👨 Personeller"
            )

            self.lbl_status.setText(
                "Personel Listesi"
            )

            return

        # =================================================
        # PERSONEL LİSTESİ
        # =================================================

        if "Personel Listesi" in text:

            self.pages.setCurrentWidget(
                self.personel_page
            )

            self.header.set_page_title(
                "👨 Personeller"
            )

            self.lbl_status.setText(
                "Personel Listesi"
            )

            return

        elif "Evraklar" in text:

            self.pages.setCurrentWidget(
                self.personel_evrak_page,
            )

            self.header.set_page_title(
                "📄 Personel Evrakları",
            )

            self.lbl_status.setText(
                "Personel Evrakları",
            )
        # =================================================
        # MAKİNELER
        # =================================================

        if "Makineler" in text:

            self.sidebar.makine_item.setExpanded(
                True
            )

            # Makine sayfası varsa aç
            self.pages.setCurrentWidget(
                self.makine_page
            )

            self.header.set_page_title(
                "🏭 Makineler"
            )

            self.lbl_status.setText(
                "Makine Listesi"
            )

            return

        # =================================================
        # MAKİNE LİSTESİ
        # =================================================

        if "Makine Listesi" in text:

            self.pages.setCurrentWidget(
                self.makine_page
            )

            self.header.set_page_title(
                "🏭 Makineler"
            )

            self.lbl_status.setText(
                "Makine Listesi"
            )

            return

    def create_connections(self):

        self.header.toggleMenuRequested.connect(
        self.sidebar.toggle
        )