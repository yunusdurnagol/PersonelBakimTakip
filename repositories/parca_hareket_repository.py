"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : repositories/parca_hareket_repository.py
Açıklama   : Parça Hareket Repository
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from datetime import date

from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from orm.parca_hareket import ParcaHareket
from repositories.base_repository import BaseRepository


class ParcaHareketRepository(BaseRepository[ParcaHareket]):
    """
    Parça Hareket Repository
    """

    def __init__(
        self,
        session: Session,
    ) -> None:

        super().__init__(
            session=session,
            model=ParcaHareket,
        )

    # =====================================================
    # GET METHODS
    # =====================================================

    def get_by_fatura_no(
        self,
        fatura_no: str,
    ) -> ParcaHareket | None:

        return self.get(
            fatura_no=fatura_no,
        )

    # =====================================================
    # LİSTELEME
    # =====================================================

    def get_by_parca(
        self,
        parca_id: int,
    ) -> list[ParcaHareket]:

        stmt = (
            self.active_stmt()
            .where(
                ParcaHareket.parca_id == parca_id
            )
            .order_by(
                ParcaHareket.alis_tarihi.desc()
            )
        )

        return self.all(stmt)

    def get_by_makine_bolumu(
        self,
        makine_bolumu_id: int,
    ) -> list[ParcaHareket]:

        stmt = (
            self.active_stmt()
            .where(
                ParcaHareket.makine_bolumu_id == makine_bolumu_id
            )
            .order_by(
                ParcaHareket.alis_tarihi.desc()
            )
        )

        return self.all(stmt)

    def get_by_tedarikci(
        self,
        tedarikci_id: int,
    ) -> list[ParcaHareket]:

        stmt = (
            self.active_stmt()
            .where(
                ParcaHareket.tedarikci_id == tedarikci_id
            )
            .order_by(
                ParcaHareket.alis_tarihi.desc()
            )
        )

        return self.all(stmt)

    def get_by_tarih(
        self,
        tarih: date,
    ) -> list[ParcaHareket]:

        stmt = (
            self.active_stmt()
            .where(
                ParcaHareket.alis_tarihi == tarih
            )
            .order_by(
                ParcaHareket.id.desc()
            )
        )

        return self.all(stmt)

    # =====================================================
    # RELATIONS
    # =====================================================

    def get_with_relations(
        self,
        hareket_id: int,
    ) -> ParcaHareket | None:

        stmt = (
            select(ParcaHareket)
            .options(
                joinedload(ParcaHareket.parca),
                joinedload(ParcaHareket.tedarikci),
                joinedload(ParcaHareket.makine_bolumu),
            )
            .where(
                ParcaHareket.id == hareket_id,
                ParcaHareket.is_deleted.is_(False),
            )
        )

        return self.one(stmt)

    # =====================================================
    # KONTROLLER
    # =====================================================

    def fatura_no_var_mi(
        self,
        fatura_no: str,
    ) -> bool:

        return self.exists(
            ParcaHareket.fatura_no == fatura_no
        )

    # =====================================================
    # İSTATİSTİKLER
    # =====================================================

    def toplam_hareket(
        self,
    ) -> int:

        return self.count()

    def parcaya_gore_adet(
        self,
        parca_id: int,
    ) -> int:

        return self.count(
            ParcaHareket.parca_id == parca_id
        )

    def makine_bolumune_gore_adet(
        self,
        makine_bolumu_id: int,
    ) -> int:

        return self.count(
            ParcaHareket.makine_bolumu_id == makine_bolumu_id
        )

    def tedarikciye_gore_adet(
        self,
        tedarikci_id: int,
    ) -> int:

        return self.count(
            ParcaHareket.tedarikci_id == tedarikci_id
        )


    def son_hareketler(
    self,
    limit: int = 10,
):

        stmt = (
            self.active_stmt()
            .order_by(
                ParcaHareket.alis_tarihi.desc(),
                ParcaHareket.id.desc(),
            )
            .limit(limit)
        )

        return self.all(stmt)