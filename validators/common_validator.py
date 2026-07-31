"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : validators/common_validator.py
Açıklama   : Ortak Validator Metotları
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

import re
from datetime import date
from decimal import Decimal

from exceptions.validation_exception import ValidationException


class CommonValidator:
    """
    Tüm validatorlarda ortak kullanılacak doğrulamalar.
    """

    # =====================================================
    # REQUIRED
    # =====================================================

    @staticmethod
    def required(
        value,
        field_name: str,
    ) -> None:

        if value is None:
            raise ValidationException(
                f"{field_name} boş bırakılamaz."
            )

        if isinstance(value, str):

            if not value.strip():

                raise ValidationException(
                    f"{field_name} boş bırakılamaz."
                )

    # =====================================================
    # STRING
    # =====================================================

    @staticmethod
    def min_length(
        value: str,
        length: int,
        field_name: str,
    ) -> None:

        if value is None:
            return

        if len(value.strip()) < length:

            raise ValidationException(
                f"{field_name} en az {length} karakter olmalıdır."
            )

    @staticmethod
    def max_length(
        value: str,
        length: int,
        field_name: str,
    ) -> None:

        if value is None:
            return

        if len(value.strip()) > length:

            raise ValidationException(
                f"{field_name} en fazla {length} karakter olabilir."
            )

    # =====================================================
    # NUMERIC
    # =====================================================

    @staticmethod
    def positive(
        value: int | float | Decimal,
        field_name: str,
    ) -> None:

        if value <= 0:

            raise ValidationException(
                f"{field_name} sıfırdan büyük olmalıdır."
            )

    @staticmethod
    def non_negative(
        value: int | float | Decimal,
        field_name: str,
    ) -> None:

        if value < 0:

            raise ValidationException(
                f"{field_name} negatif olamaz."
            )

    # =====================================================
    # DATE
    # =====================================================

    @staticmethod
    def date_order(
        start_date: date,
        end_date: date,
        start_name: str,
        end_name: str,
    ) -> None:

        if start_date > end_date:

            raise ValidationException(
                f"{start_name} {end_name} tarihinden büyük olamaz."
            )

    @staticmethod
    def future_date(
        value: date,
        field_name: str,
    ) -> None:

        if value > date.today():

            raise ValidationException(
                f"{field_name} gelecekte olamaz."
            )

    # =====================================================
    # EMAIL
    # =====================================================

    @staticmethod
    def email(
        value: str | None,
    ) -> None:

        if not value:
            return

        pattern = (
            r"^[A-Za-z0-9._%+-]+"
            r"@[A-Za-z0-9.-]+"
            r"\.[A-Za-z]{2,}$"
        )

        if not re.match(
            pattern,
            value,
        ):

            raise ValidationException(
                "Geçersiz e-posta adresi."
            )

    # =====================================================
    # PHONE
    # =====================================================

    @staticmethod
    def phone(
        value: str | None,
    ) -> None:

        if not value:
            return

        pattern = r"^[0-9()+\-\s]{10,20}$"

        if not re.match(
            pattern,
            value,
        ):

            raise ValidationException(
                "Geçersiz telefon numarası."
            )

    # =====================================================
    # TC KİMLİK
    # =====================================================

    @staticmethod
    def tc_kimlik(
        value: str | None,
    ) -> None:

        if not value:
            return

        if not value.isdigit():

            raise ValidationException(
                "TC Kimlik No yalnızca rakamlardan oluşmalıdır."
            )

        if len(value) != 11:

            raise ValidationException(
                "TC Kimlik No 11 haneli olmalıdır."
            )

    # =====================================================
    # VERGİ NO
    # =====================================================

    @staticmethod
    def vergi_no(
        value: str | None,
    ) -> None:

        if not value:
            return

        if not value.isdigit():

            raise ValidationException(
                "Vergi No yalnızca rakamlardan oluşmalıdır."
            )

        if len(value) not in (10, 11):

            raise ValidationException(
                "Vergi No geçersiz."
            )

    # =====================================================
    # DECIMAL
    # =====================================================

    @staticmethod
    def decimal_precision(
        value: Decimal,
        max_digits: int,
        decimal_places: int,
        field_name: str,
    ) -> None:

        if value is None:
            return

        sign, digits, exponent = value.as_tuple()

        total_digits = len(digits)

        decimals = abs(exponent)

        if total_digits > max_digits:

            raise ValidationException(
                f"{field_name} en fazla {max_digits} haneli olabilir."
            )

        if decimals > decimal_places:

            raise ValidationException(
                f"{field_name} en fazla {decimal_places} ondalık basamak içerebilir."
            )

    # =====================================================
    # FILE
    # =====================================================

    @staticmethod
    def file_path(
        value: str | None,
    ) -> None:

        if not value:
            return

        if len(value.strip()) < 3:

            raise ValidationException(
                "Geçersiz dosya yolu."
            )

    @staticmethod
    def id(
        id: int,
    ) -> None:

        if id <= 0:
            raise ValidationException(
                "Geçersiz ID."
            )