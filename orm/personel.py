"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : orm/personel.py
Açıklama   : Personel ORM Modeli
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from datetime import date
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from orm.base_model import BaseModel

if TYPE_CHECKING:
    from orm.pozisyon import Pozisyon
    from orm.personel_izin import PersonelIzin
    from orm.personel_evrak import PersonelEvrak


class Personel(BaseModel):
    """
    Personel Bilgileri
    """

    __tablename__ = "personeller"

    # =====================================================
    # Genel Bilgiler
    # =====================================================

    sicil_no: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False,
    )

    tc_kimlik_no: Mapped[str | None] = mapped_column(
        String(11),
        unique=True,
        nullable=True,
    )

    ad: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    soyad: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    dogum_tarihi: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    dogum_yeri: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    cinsiyet: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
    )

    egitim_durumu: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    medeni_durum: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    # =====================================================
    # İş Bilgileri
    # =====================================================

    ise_giris_tarihi: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    izin_hakki: Mapped[int] = mapped_column(
        default=14,
        nullable=False,
    )

    pozisyon_id: Mapped[int] = mapped_column(
        ForeignKey("pozisyonlar.id"),
        nullable=False,
    )

    # =====================================================
    # İletişim
    # =====================================================

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

    # =====================================================
    # Maaş
    # =====================================================

    maas: Mapped[Decimal | None] = mapped_column(
        Numeric(12, 2),
        nullable=True,
    )

    # =====================================================
    # Fotoğraf
    # =====================================================

    fotograf: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    # =====================================================
    # Açıklama
    # =====================================================

    aciklama: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # =====================================================
    # Relationship
    # =====================================================

    pozisyon: Mapped["Pozisyon"] = relationship(
        back_populates="personeller",
    )

    izinler: Mapped[list["PersonelIzin"]] = relationship(
        back_populates="personel",
        cascade="all, delete-orphan",
    )

    evraklar: Mapped[list["PersonelEvrak"]] = relationship(
        back_populates="personel",
        cascade="all, delete-orphan",
    )

    # =====================================================
    # Properties
    # =====================================================

    @property
    def ad_soyad(self) -> str:
        return f"{self.ad} {self.soyad}"

    @property
    def tam_ad(self) -> str:
        return self.ad_soyad

    # =====================================================
    # Debug
    # =====================================================

    def __repr__(self) -> str:

        return (
            f"<Personel("
            f"id={self.id}, "
            f"sicil_no='{self.sicil_no}', "
            f"ad='{self.ad_soyad}')>"
        )