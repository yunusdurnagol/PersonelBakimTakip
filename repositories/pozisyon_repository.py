
"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : repositories/pozisyon_repository.py
Açıklama   : Pozisyon Repository
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from sqlalchemy import or_
from sqlalchemy.orm import Session

from orm.pozisyon import Pozisyon
from repositories.base_repository import BaseRepository


class PozisyonRepository(BaseRepository[Pozisyon]):
    """
    Pozisyon veritabanı işlemleri.
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
    # GET
    # =====================================================

    def get_by_ad(
        self,
        ad: str,
    ) -> Pozisyon | None:

        return self.get(
            ad=ad,
        )

    # =====================================================
    # TÜM POZİSYONLAR
    # =====================================================

    def get_tum_pozisyonlar(
        self,
    ) -> list[Pozisyon]:

        stmt = (
            self.active_stmt()
            .order_by(
                Pozisyon.ad.asc()
            )
        )

        return self.all(stmt)

    # =====================================================
    # SEARCH
    # =====================================================

    def search(
        self,
        text: str,
    ) -> list[Pozisyon]:

        text = text.strip()

        if not text:
            return self.get_tum_pozisyonlar()

        stmt = (
            self.active_stmt()
            .where(
                Pozisyon.ad.ilike(
                    f"%{text}%"
                )
            )
            .order_by(
                Pozisyon.ad.asc()
            )
        )

        return self.all(stmt)

    # =====================================================
    # KONTROL
    # =====================================================

    def ad_var_mi(
        self,
        ad: str,
    ) -> bool:

        return self.exists(
            Pozisyon.ad == ad
        )

    # =====================================================
    # İSTATİSTİK
    # =====================================================

    def toplam_pozisyon(self) -> int:

        return self.count_stmt(
            self.active_stmt()
        )
 
