"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : orm/personel_izin.py
Açıklama   : Personel izin kayıtları
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from orm.base_model import BaseModel

if TYPE_CHECKING:
    from orm.personel import Personel


class PersonelIzin(BaseModel):
    """
    Personelin kullandığı izin kayıtları.
    """

    __tablename__ = "personel_izinleri"

    personel_id: Mapped[int] = mapped_column(
        ForeignKey("personeller.id"),
        nullable=False,
    )

    baslangic_tarihi: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    bitis_tarihi: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    kullanilan_gun: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    aciklama: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    personel: Mapped["Personel"] = relationship(
        back_populates="izinler",
    )

    def __repr__(self) -> str:

        return (
            f"<PersonelIzin("
            f"id={self.id}, "
            f"personel_id={self.personel_id}, "
            f"gun={self.kullanilan_gun})>"
        )