"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : repositories/page_request.py
Açıklama   : Sayfalama Parametreleri
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from dataclasses import dataclass


@dataclass(slots=True)
class PageRequest:
    """
    Sayfalama parametreleri.
    """

    page: int = 1
    page_size: int = 25

    @property
    def offset(self) -> int:
        return (self.page - 1) * self.page_size