"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : orm/parca_kategori.py
Açıklama   : Parça Kategori ORM Modeli
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


class ParcaKategori(BaseModel):
    """
    Yedek parça kategorileri.
    """

    __tablename__ = "parca_kategorileri"

    # =====================================================
    # Genel Bilgiler
    # =====================================================

    ad: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    aciklama: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # =====================================================
    # Relationship
    # =====================================================

    parcalar: Mapped[list["Parca"]] = relationship(
        back_populates="kategori",
        lazy="selectin",
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
            f"<ParcaKategori("
            f"id={self.id}, "
            f"ad='{self.ad}')>"
        )