"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : repositories/makine_bolumu_repository.py
Açıklama   : Makine Bölümü Repository
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from sqlalchemy.orm import Session

from orm.makine_bolumu import MakineBolumu
from repositories.base_repository import BaseRepository


class MakineBolumuRepository(BaseRepository[MakineBolumu]):
    """
    Makine Bölümü Repository
    """

    def __init__(
        self,
        session: Session,
    ) -> None:

        super().__init__(
            session=session,
            model=MakineBolumu,
        )

    # =====================================================
    # GET METHODS
    # =====================================================

    def get_by_ad(
        self,
        bolum_adi: str,
    ) -> MakineBolumu | None:

        return self.get(
            bolum_adi=bolum_adi,
        )

    # =====================================================
    # KONTROLLER
    # =====================================================

    def ad_var_mi(
        self,
        bolum_adi: str,
    ) -> bool:

        return self.exists(
            MakineBolumu.bolum_adi == bolum_adi
        )

    # =====================================================
    # İSTATİSTİKLER
    # =====================================================

    def toplam_bolum(
        self,
    ) -> int:

        return self.count()