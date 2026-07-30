"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : repositories/personel_izin_repository.py
Açıklama   : Personel İzin Repository
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from datetime import date

from sqlalchemy.orm import Session

from orm.personel_izin import PersonelIzin
from repositories.base_repository import BaseRepository


class PersonelIzinRepository(BaseRepository[PersonelIzin]):
    """
    Personel İzin Repository
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

        stmt = (
            self.active_stmt()
            .where(
                PersonelIzin.personel_id == personel_id
            )
            .order_by(
                PersonelIzin.izin_baslangic.desc()
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

        stmt = (
            self.active_stmt()
            .where(
                PersonelIzin.izin_baslangic <= tarih
            )
            .where(
                PersonelIzin.izin_bitis >= tarih
            )
            .order_by(
                PersonelIzin.izin_baslangic
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

        stmt = (
            self.active_stmt()
            .where(
                PersonelIzin.izin_nedeni.ilike(
                    f"%{text}%"
                )
            )
            .order_by(
                PersonelIzin.izin_baslangic.desc()
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

        return self.exists(
            PersonelIzin.personel_id == personel_id
        )

    # =====================================================
    # İSTATİSTİKLER
    # =====================================================

    def toplam_izin(
        self,
    ) -> int:

        return self.count()