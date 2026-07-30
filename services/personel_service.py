"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : services/personel_service.py
Açıklama   : Personel Service
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from datetime import date

from repositories.personel_repository import PersonelRepository
from services.base_service import BaseService
from orm.personel import Personel
 

class PersonelService(BaseService):

    def __init__(
        self,
        repository: PersonelRepository,
    ):
        super().__init__(repository)

        self.repository = repository

    # =====================================================
    # GET METHODS
    # =====================================================

    def get_by_sicil_no(
        self,
        sicil_no: str,
    ) -> Personel | None:

        return self.repository.get_by_sicil_no(
            sicil_no,
        )

    def get_by_tc_kimlik_no(
        self,
        tc_kimlik_no: str,
    ) -> Personel | None:

        return self.repository.get_by_tc_kimlik_no(
            tc_kimlik_no,
        )

    def get_by_iban(
        self,
        iban: str,
    ) -> Personel | None:

        return self.repository.get_by_iban(
            iban,
        )

    # =====================================================
    # PERSONEL LİSTELERİ
    # =====================================================

    def get_by_pozisyon(
        self,
        pozisyon_id: int,
    ) -> list[Personel]:

        return self.repository.get_by_pozisyon(
            pozisyon_id,
        )

    def get_aktif_personeller(
        self,
    ) -> list[Personel]:

        return self.repository.get_aktif_personeller()

    # =====================================================
    # SEARCH
    # =====================================================

    def search(
        self,
        text: str,
    ) -> list[Personel]:

        return self.repository.search(
            text,
        )

    def toplam_aktif_personel(
        self,
    ) -> int:

        return self.repository.toplam_aktif_personel()

    # =====================================================
    # DOĞUM GÜNÜ
    # =====================================================

    def dogum_gunu_olanlar(
        self,
        tarih: date | None = None,
    ) -> list[Personel]:

        return self.repository.dogum_gunu_olanlar(
            tarih,
        )

    # =====================================================
    # İŞE YENİ BAŞLAYANLAR
    # =====================================================

    def ise_yeni_baslayanlar(
        self,
        gun: int = 30,
    ) -> list[Personel]:

        return self.repository.ise_yeni_baslayanlar(
            gun,
        )

    # =====================================================
    # YAKLAŞAN İZİN HAKKI
    # =====================================================

    def yaklasan_izin_hakki(
        self,
        gun: int = 30,
    ) -> list[Personel]:

        return self.repository.yaklasan_izin_hakki(
            gun,
        )

    # =====================================================
    # KONTROLLER
    # =====================================================

    def sicil_no_var_mi(
        self,
        sicil_no: str,
    ) -> bool:

        return self.repository.sicil_no_var_mi(
            sicil_no,
        )

    def tc_var_mi(
        self,
        tc_kimlik_no: str,
    ) -> bool:

        return self.repository.tc_var_mi(
            tc_kimlik_no,
        )

    def iban_var_mi(
        self,
        iban: str,
    ) -> bool:

        return self.repository.iban_var_mi(
            iban,
        )

    # =====================================================
    # İSTATİSTİKLER
    # =====================================================

    def toplam_personel(
        self,
    ) -> int:

        return self.repository.toplam_personel()