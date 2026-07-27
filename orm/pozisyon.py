"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : orm/pozisyon.py
Açıklama   : Pozisyon ORM Modeli
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from orm.base_model import BaseModel

if TYPE_CHECKING:
    from orm.personel import Personel


class Pozisyon(BaseModel):
    """
    Personel pozisyonları.

    Örnek:
        Ram Operatörü
        Sanfor Operatörü
        Planlama
        Muhasebe
    """

    __tablename__ = "pozisyonlar"

    ad: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )

    aciklama: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    personeller: Mapped[list["Personel"]] = relationship(
        back_populates="pozisyon",
        lazy="select",
    )

    def __repr__(self) -> str:

        return (
            f"<Pozisyon(id={self.id}, ad='{self.ad}')>"
        )