 
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


class PozisyonService:
    """
    Pozisyon işlemlerinin servis katmanı.

    UI katmanı bu sınıf üzerinden pozisyon verilerine erişir.
    """

    def __init__(
        self,
        repository: PozisyonRepository,
    ) -> None:

        self.repository = repository

    # =====================================================
    # GET
    # =====================================================

    def get_by_id(
        self,
        pozisyon_id: int,
    ) -> Pozisyon | None:

        return self.repository.get_by_id(
            pozisyon_id
        )

    # =====================================================
    # TÜM POZİSYONLAR
    # =====================================================

    def get_tum_pozisyonlar(
        self,
    ) -> list[Pozisyon]:

        return self.repository.get_tum_pozisyonlar()

    # =====================================================
    # AKTİF POZİSYONLAR
    # =====================================================

    def get_aktif_pozisyonlar(
        self,
    ) -> list[Pozisyon]:

        return self.repository.get_tum_pozisyonlar()

    # =====================================================
    # POZİSYON BUL
    # =====================================================

    def get_by_ad(
        self,
        ad: str,
    ) -> Pozisyon | None:

        return self.repository.get_by_ad(
            ad.strip()
        )

    # =====================================================
    # ARAMA
    # =====================================================

    def search(
        self,
        text: str,
    ) -> list[Pozisyon]:

        return self.repository.search(
            text.strip()
        )

    # =====================================================
    # KONTROL
    # =====================================================

    def ad_var_mi(
        self,
        ad: str,
    ) -> bool:

        return self.repository.ad_var_mi(
            ad.strip()
        )

    # =====================================================
    # İSTATİSTİK
    # =====================================================

    def toplam_pozisyon(self) -> int:

        return self.repository.toplam_pozisyon()
 
