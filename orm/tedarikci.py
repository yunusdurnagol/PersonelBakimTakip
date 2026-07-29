"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : orm/tedarikci.py
Açıklama   : Tedarikçi ORM Modeli
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
    from orm.parca import Parca


class Tedarikci(BaseModel):
    """
    Yedek parça tedarikçileri.
    """

    __tablename__ = "tedarikciler"

    # =====================================================
    # Firma Bilgileri
    # =====================================================

    firma_adi: Mapped[str] = mapped_column(
        String(200),
        unique=True,
        nullable=False,
        index=True,
    )

    yetkili: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True,
    )

    telefon: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
    )

    email: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True,
    )

    adres: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    vergi_dairesi: Mapped[str | None] = mapped_column(
            String(150),
            nullable=True,
        )
    vergi_no: Mapped[str | None] = mapped_column(
            String(50),
            nullable=True,
        )
    aciklama: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # =====================================================
    # Relationship
    # =====================================================

    parcalar: Mapped[list["Parca"]] = relationship(
        back_populates="tedarikci",
        lazy="selectin",
    )
    parca_hareketleri = relationship(
    "ParcaHareket",
    back_populates="tedarikci",
    )
    # =====================================================
    # Properties
    # =====================================================

    @property
    def parca_sayisi(self) -> int:
        return len(self.parcalar)

    # =====================================================
    # Debug
    # =====================================================

    def __repr__(self) -> str:

        return (
            f"<Tedarikci("
            f"id={self.id}, "
            f"firma='{self.firma_adi}')>"
        )