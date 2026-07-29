"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : orm/personel_izin.py
Açıklama   : Personel İzin ORM Modeli
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
    Personel izin bilgileri.
    """

    __tablename__ = "personel_izinleri"

    # =====================================================
    # Foreign Key
    # =====================================================

    personel_id: Mapped[int] = mapped_column(
        ForeignKey("personeller.id"),
        nullable=False,
        index=True,
    )

    # =====================================================
    # İzin Bilgileri
    # =====================================================

    izin_baslangic: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    izin_bitis: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    izin_gun_sayisi: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    izin_nedeni: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    aciklama: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # =====================================================
    # Relationship
    # =====================================================

    personel: Mapped["Personel"] = relationship(
        back_populates="izinler",
        lazy="selectin",
    )

    # =====================================================
    # Debug
    # =====================================================

    def __repr__(self) -> str:

        return (
            f"<PersonelIzin("
            f"id={self.id}, "
            f"personel_id={self.personel_id}, "
            f"baslangic={self.izin_baslangic}, "
            f"bitis={self.izin_bitis})>"
        )