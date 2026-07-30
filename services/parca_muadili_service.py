"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : services/parca_muadili_service.py
Açıklama   : Parça Muadili Service
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from orm.parca_muadili import ParcaMuadili
from repositories.parca_muadili_repository import (
    ParcaMuadiliRepository,
)
from services.base_service import BaseService


class ParcaMuadiliService(
    BaseService[ParcaMuadili]
):
    """
    Parça Muadili Service
    """

    def __init__(
        self,
        repository: ParcaMuadiliRepository,
    ) -> None:

        super().__init__(repository)

    # =====================================================
    # GET METHODS
    # =====================================================

    def get_by_parca(
        self,
        parca_id: int,
    ) -> list[ParcaMuadili]:

        return self.repository.get_by_parca(
            parca_id,
        )

    def get_by_muadil_parca(
        self,
        muadil_parca_id: int,
    ) -> list[ParcaMuadili]:

        return self.repository.get_by_muadil_parca(
            muadil_parca_id,
        )

    # =====================================================
    # SEARCH
    # =====================================================

    def search(
        self,
        parca_id: int,
    ) -> list[ParcaMuadili]:

        return self.repository.search(
            parca_id,
        )

    # =====================================================
    # KONTROLLER
    # =====================================================

    def muadil_var_mi(
        self,
        parca_id: int,
        muadil_parca_id: int,
    ) -> bool:

        return self.repository.muadil_var_mi(
            parca_id,
            muadil_parca_id,
        )

    # =====================================================
    # İSTATİSTİKLER
    # =====================================================

    def toplam_muadil(
        self,
    ) -> int:

        return self.repository.toplam_muadil()

    def parca_muadil_sayisi(
        self,
        parca_id: int,
    ) -> int:

        return self.repository.parca_muadil_sayisi(
            parca_id,
        )