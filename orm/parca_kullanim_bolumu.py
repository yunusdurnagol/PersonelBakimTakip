"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : orm/parca_kullanim_bolumu.py
Açıklama   : Parça Kullanım Bölümü ORM Modeli
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations
from sqlalchemy import Text
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from orm.base_model import BaseModel

if TYPE_CHECKING:
    from orm.parca import Parca
    from orm.makine_bolumu import MakineBolumu


class ParcaKullanimBolumu(BaseModel):
    """
    Bir parçanın kullanılabildiği makine bölümlerini tutar.
    """

    __tablename__ = "parca_kullanim_bolumleri"

    # =====================================================
    # Foreign Keys
    # =====================================================

    parca_id: Mapped[int] = mapped_column(
        ForeignKey("parcalar.id"),
        nullable=False,
        index=True,
    )

    makine_bolumu_id: Mapped[int] = mapped_column(
        ForeignKey("makine_bolumleri.id"),
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

    parca: Mapped["Parca"] = relationship(
        back_populates="kullanim_bolumleri",
        lazy="selectin",
    )

    bolum: Mapped["MakineBolumu"] = relationship(
        back_populates="parca_kullanimlari",
        lazy="selectin",
    )

    # =====================================================
    # Debug
    # =====================================================

    def __repr__(self) -> str:

        return (
            f"<ParcaKullanimBolumu("
            f"id={self.id}, "
            f"parca_id={self.parca_id}, "
            f"bolum_id={self.bolum_id})>"
        )