"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : services/makine_service.py
Açıklama   : Makine Service
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from repositories.makine_repository import MakineRepository
from validators.makine_validator import MakineValidator


class MakineService:
    """
    Makine Service
    """

    def __init__(
        self,
        repository: MakineRepository,
    ) -> None:

        self.repository = repository

    # =====================================================
    # CRUD
    # =====================================================

    def create(
        self,
        *,
        kod: str,
        ad: str,
        aciklama: str | None = None,
    ):

        MakineValidator.validate_create(
            kod=kod,
            ad=ad,
            aciklama=aciklama,
        )

        if self.repository.makine_kodu_var_mi(kod):
            raise ValueError(
                "Makine kodu zaten kayıtlı."
            )

        return self.repository.create(
            kod=kod,
            ad=ad,
            aciklama=aciklama,
        )

    def update(
        self,
        id: int,
        *,
        kod: str,
        ad: str,
        aciklama: str | None = None,
    ):

        MakineValidator.validate_id(id)

        MakineValidator.validate_update(
            kod=kod,
            ad=ad,
            aciklama=aciklama,
        )

        return self.repository.update(
            id=id,
            kod=kod,
            ad=ad,
            aciklama=aciklama,
        )

    def delete(
        self,
        id: int,
    ) -> None:

        MakineValidator.validate_delete(id)

        self.repository.soft_delete(id)

    # =====================================================
    # GET METHODS
    # =====================================================

    def get_by_id(
        self,
        id: int,
    ):

        MakineValidator.validate_id(id)

        return self.repository.get_by_id(id)

    def get_by_makine_kodu(
        self,
        kod: str,
    ):

        CommonKod = kod.strip()

        return self.repository.get_by_makine_kodu(
            CommonKod
        )

    # =====================================================
    # LİSTELER
    # =====================================================

    def get_tum_makineler(
        self,
    ):

        return self.repository.get_tum_makineler()

    # =====================================================
    # SEARCH
    # =====================================================

    def search(
        self,
        text: str,
    ):

        MakineValidator.validate_search(text)

        return self.repository.search(text)

    # =====================================================
    # KONTROLLER
    # =====================================================

    def makine_kodu_var_mi(
        self,
        kod: str,
    ):

        return self.repository.makine_kodu_var_mi(
            kod
        )

    # =====================================================
    # İSTATİSTİKLER
    # =====================================================

    def toplam_makine(
        self,
    ):

        return self.repository.toplam_makine()