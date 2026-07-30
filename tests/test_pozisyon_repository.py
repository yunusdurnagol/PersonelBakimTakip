"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : test_pozisyon_repository.py
Açıklama   : Pozisyon Repository Testleri
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from core.database import SessionLocal
from orm.pozisyon import Pozisyon
from repositories.pozisyon_repository import PozisyonRepository
from uuid import uuid4



def main():

    print("=" * 60)
    print("POZİSYON REPOSITORY TESTİ")
    print("=" * 60)

    session = SessionLocal()
    repo = PozisyonRepository(session)
    TEST_POZISYON = f"TEST_{uuid4().hex[:8]}"
    

    # -------------------------------------------------
    # Eski kayıt varsa sil
    # -------------------------------------------------

    eski = repo.get_by_ad(TEST_POZISYON)

    if eski:
        repo.hard_delete(eski)

    # -------------------------------------------------
    # CREATE
    # -------------------------------------------------

    pozisyon = Pozisyon(
        ad=TEST_POZISYON,
        aciklama="TEST_POZISYON",
    )

    repo.create(pozisyon)

    print("✅ CREATE")

    # -------------------------------------------------
    # GET BY AD
    # -------------------------------------------------

    p = repo.get_by_ad(TEST_POZISYON)

    assert p is not None
    assert p.ad == TEST_POZISYON

    print("✅ GET BY AD")

    # -------------------------------------------------
    # EXISTS
    # -------------------------------------------------

    assert repo.ad_var_mi(TEST_POZISYON) is True

    print("✅ EXISTS")

    # -------------------------------------------------
    # SEARCH
    # -------------------------------------------------

    sonuc = repo.search("TEST")

    assert len(sonuc) >= 1

    print("✅ SEARCH")

    # -------------------------------------------------
    # UPDATE
    # -------------------------------------------------
    GUNCEL_POZISYON = f"{TEST_POZISYON}_GUNCEL"
    repo.update_fields(
        p,
        {
            "ad": GUNCEL_POZISYON
        }
    )

    p = repo.get_by_ad(GUNCEL_POZISYON)

    assert p is not None

    print("✅ UPDATE")

    # -------------------------------------------------
    # COUNT
    # -------------------------------------------------

    adet = repo.toplam_pozisyon()

    assert adet > 0

    print(f"✅ COUNT ({adet})")

    # -------------------------------------------------
    # SOFT DELETE
    # -------------------------------------------------

    repo.soft_delete(p)

    assert repo.get_by_ad("TEST GÜNCEL") is None

    print("✅ SOFT DELETE")

    # -------------------------------------------------
    # HARD DELETE
    # -------------------------------------------------

    silinen = repo.get_deleted(
        ad=GUNCEL_POZISYON
    )

    if silinen:
        repo.hard_delete(silinen)

    print("✅ SOFT DELETE")

    session.close()

    print("=" * 60)
    print("TÜM TESTLER BAŞARILI")
    print("=" * 60)


if __name__ == "__main__":
    main()