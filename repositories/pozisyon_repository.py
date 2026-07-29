"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : repositories/pozisyon_repository.py
Açıklama   : Pozisyon Repository
Yazar      : Yunus Durnagöl
Sürüm      : 2.0.0
---------------------------------------------------------
"""

from sqlalchemy.orm import Session

from orm.pozisyon import Pozisyon
from repositories.base_repository import BaseRepository


class PozisyonRepository(BaseRepository[Pozisyon]):
    """
    Pozisyon Repository
    """

    def __init__(
        self,
        session: Session,
    ) -> None:

        super().__init__(
            session=session,
            model=Pozisyon,
        )

    # =====================================================
    # GET METHODS
    # =====================================================

    def get_by_ad(
        self,
        ad: str,
    ) -> Pozisyon | None:

        return self.get(
            ad=ad,
        )

    # =====================================================
    # SEARCH
    # =====================================================

    def search(
        self,
        text: str,
    ) -> list[Pozisyon]:

        stmt = (
            self.active_stmt()
            .where(
                Pozisyon.ad.ilike(f"%{text}%")
            )
            .order_by(
                Pozisyon.ad
            )
        )

        return self.all(stmt)

    # =====================================================
    # KONTROLLER
    # =====================================================

    def ad_var_mi(
        self,
        ad: str,
    ) -> bool:

        return self.exists(
            Pozisyon.ad == ad
        )

    # =====================================================
    # İSTATİSTİKLER
    # =====================================================

    def toplam_pozisyon(
        self,
    ) -> int:

        return self.count()