"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : ui/widgets/modern_table.py
Açıklama   : Modern Tablo Widget
Yazar      : Yunus Durnagöl
Sürüm      : 3.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from PySide6.QtCore import (
    Qt,
    Signal,
    QSortFilterProxyModel,
)

from PySide6.QtGui import (
    QAction,
)

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QTableView,
    QHeaderView,
    QAbstractItemView,
    QSizePolicy,
    QMenu,
)


class ModernTable(QWidget):
    """
    Modern ERP Table Widget

    Bu widget;

    - Repository bilmez.
    - Service bilmez.
    - SQLAlchemy bilmez.
    - ORM bilmez.

    Sadece tablo gösterir.
    """

    ####################################################
    # SIGNALS
    ####################################################

    refreshRequested = Signal()

    excelRequested = Signal()

    pdfRequested = Signal()

    printRequested = Signal()

    rowDoubleClicked = Signal(int)

    selectionChanged = Signal(int)

    ####################################################

    def __init__(
        self,
        title: str,
        icon: str = "",
    ):

        super().__init__()

        self._title = title

        self._icon = icon

        self._model = None

        ####################################################
        # Proxy Model
        ####################################################

        self.proxy = QSortFilterProxyModel(self)

        self.proxy.setFilterCaseSensitivity(
            Qt.CaseInsensitive
        )

        self.proxy.setFilterKeyColumn(-1)

        ####################################################

        self.create_ui()

        self.create_connections()

    # ====================================================
    # UI
    # ====================================================

    def create_ui(self):

        root = QVBoxLayout(self)

        root.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        root.setSpacing(12)

        ####################################################
        # TOOLBAR
        ####################################################

        toolbar = QFrame()

        toolbar.setObjectName(
            "ModernTableToolbar"
        )

        toolbar_layout = QHBoxLayout(toolbar)

        toolbar_layout.setContentsMargins(
            16,
            12,
            16,
            12,
        )

        ####################################################
        # TITLE
        ####################################################

        title = self._title

        if self._icon:

            title = f"{self._icon} {title}"

        self.lbl_title = QLabel(title)

        self.lbl_title.setObjectName(
            "ModernTableTitle"
        )

        toolbar_layout.addWidget(
            self.lbl_title
        )

        toolbar_layout.addStretch()

        ####################################################
        # SEARCH
        ####################################################

        self.txt_search = QLineEdit()

        self.txt_search.setPlaceholderText(
            "Ara..."
        )

        self.txt_search.setMinimumWidth(
            280
        )

        self.txt_search.setClearButtonEnabled(
            True
        )

        toolbar_layout.addWidget(
            self.txt_search
        )

        ####################################################
        # BUTTONS
        ####################################################

        self.btn_refresh = QPushButton(
            "↻"
        )

        self.btn_excel = QPushButton(
            "Excel"
        )

        self.btn_pdf = QPushButton(
            "PDF"
        )

        self.btn_print = QPushButton(
            "Yazdır"
        )

        self.btn_refresh.setToolTip(
            "Yenile"
        )

        self.btn_excel.setToolTip(
            "Excel'e Aktar"
        )

        self.btn_pdf.setToolTip(
            "PDF Oluştur"
        )

        self.btn_print.setToolTip(
            "Yazdır"
        )

        toolbar_layout.addWidget(
            self.btn_refresh
        )

        toolbar_layout.addWidget(
            self.btn_excel
        )

        toolbar_layout.addWidget(
            self.btn_pdf
        )

        toolbar_layout.addWidget(
            self.btn_print
        )

        ####################################################
        # TABLE
        ####################################################

        self.table = QTableView()

        self.table.setSortingEnabled(True)

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

        self.table.setContextMenuPolicy(
            Qt.CustomContextMenu
        )

        self.table.setShowGrid(False)

        self.table.setWordWrap(False)

        self.table.verticalHeader().hide()

        header = self.table.horizontalHeader()

        header.setStretchLastSection(True)

        header.setHighlightSections(False)

        header.setSectionsMovable(True)

        header.setDefaultAlignment(
            Qt.AlignLeft | Qt.AlignVCenter
        )

        ####################################################
        # FOOTER
        ####################################################

        footer = QFrame()

        footer.setObjectName(
            "ModernTableFooter"
        )

        footer_layout = QHBoxLayout(footer)

        footer_layout.setContentsMargins(
            10,
            6,
            10,
            6,
        )

        self.lbl_total = QLabel(
            "Toplam : 0"
        )

        self.lbl_visible = QLabel(
            "Gösterilen : 0"
        )

        self.lbl_selected = QLabel(
            "Seçili : -"
        )

        footer_layout.addWidget(
            self.lbl_total
        )

        footer_layout.addSpacing(20)

        footer_layout.addWidget(
            self.lbl_visible
        )

        footer_layout.addStretch()

        footer_layout.addWidget(
            self.lbl_selected
        )

        ####################################################
        # LAYOUT
        ####################################################

        root.addWidget(toolbar)

        root.addWidget(
            self.table,
            1,
        )

        root.addWidget(footer)

        ####################################################
        # STYLE
        ####################################################

        self.setStyleSheet(
            """
            QWidget{
                background:white;
            }

            QFrame#ModernTableToolbar{
                background:white;
                border:1px solid #E5E7EB;
                border-radius:10px;
            }

            QFrame#ModernTableFooter{
                background:white;
                border:1px solid #E5E7EB;
                border-radius:10px;
            }

            QLabel#ModernTableTitle{
                font-size:15px;
                font-weight:bold;
                color:#222;
            }

            QLabel{
                color:#444;
            }

            QLineEdit{
                min-height:36px;
                border:1px solid #D6D9DE;
                border-radius:8px;
                padding-left:10px;
                background:white;
            }

            QLineEdit:focus{
                border:1px solid #3B82F6;
            }

            QPushButton{
                min-width:80px;
                min-height:36px;
                border:none;
                border-radius:8px;
                background:#F3F4F6;
            }

            QPushButton:hover{
                background:#E5E7EB;
            }

            QPushButton:pressed{
                background:#D1D5DB;
            }

            QTableView{
                border:1px solid #E5E7EB;
                border-radius:10px;
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
            """
        )

    # ====================================================
    # CONNECTIONS
    # ====================================================

    def create_connections(self):

        self.btn_refresh.clicked.connect(
            self.refreshRequested.emit
        )

        self.btn_excel.clicked.connect(
            self.excelRequested.emit
        )

        self.btn_pdf.clicked.connect(
            self.pdfRequested.emit
        )

        self.btn_print.clicked.connect(
            self.printRequested.emit
        )

        self.txt_search.textChanged.connect(
            self.on_search
        )

    # ====================================================
    # MODEL
    # ====================================================

    def set_model(self, model) -> None:
        """
        QStandardItemModel bağlar.
        """

        self._model = model

        self.proxy.setSourceModel(model)

        self.table.setModel(self.proxy)
        self.set_record_count(
        model.rowCount()
        )
        selection = self.table.selectionModel()

        if selection is not None:
            selection.selectionChanged.connect(
                self.on_selection_changed
            )

        self.table.doubleClicked.connect(
            self.on_double_clicked
        )

        self.update_footer()

        self.resize_columns()
        self.enable_context_menu()
    # ====================================================

    def model(self):

        return self._model

    # ====================================================

    def proxy_model(self):

        return self.proxy

    # ====================================================
    # SEARCH
    # ====================================================

    def on_search(
        self,
        text: str,
    ):

        self.proxy.setFilterFixedString(text)

        self.update_footer()

    # ====================================================
    # FOOTER
    # ====================================================

    def update_footer(self):

        total = 0

        visible = 0

        if self._model is not None:

            total = self._model.rowCount()

            visible = self.proxy.rowCount()

        self.lbl_total.setText(
            f"Toplam : {total}"
        )

        self.lbl_visible.setText(
            f"Gösterilen : {visible}"
        )

        row = self.selected_row()

        if row == -1:

            self.lbl_selected.setText(
                "Seçili : -"
            )

        else:

            self.lbl_selected.setText(
                f"Seçili : {row + 1}"
            )


    # RECORD COUNT
    # =====================================================

    def update_record_count(self) -> None:
        """
        Proxy modelde görünen kayıt sayısını gösterir.
        """

        if self.proxy is not None:
            self.lbl_record_count.setText(
                f"Toplam Kayıt : {self.proxy.rowCount()}"
            )
        elif self._model is not None:
            self.lbl_record_count.setText(
                f"Toplam Kayıt : {self._model.rowCount()}"
            )
        else:
            self.lbl_record_count.setText(
                "Toplam Kayıt : 0"
            )

    # ====================================================

    def set_record_count(
        self,
        count: int,
    ):

        self.lbl_total.setText(
            f"Toplam : {count}"
        )

    # ====================================================
    # TABLE
    # ====================================================

    def resize_columns(self):

        self.table.resizeColumnsToContents()

    # ====================================================

    def clear(self):

        if self._model is None:
            return

        self._model.setRowCount(0)

        self.update_footer()

    # ====================================================
    # SELECTION
    # ====================================================

    def selected_row(self):

        selection = self.table.selectionModel()

        if selection is None:
            return -1

        indexes = selection.selectedRows()

        if not indexes:
            return -1

        return self.proxy.mapToSource(
            indexes[0]
        ).row()

    # ====================================================

    def selected_column(self):

        index = self.table.currentIndex()

        if not index.isValid():
            return -1

        return index.column()

    # ====================================================

    def selected_indexes(self):

        selection = self.table.selectionModel()

        if selection is None:
            return []

        return selection.selectedRows()

    # ====================================================

    def has_selection(self):

        return self.selected_row() != -1

    # ====================================================

    def selected_data(
        self,
        column: int,
    ):

        row = self.selected_row()

        if row == -1:
            return None

        index = self._model.index(
            row,
            column,
        )

        return self._model.data(index)

    # ====================================================

    def selected_id(self):

        return self.selected_data(0)

    # ====================================================

    def current_index(self):

        return self.table.currentIndex()

    # ====================================================
    # SEARCH API
    # ====================================================

    def search_text(self):

        return self.txt_search.text()

    # ====================================================

    def set_search_text(
        self,
        text: str,
    ):

        self.txt_search.setText(text)

    # ====================================================

    def clear_search(self):

        self.txt_search.clear()

    # ====================================================

    def focus_search(self):

        self.txt_search.setFocus()

    # ====================================================
    # TABLE API
    # ====================================================

    def row_count(self):

        return self.proxy.rowCount()

    # ====================================================

    def column_count(self):

        return self.proxy.columnCount()

    # ====================================================

    def hide_column(
        self,
        column: int,
    ):

        self.table.hideColumn(column)

    # ====================================================

    def show_column(
        self,
        column: int,
    ):

        self.table.showColumn(column)

    # ====================================================

    def set_column_width(
        self,
        column: int,
        width: int,
    ):

        self.table.setColumnWidth(
            column,
            width,
        )

    # ====================================================

    def select_row(
        self,
        row: int,
    ):

        proxy_index = self.proxy.index(
            row,
            0,
        )

        self.table.selectRow(
            proxy_index.row()
        )

    # ====================================================
    # EVENTS
    # ====================================================

    def on_selection_changed(self):

        self.update_footer()

        self.selectionChanged.emit(
            self.selected_row()
        )

    # ====================================================

    def on_double_clicked(
        self,
        index,
    ):

        row = self.proxy.mapToSource(
            index
        ).row()

        self.rowDoubleClicked.emit(
            row
        )

    # ====================================================
    # CONTEXT MENU
    # ====================================================

    def enable_context_menu(self):

        self.table.customContextMenuRequested.connect(
            self.show_context_menu
        )

    # ====================================================

    def show_context_menu(
        self,
        position,
    ):

        menu = QMenu(self)

        action_refresh = QAction(
            "Yenile",
            self,
        )

        action_excel = QAction(
            "Excel'e Aktar",
            self,
        )

        action_pdf = QAction(
            "PDF Oluştur",
            self,
        )

        action_print = QAction(
            "Yazdır",
            self,
        )

        menu.addAction(action_refresh)

        menu.addSeparator()

        menu.addAction(action_excel)

        menu.addAction(action_pdf)

        menu.addAction(action_print)

        action_refresh.triggered.connect(
            self.refreshRequested.emit
        )

        action_excel.triggered.connect(
            self.excelRequested.emit
        )

        action_pdf.triggered.connect(
            self.pdfRequested.emit
        )

        action_print.triggered.connect(
            self.printRequested.emit
        )

        menu.exec(

            self.table.viewport().mapToGlobal(
                position
            )

        )

    # ====================================================
    # UTILITIES
    # ====================================================

    def auto_resize(self):

        self.table.resizeColumnsToContents()

    # ====================================================

    def stretch_last_column(self):

        self.table.horizontalHeader().setStretchLastSection(
            True
        )

    # ====================================================

    def set_sorting_enabled(
        self,
        enabled: bool,
    ):

        self.table.setSortingEnabled(
            enabled
        )

    # ====================================================

    def set_alternating_rows(
        self,
        enabled: bool,
    ):

        self.table.setAlternatingRowColors(
            enabled
        )

    # ====================================================

    def table_view(self):

        return self.table

    # ====================================================

    def refresh(self):

        self.refreshRequested.emit()

    # ====================================================

    def export_excel(self):

        self.excelRequested.emit()

    # ====================================================

    def export_pdf(self):

        self.pdfRequested.emit()

    # ====================================================

    def print_table(self):

        self.printRequested.emit()

    # ====================================================

    def set_title(
        self,
        title: str,
    ):

        self._title = title

        if self._icon:

            self.lbl_title.setText(

                f"{self._icon} {title}"

            )

        else:

            self.lbl_title.setText(title)

    # ====================================================

    def set_icon(
        self,
        icon: str,
    ):

        self._icon = icon

        self.set_title(
            self._title
        )

    # ====================================================

    def title(self):

        return self._title

    # ====================================================

    def icon(self):

        return self._icon

    def selected_id(self) -> int | None:
        value = self.selected_data(0)
        return int(value) if value is not None else None

# =====================================================
