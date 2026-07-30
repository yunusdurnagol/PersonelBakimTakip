"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : services/parca_kullanim_bolumu_service.py
Açıklama   : Parça Kullanım Bölümü Service
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from repositories.parca_kullanim_bolumu_repository import (
    ParcaKullanimBolumuRepository,
)
from services.base_service import BaseService
from orm.parca_kullanim_bolumu import ParcaKullanimBolumu


class ParcaKullanimBolumuService(
    BaseService[ParcaKullanimBolumu]
):
    """
    Parça Kullanım Bölümü Service
    """

    def __init__(
        self,
        repository: ParcaKullanimBolumuRepository,
    ) -> None:

        super().__init__(repository)

    # =====================================================
    # GET METHODS
    # =====================================================

    def get_by_parca(
        self,
        parca_id: int,
    ) -> list[ParcaKullanimBolumu]:

        return self.repository.get_by_parca(
            parca_id,
        )

    def get_by_bolum(
        self,
        makine_bolumu_id: int,
    ) -> list[ParcaKullanimBolumu]:

        return self.repository.get_by_bolum(
            makine_bolumu_id,
        )

    # =====================================================
    # SEARCH
    # =====================================================

    def search(
        self,
        text: str,
    ) -> list[ParcaKullanimBolumu]:

        return self.repository.search(text)

    # =====================================================
    # KONTROLLER
    # =====================================================

    def kullanim_var_mi(
        self,
        parca_id: int,
        makine_bolumu_id: int,
    ) -> bool:

        return self.repository.kullanim_var_mi(
            parca_id,
            makine_bolumu_id,
        )

    # =====================================================
    # İSTATİSTİKLER
    # =====================================================

    def toplam_kullanim(
        self,
    ) -> int:

        return self.repository.toplam_kullanim()

    def parca_kullanim_sayisi(
        self,
        parca_id: int,
    ) -> int:

        return self.repository.parca_kullanim_sayisi(
            parca_id,
        )

    def bolum_kullanim_sayisi(
        self,
        makine_bolumu_id: int,
    ) -> int:

        return self.repository.bolum_kullanim_sayisi(
            makine_bolumu_id,
        )