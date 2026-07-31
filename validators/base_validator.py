"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : validators/base_validator.py
Açıklama   : Ortak Validator Sınıfı
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from typing import Any


class BaseValidator:
    """
    Tüm validator sınıflarının temelidir.

    Her validator bu sınıftan türetilir.

    Örnek:

        validator = PersonelValidator()

        validator.required(ad, "Ad")
        validator.max_length(ad, 100, "Ad")
        validator.positive(maas, "Maaş")
    """

    # =====================================================
    # STRING VALIDATION
    # =====================================================

    @staticmethod
    def required(
        value: Any,
        field_name: str,
    ) -> None:
        """
        Boş değer kontrolü.
        """

        if value is None:
            raise ValueError(
                f"{field_name} boş bırakılamaz."
            )

        if isinstance(value, str):

            if value.strip() == "":
                raise ValueError(
                    f"{field_name} boş bırakılamaz."
                )

    @staticmethod
    def min_length(
        value: str,
        length: int,
        field_name: str,
    ) -> None:
        """
        Minimum karakter kontrolü.
        """

        if value is None:
            return

        if len(value.strip()) < length:

            raise ValueError(
                f"{field_name} en az "
                f"{length} karakter olmalıdır."
            )

    @staticmethod
    def max_length(
        value: str,
        length: int,
        field_name: str,
    ) -> None:
        """
        Maksimum karakter kontrolü.
        """

        if value is None:
            return

        if len(value.strip()) > length:

            raise ValueError(
                f"{field_name} en fazla "
                f"{length} karakter olabilir."
            )

    # =====================================================
    # NUMBER VALIDATION
    # =====================================================

    @staticmethod
    def positive(
        value: int | float,
        field_name: str,
    ) -> None:
        """
        Pozitif sayı kontrolü.
        """

        if value <= 0:

            raise ValueError(
                f"{field_name} sıfırdan büyük olmalıdır."
            )

    @staticmethod
    def non_negative(
        value: int | float,
        field_name: str,
    ) -> None:
        """
        Negatif olmama kontrolü.
        """

        if value < 0:

            raise ValueError(
                f"{field_name} negatif olamaz."
            )

    @staticmethod
    def between(
        value: int | float,
        minimum: int | float,
        maximum: int | float,
        field_name: str,
    ) -> None:
        """
        Sayısal aralık kontrolü.
        """

        if not minimum <= value <= maximum:

            raise ValueError(
                f"{field_name} "
                f"{minimum} ile {maximum} arasında olmalıdır."
            )

    # =====================================================
    # DATE VALIDATION
    # =====================================================

    @staticmethod
    def date_order(
        start_date,
        end_date,
        start_name: str,
        end_name: str,
    ) -> None:
        """
        Başlangıç tarihi bitiş tarihinden büyük olamaz.
        """

        if start_date > end_date:

            raise ValueError(
                f"{start_name} "
                f"{end_name}'nden sonra olamaz."
            )

    # =====================================================
    # COLLECTION VALIDATION
    # =====================================================

    @staticmethod
    def not_empty(
        values,
        field_name: str,
    ) -> None:
        """
        Liste boş olamaz.
        """

        if not values:

            raise ValueError(
                f"{field_name} boş olamaz."
            )

    # =====================================================
    # CHOICE VALIDATION
    # =====================================================

    @staticmethod
    def in_list(
        value,
        valid_values,
        field_name: str,
    ) -> None:
        """
        Değer izin verilen listede olmalıdır.
        """

        if value not in valid_values:

            raise ValueError(
                f"{field_name} geçersiz."
            )