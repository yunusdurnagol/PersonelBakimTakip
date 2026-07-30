"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : tests/test_parca_kategori_service.py
Açıklama   : Parça Kategori Service Testleri
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from core.database import SessionLocal
from repositories.parca_kategori_repository import ParcaKategoriRepository
from services.parca_kategori_service import ParcaKategoriService


def yazdir(baslik: str):
    print("\n" + "=" * 70)
    print(baslik)
    print("=" * 70)


def main():

    session = SessionLocal()

    try:

        repo = ParcaKategoriRepository(session)
        service = ParcaKategoriService(repo)

        yazdir("PARÇA KATEGORİ SERVICE TESTLERİ")

        # -------------------------------------------------
        # GET
        # -------------------------------------------------

        print("\n1) get_by_id()")

        kategori = service.get_by_id(1)

        print(kategori)

        # -------------------------------------------------

        print("\n2) get_by_kategori_adi()")

        kategori = service.get_by_kategori_adi("Rulman")

        print(kategori)

        # -------------------------------------------------
        # LİSTELEME
        # -------------------------------------------------

        yazdir("LİSTELEME")

        kategoriler = service.get_all()

        print("Toplam Kategori :", len(kategoriler))

        for kategori in kategoriler:

            print(
                kategori.id,
                kategori.ad,
            )

        # -------------------------------------------------
        # SEARCH
        # -------------------------------------------------

        yazdir("SEARCH")

        sonuc = service.search("Rul")

        print("Bulunan :", len(sonuc))

        for kategori in sonuc:

            print(kategori.ad)

        # -------------------------------------------------
        # KONTROLLER
        # -------------------------------------------------

        yazdir("KONTROLLER")

        print(
            "Kategori Var :",
            service.kategori_var_mi("Rulman"),
        )

        print(
            "Kategori Var :",
            service.kategori_var_mi("XYZ"),
        )

        # -------------------------------------------------
        # İSTATİSTİKLER
        # -------------------------------------------------

        yazdir("İSTATİSTİKLER")

        print(
            "Toplam Kategori :",
            service.toplam_kategori(),
        )

        print("\nTESTLER BAŞARIYLA TAMAMLANDI")

    finally:

        session.close()


if __name__ == "__main__":
    main()