"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : tests/test_parca_marka_service.py
Açıklama   : Parça Marka Service Testleri
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from core.database import SessionLocal
from repositories.parca_marka_repository import ParcaMarkaRepository
from services.parca_marka_service import ParcaMarkaService


def yazdir(baslik: str):
    print("\n" + "=" * 70)
    print(baslik)
    print("=" * 70)


def main():

    session = SessionLocal()

    try:

        repo = ParcaMarkaRepository(session)
        service = ParcaMarkaService(repo)

        yazdir("PARÇA MARKA SERVICE TESTLERİ")

        # -------------------------------------------------
        # GET
        # -------------------------------------------------

        print("\n1) get_by_id()")
        print(service.get_by_id(1))

        print("\n2) get_by_marka_adi()")
        print(service.get_by_marka_adi("SKF"))

        # -------------------------------------------------
        # LİSTELEME
        # -------------------------------------------------

        yazdir("LİSTELEME")

        markalar = service.get_all()

        print("Toplam Marka :", len(markalar))

        for marka in markalar:
            print(
                marka.id,
                marka.ad,
            )

        # -------------------------------------------------
        # SEARCH
        # -------------------------------------------------

        yazdir("SEARCH")

        sonuc = service.search("SK")

        print("Bulunan :", len(sonuc))

        for marka in sonuc:
            print(marka.ad)

        # -------------------------------------------------
        # KONTROLLER
        # -------------------------------------------------

        yazdir("KONTROLLER")

        print(
            "Marka Var :",
            service.marka_var_mi("SKF"),
        )

        print(
            "Marka Var :",
            service.marka_var_mi("XXXX"),
        )

        # -------------------------------------------------
        # İSTATİSTİKLER
        # -------------------------------------------------

        yazdir("İSTATİSTİKLER")

        print(
            "Toplam Marka :",
            service.toplam_marka(),
        )

        print("\nTESTLER BAŞARIYLA TAMAMLANDI")

    finally:

        session.close()


if __name__ == "__main__":
    main()