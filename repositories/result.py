"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : repositories/result.py
Açıklama   : Repository Sonuç Modelleri
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from dataclasses import dataclass
from math import ceil
from typing import Generic
from typing import TypeVar

T = TypeVar("T")


@dataclass(slots=True)
class PagedResult(Generic[T]):
    """
    Sayfalı sorgu sonucu.

    Attributes
    ----------
    items : list[T]
        Dönen kayıtlar.

    total_count : int
        Toplam kayıt sayısı.

    page : int
        Mevcut sayfa.

    page_size : int
        Sayfa başına kayıt sayısı.
    """

    items: list[T]

    total_count: int

    page: int

    page_size: int

    @property
    def total_pages(self) -> int:
        """
        Toplam sayfa sayısı.
        """

        if self.page_size <= 0:
            return 0

        return ceil(self.total_count / self.page_size)

    @property
    def has_previous(self) -> bool:
        """
        Önceki sayfa var mı?
        """

        return self.page > 1

    @property
    def has_next(self) -> bool:
        """
        Sonraki sayfa var mı?
        """

        return self.page < self.total_pages

    @property
    def is_empty(self) -> bool:
        """
        Sonuç boş mu?
        """

        return len(self.items) == 0

    def __len__(self) -> int:
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index: int) -> T:
        return self.items[index]