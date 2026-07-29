"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : orm/makine_bolumu.py
Açıklama   : Makine Bölümü ORM Modeli
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
from sqlalchemy import ForeignKey
from orm.base_model import BaseModel

if TYPE_CHECKING:
    from orm.makine import Makine
    from orm.parca_kullanim_bolumu import ParcaKullanimBolumu


class MakineBolumu(BaseModel):
    """
    Fabrikadaki makine bölümleri.

    Örnek:
        Boyahane
        Ram
        Sanfor
        Kesim
        Paketleme
    """

    __tablename__ = "makine_bolumleri"

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
    makine_id: Mapped[int] = mapped_column(
        ForeignKey("makineler.id"),
        nullable=False,
    )
    # =====================================================
    # Relationship
    # =====================================================

    makine = relationship(
        "Makine",
        back_populates="bolumler",
    )
   
    

    parca_kullanimlari: Mapped[list["ParcaKullanimBolumu"]] = relationship(
        back_populates="bolum",
        lazy="selectin",
    )
    parca_hareketleri = relationship(
    "ParcaHareket",
    back_populates="makine_bolumu",
    )
    
    # =====================================================
    # Debug
    # =====================================================

    def __repr__(self) -> str:
        return (
            f"<MakineBolumu("
            f"id={self.id}, "
            f"ad='{self.ad}')>"
        )