"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : tests/test_parca_service.py
Açıklama   : Parça Service Testleri
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from core.database import SessionLocal
from repositories.parca_repository import ParcaRepository
from services.parca_service import ParcaService


def yazdir(baslik: str):

    print("\n" + "=" * 70)
    print(baslik)
    print("=" * 70)


def main():

    session = SessionLocal()

    try:

        repo = ParcaRepository(session)

        service = ParcaService(repo)

        yazdir("PARÇA SERVICE TESTLERİ")

        # -------------------------------------------------
        # GET
        # -------------------------------------------------

        print("\n1) get_by_id()")

        parca = service.get_by_id(9)

        print(parca)

        # -------------------------------------------------

        print("\n2) get_by_stok_kodu()")

        print(
            service.get_by_stok_kodu(
                "STK-001"
            )
        )

        # -------------------------------------------------

        print("\n3) get_by_orijinal_kod()")

        print(
            service.get_by_orijinal_kod(
                "SKF-6004-2RS"
            )
        )

        # -------------------------------------------------
        # LİSTELEME
        # -------------------------------------------------

        yazdir("LİSTELEME")

        print("\nKategori")

        kategori = service.get_by_kategori(1)

        print("Toplam :", len(kategori))

        for item in kategori:

            print(
                item.stok_kodu,
                item.parca_adi,
            )

        # -------------------------------------------------

        print("\nMarka")

        marka = service.get_by_marka(1)

        print("Toplam :", len(marka))

        # -------------------------------------------------

        print("\nTedarikçi")

        tedarikci = service.get_by_tedarikci(1)

        print("Toplam :", len(tedarikci))

        # -------------------------------------------------
        # RELATIONS
        # -------------------------------------------------

        yazdir("RELATIONS")

        parca = service.get_with_relations(9)

        print(parca)

        if parca:

            print("Kategori :", parca.kategori_adi)

            print("Marka :", parca.marka_adi)

            print("Tedarikçi :", parca.tedarikci_adi)

            print("Hareket :", parca.hareket_sayisi)

            print("Muadil :", parca.muadil_sayisi)

            print(
                "Kullanım Bölümü :",
                parca.kullanim_bolumu_sayisi,
            )

        # -------------------------------------------------
        # SEARCH
        # -------------------------------------------------

        yazdir("SEARCH")

        sonuc = service.search("SKF")

        print("Bulunan :", len(sonuc))

        for item in sonuc:

            print(
                item.stok_kodu,
                item.parca_adi,
            )

        # -------------------------------------------------
        # EXISTS
        # -------------------------------------------------

        yazdir("KONTROLLER")

        print(
            "Stok Kodu Var :",
            service.stok_kodu_var_mi(
                "STK-001"
            ),
        )

        print(
            "Orijinal Kod Var :",
            service.orijinal_kod_var_mi(
                "SKF-6004"
            ),
        )

        # -------------------------------------------------
        # İSTATİSTİKLER
        # -------------------------------------------------

        yazdir("İSTATİSTİK")

        print(
            "Toplam Parça :",
            service.toplam_parca(),
        )

        print(
            "Kategoriye Göre :",
            service.kategoriye_gore_adet(1),
        )

        print(
            "Markaya Göre :",
            service.markaya_gore_adet(1),
        )

        print(
            "Tedarikçiye Göre :",
            service.tedarikciye_gore_adet(1),
        )

        print("\nTESTLER TAMAMLANDI")

    finally:

        session.close()


if __name__ == "__main__":
    main()