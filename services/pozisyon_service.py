"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : services/pozisyon_service.py
Açıklama   : Pozisyon Service
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from orm.pozisyon import Pozisyon
from repositories.pozisyon_repository import PozisyonRepository
from services.base_service import BaseService


class PozisyonService(BaseService[Pozisyon]):
    """
    Pozisyon Service
    """

    def __init__(
        self,
        repository: PozisyonRepository,
    ) -> None:

        super().__init__(repository)

    # =====================================================
    # GET METHODS
    # =====================================================

    def get_by_ad(
        self,
        ad: str,
    ) -> Pozisyon | None:

        return self.repository.get_by_ad(ad)

    # =====================================================
    # SEARCH
    # =====================================================

    def search(
        self,
        text: str,
    ) -> list[Pozisyon]:

        return self.repository.search(text)

    # =====================================================
    # KONTROLLER
    # =====================================================

    def ad_var_mi(
        self,
        ad: str,
    ) -> bool:

        return self.repository.ad_var_mi(ad)

    # =====================================================
    # İSTATİSTİKLER
    # =====================================================

    def toplam_pozisyon(
        self,
    ) -> int:

        return self.repository.toplam_pozisyon()