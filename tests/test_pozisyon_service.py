"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : tests/test_pozisyon_service.py
Açıklama   : Pozisyon Service Testleri
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from core.database import SessionLocal
from repositories.pozisyon_repository import PozisyonRepository
from services.pozisyon_service import PozisyonService


def yazdir(baslik: str):
    print("\n" + "=" * 70)
    print(baslik)
    print("=" * 70)


def main():

    session = SessionLocal()

    try:

        repo = PozisyonRepository(session)

        service = PozisyonService(repo)

        yazdir("POZİSYON SERVICE TESTLERİ")

        # =====================================================
        # get_by_id
        # =====================================================

        print("\n1) get_by_id()")

        pozisyon = service.get_by_id(1)

        if pozisyon:
            print("OK :", pozisyon.id, "-", pozisyon.ad)
        else:
            print("Kayıt bulunamadı.")

        # =====================================================
        # get_by_ad
        # =====================================================

        print("\n2) get_by_ad()")

        pozisyon = service.get_by_ad("Muhasebe")

        if pozisyon:
            print("OK :", pozisyon.id, "-", pozisyon.ad)
        else:
            print("Bulunamadı.")

        # =====================================================
        # get_all
        # =====================================================

        yazdir("GET ALL")

        liste = service.get_all()

        print("Toplam :", len(liste))

        for item in liste:

            print(
                item.id,
                item.ad,
            )

        # =====================================================
        # SEARCH
        # =====================================================

        yazdir("SEARCH")

        sonuc = service.search("Operatör")

        print("Bulunan :", len(sonuc))

        for item in sonuc:

            print(item.ad)

        # =====================================================
        # EXISTS
        # =====================================================

        yazdir("KONTROLLER")

        print(
            "Muhasebe Var :",
            service.ad_var_mi("Muhasebe"),
        )

        print(
            "XYZ Var :",
            service.ad_var_mi("XYZ"),
        )

        # =====================================================
        # COUNT
        # =====================================================

        yazdir("İSTATİSTİK")

        print(
            "Toplam Pozisyon :",
            service.toplam_pozisyon(),
        )

        print("\nTESTLER BAŞARIYLA TAMAMLANDI")

    finally:

        session.close()


if __name__ == "__main__":
    main()