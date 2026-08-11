"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : repositories/personel_izin_repository.py
Açıklama   : Personel İzin Repository
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from datetime import date

from sqlalchemy.orm import Session

from orm.personel_izin import PersonelIzin
from repositories.base_repository import BaseRepository


class PersonelIzinRepository(
    BaseRepository[PersonelIzin]
):
    """
    Personel İzin Repository.

    UI veya Service katmanı veritabanına
    doğrudan erişmez.

    UI
        ↓
    PersonelIzinService
        ↓
    PersonelIzinRepository
        ↓
    PersonelIzin ORM
    """

    def __init__(
        self,
        session: Session,
    ) -> None:

        super().__init__(
            session=session,
            model=PersonelIzin,
        )

    # =====================================================
    # GET METHODS
    # =====================================================

    def get_by_personel(
        self,
        personel_id: int,
    ) -> list[PersonelIzin]:
        """
        Belirli personele ait izinleri getirir.

        En son eklenen izin üstte görünür.
        """

        stmt = (
            self.active_stmt()
            .where(
                PersonelIzin.personel_id == personel_id
            )
            .order_by(
                PersonelIzin.id.desc()
            )
        )

        return self.all(stmt)

    # =====================================================
    # TÜM İZİNLER
    # =====================================================

    def get_tum_izinler(
        self,
    ) -> list[PersonelIzin]:
        """
        Tüm aktif izin kayıtlarını getirir.

        En son eklenen izin üstte görünür.
        """

        stmt = (
            self.active_stmt()
            .order_by(
                PersonelIzin.id.desc()
            )
        )

        return self.all(stmt)

    # =====================================================
    # TARİH ARALIĞI
    # =====================================================

    def get_by_tarih(
        self,
        tarih: date,
    ) -> list[PersonelIzin]:
        """
        Belirli bir tarihte izinli olan personelleri getirir.
        """

        stmt = (
            self.active_stmt()
            .where(
                PersonelIzin.izin_baslangic <= tarih
            )
            .where(
                PersonelIzin.izin_bitis >= tarih
            )
            .order_by(
                PersonelIzin.id.desc()
            )
        )

        return self.all(stmt)

    # =====================================================
    # SEARCH
    # =====================================================

    def search(
        self,
        text: str,
    ) -> list[PersonelIzin]:
        """
        İzin nedeni ve açıklama üzerinden arama yapar.
        """

        text = text.strip()

        if not text:
            return self.get_tum_izinler()

        stmt = (
            self.active_stmt()
            .where(
                PersonelIzin.izin_nedeni.ilike(
                    f"%{text}%"
                )
            )
            .order_by(
                PersonelIzin.id.desc()
            )
        )

        return self.all(stmt)

    # =====================================================
    # KONTROLLER
    # =====================================================

    def personel_izin_var_mi(
        self,
        personel_id: int,
    ) -> bool:
        """
        Personelin en az bir izin kaydı var mı?
        """

        return self.exists(
            PersonelIzin.personel_id == personel_id
        )

    # =====================================================
    # İSTATİSTİKLER
    # =====================================================

    def toplam_izin(
        self,
    ) -> int:
        """
        Aktif toplam izin kayıt sayısını döndürür.
        """

        return self.count()

    # =====================================================
    # PERSONELİN KULLANDIĞI TOPLAM GÜN
    # =====================================================

    def toplam_kullanilan_izin_gunu(
        self,
        personel_id: int,
    ) -> int:
        """
        Personelin kayıtlı izinlerinde
        manuel girilmiş izin günlerini toplar.

        DİKKAT:
        İzin hakkı hesaplamaz.
        Sadece kayıtlı izin_gun_sayisi değerlerini toplar.
        """

        izinler = self.get_by_personel(
            personel_id
        )

        return sum(
            izin.izin_gun_sayisi
            for izin in izinler
        )