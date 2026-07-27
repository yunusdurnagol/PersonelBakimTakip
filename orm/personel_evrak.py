"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : orm/personel_evrak.py
Açıklama   : Personel Evrak ORM Modeli
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from orm.base_model import BaseModel

if TYPE_CHECKING:
    from orm.personel import Personel


class PersonelEvrak(BaseModel):
    """
    Personel Evrakları
    """

    __tablename__ = "personel_evraklari"

    personel_id: Mapped[int] = mapped_column(
        ForeignKey("personeller.id"),
        nullable=False,
    )

    evrak_turu: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    dosya_adi: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    dosya_yolu: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    aciklama: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    personel: Mapped["Personel"] = relationship(
        back_populates="evraklar",
    )

    def __repr__(self) -> str:

        return (
            f"<PersonelEvrak("
            f"id={self.id}, "
            f"evrak='{self.evrak_turu}')>"
        )