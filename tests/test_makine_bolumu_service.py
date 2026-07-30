"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : tests/test_makine_bolumu_service.py
Açıklama   : Makine Bölümü Service Testleri
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from core.database import SessionLocal
from repositories.makine_bolumu_repository import MakineBolumuRepository
from services.makine_bolumu_service import MakineBolumuService


def yazdir(baslik: str):
    print("\n" + "=" * 70)
    print(baslik)
    print("=" * 70)


def main():

    session = SessionLocal()

    try:

        repo = MakineBolumuRepository(session)
        service = MakineBolumuService(repo)

        yazdir("MAKİNE BÖLÜMÜ SERVICE TESTLERİ")

        # -------------------------------------------------
        # GET
        # -------------------------------------------------

        print("\n1) get_by_id()")
        print(service.get_by_id(1))

        print("\n2) get_by_ad()")
        print(service.get_by_ad("Ram"))

        # -------------------------------------------------
        # LİSTELEME
        # -------------------------------------------------

        yazdir("LİSTELEME")

        bolumler = service.get_all()

        print("Toplam :", len(bolumler))

        for bolum in bolumler:

            print(
                bolum.id,
                bolum.ad,
            )

        # -------------------------------------------------
        # KONTROLLER
        # -------------------------------------------------

        yazdir("KONTROLLER")

        print(
            "Ad Var :",
            service.ad_var_mi("Ram"),
        )

        print(
            "Ad Var :",
            service.ad_var_mi("XYZ"),
        )

        # -------------------------------------------------
        # İSTATİSTİKLER
        # -------------------------------------------------

        yazdir("İSTATİSTİKLER")

        print(
            "Toplam Bölüm :",
            service.toplam_bolum(),
        )

        print("\nTESTLER BAŞARIYLA TAMAMLANDI")

    finally:

        session.close()


if __name__ == "__main__":
    main()