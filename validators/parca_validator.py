"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : validators/parca_validator.py
Açıklama   : Parça Validator
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from validators.common_validator import CommonValidator


class ParcaValidator:
    """
    Parça doğrulama işlemleri.
    """

    # =====================================================
    # CREATE
    # =====================================================

    @staticmethod
    def validate_create(
        *,
        stok_kodu: str,
        parca_adi: str,
        kategori_id: int,
        birim: str,
        orijinal_kod: str | None = None,
        marka_id: int | None = None,
        model: str | None = None,
        tedarikci_id: int | None = None,
        fotograf: str | None = None,
        aciklama: str | None = None,
    ) -> None:

        CommonValidator.required(
            stok_kodu,
            "Stok Kodu",
        )

        CommonValidator.required(
            parca_adi,
            "Parça Adı",
        )

        CommonValidator.required(
            birim,
            "Birim",
        )

        CommonValidator.id(
            kategori_id,
        )

        if marka_id is not None:
            CommonValidator.id(
                marka_id,
            )

        if tedarikci_id is not None:
            CommonValidator.id(
                tedarikci_id,
            )

        CommonValidator.max_length(
            stok_kodu,
            100,
            "Stok Kodu",
        )

        CommonValidator.max_length(
            parca_adi,
            250,
            "Parça Adı",
        )

        CommonValidator.max_length(
            birim,
            20,
            "Birim",
        )

        if orijinal_kod:

            CommonValidator.max_length(
                orijinal_kod,
                150,
                "Orijinal Kod",
            )

        if model:

            CommonValidator.max_length(
                model,
                150,
                "Model",
            )

        if fotograf:

            CommonValidator.max_length(
                fotograf,
                500,
                "Fotoğraf",
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

        ParcaValidator.validate_create(
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
    # REPOSITORY METOTLARI
    # =====================================================

    @staticmethod
    def validate_stok_kodu(
        stok_kodu: str,
    ) -> None:

        CommonValidator.required(
            stok_kodu,
            "Stok Kodu",
        )

        CommonValidator.max_length(
            stok_kodu,
            100,
            "Stok Kodu",
        )

    @staticmethod
    def validate_orijinal_kod(
        orijinal_kod: str,
    ) -> None:

        CommonValidator.required(
            orijinal_kod,
            "Orijinal Kod",
        )

        CommonValidator.max_length(
            orijinal_kod,
            150,
            "Orijinal Kod",
        )

    @staticmethod
    def validate_kategori_id(
        kategori_id: int,
    ) -> None:

        CommonValidator.id(
            kategori_id,
        )

    @staticmethod
    def validate_marka_id(
        marka_id: int,
    ) -> None:

        CommonValidator.id(
            marka_id,
        )

    @staticmethod
    def validate_tedarikci_id(
        tedarikci_id: int,
    ) -> None:

        CommonValidator.id(
            tedarikci_id,
        )