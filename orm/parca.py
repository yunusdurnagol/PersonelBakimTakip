"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : orm/parca.py
Açıklama   : Yedek Parça ORM Modeli
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from orm.base_model import BaseModel

if TYPE_CHECKING:
    from orm.parca_hareket import ParcaHareket
    from orm.parca_kategori import ParcaKategori
    from orm.parca_kullanim_bolumu import ParcaKullanimBolumu
    from orm.parca_marka import ParcaMarka
    from orm.parca_muadili import ParcaMuadili
    from orm.tedarikci import Tedarikci


class Parca(BaseModel):
    """
    Fabrikada kullanılan yedek parçalar.
    """

    __tablename__ = "parcalar"

    # =====================================================
    # Genel Bilgiler
    # =====================================================

    stok_kodu: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    orijinal_kod: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True,
        index=True,
    )

    parca_adi: Mapped[str] = mapped_column(
        String(250),
        nullable=False,
        index=True,
    )

    kategori_id: Mapped[int] = mapped_column(
        ForeignKey("parca_kategorileri.id"),
        nullable=False,
        index=True,
    )

    marka_id: Mapped[int | None] = mapped_column(
        ForeignKey("parca_markalari.id"),
        nullable=True,
        index=True,
    )

    model: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True,
        index=True,
    )

    tedarikci_id: Mapped[int | None] = mapped_column(
        ForeignKey("tedarikciler.id"),
        nullable=True,
        index=True,
    )

    birim: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    fotograf: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    aciklama: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # =====================================================
    # Relationship
    # =====================================================

    kategori: Mapped["ParcaKategori"] = relationship(
        back_populates="parcalar",
        lazy="selectin",
    )

    marka: Mapped["ParcaMarka"] = relationship(
        back_populates="parcalar",
        lazy="selectin",
    )

    tedarikci: Mapped["Tedarikci"] = relationship(
        back_populates="parcalar",
        lazy="selectin",
    )

    hareketler: Mapped[list["ParcaHareket"]] = relationship(
        back_populates="parca",
        cascade="all, delete-orphan",
        lazy="selectin",
    )

    kullanim_bolumleri: Mapped[list["ParcaKullanimBolumu"]] = relationship(
        back_populates="parca",
        cascade="all, delete-orphan",
        lazy="selectin",
    )

    
    muadiller: Mapped[list["ParcaMuadili"]] = relationship(
        "ParcaMuadili",
        foreign_keys="ParcaMuadili.parca_id",
        back_populates="parca",
        cascade="all, delete-orphan",
        lazy="selectin",
    )

        # =====================================================
    # Properties
    # =====================================================

    @property
    def tam_ad(self) -> str:
        return f"{self.stok_kodu} - {self.parca_adi}"

    @property
    def marka_adi(self) -> str | None:
        return self.marka.ad if self.marka else None

    @property
    def kategori_adi(self) -> str:
        return self.kategori.ad

    @property
    def tedarikci_adi(self) -> str | None:
        return self.tedarikci.firma_adi if self.tedarikci else None

    @property
    def hareket_sayisi(self) -> int:
        return len(self.hareketler)

    @property
    def kullanim_bolumu_sayisi(self) -> int:
        return len(self.kullanim_bolumleri)

    @property
    def muadil_sayisi(self) -> int:
        return len(self.muadiller)

    # =====================================================
    # Debug
    # =====================================================

    def __repr__(self) -> str:

        return (
            f"<Parca("
            f"id={self.id}, "
            f"stok_kodu='{self.stok_kodu}', "
            f"parca_adi='{self.parca_adi}')>"
        )



 