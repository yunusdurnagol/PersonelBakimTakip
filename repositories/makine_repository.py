"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : repositories/makine_repository.py
Açıklama   : Makine Repository
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from sqlalchemy import or_
from sqlalchemy.orm import Session

from orm.makine import Makine
from repositories.base_repository import BaseRepository


class MakineRepository(BaseRepository[Makine]):
    """
    Makine Repository
    """

    def __init__(
        self,
        session: Session,
    ) -> None:

        super().__init__(
            session=session,
            model=Makine,
        )

    # =====================================================
    # GET METHODS
    # =====================================================

    def get_by_makine_kodu(
        self,
        makine_kodu: str,
    ) -> Makine | None:

        return self.get(
            makine_kodu=makine_kodu,
        )

    def get_by_seri_no(
        self,
        seri_no: str,
    ) -> Makine | None:

        return self.get(
            seri_no=seri_no,
        )

    def get_by_bolum(
        self,
        bolum_id: int,
    ) -> list[Makine]:

        stmt = (
            self.active_stmt()
            .where(
                Makine.bolum_id == bolum_id
            )
            .order_by(
                Makine.makine_kodu
            )
        )

        return self.all(stmt)

    # =====================================================
    # LİSTELER
    # =====================================================

    def get_tum_makineler(
        self,
    ) -> list[Makine]:

        stmt = (
            self.active_stmt()
            .order_by(
                Makine.makine_kodu
            )
        )

        return self.all(stmt)

    # =====================================================
    # SEARCH
    # =====================================================

    def search(
        self,
        text: str,
    ) -> list[Makine]:

        stmt = (
            self.active_stmt()
            .where(
                or_(
                    Makine.makine_kodu.ilike(f"%{text}%"),
                    Makine.makine_adi.ilike(f"%{text}%"),
                    Makine.seri_no.ilike(f"%{text}%"),
                )
            )
            .order_by(
                Makine.makine_kodu
            )
        )

        return self.all(stmt)

    # =====================================================
    # KONTROLLER
    # =====================================================

    def makine_kodu_var_mi(
        self,
        makine_kodu: str,
    ) -> bool:

        return self.exists(
            Makine.makine_kodu == makine_kodu
        )

    def seri_no_var_mi(
        self,
        seri_no: str,
    ) -> bool:

        return self.exists(
            Makine.seri_no == seri_no
        )

    # =====================================================
    # İSTATİSTİKLER
    # =====================================================

    def toplam_makine(
        self,
    ) -> int:

        return self.count()