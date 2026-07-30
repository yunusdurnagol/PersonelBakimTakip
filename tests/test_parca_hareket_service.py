"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : tests/test_parca_hareket_service.py
Açıklama   : Parça Hareket Service Testleri
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from datetime import date

from core.database import SessionLocal
from repositories.parca_hareket_repository import ParcaHareketRepository
from services.parca_hareket_service import ParcaHareketService


def yazdir(baslik: str):
    print("\n" + "=" * 70)
    print(baslik)
    print("=" * 70)


def main():

    session = SessionLocal()

    try:

        repo = ParcaHareketRepository(session)
        service = ParcaHareketService(repo)

        yazdir("PARÇA HAREKET SERVICE TESTLERİ")

        # -------------------------------------------------

        print("\n1) get_by_id()")

        veri = service.get_by_id(32)

        print(veri)

        # -------------------------------------------------

        print("\n2) get_by_fatura_no()")

        print(
            service.get_by_fatura_no(
                "FAT001"
            )
        )

        # -------------------------------------------------

        yazdir("LİSTELEME")

        print(
            "Parçaya Göre :",
            len(
                service.get_by_parca(1)
            ),
        )

        print(
            "Makine Bölümüne Göre :",
            len(
                service.get_by_makine_bolumu(1)
            ),
        )

        print(
            "Tedarikçiye Göre :",
            len(
                service.get_by_tedarikci(1)
            ),
        )

        print(
            "Tarihe Göre :",
            len(
                service.get_by_tarih(
                    date.today()
                )
            ),
        )

        # -------------------------------------------------

        yazdir("RELATIONS")

        print(
            service.get_with_relations(1)
        )

        # -------------------------------------------------

        yazdir("KONTROLLER")

        print(
            "Fatura Var :",
            service.fatura_no_var_mi(
                "FAT001"
            ),
        )

        # -------------------------------------------------

        yazdir("İSTATİSTİKLER")

        print(
            "Toplam Hareket :",
            service.toplam_hareket(),
        )

        print(
            "Parçaya Göre :",
            service.parcaya_gore_adet(1),
        )

        print(
            "Makine Bölümüne Göre :",
            service.makine_bolumune_gore_adet(1),
        )

        print(
            "Tedarikçiye Göre :",
            service.tedarikciye_gore_adet(1),
        )

        print("\nTESTLER BAŞARILI")

    finally:

        session.close()


if __name__ == "__main__":
    main()