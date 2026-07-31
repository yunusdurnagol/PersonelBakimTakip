"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : validators/personel_evrak_validator.py
Açıklama   : Personel Evrak Validator
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from validators.common_validator import CommonValidator


class PersonelEvrakValidator:
    """
    Personel Evrak doğrulama işlemleri.
    """

    # =====================================================
    # CREATE
    # =====================================================

    @staticmethod
    def validate_create(
        *,
        personel_id: int,
        evrak_adi: str,
        dosya_adi: str,
        dosya_yolu: str,
        aciklama: str | None = None,
    ) -> None:

        CommonValidator.id(personel_id)

        CommonValidator.required(
            evrak_adi,
            "Evrak Adı",
        )

        CommonValidator.required(
            dosya_adi,
            "Dosya Adı",
        )

        CommonValidator.required(
            dosya_yolu,
            "Dosya Yolu",
        )

        CommonValidator.max_length(
            evrak_adi,
            150,
            "Evrak Adı",
        )

        CommonValidator.max_length(
            dosya_adi,
            255,
            "Dosya Adı",
        )

        CommonValidator.max_length(
            dosya_yolu,
            500,
            "Dosya Yolu",
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
        personel_id: int,
        evrak_adi: str,
        dosya_adi: str,
        dosya_yolu: str,
        aciklama: str | None = None,
    ) -> None:

        PersonelEvrakValidator.validate_create(
            personel_id=personel_id,
            evrak_adi=evrak_adi,
            dosya_adi=dosya_adi,
            dosya_yolu=dosya_yolu,
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
            150,
            "Arama Metni",
        )

    # =====================================================
    # GET METHODS
    # =====================================================

    @staticmethod
    def validate_get_by_personel(
        personel_id: int,
    ) -> None:

        CommonValidator.id(personel_id)

    @staticmethod
    def validate_get_by_evrak_adi(
        evrak_adi: str,
    ) -> None:

        CommonValidator.required(
            evrak_adi,
            "Evrak Adı",
        )

        CommonValidator.max_length(
            evrak_adi,
            150,
            "Evrak Adı",
        )

    # =====================================================
    # KONTROLLER
    # =====================================================

    @staticmethod
    def validate_evrak_var_mi(
        personel_id: int,
        evrak_adi: str,
    ) -> None:

        CommonValidator.id(personel_id)

        CommonValidator.required(
            evrak_adi,
            "Evrak Adı",
        )

        CommonValidator.max_length(
            evrak_adi,
            150,
            "Evrak Adı",
        )

    # =====================================================
    # İSTATİSTİKLER
    # =====================================================

    @staticmethod
    def validate_toplam_evrak() -> None:
        pass

    @staticmethod
    def validate_personele_gore_evrak_sayisi(
        personel_id: int,
    ) -> None:

        CommonValidator.id(personel_id)

    # =====================================================
    # ID
    # =====================================================

    @staticmethod
    def validate_id(
        id: int,
    ) -> None:

        CommonValidator.id(id)