"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : tests/test_tedarikci_service.py
Açıklama   : Tedarikçi Service Testleri
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from core.database import SessionLocal
from repositories.tedarikci_repository import TedarikciRepository
from services.tedarikci_service import TedarikciService


def yazdir(baslik: str):
    print("\n" + "=" * 70)
    print(baslik)
    print("=" * 70)


def main():

    session = SessionLocal()

    try:

        repo = TedarikciRepository(session)
        service = TedarikciService(repo)

        yazdir("TEDARİKÇİ SERVICE TESTLERİ")

        # -------------------------------------------------
        # GET
        # -------------------------------------------------

        print("\n1) get_by_id()")

        tedarikci = service.get_by_id(1)

        print(tedarikci)

        # -------------------------------------------------

        print("\n2) get_by_firma_adi()")

        tedarikci = service.get_by_firma_adi(
            "SKF Türkiye"
        )

        print(tedarikci)

        # -------------------------------------------------

        print("\n3) get_by_vergi_no()")

        tedarikci = service.get_by_vergi_no(
            "1234567890"
        )

        print(tedarikci)

        # -------------------------------------------------
        # LİSTELEME
        # -------------------------------------------------

        yazdir("LİSTELEME")

        liste = service.get_all()

        print("Toplam :", len(liste))

        for item in liste:

            print(
                item.id,
                item.firma_adi,
            )

        # -------------------------------------------------
        # SEARCH
        # -------------------------------------------------

        yazdir("SEARCH")

        sonuc = service.search("SKF")

        print("Bulunan :", len(sonuc))

        for item in sonuc:

            print(item.firma_adi)

        # -------------------------------------------------
        # KONTROLLER
        # -------------------------------------------------

        yazdir("KONTROLLER")

        print(
            "Firma Var :",
            service.firma_var_mi(
                "SKF Türkiye"
            ),
        )

        print(
            "Vergi No Var :",
            service.vergi_no_var_mi(
                "1234567890"
            ),
        )

        # -------------------------------------------------
        # İSTATİSTİKLER
        # -------------------------------------------------

        yazdir("İSTATİSTİKLER")

        print(
            "Toplam Tedarikçi :",
            service.toplam_tedarikci(),
        )

        print("\nTESTLER BAŞARIYLA TAMAMLANDI")

    finally:

        session.close()


if __name__ == "__main__":
    main()