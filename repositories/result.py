"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : repositories/result.py
Açıklama   : Repository Sonuç Modelleri
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from dataclasses import dataclass
from math import ceil
from typing import Generic
from typing import TypeVar

T = TypeVar("T")


@dataclass(slots=True)
class PagedResult(Generic[T]):
    """
    Sayfalı sorgu sonucu.
    """

    items: list[T]

    total_count: int

    page: int

    page_size: int

    @property
    def total_pages(self) -> int:
        if self.page_size == 0:
            return 0

        return ceil(self.total_count / self.page_size)

    @property
    def has_next(self) -> bool:
        return self.page < self.total_pages

    @property
    def has_previous(self) -> bool:
        return self.page > 1