"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : repositories/personel_evrak_repository.py
Açıklama   : Personel Evrak Repository
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from sqlalchemy.orm import Session

from orm.personel_evrak import PersonelEvrak
from repositories.base_repository import BaseRepository


class PersonelEvrakRepository(
    BaseRepository[PersonelEvrak]
):
    """
    Personel Evrak Repository
    """

    def __init__(
        self,
        session: Session,
    ) -> None:

        super().__init__(
            session=session,
            model=PersonelEvrak,
        )

    # =====================================================
    # GET METHODS
    # =====================================================

    def get_by_personel(
        self,
        personel_id: int,
    ) -> list[PersonelEvrak]:

        stmt = (
            self.active_stmt()
            .where(
                PersonelEvrak.personel_id == personel_id
            )
            .order_by(
                PersonelEvrak.evrak_adi
            )
        )

        return self.all(stmt)

    def get_by_evrak_adi(
        self,
        evrak_adi: str,
    ) -> PersonelEvrak | None:

        return self.get(
            evrak_adi=evrak_adi,
        )

    # =====================================================
    # SEARCH
    # =====================================================

    def search(
        self,
        text: str,
    ) -> list[PersonelEvrak]:

        stmt = (
            self.active_stmt()
            .where(
                PersonelEvrak.evrak_adi.ilike(
                    f"%{text}%"
                )
            )
            .order_by(
                PersonelEvrak.evrak_adi
            )
        )

        return self.all(stmt)

    # =====================================================
    # KONTROLLER
    # =====================================================

    def evrak_var_mi(
        self,
        personel_id: int,
        evrak_adi: str,
    ) -> bool:

        return self.exists(
            PersonelEvrak.personel_id == personel_id,
            PersonelEvrak.evrak_adi == evrak_adi,
        )

    # =====================================================
    # İSTATİSTİKLER
    # =====================================================

    def toplam_evrak(
        self,
    ) -> int:

        return self.count()

    def personele_gore_evrak_sayisi(
        self,
        personel_id: int,
    ) -> int:

        return self.count(
            PersonelEvrak.personel_id == personel_id
        )