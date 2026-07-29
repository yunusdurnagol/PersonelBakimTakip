"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : repositories/parca_repository.py
Açıklama   : Parça Repository
Yazar      : Yunus Durnagöl
Sürüm      : 2.0.0
---------------------------------------------------------
"""

from sqlalchemy import or_
from sqlalchemy import select
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

    def get_by_stok_kodu(
        self,
        stok_kodu: str,
    ) -> Parca | None:

        return self.get(
            stok_kodu=stok_kodu,
        )

    def get_by_orijinal_kod(
        self,
        orijinal_kod: str,
    ) -> Parca | None:

        return self.get(
            orijinal_kod=orijinal_kod,
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
    # RELATIONS
    # =====================================================

    def get_with_relations(
        self,
        parca_id: int,
    ) -> Parca | None:

        stmt = (
            select(Parca)
            .options(
                joinedload(Parca.kategori),
                joinedload(Parca.marka),
                joinedload(Parca.tedarikci),
                joinedload(Parca.hareketler),
                joinedload(Parca.muadiller),
                joinedload(Parca.kullanim_bolumleri),
            )
            .where(
                Parca.id == parca_id,
                Parca.is_deleted.is_(False),
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
                    Parca.stok_kodu.ilike(f"%{text}%"),
                    Parca.orijinal_kod.ilike(f"%{text}%"),
                    Parca.parca_adi.ilike(f"%{text}%"),
                    Parca.model.ilike(f"%{text}%"),
                )
            )
            .order_by(
                Parca.parca_adi
            )
        )

        return self.all(stmt)

    # =====================================================
    # KONTROLLER
    # =====================================================

    def stok_kodu_var_mi(
        self,
        stok_kodu: str,
    ) -> bool:

        return self.exists(
            Parca.stok_kodu == stok_kodu
        )

    def orijinal_kod_var_mi(
        self,
        orijinal_kod: str,
    ) -> bool:

        return self.exists(
            Parca.orijinal_kod == orijinal_kod
        )

    # =====================================================
    # İSTATİSTİKLER
    # =====================================================

    def toplam_parca(
        self,
    ) -> int:

        return self.count()

    def kategoriye_gore_adet(
        self,
        kategori_id: int,
    ) -> int:

        return self.count(
            Parca.kategori_id == kategori_id
        )

    def markaya_gore_adet(
        self,
        marka_id: int,
    ) -> int:

        return self.count(
            Parca.marka_id == marka_id
        )

    def tedarikciye_gore_adet(
        self,
        tedarikci_id: int,
    ) -> int:

        return self.count(
            Parca.tedarikci_id == tedarikci_id
        )