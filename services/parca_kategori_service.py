"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : services/parca_kategori_service.py
Açıklama   : Parça Kategori Service
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from orm.parca_kategori import ParcaKategori
from repositories.parca_kategori_repository import ParcaKategoriRepository
from services.base_service import BaseService


class ParcaKategoriService(BaseService[ParcaKategori]):
    """
    Parça Kategori Service
    """

    def __init__(
        self,
        repository: ParcaKategoriRepository,
    ) -> None:

        super().__init__(repository)

    # =====================================================
    # GET METHODS
    # =====================================================

    def get_by_kategori_adi(
        self,
        ad: str,
    ) -> ParcaKategori | None:

        return self.repository.get_by_kategori_adi(ad)

    # =====================================================
    # SEARCH
    # =====================================================

    def search(
        self,
        text: str,
    ) -> list[ParcaKategori]:

        return self.repository.search(text)

    # =====================================================
    # KONTROLLER
    # =====================================================

    def kategori_var_mi(
        self,
        ad: str,
    ) -> bool:

        return self.repository.kategori_var_mi(ad)

    # =====================================================
    # İSTATİSTİKLER
    # =====================================================

    def toplam_kategori(
        self,
    ) -> int:

        return self.repository.toplam_kategori()