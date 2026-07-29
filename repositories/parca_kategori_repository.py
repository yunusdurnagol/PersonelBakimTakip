"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : repositories/parca_kategori_repository.py
Açıklama   : Parça Kategori Repository
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from sqlalchemy.orm import Session

from orm.parca_kategori import ParcaKategori
from repositories.base_repository import BaseRepository


class ParcaKategoriRepository(BaseRepository[ParcaKategori]):
    """
    Parça Kategori Repository
    """

    def __init__(
        self,
        session: Session,
    ) -> None:

        super().__init__(
            session=session,
            model=ParcaKategori,
        )

    # =====================================================
    # GET METHODS
    # =====================================================

    def get_by_kategori_adi(
        self,
        kategori_adi: str,
    ) -> ParcaKategori | None:

        return self.get(
            kategori_adi=kategori_adi,
        )

    # =====================================================
    # SEARCH
    # =====================================================

    def search(
        self,
        text: str,
    ) -> list[ParcaKategori]:

        stmt = (
            self.active_stmt()
            .where(
                ParcaKategori.kategori_adi.ilike(
                    f"%{text}%"
                )
            )
            .order_by(
                ParcaKategori.kategori_adi
            )
        )

        return self.all(stmt)

    # =====================================================
    # KONTROLLER
    # =====================================================

    def kategori_var_mi(
        self,
        kategori_adi: str,
    ) -> bool:

        return self.exists(
            ParcaKategori.kategori_adi == kategori_adi
        )

    # =====================================================
    # İSTATİSTİKLER
    # =====================================================

    def toplam_kategori(
        self,
    ) -> int:

        return self.count()