"""
=========================================================
Tedarikci Repository Testi
=========================================================
"""

from uuid import uuid4

from core.database import SessionLocal
from orm.tedarikci import Tedarikci
from repositories.tedarikci_repository import TedarikciRepository


TEST_FIRMA = f"TEST TEDARIKCI {uuid4().hex[:8]}"
TEST_VERGI = uuid4().hex[:10]


def main():

    db = SessionLocal()
    repo = TedarikciRepository(db)

    print("=" * 60)
    print("TEDARİKÇİ REPOSITORY TESTİ")
    print("=" * 60)

    # -------------------------------------------------
    # Eski test kaydı varsa temizle
    # -------------------------------------------------

    eski = repo.get_by_firma_adi(TEST_FIRMA)

    if eski:
        repo.delete(eski)

    # -------------------------------------------------
    # CREATE
    # -------------------------------------------------

    tedarikci = Tedarikci(
        firma_adi=TEST_FIRMA,
        yetkili="Ahmet Yılmaz",
        telefon="05321234567",
        email="test@test.com",
        adres="İstanbul",
        vergi_dairesi="Çatalca",
        vergi_no=TEST_VERGI,
        aciklama="Repository Testi",
    )

    repo.create(tedarikci)

    print("✅ CREATE")

    # -------------------------------------------------
    # GET BY FİRMA
    # -------------------------------------------------

    bulunan = repo.get_by_firma_adi(TEST_FIRMA)

    assert bulunan is not None

    print("✅ GET BY FİRMA")

    # -------------------------------------------------
    # GET BY VERGİ NO
    # -------------------------------------------------

    bulunan = repo.get_by_vergi_no(TEST_VERGI)

    assert bulunan is not None

    print("✅ GET BY VERGİ NO")

    # -------------------------------------------------
    # EXISTS
    # -------------------------------------------------

    assert repo.firma_var_mi(TEST_FIRMA)
    assert repo.vergi_no_var_mi(TEST_VERGI)

    print("✅ EXISTS")

    # -------------------------------------------------
    # SEARCH
    # -------------------------------------------------

    sonuc = repo.search("TEST")

    assert len(sonuc) > 0

    print("✅ SEARCH")

    # -------------------------------------------------
    # UPDATE
    # -------------------------------------------------

    repo.update_fields(
        tedarikci,
        {
            "yetkili": "Mehmet Kaya",
            "telefon": "05555555555",
        },
    )

    print("✅ UPDATE")

    # -------------------------------------------------
    # COUNT
    # -------------------------------------------------

    toplam = repo.toplam_tedarikci()

    assert toplam > 0

    print(f"✅ COUNT ({toplam})")

    # -------------------------------------------------
    # DELETE
    # -------------------------------------------------

    repo.delete(tedarikci)

    print("✅ SOFT DELETE")

    print("=" * 60)
    print("TÜM TESTLER BAŞARILI")
    print("=" * 60)

    db.close()


if __name__ == "__main__":
    main()