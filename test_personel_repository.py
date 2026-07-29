"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : tests/test_personel_repository.py
Açıklama   : Personel Repository Testi
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from datetime import date
from decimal import Decimal

from core.database import SessionLocal
from orm.personel import Personel
from repositories.personel_repository import PersonelRepository


def main():

    session = SessionLocal()

    try:

        repo = PersonelRepository(session)

        print("=" * 60)
        print("PERSONEL REPOSITORY TESTİ")
        print("=" * 60)

        # -------------------------------------------------
        # CREATE
        # -------------------------------------------------
        personel = Personel(
            sicil_no="TST001",
            tc_kimlik_no="12111241111",
            ad="Test",
            soyad="Personel",
            ise_giris_tarihi=date.today(),
            pozisyon_id=1,
            telefon="5555555555",
            email="test@test.com",
            maas=Decimal("35000"),
            iban="TR000000000000000000000001",
        )

        repo.create(personel)

        print("✅ CREATE")

        # -------------------------------------------------
        # GET
        # -------------------------------------------------

        p = repo.get_by_sicil_no("TST001")

        assert p is not None

        print("✅ GET BY SİCİL")

        # -------------------------------------------------
        # EXISTS
        # -------------------------------------------------

        assert repo.sicil_no_var_mi("TST001")

        print("✅ EXISTS")

        # -------------------------------------------------
        # SEARCH
        # -------------------------------------------------

        sonuc = repo.search("Test")

        assert len(sonuc) > 0

        print("✅ SEARCH")

        # -------------------------------------------------
        # UPDATE
        # -------------------------------------------------

       # UPDATE

        repo.update_fields(
            p,
            {
                "telefon": "5000000000",
            },
        )

        print("✅ UPDATE")
        print("✅ UPDATE")

        # -------------------------------------------------
        # COUNT
        # -------------------------------------------------

        print(
            "Toplam Personel :",
            repo.toplam_personel(),
        )

        print(
            "Aktif Personel :",
            repo.toplam_aktif_personel(),
        )

        print("✅ COUNT")

        # -------------------------------------------------
        # SOFT DELETE
        # -------------------------------------------------

        repo.soft_delete(p)

        print("✅ SOFT DELETE")

        # -------------------------------------------------
        # RESTORE
        # -------------------------------------------------

        repo.restore(p)

        print("✅ RESTORE")

        # -------------------------------------------------
        # DELETE
        # -------------------------------------------------

        repo.delete(p)

        print("✅ DELETE")

        print("=" * 60)
        print("TÜM TESTLER BAŞARILI")
        print("=" * 60)

    finally:

        session.close()


if __name__ == "__main__":
    main()