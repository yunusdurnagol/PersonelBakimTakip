"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : services/parca_hareket_service.py
Açıklama   : Parça Hareket Service
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from repositories.parca_hareket_repository import ParcaHareketRepository
from services.base_service import BaseService


class ParcaHareketService(BaseService):
    """
    Parça Hareket Service
    """

    def __init__(
        self,
        repository: ParcaHareketRepository,
    ) -> None:

        super().__init__(repository)

    # =====================================================
    # GET METHODS
    # =====================================================

    def get_by_fatura_no(
        self,
        fatura_no: str,
    ):
        return self.repository.get_by_fatura_no(
            fatura_no,
        )

    # =====================================================
    # LİSTELEME
    # =====================================================

    def get_by_parca(
        self,
        parca_id: int,
    ):
        return self.repository.get_by_parca(
            parca_id,
        )

    def get_by_makine_bolumu(
        self,
        makine_bolumu_id: int,
    ):
        return self.repository.get_by_makine_bolumu(
            makine_bolumu_id,
        )

    def get_by_tedarikci(
        self,
        tedarikci_id: int,
    ):
        return self.repository.get_by_tedarikci(
            tedarikci_id,
        )

    def get_by_tarih(
        self,
        tarih,
    ):
        return self.repository.get_by_tarih(
            tarih,
        )

    # =====================================================
    # RELATIONS
    # =====================================================

    def get_with_relations(
        self,
        hareket_id: int,
    ):
        return self.repository.get_with_relations(
            hareket_id,
        )

    # =====================================================
    # KONTROLLER
    # =====================================================

    def fatura_no_var_mi(
        self,
        fatura_no: str,
    ):
        return self.repository.fatura_no_var_mi(
            fatura_no,
        )

    # =====================================================
    # İSTATİSTİKLER
    # =====================================================

    def toplam_hareket(self):
        return self.repository.toplam_hareket()

    def parcaya_gore_adet(
        self,
        parca_id: int,
    ):
        return self.repository.parcaya_gore_adet(
            parca_id,
        )

    def makine_bolumune_gore_adet(
        self,
        makine_bolumu_id: int,
    ):
        return self.repository.makine_bolumune_gore_adet(
            makine_bolumu_id,
        )

    def tedarikciye_gore_adet(
        self,
        tedarikci_id: int,
    ):
        return self.repository.tedarikciye_gore_adet(
            tedarikci_id,
        )