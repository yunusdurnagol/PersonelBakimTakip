"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : tests/test_parca_muadili_service.py
Açıklama   : Parça Muadili Service Testleri
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from core.database import SessionLocal
from repositories.parca_muadili_repository import (
    ParcaMuadiliRepository,
)
from services.parca_muadili_service import (
    ParcaMuadiliService,
)


def yazdir(baslik: str):
    print("\n" + "=" * 70)
    print(baslik)
    print("=" * 70)


def main():

    session = SessionLocal()

    try:

        repo = ParcaMuadiliRepository(session)
        service = ParcaMuadiliService(repo)

        yazdir("PARÇA MUADİLİ SERVICE TESTLERİ")

        # -------------------------------------------------
        # GET
        # -------------------------------------------------

        print("\n1) get_by_id()")
        print(service.get_by_id(1))

        print("\n2) get_by_parca()")

        liste = service.get_by_parca(8)

        print("Toplam :", len(liste))

        for item in liste:
            print(item)

        print("\n3) get_by_muadil_parca()")

        liste = service.get_by_muadil_parca(9)

        print("Toplam :", len(liste))

        for item in liste:
            print(item)

        # -------------------------------------------------
        # SEARCH
        # -------------------------------------------------

        yazdir("SEARCH")

        sonuc = service.search(8)

        print("Bulunan :", len(sonuc))

        for item in sonuc:
            print(item)

        # -------------------------------------------------
        # KONTROLLER
        # -------------------------------------------------

        yazdir("KONTROLLER")

        print(
            "Muadil Var :",
            service.muadil_var_mi(
                8,
                9,
            ),
        )

        # -------------------------------------------------
        # İSTATİSTİK
        # -------------------------------------------------

        yazdir("İSTATİSTİK")

        print(
            "Toplam Muadil :",
            service.toplam_muadil(),
        )

        print(
            "Parça Muadil Sayısı :",
            service.parca_muadil_sayisi(
                8,
            ),
        )

        print("\nTESTLER TAMAMLANDI")

    finally:

        session.close()


if __name__ == "__main__":
    main()