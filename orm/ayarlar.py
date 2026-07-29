"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : orm/ayarlar.py
Açıklama   : Uygulama Ayarları ORM Modeli
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from sqlalchemy import Boolean
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from orm.base_model import BaseModel


class Ayarlar(BaseModel):
    """
    Uygulama genel ayarları.
    """

    __tablename__ = "ayarlar"

    # =====================================================
    # Firma Bilgileri
    # =====================================================

    firma_adi: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    firma_logo: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    # =====================================================
    # Personel Ayarları
    # =====================================================

    varsayilan_yillik_izin: Mapped[int] = mapped_column(
        Integer,
        default=14,
        nullable=False,
    )

    emekli_yillik_izin: Mapped[int] = mapped_column(
        Integer,
        default=20,
        nullable=False,
    )

    elli_yas_ustu_izin: Mapped[int] = mapped_column(
        Integer,
        default=20,
        nullable=False,
    )

    # =====================================================
    # Sistem Ayarları
    # =====================================================

    otomatik_yedekleme: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    # =====================================================
    # Debug
    # =====================================================

    def __repr__(self) -> str:

        return (
            f"<Ayarlar("
            f"id={self.id}, "
            f"firma='{self.firma_adi}')>"
        )