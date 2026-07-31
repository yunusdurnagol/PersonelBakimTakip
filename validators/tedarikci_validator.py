"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : validators/tedarikci_validator.py
Açıklama   : Tedarikçi Validator
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from validators.common_validator import CommonValidator


class TedarikciValidator:
    """
    Tedarikçi doğrulama işlemleri.
    """

    # =====================================================
    # CREATE
    # =====================================================

    @staticmethod
    def validate_create(
        *,
        firma_adi: str,
        yetkili: str | None = None,
        telefon: str | None = None,
        email: str | None = None,
        adres: str | None = None,
        vergi_dairesi: str | None = None,
        vergi_no: str | None = None,
        aciklama: str | None = None,
    ) -> None:

        CommonValidator.required(
            firma_adi,
            "Firma Adı",
        )

        CommonValidator.max_length(
            firma_adi,
            200,
            "Firma Adı",
        )

        if yetkili:

            CommonValidator.max_length(
                yetkili,
                150,
                "Yetkili",
            )

        if telefon:

            CommonValidator.max_length(
                telefon,
                30,
                "Telefon",
            )

        if email:

            CommonValidator.email(
                email,
            )

            CommonValidator.max_length(
                email,
                150,
                "E-Posta",
            )

        if adres:

            CommonValidator.max_length(
                adres,
                1000,
                "Adres",
            )

        if vergi_dairesi:

            CommonValidator.max_length(
                vergi_dairesi,
                150,
                "Vergi Dairesi",
            )

        if vergi_no:

            CommonValidator.max_length(
                vergi_no,
                50,
                "Vergi No",
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
        **kwargs,
    ) -> None:

        TedarikciValidator.validate_create(
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
    # ID
    # =====================================================

    @staticmethod
    def validate_id(
        id: int,
    ) -> None:

        CommonValidator.id(id)

    # =====================================================
    # GET METHODS
    # =====================================================

    @staticmethod
    def validate_firma_adi(
        firma_adi: str,
    ) -> None:

        CommonValidator.required(
            firma_adi,
            "Firma Adı",
        )

        CommonValidator.max_length(
            firma_adi,
            200,
            "Firma Adı",
        )

    @staticmethod
    def validate_vergi_no(
        vergi_no: str,
    ) -> None:

        CommonValidator.required(
            vergi_no,
            "Vergi No",
        )

        CommonValidator.max_length(
            vergi_no,
            50,
            "Vergi No",
        )