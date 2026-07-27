"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : repositories/filters.py
Açıklama   : Filtre ve Sıralama Modelleri
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from repositories.enums import FilterOperator
from repositories.enums import SortDirection


@dataclass(slots=True, frozen=True)
class FilterRule:
    """
    Repository filtre kuralı.

    Örnek:
        FilterRule(
            field="ad",
            operator=FilterOperator.CONTAINS,
            value="Yunus"
        )
    """

    field: str
    operator: FilterOperator
    value: Any
    second_value: Any | None = None


@dataclass(slots=True, frozen=True)
class SortRule:
    """
    Repository sıralama kuralı.

    Örnek:
        SortRule(
            field="ad",
            direction=SortDirection.ASC
        )
    """

    field: str
    direction: SortDirection = SortDirection.ASC