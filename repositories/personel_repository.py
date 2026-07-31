"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : repositories/personel_repository.py
Açıklama   : Personel Repository
Yazar      : Yunus Durnagöl
Sürüm      : 3.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from datetime import date
from datetime import timedelta

from sqlalchemy import extract
from sqlalchemy import or_
from sqlalchemy.orm import Session

from orm.personel import Personel
from repositories.base_repository import BaseRepository


class PersonelRepository(BaseRepository[Personel]):
    """
    Personel Repository
    """

    def __init__(
        self,
        session: Session,
    ) -> None:

        super().__init__(
            session=session,
            model=Personel,
        )

    # =====================================================
    # GET METHODS
    # =====================================================

    def get_by_sicil_no(
        self,
        sicil_no: str,
    ) -> Personel | None:

        return self.get(
            sicil_no=sicil_no,
        )

    def get_by_tc_kimlik_no(
        self,
        tc_kimlik_no: str,
    ) -> Personel | None:

        return self.get(
            tc_kimlik_no=tc_kimlik_no,
        )

    def get_by_iban(
        self,
        iban: str,
    ) -> Personel | None:

        return self.get(
            iban=iban,
        )

    # =====================================================
    # PERSONEL LİSTELERİ
    # =====================================================

    def get_by_pozisyon(
        self,
        pozisyon_id: int,
    ) -> list[Personel]:

        stmt = (
            self.active_stmt()
            .where(
                Personel.pozisyon_id == pozisyon_id
            )
            .order_by(
                Personel.ad,
                Personel.soyad,
            )
        )

        return self.all(stmt)


    def get_aktif_personeller(
        self,
    ) -> list[Personel]:

        stmt = (
            self.active_stmt()
            .order_by(
                Personel.ad,
                Personel.soyad,
            )
        )

        return self.all(stmt)

    # =====================================================
    # SEARCH
    # =====================================================

    def search(
        self,
        text: str,
    ) -> list[Personel]:

        stmt = (
            self.active_stmt()
            .where(
                or_(
                    Personel.ad.ilike(f"%{text}%"),
                    Personel.soyad.ilike(f"%{text}%"),
                    Personel.sicil_no.ilike(f"%{text}%"),
                    Personel.tc_kimlik_no.ilike(f"%{text}%"),
                )
            )
            .order_by(
                Personel.ad,
                Personel.soyad,
            )
        )

        return self.all(stmt)

    def toplam_aktif_personel(self) -> int:

        return self.count_stmt(
            self.active_stmt()
        )

        # =====================================================
    # DOĞUM GÜNÜ
    # =====================================================

    def dogum_gunu_olanlar(
        self,
        tarih: date | None = None,
    ) -> list[Personel]:

        if tarih is None:
            tarih = date.today()

        stmt = (
            self.active_stmt()
            .where(
                extract(
                    "day",
                    Personel.dogum_tarihi,
                ) == tarih.day
            )
            .where(
                extract(
                    "month",
                    Personel.dogum_tarihi,
                ) == tarih.month
            )
            .order_by(
                Personel.ad,
                Personel.soyad,
            )
        )

        return self.all(stmt)

    # =====================================================
    # İŞE YENİ BAŞLAYANLAR
    # =====================================================

    def ise_yeni_baslayanlar(
        self,
        gun: int = 30,
    ) -> list[Personel]:

        tarih = date.today() - timedelta(days=gun)

        stmt = (
            self.active_stmt()
            .where(
                Personel.ise_giris_tarihi >= tarih
            )
            .order_by(
                Personel.ise_giris_tarihi.desc()
            )
        )

        return self.all(stmt)

    # =====================================================
    # YAKLAŞAN İZİN HAKKI
    # =====================================================

    def yaklasan_izin_hakki(
        self,
        gun: int = 30,
    ) -> list[Personel]:

        hedef = date.today() + timedelta(days=gun)

        stmt = (
            self.active_stmt()
            .where(
                extract(
                    "month",
                    Personel.ise_giris_tarihi,
                ) == hedef.month
            )
            .where(
                extract(
                    "day",
                    Personel.ise_giris_tarihi,
                ) <= hedef.day
            )
            .order_by(
                Personel.ise_giris_tarihi
            )
        )

        return self.all(stmt)

    # =====================================================
    # KONTROLLER
    # =====================================================

    def sicil_no_var_mi(
        self,
        sicil_no: str,
    ) -> bool:

        return self.exists(
            Personel.sicil_no == sicil_no
        )

    def tc_var_mi(
        self,
        tc_kimlik_no: str,
    ) -> bool:

        return self.exists(
            Personel.tc_kimlik_no == tc_kimlik_no
        )

    def iban_var_mi(
        self,
        iban: str,
    ) -> bool:

        return self.exists(
            Personel.iban == iban
        )

    # =====================================================
    # İSTATİSTİKLER
    # =====================================================

    def toplam_personel(self) -> int:

        return self.count()


    def son_eklenenler(
    self,
    limit: int = 10,
) -> list[Personel]:

        stmt = (
            self.active_stmt()
            .order_by(
                Personel.created_at.desc()
            )
            .limit(limit)
        )

        return self.all(stmt)