"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : tests/test_personel_izin_service.py
Açıklama   : Personel İzin Service Testleri
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from pathlib import Path
import sys
from datetime import date

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from core.database import SessionLocal
from repositories.personel_izin_repository import (
    PersonelIzinRepository,
)
from services.personel_izin_service import (
    PersonelIzinService,
)


def yazdir(baslik: str):
    print("\n" + "=" * 70)
    print(baslik)
    print("=" * 70)


def main():

    session = SessionLocal()

    try:

        repo = PersonelIzinRepository(session)
        service = PersonelIzinService(repo)

        yazdir("PERSONEL İZİN SERVICE TESTLERİ")

        # -------------------------------------------------
        # GET
        # -------------------------------------------------

        print("\n1) get_by_id()")
        print(service.get_by_id(6))

        print("\n2) get_by_personel()")

        liste = service.get_by_personel(15)

        print("Toplam :", len(liste))

        for item in liste:
            print(item)

        # -------------------------------------------------

        print("\n3) get_by_tarih()")

        liste = service.get_by_tarih(
            date.today()
        )

        print("Bugün izinli :", len(liste))

        for item in liste:
            print(item)

        # -------------------------------------------------
        # SEARCH
        # -------------------------------------------------

        yazdir("SEARCH")

        sonuc = service.search("Yıllık")

        print("Bulunan :", len(sonuc))

        for item in sonuc:
            print(item)

        # -------------------------------------------------
        # KONTROLLER
        # -------------------------------------------------

        yazdir("KONTROLLER")

        print(
            "Personelin İzni Var :",
            service.personel_izin_var_mi(1),
        )

        # -------------------------------------------------
        # İSTATİSTİKLER
        # -------------------------------------------------

        yazdir("İSTATİSTİK")

        print(
            "Toplam İzin :",
            service.toplam_izin(),
        )

        print("\nTESTLER TAMAMLANDI")

    finally:

        session.close()


if __name__ == "__main__":
    main()