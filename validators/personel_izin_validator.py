"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : validators/personel_izin_validator.py
Açıklama   : Personel İzin Validator
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from datetime import date

from validators.common_validator import CommonValidator


class PersonelIzinValidator:
    """
    Personel izin doğrulama işlemleri.
    """

    # =====================================================
    # CREATE
    # =====================================================

    @staticmethod
    def validate_create(
        *,
        personel_id: int,
        izin_baslangic: date,
        izin_bitis: date,
        izin_gun_sayisi: int,
        izin_nedeni: str | None = None,
        aciklama: str | None = None,
    ) -> None:

        CommonValidator.id(personel_id)

        if izin_baslangic is None:
            raise ValueError("İzin başlangıç tarihi boş olamaz.")

        if izin_bitis is None:
            raise ValueError("İzin bitiş tarihi boş olamaz.")

        if izin_bitis < izin_baslangic:
            raise ValueError(
                "İzin bitiş tarihi başlangıç tarihinden önce olamaz."
            )

        if izin_gun_sayisi <= 0:
            raise ValueError(
                "İzin gün sayısı 0'dan büyük olmalıdır."
            )

        if izin_nedeni:

            CommonValidator.max_length(
                izin_nedeni,
                100,
                "İzin Nedeni",
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
        izin_baslangic: date,
        izin_bitis: date,
        izin_gun_sayisi: int,
        izin_nedeni: str | None = None,
        aciklama: str | None = None,
    ) -> None:

        PersonelIzinValidator.validate_create(
            personel_id=personel_id,
            izin_baslangic=izin_baslangic,
            izin_bitis=izin_bitis,
            izin_gun_sayisi=izin_gun_sayisi,
            izin_nedeni=izin_nedeni,
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
    # GET METHODS
    # =====================================================

    @staticmethod
    def validate_get_by_personel(
        personel_id: int,
    ) -> None:

        CommonValidator.id(personel_id)

    @staticmethod
    def validate_get_by_tarih(
        tarih: date,
    ) -> None:

        if tarih is None:
            raise ValueError(
                "Tarih boş olamaz."
            )

    # =====================================================
    # KONTROLLER
    # =====================================================

    @staticmethod
    def validate_personel_izin_var_mi(
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