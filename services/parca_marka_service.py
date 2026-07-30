"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : services/parca_marka_service.py
Açıklama   : Parça Marka Service
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from orm.parca_marka import ParcaMarka
from repositories.parca_marka_repository import ParcaMarkaRepository
from services.base_service import BaseService


class ParcaMarkaService(BaseService[ParcaMarka]):
    """
    Parça Marka Service
    """

    def __init__(
        self,
        repository: ParcaMarkaRepository,
    ) -> None:

        super().__init__(repository)

    # =====================================================
    # GET METHODS
    # =====================================================

    def get_by_marka_adi(
        self,
        ad: str,
    ) -> ParcaMarka | None:

        return self.repository.get_by_marka_adi(ad)

    # =====================================================
    # SEARCH
    # =====================================================

    def search(
        self,
        text: str,
    ) -> list[ParcaMarka]:

        return self.repository.search(text)

    # =====================================================
    # KONTROLLER
    # =====================================================

    def marka_var_mi(
        self,
        ad: str,
    ) -> bool:

        return self.repository.marka_var_mi(ad)

    # =====================================================
    # İSTATİSTİKLER
    # =====================================================

    def toplam_marka(
        self,
    ) -> int:

        return self.repository.toplam_marka()