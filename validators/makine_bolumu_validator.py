"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : validators/makine_bolumu_validator.py
Açıklama   : Makine Bölümü Validator
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from validators.common_validator import CommonValidator


class MakineBolumuValidator:
    """
    Makine Bölümü doğrulama işlemleri.
    """

    # =====================================================
    # CREATE
    # =====================================================

    @staticmethod
    def validate_create(
        *,
        ad: str,
        makine_id: int,
        aciklama: str | None = None,
    ) -> None:

        CommonValidator.required(
            ad,
            "Bölüm Adı",
        )

        CommonValidator.max_length(
            ad,
            100,
            "Bölüm Adı",
        )

        CommonValidator.id(
            makine_id,
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
        makine_id: int,
        aciklama: str | None = None,
    ) -> None:

        MakineBolumuValidator.validate_create(
            ad=ad,
            makine_id=makine_id,
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