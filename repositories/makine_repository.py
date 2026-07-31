"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : repositories/makine_repository.py
Açıklama   : Makine Repository
Yazar      : Yunus Durnagöl
Sürüm      : 2.0.0
---------------------------------------------------------
"""

from sqlalchemy import or_
from sqlalchemy.orm import Session

from orm.makine import Makine
from repositories.base_repository import BaseRepository


class MakineRepository(BaseRepository[Makine]):
    """
    Makine Repository
    """

    def __init__(
        self,
        session: Session,
    ) -> None:

        super().__init__(
            session=session,
            model=Makine,
        )

    # =====================================================
    # GET METHODS
    # =====================================================

    def get_by_makine_kodu(
        self,
        kod: str,
    ) -> Makine | None:

        return self.get(
            kod=kod,
        )

    # =====================================================
    # LİSTELER
    # =====================================================

    def get_tum_makineler(
        self,
    ) -> list[Makine]:

        stmt = (
            self.active_stmt()
            .order_by(
                Makine.kod
            )
        )

        return self.all(stmt)

    # =====================================================
    # SEARCH
    # =====================================================

    def search(
        self,
        text: str,
    ) -> list[Makine]:

        stmt = (
            self.active_stmt()
            .where(
                or_(
                    Makine.kod.ilike(f"%{text}%"),
                    Makine.ad.ilike(f"%{text}%"),
                )
            )
            .order_by(
                Makine.kod
            )
        )

        return self.all(stmt)

    # =====================================================
    # KONTROLLER
    # =====================================================

    def makine_kodu_var_mi(
        self,
        kod: str,
    ) -> bool:

        return self.exists(
            Makine.kod == kod
        )

    # =====================================================
    # İSTATİSTİKLER
    # =====================================================

    def toplam_makine(
        self,
    ) -> int:

        return self.count()