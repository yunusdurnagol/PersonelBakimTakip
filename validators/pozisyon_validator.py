"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : validators/pozisyon_validator.py
Açıklama   : Pozisyon Validator
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from validators.common_validator import CommonValidator


class PozisyonValidator:
    """
    Pozisyon doğrulama işlemleri.
    """

    # =====================================================
    # CREATE
    # =====================================================

    @staticmethod
    def validate_create(
        *,
        ad: str,
        aciklama: str | None = None,
    ) -> None:

        CommonValidator.required(
            ad,
            "Pozisyon Adı",
        )

        CommonValidator.max_length(
            ad,
            100,
            "Pozisyon Adı",
        )

        if aciklama:

            CommonValidator.max_length(
                aciklama,
                1000,
                "Açıklama",
            )

    # =====================================================
    # UPDATE
    # =====================================================

    @staticmethod
    def validate_update(
        *,
        ad: str,
        aciklama: str | None = None,
    ) -> None:

        PozisyonValidator.validate_create(
            ad=ad,
            aciklama=aciklama,
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
    # ID
    # =====================================================

    @staticmethod
    def validate_id(
        id: int,
    ) -> None:

        CommonValidator.id(id)