"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : services/parca_service.py
Açıklama   : Parça Service
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from repositories.parca_repository import ParcaRepository
from services.base_service import BaseService
from orm.parca import Parca


class ParcaService(BaseService[Parca]):
    """
    Parça Service
    """

    def __init__(
        self,
        repository: ParcaRepository,
    ) -> None:

        super().__init__(repository)

        self.repository = repository

    # =====================================================
    # GET METHODS
    # =====================================================

    def get_by_stok_kodu(
        self,
        stok_kodu: str,
    ) -> Parca | None:

        return self.repository.get_by_stok_kodu(
            stok_kodu
        )

    def get_by_orijinal_kod(
        self,
        orijinal_kod: str,
    ) -> Parca | None:

        return self.repository.get_by_orijinal_kod(
            orijinal_kod
        )

    # =====================================================
    # LİSTELEME
    # =====================================================

    def get_by_kategori(
        self,
        kategori_id: int,
    ) -> list[Parca]:

        return self.repository.get_by_kategori(
            kategori_id
        )

    def get_by_marka(
        self,
        marka_id: int,
    ) -> list[Parca]:

        return self.repository.get_by_marka(
            marka_id
        )

    def get_by_tedarikci(
        self,
        tedarikci_id: int,
    ) -> list[Parca]:

        return self.repository.get_by_tedarikci(
            tedarikci_id
        )

    # =====================================================
    # RELATIONS
    # =====================================================

    def get_with_relations(
        self,
        parca_id: int,
    ) -> Parca | None:

        return self.repository.get_with_relations(
            parca_id
        )

    # =====================================================
    # SEARCH
    # =====================================================

    def search(
        self,
        text: str,
    ) -> list[Parca]:

        return self.repository.search(
            text
        )

    # =====================================================
    # KONTROLLER
    # =====================================================

    def stok_kodu_var_mi(
        self,
        stok_kodu: str,
    ) -> bool:

        return self.repository.stok_kodu_var_mi(
            stok_kodu
        )

    def orijinal_kod_var_mi(
        self,
        orijinal_kod: str,
    ) -> bool:

        return self.repository.orijinal_kod_var_mi(
            orijinal_kod
        )

    # =====================================================
    # İSTATİSTİKLER
    # =====================================================

    def toplam_parca(
        self,
    ) -> int:

        return self.repository.toplam_parca()

    def kategoriye_gore_adet(
        self,
        kategori_id: int,
    ) -> int:

        return self.repository.kategoriye_gore_adet(
            kategori_id
        )

    def markaya_gore_adet(
        self,
        marka_id: int,
    ) -> int:

        return self.repository.markaya_gore_adet(
            marka_id
        )

    def tedarikciye_gore_adet(
        self,
        tedarikci_id: int,
    ) -> int:

        return self.repository.tedarikciye_gore_adet(
            tedarikci_id
        )