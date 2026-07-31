"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : ui/widgets/dashboard_card.py
Açıklama   : Dashboard Bilgi Kartı
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
)


class DashboardCard(QFrame):

    def __init__(
        self,
        title: str,
        icon: str,
    ):

        super().__init__()

        self.setObjectName("DashboardCard")

        layout = QVBoxLayout(self)

        self.icon = QLabel(icon)
        self.icon.setAlignment(Qt.AlignCenter)

        self.icon.setStyleSheet("""
            font-size:36px;
        """)

        self.value = QLabel("0")

        self.value.setAlignment(Qt.AlignCenter)

        self.value.setStyleSheet("""
            font-size:34px;
            font-weight:bold;
        """)

        self.title = QLabel(title)

        self.title.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.icon)
        layout.addWidget(self.value)
        layout.addWidget(self.title)

        self.setMinimumHeight(180)

    def set_value(self, value):

        self.value.setText(str(value))