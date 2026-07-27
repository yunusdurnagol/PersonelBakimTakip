"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : repositories/personel_repository.py
Açıklama   : Personel Repository
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from orm.personel import Personel

from repositories.base_repository import BaseRepository


class PersonelRepository(
    BaseRepository[Personel]
):
    """
    Personel Repository
    """

    def __init__(
        self,
        session: Session,
    ) -> None:

        super().__init__(
            session=session,
            model=Personel,
        )

    # ---------------------------------------------------------
    # Sicil No
    # ---------------------------------------------------------

    def get_by_sicil_no(
        self,
        sicil_no: str,
    ) -> Personel | None:

        statement = (
            select(Personel)
            .where(
                Personel.sicil_no == sicil_no,
                Personel.is_deleted == False,
            )
        )

        return self.session.scalar(statement)

    # ---------------------------------------------------------
    # TC Kimlik No
    # ---------------------------------------------------------

    def get_by_tc(
        self,
        tc: str,
    ) -> Personel | None:

        statement = (
            select(Personel)
            .where(
                Personel.tc_kimlik_no == tc,
                Personel.is_deleted == False,
            )
        )

        return self.session.scalar(statement)

    # ---------------------------------------------------------
    # Ada Göre Arama
    # ---------------------------------------------------------

    def search_by_name(
        self,
        text: str,
    ) -> list[Personel]:

        statement = (
            select(Personel)
            .where(
                Personel.ad.ilike(f"%{text}%"),
                Personel.is_deleted == False,
            )
            .order_by(
                Personel.ad,
            )
        )

        return list(
            self.session.scalars(statement)
        )

    # ---------------------------------------------------------
    # Soyada Göre Arama
    # ---------------------------------------------------------

    def search_by_surname(
        self,
        text: str,
    ) -> list[Personel]:

        statement = (
            select(Personel)
            .where(
                Personel.soyad.ilike(f"%{text}%"),
                Personel.is_deleted == False,
            )
            .order_by(
                Personel.soyad,
            )
        )

        return list(
            self.session.scalars(statement)
        )

    # ---------------------------------------------------------
    # Ad Soyad
    # ---------------------------------------------------------

    def search(
        self,
        text: str,
    ) -> list[Personel]:

        statement = (
            select(Personel)
            .where(
                (
                    Personel.ad.ilike(f"%{text}%")
                )
                |
                (
                    Personel.soyad.ilike(f"%{text}%")
                ),
                Personel.is_deleted == False,
            )
            .order_by(
                Personel.ad,
                Personel.soyad,
            )
        )

        return list(
            self.session.scalars(statement)
        )