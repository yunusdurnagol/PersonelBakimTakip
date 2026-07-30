"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : services/tedarikci_service.py
Açıklama   : Tedarikçi Service
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from orm.tedarikci import Tedarikci
from repositories.tedarikci_repository import TedarikciRepository
from services.base_service import BaseService


class TedarikciService(BaseService[Tedarikci]):
    """
    Tedarikçi Service
    """

    def __init__(
        self,
        repository: TedarikciRepository,
    ) -> None:

        super().__init__(repository)

    # =====================================================
    # GET METHODS
    # =====================================================

    def get_by_firma_adi(
        self,
        firma_adi: str,
    ) -> Tedarikci | None:

        return self.repository.get_by_firma_adi(
            firma_adi
        )

    def get_by_vergi_no(
        self,
        vergi_no: str,
    ) -> Tedarikci | None:

        return self.repository.get_by_vergi_no(
            vergi_no
        )

    # =====================================================
    # SEARCH
    # =====================================================

    def search(
        self,
        text: str,
    ) -> list[Tedarikci]:

        return self.repository.search(text)

    # =====================================================
    # KONTROLLER
    # =====================================================

    def firma_var_mi(
        self,
        firma_adi: str,
    ) -> bool:

        return self.repository.firma_var_mi(
            firma_adi
        )

    def vergi_no_var_mi(
        self,
        vergi_no: str,
    ) -> bool:

        return self.repository.vergi_no_var_mi(
            vergi_no
        )

    # =====================================================
    # İSTATİSTİKLER
    # =====================================================

    def toplam_tedarikci(
        self,
    ) -> int:

        return self.repository.toplam_tedarikci()