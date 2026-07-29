"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : orm/parca_hareket.py
Açıklama   : Parça Hareket ORM Modeli
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from datetime import date
from decimal import Decimal

from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from orm.base_model import BaseModel


class ParcaHareket(BaseModel):
    """
    Parça Hareket Modeli
    """

    __tablename__ = "parca_hareketleri"

    parca_id: Mapped[int] = mapped_column(
        ForeignKey("parcalar.id"),
        nullable=False,
    )

    makine_bolumu_id: Mapped[int] = mapped_column(
        ForeignKey("makine_bolumleri.id"),
        nullable=False,
    )

    tedarikci_id: Mapped[int] = mapped_column(
        ForeignKey("tedarikciler.id"),
        nullable=False,
    )

    alis_tarihi: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    adet: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    birim_fiyat: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    toplam_tutar: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    para_birimi: Mapped[str] = mapped_column(
        String(3),
        nullable=False,
    )

    fatura_no: Mapped[str | None] = mapped_column(
        String(100),
    )

    fatura_tarihi: Mapped[date | None] = mapped_column(
        Date,
    )

    fatura_dosyasi: Mapped[str | None] = mapped_column(
        String(500),
    )

    tedarikci_urun_kodu: Mapped[str | None] = mapped_column(
        String(150),
    )

    aciklama: Mapped[str | None] = mapped_column(
        Text,
    )

    # =====================================================
    # RELATIONSHIPS
    # =====================================================

    parca = relationship(
        "Parca",
        back_populates="hareketler",
    )

    makine_bolumu = relationship(
        "MakineBolumu",
        back_populates="parca_hareketleri",
    )

    tedarikci = relationship(
        "Tedarikci",
        back_populates="parca_hareketleri",
    )