"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : tests/test_parca_kullanim_bolumu_service.py
Açıklama   : Parça Kullanım Bölümü Service Testleri
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from core.database import SessionLocal
from repositories.parca_kullanim_bolumu_repository import (
    ParcaKullanimBolumuRepository,
)
from services.parca_kullanim_bolumu_service import (
    ParcaKullanimBolumuService,
)


def yazdir(baslik: str):
    print("\n" + "=" * 70)
    print(baslik)
    print("=" * 70)


def main():

    session = SessionLocal()

    try:

        repo = ParcaKullanimBolumuRepository(session)
        service = ParcaKullanimBolumuService(repo)

        yazdir("PARÇA KULLANIM BÖLÜMÜ SERVICE TESTLERİ")

        print("\n1) get_by_id()")
        print(service.get_by_id(1))

        print("\n2) get_by_parca()")
        liste = service.get_by_parca(8)
        print("Toplam :", len(liste))
        for item in liste:
            print(item)

        print("\n3) get_by_bolum()")
        liste = service.get_by_bolum(1)
        print("Toplam :", len(liste))
        for item in liste:
            print(item)

        yazdir("SEARCH")

        sonuc = service.search("")
        print("Bulunan :", len(sonuc))

        yazdir("KONTROLLER")

        print(
            "Kullanım Var :",
            service.kullanim_var_mi(
                8,
                1,
            ),
        )

        yazdir("İSTATİSTİK")

        print(
            "Toplam Kullanım :",
            service.toplam_kullanim(),
        )

        print(
            "Parça Kullanım Sayısı :",
            service.parca_kullanim_sayisi(
                8,
            ),
        )

        print(
            "Bölüm Kullanım Sayısı :",
            service.bolum_kullanim_sayisi(
                1,
            ),
        )

        print("\nTESTLER TAMAMLANDI")

    finally:
        session.close()


if __name__ == "__main__":
    main()