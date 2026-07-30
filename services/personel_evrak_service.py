"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : services/personel_evrak_service.py
Açıklama   : Personel Evrak Service
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from orm.personel_evrak import PersonelEvrak
from repositories.personel_evrak_repository import (
    PersonelEvrakRepository,
)
from services.base_service import BaseService


class PersonelEvrakService(
    BaseService[PersonelEvrak]
):
    """
    Personel Evrak Service
    """

    def __init__(
        self,
        repository: PersonelEvrakRepository,
    ) -> None:

        super().__init__(repository)

    # =====================================================
    # GET METHODS
    # =====================================================

    def get_by_personel(
        self,
        personel_id: int,
    ) -> list[PersonelEvrak]:

        return self.repository.get_by_personel(
            personel_id,
        )

    def get_by_evrak_adi(
        self,
        evrak_adi: str,
    ) -> PersonelEvrak | None:

        return self.repository.get_by_evrak_adi(
            evrak_adi,
        )

    # =====================================================
    # SEARCH
    # =====================================================

    def search(
        self,
        text: str,
    ) -> list[PersonelEvrak]:

        return self.repository.search(
            text,
        )

    # =====================================================
    # KONTROLLER
    # =====================================================

    def evrak_var_mi(
        self,
        personel_id: int,
        evrak_adi: str,
    ) -> bool:

        return self.repository.evrak_var_mi(
            personel_id,
            evrak_adi,
        )

    # =====================================================
    # İSTATİSTİKLER
    # =====================================================

    def toplam_evrak(
        self,
    ) -> int:

        return self.repository.toplam_evrak()

    def personele_gore_evrak_sayisi(
        self,
        personel_id: int,
    ) -> int:

        return self.repository.personele_gore_evrak_sayisi(
            personel_id,
        )