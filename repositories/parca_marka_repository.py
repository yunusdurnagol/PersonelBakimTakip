"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : repositories/parca_marka_repository.py
Açıklama   : Parça Marka Repository
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from sqlalchemy.orm import Session

from orm.parca_marka import ParcaMarka
from repositories.base_repository import BaseRepository


class ParcaMarkaRepository(BaseRepository[ParcaMarka]):
    """
    Parça Marka Repository
    """

    def __init__(
        self,
        session: Session,
    ) -> None:

        super().__init__(
            session=session,
            model=ParcaMarka,
        )

    # =====================================================
    # GET METHODS
    # =====================================================

    def get_by_marka_adi(
        self,
        marka_adi: str,
    ) -> ParcaMarka | None:

        return self.get(
            marka_adi=marka_adi,
        )

    # =====================================================
    # SEARCH
    # =====================================================

    def search(
        self,
        text: str,
    ) -> list[ParcaMarka]:

        stmt = (
            self.active_stmt()
            .where(
                ParcaMarka.marka_adi.ilike(
                    f"%{text}%"
                )
            )
            .order_by(
                ParcaMarka.marka_adi
            )
        )

        return self.all(stmt)

    # =====================================================
    # KONTROLLER
    # =====================================================

    def marka_var_mi(
        self,
        marka_adi: str,
    ) -> bool:

        return self.exists(
            ParcaMarka.marka_adi == marka_adi
        )

    # =====================================================
    # İSTATİSTİKLER
    # =====================================================

    def toplam_marka(
        self,
    ) -> int:

        return self.count()