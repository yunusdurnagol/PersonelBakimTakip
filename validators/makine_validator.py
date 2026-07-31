"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : validators/makine_validator.py
Açıklama   : Makine Validator
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from validators.common_validator import CommonValidator


class MakineValidator:
    """
    Makine doğrulama işlemleri.
    """

    # =====================================================
    # CREATE
    # =====================================================

    @staticmethod
    def validate_create(
        *,
        kod: str,
        ad: str,
        aciklama: str | None = None,
    ) -> None:

        CommonValidator.required(
            kod,
            "Makine Kodu",
        )

        CommonValidator.required(
            ad,
            "Makine Adı",
        )

        CommonValidator.max_length(
            kod,
            30,
            "Makine Kodu",
        )

        CommonValidator.max_length(
            ad,
            150,
            "Makine Adı",
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
        kod: str,
        ad: str,
        aciklama: str | None = None,
    ) -> None:

        MakineValidator.validate_create(
            kod=kod,
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