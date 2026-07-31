"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : validators/parca_hareket_validator.py
Açıklama   : Parça Hareket Validator
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from datetime import date
from decimal import Decimal

from validators.common_validator import CommonValidator


class ParcaHareketValidator:
    """
    Parça Hareket doğrulama işlemleri.
    """

    # =====================================================
    # CREATE
    # =====================================================

    @staticmethod
    def validate_create(
        *,
        parca_id: int,
        makine_bolumu_id: int,
        tedarikci_id: int,
        alis_tarihi: date,
        adet: Decimal,
        birim_fiyat: Decimal,
        toplam_tutar: Decimal,
        para_birimi: str,
        fatura_no: str | None = None,
        fatura_tarihi: date | None = None,
        fatura_dosyasi: str | None = None,
        tedarikci_urun_kodu: str | None = None,
        aciklama: str | None = None,
    ) -> None:

        CommonValidator.id(parca_id)
        CommonValidator.id(makine_bolumu_id)
        CommonValidator.id(tedarikci_id)

        CommonValidator.required(
            alis_tarihi,
            "Alış Tarihi",
        )

        CommonValidator.required(
            para_birimi,
            "Para Birimi",
        )

        CommonValidator.positive(
            adet,
            "Adet",
        )

        CommonValidator.positive(
            birim_fiyat,
            "Birim Fiyat",
        )

        CommonValidator.positive(
            toplam_tutar,
            "Toplam Tutar",
        )

        CommonValidator.max_length(
            para_birimi,
            3,
            "Para Birimi",
        )

        if fatura_no:

            CommonValidator.max_length(
                fatura_no,
                100,
                "Fatura No",
            )

        if fatura_dosyasi:

            CommonValidator.max_length(
                fatura_dosyasi,
                500,
                "Fatura Dosyası",
            )

        if tedarikci_urun_kodu:

            CommonValidator.max_length(
                tedarikci_urun_kodu,
                150,
                "Tedarikçi Ürün Kodu",
            )

        if aciklama:

            CommonValidator.max_length(
                aciklama,
                1000,
                "Açıklama",
            )

        if fatura_tarihi and fatura_tarihi > date.today():

            raise ValueError(
                "Fatura tarihi gelecekte olamaz."
            )

        if alis_tarihi > date.today():

            raise ValueError(
                "Alış tarihi gelecekte olamaz."
            )

    # =====================================================
    # UPDATE
    # =====================================================

    @staticmethod
    def validate_update(
        **kwargs,
    ) -> None:

        ParcaHareketValidator.validate_create(
            **kwargs,
        )

    # =====================================================
    # DELETE
    # =====================================================

    @staticmethod
    def validate_delete(
        id: int,
    ) -> None:

        CommonValidator.id(id)

    # =====================================================
    # SEARCH
    # =====================================================

    @staticmethod
    def validate_search(
        text: str,
    ) -> None:

        CommonValidator.required(
            text,
            "Arama Metni",
        )

        CommonValidator.max_length(
            text,
            100,
            "Arama Metni",
        )

    # =====================================================
    # GET BY TARİH
    # =====================================================

    @staticmethod
    def validate_tarih(
        tarih: date,
    ) -> None:

        CommonValidator.required(
            tarih,
            "Tarih",
        )

    # =====================================================
    # ID
    # =====================================================

    @staticmethod
    def validate_id(
        id: int,
    ) -> None:

        CommonValidator.id(id)