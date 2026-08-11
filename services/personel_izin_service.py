"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : services/personel_izin_service.py
Açıklama   : Personel İzin İşlemleri Service Katmanı
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from datetime import date

from orm.personel_izin import PersonelIzin
from repositories.personel_izin_repository import (
    PersonelIzinRepository,
)
from services.base_service import BaseService


class PersonelIzinService(
    BaseService[PersonelIzin]
):
    """
    Personel izin işlemlerinin iş katmanı.

    UI
        ↓
    PersonelIzinService
        ↓
    PersonelIzinRepository
        ↓
    PersonelIzin ORM

    Not:
    Bu servis izin hakkı hesaplamaz.

    Kullanıcının girdiği
    `izin_gun_sayisi`
    değeri doğrudan kayıt edilir.
    """

    def __init__(
        self,
        repository: PersonelIzinRepository,
    ) -> None:

        super().__init__(
            repository
        )

        self.repository = repository

    # =====================================================
    # PERSONELE AİT İZİNLER
    # =====================================================

    def get_by_personel(
        self,
        personel_id: int,
    ) -> list[PersonelIzin]:
        """
        Belirli personele ait izinleri getirir.

        En son eklenen izin üstte görünür.
        """

        if not personel_id:

            return []

        return self.repository.get_by_personel(
            personel_id
        )

    # =====================================================
    # TÜM İZİNLER
    # =====================================================

    def get_tum_izinler(
        self,
    ) -> list[PersonelIzin]:
        """
        Sistemdeki tüm aktif izin kayıtlarını getirir.
        """

        return self.repository.get_tum_izinler()

    # =====================================================
    # İZİN EKLE
    # =====================================================

    def izin_ekle(
        self,
        *,
        personel_id: int,
        izin_baslangic: date,
        izin_bitis: date,
        izin_gun_sayisi: int,
        izin_nedeni: str = "Yıllık İzin",
        aciklama: str | None = None,
    ) -> PersonelIzin:
        """
        Yeni izin kaydı oluşturur.

        Gün sayısı sistem tarafından hesaplanmaz.
        Kullanıcının girdiği değer kaydedilir.
        """

        # -------------------------------------------------
        # Personel kontrolü
        # -------------------------------------------------

        if not personel_id:

            raise ValueError(
                "Personel belirtilmelidir."
            )

        # -------------------------------------------------
        # Tarih kontrolleri
        # -------------------------------------------------

        if not izin_baslangic:

            raise ValueError(
                "İzin başlangıç tarihi belirtilmelidir."
            )

        if not izin_bitis:

            raise ValueError(
                "İzin bitiş tarihi belirtilmelidir."
            )

        if izin_bitis < izin_baslangic:

            raise ValueError(
                "İzin bitiş tarihi, "
                "başlangıç tarihinden önce olamaz."
            )

        # -------------------------------------------------
        # Gün sayısı
        # -------------------------------------------------

        if izin_gun_sayisi is None:

            raise ValueError(
                "İzin gün sayısı belirtilmelidir."
            )

        try:

            izin_gun_sayisi = int(
                izin_gun_sayisi
            )

        except (
            TypeError,
            ValueError,
        ):

            raise ValueError(
                "İzin gün sayısı geçerli "
                "bir sayı olmalıdır."
            )

        if izin_gun_sayisi <= 0:

            raise ValueError(
                "İzin gün sayısı 0'dan büyük olmalıdır."
            )

        # -------------------------------------------------
        # İzin nedeni
        # -------------------------------------------------

        if izin_nedeni is None:

            izin_nedeni = "Yıllık İzin"

        izin_nedeni = izin_nedeni.strip()

        if not izin_nedeni:

            izin_nedeni = "Yıllık İzin"

        # -------------------------------------------------
        # Açıklama
        # -------------------------------------------------

        if aciklama is not None:

            aciklama = aciklama.strip()

            if not aciklama:

                aciklama = None

        # -------------------------------------------------
        # ORM nesnesi
        # -------------------------------------------------

        izin = PersonelIzin(
            personel_id=personel_id,
            izin_baslangic=izin_baslangic,
            izin_bitis=izin_bitis,
            izin_gun_sayisi=izin_gun_sayisi,
            izin_nedeni=izin_nedeni,
            aciklama=aciklama,
        )

        # -------------------------------------------------
        # Kaydet
        # -------------------------------------------------

        return self.repository.create(
            izin
        )

    # =====================================================
    # ID İLE GETİR
    # =====================================================

    def get_by_id(
        self,
        izin_id: int,
    ) -> PersonelIzin | None:
        """
        ID ile izin kaydı getirir.
        """

        if not izin_id:

            return None

        return self.repository.get_by_id(
            izin_id
        )

    # =====================================================
    # TARİH
    # =====================================================

    def get_by_tarih(
        self,
        tarih: date,
    ) -> list[PersonelIzin]:
        """
        Belirli bir tarihte izinli olan
        personelleri getirir.
        """

        return self.repository.get_by_tarih(
            tarih
        )

    # =====================================================
    # ARAMA
    # =====================================================

    def search(
        self,
        text: str,
    ) -> list[PersonelIzin]:
        """
        İzin nedeni üzerinden arama yapar.
        """

        return self.repository.search(
            text
        )

    # =====================================================
    # PERSONELİN İZİNİ VAR MI?
    # =====================================================

    def personel_izin_var_mi(
        self,
        personel_id: int,
    ) -> bool:
        """
        Personelin kayıtlı en az bir izni
        olup olmadığını kontrol eder.
        """

        return self.repository.personel_izin_var_mi(
            personel_id
        )

    # =====================================================
    # TOPLAM İZİN
    # =====================================================

    def toplam_izin(self) -> int:
        """
        Sistemdeki toplam aktif izin
        kayıt sayısını döndürür.
        """

        return self.repository.toplam_izin()

    # =====================================================
    # KULLANILAN İZİN GÜNÜ
    # =====================================================

    def toplam_kullanilan_izin_gunu(
        self,
        personel_id: int,
    ) -> int:
        """
        Personelin kayıtlı izinlerinin
        toplam gün sayısını döndürür.

        ÖNEMLİ:
        Bu değer izin hakkı değildir.

        Sadece kayıtlı izinlerdeki
        izin_gun_sayisi alanlarının toplamıdır.
        """

        if not personel_id:

            return 0

        return self.repository.toplam_kullanilan_izin_gunu(
            personel_id
        )