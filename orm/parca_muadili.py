"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : orm/parca_muadili.py
Açıklama   : Parça Muadili ORM Modeli
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from orm.base_model import BaseModel

if TYPE_CHECKING:
    from orm.parca import Parca


class ParcaMuadili(BaseModel):
    """
    Parçaların muadil ilişkilerini tutar.
    """

    __tablename__ = "parca_muadilleri"

    # =====================================================
    # Foreign Keys
    # =====================================================

    parca_id: Mapped[int] = mapped_column(
        ForeignKey("parcalar.id"),
        nullable=False,
        index=True,
    )

    muadil_parca_id: Mapped[int] = mapped_column(
        ForeignKey("parcalar.id"),
        nullable=False,
        index=True,
    )

    # =====================================================
    # Relationship
    # =====================================================

    parca: Mapped["Parca"] = relationship(
        foreign_keys=[parca_id],
        back_populates="muadiller",
        lazy="selectin",
    )

    muadil_parca: Mapped["Parca"] = relationship(
        foreign_keys=[muadil_parca_id],
        lazy="selectin",
    )

    # =====================================================
    # Debug
    # =====================================================

    def __repr__(self) -> str:

        return (
            f"<ParcaMuadili("
            f"id={self.id}, "
            f"parca_id={self.parca_id}, "
            f"muadil_parca_id={self.muadil_parca_id})>"
        )