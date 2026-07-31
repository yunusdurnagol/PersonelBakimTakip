"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : ui/widgets/base_page.py
Açıklama   : Tüm ekranların temel sınıfı
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QTableView,
    QVBoxLayout,
    QWidget,
)


class BasePage(QWidget):
    """
    Tüm liste ekranlarının temel sınıfı.

    Personeller
    Makineler
    Parçalar
    Tedarikçiler
    vb...
    """

    def __init__(
        self,
        title: str,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self.title = title

        self._create_widgets()
        self._create_layout()
        self._connect_signals()

    # =====================================================
    # WIDGETS
    # =====================================================

    def _create_widgets(self) -> None:

        self.lbl_title = QLabel(self.title)

        self.lbl_title.setObjectName("pageTitle")

        self.btn_new = QPushButton("Yeni")

        self.btn_edit = QPushButton("Düzenle")

        self.btn_delete = QPushButton("Sil")

        self.btn_refresh = QPushButton("Yenile")

        self.txt_search = QLineEdit()

        self.txt_search.setPlaceholderText(
            "Ara..."
        )

        self.table = QTableView()

        self.table.setAlternatingRowColors(True)

        self.table.setSelectionBehavior(
            QTableView.SelectRows
        )

        self.table.setSelectionMode(
            QTableView.SingleSelection
        )

        self.table.setSortingEnabled(True)

        self.table.verticalHeader().setVisible(False)

        self.table.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding,
        )

        self.lbl_count = QLabel(
            "Toplam Kayıt : 0"
        )

    # =====================================================
    # LAYOUT
    # =====================================================

    def _create_layout(self) -> None:

        main_layout = QVBoxLayout(self)

        # -------------------------
        # Başlık
        # -------------------------

        main_layout.addWidget(
            self.lbl_title
        )

        # -------------------------
        # Toolbar
        # -------------------------

        toolbar = QHBoxLayout()

        toolbar.addWidget(
            self.btn_new
        )

        toolbar.addWidget(
            self.btn_edit
        )

        toolbar.addWidget(
            self.btn_delete
        )

        toolbar.addWidget(
            self.btn_refresh
        )

        toolbar.addStretch()

        toolbar.addWidget(
            self.txt_search
        )

        main_layout.addLayout(toolbar)

        # -------------------------
        # Table
        # -------------------------

        main_layout.addWidget(
            self.table
        )

        # -------------------------
        # Footer
        # -------------------------

        footer = QHBoxLayout()

        footer.addWidget(
            self.lbl_count
        )

        footer.addStretch()

        main_layout.addLayout(
            footer
        )

    # =====================================================
    # SIGNALS
    # =====================================================

    def _connect_signals(self) -> None:

        self.txt_search.textChanged.connect(
            self.on_search
        )

        self.btn_refresh.clicked.connect(
            self.on_refresh
        )

    # =====================================================
    # EVENTS
    # =====================================================

    def on_search(
        self,
        text: str,
    ) -> None:
        """
        Alt sınıfta override edilir.
        """
        pass

    def on_refresh(
        self,
    ) -> None:
        """
        Alt sınıfta override edilir.
        """
        pass

    # =====================================================
    # HELPERS
    # =====================================================

    def set_record_count(
        self,
        count: int,
    ) -> None:

        self.lbl_count.setText(
            f"Toplam Kayıt : {count}"
        )

    def set_title(
        self,
        title: str,
    ) -> None:

        self.lbl_title.setText(title)

    def get_selected_row(self) -> int:

        indexes = self.table.selectionModel().selectedRows()

        if not indexes:
            return -1

        return indexes[0].row()