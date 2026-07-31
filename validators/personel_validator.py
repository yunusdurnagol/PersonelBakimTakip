"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : validators/personel_validator.py
Açıklama   : Personel Validator
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from datetime import date

from exceptions.validation_exception import ValidationException
from validators.common_validator import CommonValidator


class PersonelValidator:
    """
    Personel doğrulama işlemleri.
    """

    # =====================================================
    # CREATE
    # =====================================================

    @staticmethod
    def validate_create(
        *,
        sicil_no: str,
        ad: str,
        soyad: str,
        tc_kimlik_no: str | None,
        telefon: str | None,
        email: str | None,
        ise_giris_tarihi: date,
        guncel_maas,
    ) -> None:

        CommonValidator.required(
            sicil_no,
            "Sicil No",
        )

        CommonValidator.required(
            ad,
            "Ad",
        )

        CommonValidator.required(
            soyad,
            "Soyad",
        )

        CommonValidator.max_length(
            sicil_no,
            20,
            "Sicil No",
        )

        CommonValidator.max_length(
            ad,
            100,
            "Ad",
        )

        CommonValidator.max_length(
            soyad,
            100,
            "Soyad",
        )

        CommonValidator.tc_kimlik(
            tc_kimlik_no,
        )

        CommonValidator.phone(
            telefon,
        )

        CommonValidator.email(
            email,
        )

        CommonValidator.future_date(
            ise_giris_tarihi,
            "İşe Giriş Tarihi",
        )

        CommonValidator.non_negative(
            guncel_maas,
            "Güncel Maaş",
        )

    # =====================================================
    # UPDATE
    # =====================================================

    @staticmethod
    def validate_update(
        **kwargs,
    ) -> None:

        PersonelValidator.validate_create(
            **kwargs,
        )

    # =====================================================
    # DELETE
    # =====================================================

    @staticmethod
    def validate_delete(
        id: int,
    ) -> None:

        if id <= 0:

            raise ValidationException(
                "Geçersiz Personel ID."
            )

    # =====================================================
    # SEARCH
    # =====================================================

    @staticmethod
    def validate_search(
        text: str,
    ) -> None:

        CommonValidator.required(
            text,
            "Arama",
        )

        CommonValidator.max_length(
            text,
            100,
            "Arama",
        )

    # =====================================================
    # ID
    # =====================================================

    @staticmethod
    def validate_id(
        id: int,
    ) -> None:

        if id <= 0:

            raise ValidationException(
                "Geçersiz Personel ID."
            )

    @staticmethod
    def validate_id(
        id: int,
    ) -> None:

        CommonValidator.id(id)