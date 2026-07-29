"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : repositories/tedarikci_repository.py
Açıklama   : Tedarikçi Repository
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from sqlalchemy.orm import Session

from orm.tedarikci import Tedarikci
from repositories.base_repository import BaseRepository


class TedarikciRepository(BaseRepository[Tedarikci]):
    """
    Tedarikçi Repository
    """

    def __init__(
        self,
        session: Session,
    ) -> None:

        super().__init__(
            session=session,
            model=Tedarikci,
        )

    # =====================================================
    # GET METHODS
    # =====================================================

    def get_by_firma_adi(
        self,
        firma_adi: str,
    ) -> Tedarikci | None:

        return self.get(
            firma_adi=firma_adi,
        )

    def get_by_vergi_no(
        self,
        vergi_no: str,
    ) -> Tedarikci | None:

        return self.get(
            vergi_no=vergi_no,
        )

    # =====================================================
    # SEARCH
    # =====================================================

    def search(
        self,
        text: str,
    ) -> list[Tedarikci]:

        stmt = (
            self.active_stmt()
            .where(
                Tedarikci.firma_adi.ilike(f"%{text}%")
            )
            .order_by(
                Tedarikci.firma_adi
            )
        )

        return self.all(stmt)

    # =====================================================
    # KONTROLLER
    # =====================================================

    def firma_var_mi(
        self,
        firma_adi: str,
    ) -> bool:

        return self.exists(
            Tedarikci.firma_adi == firma_adi
        )

    def vergi_no_var_mi(
        self,
        vergi_no: str,
    ) -> bool:

        return self.exists(
            Tedarikci.vergi_no == vergi_no
        )

    # =====================================================
    # İSTATİSTİKLER
    # =====================================================

    def toplam_tedarikci(
        self,
    ) -> int:

        return self.count()