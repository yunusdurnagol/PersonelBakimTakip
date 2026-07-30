"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : tests/test_personel_service.py
Açıklama   : Personel Service Testleri
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from datetime import date

from core.database import SessionLocal
from services.personel_service import PersonelService
from repositories.personel_repository import PersonelRepository
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

def yazdir(baslik: str):
    print("\n" + "=" * 70)
    print(baslik)
    print("=" * 70)


def main():

    db = SessionLocal()

    try:

        repo = PersonelRepository(db)
        service = PersonelService(repo)
        yazdir("PERSONEL SERVICE TESTLERİ")

        # -------------------------------------------------
        # GET
        # -------------------------------------------------

        print("\n1) get_by_id()")

        personel = service.get_by_id(20)

        if personel:
            print("OK :",personel.id,)
        else:
            print("Kayıt bulunamadı.")

        # -------------------------------------------------

        print("\n2) get_by_sicil_no()")

        personel = service.get_by_sicil_no("TST-19998cc8")

        if personel:
            print("OK :", personel.ad, personel.soyad)
        else:
            print("Bulunamadı.")

        # -------------------------------------------------

        print("\n3) get_by_tc_kimlik_no()")

        personel = service.get_by_tc_kimlik_no("12111211111")

        print(personel)

        # -------------------------------------------------

        print("\n4) get_by_iban()")

        personel = service.get_by_iban(
            "TR000000000000000000000001"
        )

        print(personel)

        # -------------------------------------------------
        # LİSTELEME
        # -------------------------------------------------

        yazdir("LİSTELEME")

        aktifler = service.get_aktif_personeller()

        print("Aktif Personel :", len(aktifler))

        for p in aktifler[:5]:
            print(
                p.sicil_no,
                p.ad,
                p.soyad,
            )

        # -------------------------------------------------

        print("\nPozisyona Göre")

        personeller = service.get_by_pozisyon(1)

        print("Toplam :", len(personeller))

        # -------------------------------------------------
        # SEARCH
        # -------------------------------------------------

        yazdir("SEARCH")

        sonuc = service.search("Ali")

        print("Bulunan :", len(sonuc))

        # -------------------------------------------------
        # DOĞUM GÜNÜ
        # -------------------------------------------------

        yazdir("DOĞUM GÜNÜ")

        liste = service.dogum_gunu_olanlar()

        print("Bugün :", len(liste))

        # -------------------------------------------------
        # YENİ BAŞLAYANLAR
        # -------------------------------------------------

        yazdir("YENİ BAŞLAYANLAR")

        liste = service.ise_yeni_baslayanlar()

        print("Son 30 Gün :", len(liste))

        # -------------------------------------------------
        # İZİN
        # -------------------------------------------------

        yazdir("YAKLAŞAN İZİN HAKKI")

        liste = service.yaklasan_izin_hakki()

        print("Toplam :", len(liste))

        # -------------------------------------------------
        # EXISTS
        # -------------------------------------------------

        yazdir("KONTROLLER")

        print(
            "Sicil Var :",
            service.sicil_no_var_mi("A001"),
        )

        print(
            "TC Var :",
            service.tc_var_mi("11111111111"),
        )

        print(
            "IBAN Var :",
            service.iban_var_mi(
                "TR000000000000000000000001"
            ),
        )

        # -------------------------------------------------
        # COUNT
        # -------------------------------------------------

        yazdir("İSTATİSTİK")

        print(
            "Toplam Personel :",
            service.toplam_personel(),
        )

        print(
            "Aktif Personel :",
            service.toplam_aktif_personel(),
        )

        print("\nTESTLER TAMAMLANDI")

    finally:

        db.close()


if __name__ == "__main__":
    main()