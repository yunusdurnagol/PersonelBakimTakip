"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : tests/test_personel_evrak_service.py
Açıklama   : Personel Evrak Service Testleri
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from core.database import SessionLocal
from repositories.personel_evrak_repository import (
    PersonelEvrakRepository,
)
from services.personel_evrak_service import (
    PersonelEvrakService,
)


def yazdir(baslik: str):
    print("\n" + "=" * 70)
    print(baslik)
    print("=" * 70)


def main():

    session = SessionLocal()

    try:

        repo = PersonelEvrakRepository(session)
        service = PersonelEvrakService(repo)

        yazdir("PERSONEL EVRAK SERVICE TESTLERİ")

        # -------------------------------------------------
        # GET
        # -------------------------------------------------

        print("\n1) get_by_id()")
        print(service.get_by_id(1))

        print("\n2) get_by_personel()")

        liste = service.get_by_personel(1)

        print("Toplam :", len(liste))

        for item in liste:
            print(item)

        print("\n3) get_by_evrak_adi()")

        print(
            service.get_by_evrak_adi(
                "Kimlik Fotokopisi"
            )
        )

        # -------------------------------------------------
        # SEARCH
        # -------------------------------------------------

        yazdir("SEARCH")

        sonuc = service.search("Kimlik")

        print("Bulunan :", len(sonuc))

        for item in sonuc:
            print(item)

        # -------------------------------------------------
        # KONTROLLER
        # -------------------------------------------------

        yazdir("KONTROLLER")

        print(
            "Evrak Var :",
            service.evrak_var_mi(
                1,
                "Kimlik Fotokopisi",
            ),
        )

        # -------------------------------------------------
        # İSTATİSTİK
        # -------------------------------------------------

        yazdir("İSTATİSTİK")

        print(
            "Toplam Evrak :",
            service.toplam_evrak(),
        )

        print(
            "Personele Göre Evrak Sayısı :",
            service.personele_gore_evrak_sayisi(
                1,
            ),
        )

        print("\nTESTLER TAMAMLANDI")

    finally:

        session.close()


if __name__ == "__main__":
    main()