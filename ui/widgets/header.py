"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : ui/widgets/header.py
Açıklama   : Modern Header
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from datetime import datetime

from PySide6.QtCore import Qt
from PySide6.QtCore import QTimer

from PySide6.QtGui import QFont

from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
)


class Header(QFrame):

    def __init__(self):

        super().__init__()

        self.setObjectName("Header")

        self.setFixedHeight(70)

        self.setStyleSheet("""
        #Header{
            background:white;
            border:none;
            border-bottom:1px solid #E5E7EB;
        }

        QLabel{
            color:#1F2937;
        }
        """)

        self.create_ui()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)

        self.update_clock()

    # =====================================================

    def create_ui(self):

        layout = QHBoxLayout(self)

        layout.setContentsMargins(25, 10, 25, 10)

        ####################################################

        self.lbl_title = QLabel("🏠 Dashboard")

        self.lbl_title.setFont(
            QFont(
                "Segoe UI",
                18,
                QFont.Bold,
            )
        )

        layout.addWidget(self.lbl_title)

        layout.addStretch()

        ####################################################

        right = QVBoxLayout()

        self.lbl_time = QLabel()

        self.lbl_time.setAlignment(
            Qt.AlignRight
        )

        self.lbl_time.setFont(
            QFont(
                "Segoe UI",
                11,
                QFont.Bold,
            )
        )

        self.lbl_user = QLabel(
            "👤 Yunus Durnagöl"
        )

        self.lbl_user.setAlignment(
            Qt.AlignRight
        )

        self.lbl_user.setStyleSheet("""
        color:#6B7280;
        """)

        right.addWidget(self.lbl_time)
        right.addWidget(self.lbl_user)

        layout.addLayout(right)

    # =====================================================

    def set_page_title(
        self,
        title: str,
    ):

        self.lbl_title.setText(title)

    # =====================================================

    def update_clock(self):

        now = datetime.now()

        self.lbl_time.setText(

            now.strftime(

                "%d.%m.%Y   %H:%M:%S"

            )

        )