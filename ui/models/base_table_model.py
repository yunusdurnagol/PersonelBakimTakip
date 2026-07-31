"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : ui/models/base_table_model.py
Açıklama   : Ortak Table Model
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from PySide6.QtCore import (
    QAbstractTableModel,
    QModelIndex,
    Qt,
)


class BaseTableModel(QAbstractTableModel):
    """
    Ortak Table Model.

    Tüm liste ekranları bu sınıftan türeyecektir.
    """

    def __init__(
        self,
        headers: list[str],
        rows: list = None,
    ) -> None:

        super().__init__()

        self._headers = headers
        self._rows = rows or []

    # =====================================================
    # ROW / COLUMN
    # =====================================================

    def rowCount(
        self,
        parent=QModelIndex(),
    ) -> int:

        return len(self._rows)

    def columnCount(
        self,
        parent=QModelIndex(),
    ) -> int:

        return len(self._headers)

    # =====================================================
    # DATA
    # =====================================================

    def data(
        self,
        index,
        role=Qt.DisplayRole,
    ):

        if (
            not index.isValid()
            or role != Qt.DisplayRole
        ):
            return None

        row = self._rows[index.row()]

        return self.get_value(
            row,
            index.column(),
        )

    # =====================================================
    # HEADER
    # =====================================================

    def headerData(
        self,
        section,
        orientation,
        role=Qt.DisplayRole,
    ):

        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            return self._headers[section]

        return str(section + 1)

    # =====================================================
    # ABSTRACT
    # =====================================================

    def get_value(
        self,
        row,
        column: int,
    ):

        """
        Alt sınıfta override edilir.
        """

        return ""

    # =====================================================
    # HELPERS
    # =====================================================

    def set_rows(
        self,
        rows: list,
    ) -> None:

        self.beginResetModel()

        self._rows = rows

        self.endResetModel()

    def row(
        self,
        index: int,
    ):

        return self._rows[index]

    def clear(
        self,
    ):

        self.set_rows([])

    @property
    def count(
        self,
    ) -> int:

        return len(self._rows)