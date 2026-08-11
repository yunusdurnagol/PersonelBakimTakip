"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : services/personel_evrak_service.py
Açıklama   : Personel Evrak İş Katmanı
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

import shutil
from pathlib import Path

from orm.personel_evrak import PersonelEvrak
from repositories.personel_evrak_repository import (
    PersonelEvrakRepository,
)
from services.base_service import BaseService


class PersonelEvrakService(BaseService[PersonelEvrak]):
    """
    Personel evrak işlemlerinin iş katmanı.

    UI
        ↓
    PersonelEvrakService
        ↓
    PersonelEvrakRepository
        ↓
    PersonelEvrak ORM
    """

    def __init__(
        self,
        repository: PersonelEvrakRepository,
    ) -> None:

        super().__init__(repository)

        self.repository = repository

    # =====================================================
    # PERSONELE AİT EVRAKLAR
    # =====================================================

    def get_by_personel(
        self,
        personel_id: int,
    ) -> list[PersonelEvrak]:

        return self.repository.get_by_personel(
            personel_id
        )

    # =====================================================
    # EVRAK EKLE
    # =====================================================

    def evrak_ekle(
        self,
        *,
        personel_id: int,
        evrak_adi: str,
        dosya_adi: str,
        dosya_yolu: str,
        belge_tarihi=None,
        aciklama: str | None = None,
    ) -> PersonelEvrak:

        # -------------------------------------------------
        # Temel kontroller
        # -------------------------------------------------

        if not personel_id:
            raise ValueError(
                "Personel belirtilmelidir."
            )

        evrak_adi = evrak_adi.strip()
        dosya_adi = dosya_adi.strip()
        dosya_yolu = dosya_yolu.strip()

        if not evrak_adi:
            raise ValueError(
                "Evrak adı boş bırakılamaz."
            )

        if not dosya_adi:
            raise ValueError(
                "Dosya adı boş bırakılamaz."
            )

        if not dosya_yolu:
            raise ValueError(
                "Dosya yolu boş bırakılamaz."
            )

        # -------------------------------------------------
        # Kaynak dosya kontrolü
        # -------------------------------------------------

        kaynak_dosya = Path(dosya_yolu)

        if not kaynak_dosya.exists():
            raise ValueError(
                "Seçilen dosya bulunamadı."
            )

        if not kaynak_dosya.is_file():
            raise ValueError(
                "Seçilen yol geçerli bir dosya değil."
            )

        # -------------------------------------------------
        # Evrak adını benzersiz yap
        #
        # Kimlik
        # Kimlik 1
        # Kimlik 2
        # Kimlik 3
        # -------------------------------------------------

        evrak_adi = self._benzersiz_evrak_adi(
            personel_id=personel_id,
            evrak_adi=evrak_adi,
        )

        # -------------------------------------------------
        # Personel evrak klasörü
        #
        # data/
        #   personel_evraklari/
        #       15/
        # -------------------------------------------------

        klasor = self._personel_evrak_klasoru(
            personel_id
        )

        klasor.mkdir(
            parents=True,
            exist_ok=True,
        )

        # -------------------------------------------------
        # Dosya adını benzersiz yap
        #
        # kimlik.pdf
        # kimlik_1.pdf
        # kimlik_2.pdf
        # -------------------------------------------------

        hedef_dosya = self._benzersiz_dosya_yolu(
            klasor=klasor,
            dosya_adi=kaynak_dosya.name,
        )

        # -------------------------------------------------
        # Dosyayı kopyala
        # -------------------------------------------------

        try:

            shutil.copy2(
                kaynak_dosya,
                hedef_dosya,
            )

        except OSError as exc:

            raise ValueError(
                f"Dosya kopyalanamadı: {exc}"
            ) from exc

        # -------------------------------------------------
        # Veritabanında tutulacak yol
        # -------------------------------------------------

        dosya_yolu_db = str(
            hedef_dosya
        )

        # Windows'ta daha düzenli kayıt için
        dosya_yolu_db = dosya_yolu_db.replace(
            "\\",
            "/",
        )

        # -------------------------------------------------
        # ORM
        # -------------------------------------------------

        evrak = PersonelEvrak(
            personel_id=personel_id,
            evrak_adi=evrak_adi,
            dosya_adi=hedef_dosya.name,
            dosya_yolu=dosya_yolu_db,
            belge_tarihi=belge_tarihi,
            aciklama=aciklama,
        )

        # -------------------------------------------------
        # Veritabanına kaydet
        # -------------------------------------------------

        try:

            return self.repository.create(
                evrak
            )

        except Exception:

            # DB kaydı başarısız olursa,
            # az önce kopyaladığımız dosyayı
            # mümkünse geri siliyoruz.

            try:

                if hedef_dosya.exists():
                    hedef_dosya.unlink()

            except OSError:
                pass

            raise

    # =====================================================
    # PERSONEL EVRAK KLASÖRÜ
    # =====================================================

    @staticmethod
    def _personel_evrak_klasoru(
        personel_id: int,
    ) -> Path:

        proje_koku = Path(
            __file__
        ).resolve().parent.parent

        return (
            proje_koku
            / "data"
            / "personel_evraklari"
            / str(personel_id)
        )

    # =====================================================
    # BENZERSİZ EVRAK ADI
    # =====================================================

    def _benzersiz_evrak_adi(
        self,
        *,
        personel_id: int,
        evrak_adi: str,
    ) -> str:

        temel_ad = evrak_adi.strip()

        mevcutlar = (
            self.repository.get_by_personel(
                personel_id
            )
        )

        isimler = {
            evrak.evrak_adi.strip().lower()
            for evrak in mevcutlar
        }

        if temel_ad.lower() not in isimler:
            return temel_ad

        sayi = 1

        while True:

            yeni_ad = (
                f"{temel_ad} {sayi}"
            )

            if yeni_ad.lower() not in isimler:
                return yeni_ad

            sayi += 1

    # =====================================================
    # BENZERSİZ DOSYA YOLU
    # =====================================================

    @staticmethod
    def _benzersiz_dosya_yolu(
        *,
        klasor: Path,
        dosya_adi: str,
    ) -> Path:

        temel = Path(dosya_adi)

        isim = temel.stem
        uzanti = temel.suffix

        hedef = klasor / dosya_adi

        if not hedef.exists():
            return hedef

        sayi = 1

        while True:

            yeni_dosya_adi = (
                f"{isim}_{sayi}{uzanti}"
            )

            hedef = (
                klasor
                / yeni_dosya_adi
            )

            if not hedef.exists():
                return hedef

            sayi += 1

    # =====================================================
    # EVRAK GETİR
    # =====================================================

    def get_by_id(
        self,
        evrak_id: int,
    ) -> PersonelEvrak | None:

        return self.repository.get_by_id(
            evrak_id
        )

    # =====================================================
    # İSTATİSTİKLER
    # =====================================================

    def toplam_evrak(self) -> int:

        return self.repository.toplam_evrak()

    def personele_gore_evrak_sayisi(
        self,
        personel_id: int,
    ) -> int:

        return (
            self.repository
            .personele_gore_evrak_sayisi(
                personel_id
            )
        )