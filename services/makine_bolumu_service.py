"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : services/makine_bolumu_service.py
Açıklama   : Makine Bölümü Service
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from orm.makine_bolumu import MakineBolumu
from repositories.makine_bolumu_repository import MakineBolumuRepository
from services.base_service import BaseService


class MakineBolumuService(BaseService[MakineBolumu]):
    """
    Makine Bölümü Service
    """

    def __init__(
        self,
        repository: MakineBolumuRepository,
    ) -> None:

        super().__init__(repository)

    # =====================================================
    # GET METHODS
    # =====================================================

    def get_by_ad(
        self,
        ad: str,
    ) -> MakineBolumu | None:

        return self.repository.get_by_ad(ad)

    # =====================================================
    # KONTROLLER
    # =====================================================

    def ad_var_mi(
        self,
        ad: str,
    ) -> bool:

        return self.repository.ad_var_mi(ad)

    # =====================================================
    # İSTATİSTİKLER
    # =====================================================

    def toplam_bolum(
        self,
    ) -> int:

        return self.repository.toplam_bolum()