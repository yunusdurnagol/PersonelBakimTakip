"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : ui/widgets/header.py
Açıklama   : Header Widget
Yazar      : Yunus Durnagöl
Sürüm      : 2.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from PySide6.QtCore import Qt, Signal

from PySide6.QtGui import (
    QFont,
)

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QFrame,
)


class Header(QFrame):
    """
    Uygulamanın üst bilgi alanı.

    Sol tarafta:
        ☰ Menü Butonu
        Sayfa Başlığı

    Sağ tarafta:
        Kullanıcı bilgileri
    """

    ####################################################
    # Signals
    ####################################################
    toggleMenuRequested = Signal()
     

    ####################################################

    def __init__(self):

        super().__init__()

        self.create_ui()

        self.create_connections()

    # =====================================================
    # UI
    # =====================================================

    def create_ui(self):

        self.setObjectName("Header")

        self.setFixedHeight(70)

        layout = QHBoxLayout(self)

        layout.setContentsMargins(
            20,
            0,
            20,
            0,
        )

        layout.setSpacing(12)

        ####################################################
        # MENU BUTTON
        ####################################################

        self.btn_menu = QPushButton("☰")

        self.btn_menu.setObjectName(
            "MenuButton"
        )

        self.btn_menu.setFixedSize(
            42,
            42,
        )

        layout.addWidget(
            self.btn_menu,
            alignment=Qt.AlignVCenter,
        )

        ####################################################
        # PAGE TITLE
        ####################################################

        self.lbl_title = QLabel(
            "🏠 Dashboard"
        )

        self.lbl_title.setFont(
            QFont(
                "Segoe UI",
                16,
                QFont.Bold,
            )
        )

        layout.addWidget(
            self.lbl_title,
            alignment=Qt.AlignVCenter,
        )

        layout.addStretch()

        ####################################################
        # USER
        ####################################################

        self.lbl_user = QLabel(
            "👤 Yönetici"
        )

        self.lbl_user.setFont(
            QFont(
                "Segoe UI",
                10,
            )
        )

        layout.addWidget(
            self.lbl_user,
            alignment=Qt.AlignVCenter,
        )

        ####################################################
        # STYLE
        ####################################################

        self.setStyleSheet(
            """
            QFrame#Header{

                background:white;

                border-bottom:1px solid #E5E7EB;

            }

            QPushButton#MenuButton{

                    border:1px solid #E5E7EB;

                    border-radius:8px;

                    background:#FFFFFF;

                    font-size:24px;

                    font-weight:bold;

                    color:#1F2937;

            }

            QPushButton#MenuButton:hover{

                background:#EEF4FF;

                color:#2563EB;

            }

            QLabel{

                color:#222;

            }
            """
        )

    # =====================================================
    # CONNECTIONS
    # =====================================================

    def create_connections(self):
        
        self.btn_menu.clicked.connect(
            self.toggleMenuRequested.emit
        )

    # =====================================================
    # TITLE
    # =====================================================

    def set_page_title(
        self,
        title: str,
    ):

        self.lbl_title.setText(title)

    # =====================================================

    def page_title(self) -> str:

        return self.lbl_title.text()

    # =====================================================
    # USER
    # =====================================================

    def set_user_name(
        self,
        name: str,
    ):

        self.lbl_user.setText(
            f"👤 {name}"
        )