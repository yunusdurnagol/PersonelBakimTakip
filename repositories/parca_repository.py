"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : repositories/parca_repository.py
Açıklama   : Parça Repository
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from sqlalchemy import or_
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from orm.parca import Parca
from repositories.base_repository import BaseRepository


class ParcaRepository(BaseRepository[Parca]):
    """
    Parça Repository
    """

    def __init__(
        self,
        session: Session,
    ) -> None:

        super().__init__(
            session=session,
            model=Parca,
        )

    # =====================================================
    # GET METHODS
    # =====================================================

    def get_by_parca_kodu(
        self,
        parca_kodu: str,
    ) -> Parca | None:

        return self.get(
            parca_kodu=parca_kodu,
        )

    def get_by_barkod(
        self,
        barkod: str,
    ) -> Parca | None:

        return self.get(
            barkod=barkod,
        )

    # =====================================================
    # LİSTELEME
    # =====================================================

    def get_by_kategori(
        self,
        kategori_id: int,
    ) -> list[Parca]:

        stmt = (
            self.active_stmt()
            .where(
                Parca.kategori_id == kategori_id
            )
            .order_by(
                Parca.parca_adi
            )
        )

        return self.all(stmt)

    def get_by_marka(
        self,
        marka_id: int,
    ) -> list[Parca]:

        stmt = (
            self.active_stmt()
            .where(
                Parca.marka_id == marka_id
            )
            .order_by(
                Parca.parca_adi
            )
        )

        return self.all(stmt)

    def get_by_tedarikci(
        self,
        tedarikci_id: int,
    ) -> list[Parca]:

        stmt = (
            self.active_stmt()
            .where(
                Parca.tedarikci_id == tedarikci_id
            )
            .order_by(
                Parca.parca_adi
            )
        )

        return self.all(stmt)

    # =====================================================
    # RELATIONSHIP
    # =====================================================

    def get_with_relations(
        self,
        parca_id: int,
    ) -> Parca | None:

        stmt = (
            self.stmt()
            .options(
                joinedload(Parca.kategori),
                joinedload(Parca.marka),
                joinedload(Parca.tedarikci),
            )
            .where(
                Parca.id == parca_id
            )
            .where(
                Parca.is_deleted.is_(False)
            )
        )

        return self.one(stmt)

    # =====================================================
    # SEARCH
    # =====================================================

    def search(
        self,
        text: str,
    ) -> list[Parca]:

        stmt = (
            self.active_stmt()
            .where(
                or_(
                    Parca.parca_kodu.ilike(f"%{text}%"),
                    Parca.parca_adi.ilike(f"%{text}%"),
                    Parca.barkod.ilike(f"%{text}%"),
                )
            )
            .order_by(
                Parca.parca_adi
            )
        )

        return self.all(stmt)