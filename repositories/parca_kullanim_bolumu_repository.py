"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : repositories/parca_kullanim_bolumu_repository.py
Açıklama   : Parça Kullanım Bölümü Repository
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from sqlalchemy import or_
from sqlalchemy.orm import Session

from orm.parca_kullanim_bolumu import ParcaKullanimBolumu
from repositories.base_repository import BaseRepository


class ParcaKullanimBolumuRepository(
    BaseRepository[ParcaKullanimBolumu]
):
    """
    Parça Kullanım Bölümü Repository
    """

    def __init__(
        self,
        session: Session,
    ) -> None:

        super().__init__(
            session=session,
            model=ParcaKullanimBolumu,
        )

    # =====================================================
    # GET METHODS
    # =====================================================

    def get_by_parca(
        self,
        parca_id: int,
    ) -> list[ParcaKullanimBolumu]:

        stmt = (
            self.active_stmt()
            .where(
                ParcaKullanimBolumu.parca_id == parca_id
            )
            .order_by(
                ParcaKullanimBolumu.id
            )
        )

        return self.all(stmt)

    def get_by_bolum(
        self,
        makine_bolumu_id: int,
    ) -> list[ParcaKullanimBolumu]:

        stmt = (
            self.active_stmt()
            .where(
                ParcaKullanimBolumu.makine_bolumu_id
                == makine_bolumu_id
            )
            .order_by(
                ParcaKullanimBolumu.id
            )
        )

        return self.all(stmt)

    # =====================================================
    # SEARCH
    # =====================================================

    def search(
        self,
        text: str,
    ) -> list[ParcaKullanimBolumu]:

        stmt = (
            self.active_stmt()
            .where(
                ParcaKullanimBolumu.aciklama.ilike(
                    f"%{text}%"
                )
            )
            .order_by(
                ParcaKullanimBolumu.id
            )
        )

        return self.all(stmt)

    # =====================================================
    # KONTROLLER
    # =====================================================

    def kullanim_var_mi(
        self,
        parca_id: int,
        makine_bolumu_id: int,
    ) -> bool:

        return self.exists(
            ParcaKullanimBolumu.parca_id == parca_id,
            ParcaKullanimBolumu.makine_bolumu_id
            == makine_bolumu_id,
        )

    # =====================================================
    # İSTATİSTİKLER
    # =====================================================

    def toplam_kullanim(
        self,
    ) -> int:

        return self.count()

    def parca_kullanim_sayisi(
        self,
        parca_id: int,
    ) -> int:

        return self.count(
            ParcaKullanimBolumu.parca_id == parca_id
        )

    def bolum_kullanim_sayisi(
        self,
        makine_bolumu_id: int,
    ) -> int:

        return self.count(
            ParcaKullanimBolumu.makine_bolumu_id
            == makine_bolumu_id
        )