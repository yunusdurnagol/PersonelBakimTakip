"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : ui/widgets/modern_table.py
Açıklama   : Modern Tablo Widget
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QHeaderView,
    QAbstractItemView,
)


class ModernTable(QWidget):

    def __init__(
        self,
        title: str,
        headers: list[str],
    ):

        super().__init__()

        self.headers = headers

        self.create_ui(title)

    # =====================================================

    def create_ui(
        self,
        title: str,
    ):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(0, 0, 0, 0)

        ####################################################
        # ÜST BAR
        ####################################################

        top = QHBoxLayout()

        lbl = QLabel(title)

        lbl.setObjectName("TableTitle")

        self.search = QLineEdit()

        self.search.setPlaceholderText(
            "Ara..."
        )

        self.btn_refresh = QPushButton("↻")

        self.btn_export = QPushButton("Excel")

        self.btn_print = QPushButton("Yazdır")

        top.addWidget(lbl)

        top.addStretch()

        top.addWidget(self.search)

        top.addWidget(self.btn_refresh)

        top.addWidget(self.btn_export)

        top.addWidget(self.btn_print)

        ####################################################
        # TABLE
        ####################################################

        self.table = QTableWidget()

        self.table.setColumnCount(
            len(self.headers)
        )

        self.table.setHorizontalHeaderLabels(
            self.headers
        )

        self.table.setAlternatingRowColors(True)

        self.table.setSelectionBehavior(
            QAbstractItemView.SelectRows
        )

        self.table.setSelectionMode(
            QAbstractItemView.SingleSelection
        )

        self.table.setEditTriggers(
            QAbstractItemView.NoEditTriggers
        )

        self.table.setSortingEnabled(True)

        self.table.verticalHeader().hide()

        self.table.horizontalHeader().setStretchLastSection(
            True
        )

        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Interactive
        )

        self.table.setShowGrid(False)

        ####################################################

        layout.addLayout(top)

        layout.addWidget(self.table)

        self.setStyleSheet(
            """
            QWidget{

                background:white;

            }

            QLabel#TableTitle{

                font-size:15px;

                font-weight:bold;

            }

            QLineEdit{

                min-height:34px;

                border:1px solid #D9DEE7;

                border-radius:8px;

                padding-left:10px;

                background:white;

            }

            QPushButton{

                min-height:34px;

                padding-left:16px;

                padding-right:16px;

                border:none;

                border-radius:8px;

                background:#F3F4F6;

            }

            QPushButton:hover{

                background:#E5E7EB;

            }

            QTableWidget{

                border:1px solid #E5E7EB;

                border-radius:10px;

                gridline-color:transparent;

                alternate-background-color:#FAFAFA;

                selection-background-color:#DCEBFF;

                selection-color:black;

            }

            QHeaderView::section{

                background:#F8F9FB;

                border:none;

                border-bottom:1px solid #E5E7EB;

                padding:8px;

                font-weight:bold;

            }

            QTableWidget::item{

                padding:8px;

            }

            QTableWidget::item:hover{

                background:#EEF5FF;

            }
            """
        )

    # =====================================================

    def set_row_count(
        self,
        count: int,
    ):

        self.table.setRowCount(count)

    # =====================================================

    def clear(self):

        self.table.setRowCount(0)