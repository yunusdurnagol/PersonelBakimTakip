"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : orm/makine.py
Açıklama   : Makine ORM Modeli
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from orm.base_model import BaseModel
from sqlalchemy.orm import relationship


class Makine(BaseModel):
    """
    Makine Modeli
    """

    __tablename__ = "makineler"

    kod: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        unique=True,
        index=True,
    )

    ad: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
        index=True,
    )

    aciklama: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )
    bolumler = relationship(
    "MakineBolumu",
    back_populates="makine",
    cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return (
            f"<Makine(id={self.id}, "
            f"kod='{self.kod}', "
            f"ad='{self.ad}')>"
        )