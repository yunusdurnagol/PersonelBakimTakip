"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : services/personel_izin_service.py
Açıklama   : Personel İzin Service
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from datetime import date

from orm.personel_izin import PersonelIzin
from repositories.personel_izin_repository import (
    PersonelIzinRepository,
)
from services.base_service import BaseService


class PersonelIzinService(
    BaseService[PersonelIzin]
):
    """
    Personel İzin Service
    """

    def __init__(
        self,
        repository: PersonelIzinRepository,
    ) -> None:

        super().__init__(repository)

    # =====================================================
    # GET METHODS
    # =====================================================

    def get_by_personel(
        self,
        personel_id: int,
    ) -> list[PersonelIzin]:

        return self.repository.get_by_personel(
            personel_id,
        )

    # =====================================================
    # TARİH
    # =====================================================

    def get_by_tarih(
        self,
        tarih: date,
    ) -> list[PersonelIzin]:

        return self.repository.get_by_tarih(
            tarih,
        )

    # =====================================================
    # SEARCH
    # =====================================================

    def search(
        self,
        text: str,
    ) -> list[PersonelIzin]:

        return self.repository.search(
            text,
        )

    # =====================================================
    # KONTROLLER
    # =====================================================

    def personel_izin_var_mi(
        self,
        personel_id: int,
    ) -> bool:

        return self.repository.personel_izin_var_mi(
            personel_id,
        )

    # =====================================================
    # İSTATİSTİKLER
    # =====================================================

    def toplam_izin(
        self,
    ) -> int:

        return self.repository.toplam_izin()