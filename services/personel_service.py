"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : services/personel_service.py
Açıklama   : Personel servis işlemleri
Yazar      : Yunus Durnagöl
Sürüm      : 3.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from datetime import date
from decimal import Decimal

from orm.personel import Personel
from repositories.personel_repository import PersonelRepository


class PersonelService:
    """
    Personel işlemlerinin iş katmanı.

    UI katmanı Repository veya ORM ile doğrudan konuşmaz.
    Tüm işlemler bu servis üzerinden yürütülür.
    """

    def __init__(
        self,
        repository: PersonelRepository,
    ) -> None:

        self.repository = repository

    # =====================================================
    # LİSTELEME
    # =====================================================

    def get_tum_personeller(self) -> list[Personel]:

        return self.repository.get_aktif_personeller()

    def get_by_id(
        self,
        personel_id: int,
    ) -> Personel | None:

        return self.repository.get_by_id(personel_id)

    def son_eklenenler(
        self,
        limit: int = 10,
    ) -> list[Personel]:

        return self.repository.son_eklenenler(limit)

    # =====================================================
    # PERSONEL EKLE
    # =====================================================

    def personel_ekle(
        self,
        *,
        sicil_no: str,
        ad: str,
        soyad: str,
        ise_giris_tarihi: date,
        pozisyon_id: int,
        tc_kimlik_no: str | None = None,
        cinsiyet: str | None = None,
        dogum_tarihi: date | None = None,
        dogum_yeri: str | None = None,
        uyruk: str | None = None,
        medeni_durum: str | None = None,
        egitim_durumu: str | None = None,
        izin_hakki: int = 14,
        telefon: str | None = None,
        email: str | None = None,
        adres: str | None = None,
        maas: Decimal | None = None,
        iban: str | None = None,
        fotograf: str | None = None,
        aciklama: str | None = None,
    ) -> Personel:

        sicil_no = sicil_no.strip()
        ad = ad.strip()
        soyad = soyad.strip()

        if not sicil_no:
            raise ValueError("Sicil numarası boş bırakılamaz.")

        if not ad:
            raise ValueError("Ad boş bırakılamaz.")

        if not soyad:
            raise ValueError("Soyad boş bırakılamaz.")

        if not ise_giris_tarihi:
            raise ValueError(
                "İşe giriş tarihi belirtilmelidir."
            )

        if not pozisyon_id:
            raise ValueError(
                "Pozisyon seçilmelidir."
            )

        if self.repository.sicil_no_var_mi(sicil_no):
            raise ValueError(
                f"{sicil_no} sicil numarası zaten kayıtlı."
            )

        if tc_kimlik_no:

            tc_kimlik_no = tc_kimlik_no.strip()

            if self.repository.tc_var_mi(tc_kimlik_no):
                raise ValueError(
                    "Bu TC Kimlik Numarası zaten kayıtlı."
                )

        if iban:

            iban = iban.strip()

            if self.repository.iban_var_mi(iban):
                raise ValueError(
                    "Bu IBAN zaten kayıtlı."
                )

        personel = Personel(
            sicil_no=sicil_no,
            tc_kimlik_no=tc_kimlik_no,
            ad=ad,
            soyad=soyad,
            cinsiyet=cinsiyet,
            dogum_tarihi=dogum_tarihi,
            dogum_yeri=dogum_yeri,
            uyruk=uyruk,
            medeni_durum=medeni_durum,
            egitim_durumu=egitim_durumu,
            ise_giris_tarihi=ise_giris_tarihi,
            izin_hakki=izin_hakki,
            pozisyon_id=pozisyon_id,
            telefon=telefon,
            email=email,
            adres=adres,
            maas=maas,
            iban=iban,
            fotograf=fotograf,
            aciklama=aciklama,
        )

        return self.repository.create(personel)

    # =====================================================
    # PERSONEL GÜNCELLE
    # =====================================================

    def personel_guncelle(
        self,
        personel_id: int,
        *,
        sicil_no: str,
        ad: str,
        soyad: str,
        ise_giris_tarihi: date,
        pozisyon_id: int,
        tc_kimlik_no: str | None = None,
        cinsiyet: str | None = None,
        dogum_tarihi: date | None = None,
        dogum_yeri: str | None = None,
        uyruk: str | None = None,
        medeni_durum: str | None = None,
        egitim_durumu: str | None = None,
        izin_hakki: int = 14,
        telefon: str | None = None,
        email: str | None = None,
        adres: str | None = None,
        maas: Decimal | None = None,
        iban: str | None = None,
        fotograf: str | None = None,
        aciklama: str | None = None,
    ) -> Personel:

        personel = self.repository.get_by_id(
            personel_id
        )

        if personel is None:
            raise ValueError(
                "Güncellenecek personel bulunamadı."
            )

        sicil_no = sicil_no.strip()
        ad = ad.strip()
        soyad = soyad.strip()

        if not sicil_no:
            raise ValueError(
                "Sicil numarası boş bırakılamaz."
            )

        if not ad:
            raise ValueError(
                "Ad boş bırakılamaz."
            )

        if not soyad:
            raise ValueError(
                "Soyad boş bırakılamaz."
            )

        if not ise_giris_tarihi:
            raise ValueError(
                "İşe giriş tarihi belirtilmelidir."
            )

        if not pozisyon_id:
            raise ValueError(
                "Pozisyon seçilmelidir."
            )

        # -------------------------------------------------
        # Sicil kontrolü
        # -------------------------------------------------

        mevcut = self.repository.get_by_sicil_no(
            sicil_no
        )

        if mevcut and mevcut.id != personel_id:

            raise ValueError(
                f"{sicil_no} sicil numarası "
                f"başka bir personelde kayıtlı."
            )

        # -------------------------------------------------
        # TC kontrolü
        # -------------------------------------------------

        if tc_kimlik_no:

            tc_kimlik_no = tc_kimlik_no.strip()

            mevcut = (
                self.repository.get_by_tc_kimlik_no(
                    tc_kimlik_no
                )
            )

            if mevcut and mevcut.id != personel_id:

                raise ValueError(
                    "Bu TC Kimlik Numarası "
                    "başka bir personelde kayıtlı."
                )

        # -------------------------------------------------
        # IBAN kontrolü
        # -------------------------------------------------

        if iban:

            iban = iban.strip()

            mevcut = self.repository.get_by_iban(
                iban
            )

            if mevcut and mevcut.id != personel_id:

                raise ValueError(
                    "Bu IBAN başka bir personelde kayıtlı."
                )

        # -------------------------------------------------
        # Güncelle
        # -------------------------------------------------

        personel.sicil_no = sicil_no
        personel.tc_kimlik_no = tc_kimlik_no

        personel.ad = ad
        personel.soyad = soyad

        personel.cinsiyet = cinsiyet
        personel.dogum_tarihi = dogum_tarihi
        personel.dogum_yeri = dogum_yeri

        personel.uyruk = uyruk
        personel.medeni_durum = medeni_durum
        personel.egitim_durumu = egitim_durumu

        personel.ise_giris_tarihi = ise_giris_tarihi
        personel.izin_hakki = izin_hakki
        personel.pozisyon_id = pozisyon_id

        personel.telefon = telefon
        personel.email = email
        personel.adres = adres

        personel.maas = maas
        personel.iban = iban

        personel.fotograf = fotograf
        personel.aciklama = aciklama

        return self.repository.update(personel)

    # =====================================================
    # PERSONEL SİL
    # =====================================================

# =====================================================
# PERSONEL SİL
# =====================================================

    def personel_sil(
        self,
        personel_id: int,
    ) -> bool:

        personel = self.repository.get_by_id(
            personel_id
        )

        if personel is None:
            raise ValueError(
                "Silinecek personel bulunamadı."
            )

        self.repository.delete(
            personel
        )

        return True

    # =====================================================
    # SAYI
    # =====================================================

    def toplam_personel(self) -> int:

        return self.repository.toplam_personel()

    def toplam_aktif_personel(self) -> int:

        return self.repository.toplam_aktif_personel()