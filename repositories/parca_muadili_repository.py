"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : repositories/parca_muadili_repository.py
Açıklama   : Parça Muadili Repository
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from sqlalchemy import or_
from sqlalchemy.orm import Session

from orm.parca_muadili import ParcaMuadili
from repositories.base_repository import BaseRepository


class ParcaMuadiliRepository(BaseRepository[ParcaMuadili]):
    """
    Parça Muadili Repository
    """

    def __init__(
        self,
        session: Session,
    ) -> None:

        super().__init__(
            session=session,
            model=ParcaMuadili,
        )

    # =====================================================
    # GET METHODS
    # =====================================================

    def get_by_parca(
        self,
        parca_id: int,
    ) -> list[ParcaMuadili]:

        stmt = (
            self.active_stmt()
            .where(
                ParcaMuadili.parca_id == parca_id
            )
            .order_by(
                ParcaMuadili.id
            )
        )

        return self.all(stmt)

    def get_by_muadil_parca(
        self,
        muadil_parca_id: int,
    ) -> list[ParcaMuadili]:

        stmt = (
            self.active_stmt()
            .where(
                ParcaMuadili.muadil_parca_id == muadil_parca_id
            )
            .order_by(
                ParcaMuadili.id
            )
        )

        return self.all(stmt)

    # =====================================================
    # SEARCH
    # =====================================================

    def search(
        self,
        parca_id: int,
    ) -> list[ParcaMuadili]:

        stmt = (
            self.active_stmt()
            .where(
                or_(
                    ParcaMuadili.parca_id == parca_id,
                    ParcaMuadili.muadil_parca_id == parca_id,
                )
            )
            .order_by(
                ParcaMuadili.id
            )
        )

        return self.all(stmt)

    # =====================================================
    # KONTROLLER
    # =====================================================

    def muadil_var_mi(
        self,
        parca_id: int,
        muadil_parca_id: int,
    ) -> bool:

        return self.exists(
            ParcaMuadili.parca_id == parca_id,
            ParcaMuadili.muadil_parca_id == muadil_parca_id,
        )

    # =====================================================
    # İSTATİSTİKLER
    # =====================================================

    def toplam_muadil(
        self,
    ) -> int:

        return self.count()

    def parca_muadil_sayisi(
        self,
        parca_id: int,
    ) -> int:

        return self.count(
            ParcaMuadili.parca_id == parca_id
        )