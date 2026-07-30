"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : test_parca_repository.py
Açıklama   : Parça Repository Testi
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from uuid import uuid4

from core.database import SessionLocal
from orm.parca import Parca
from repositories.parca_repository import ParcaRepository
from core.database import engine

 

def main():
     
    print(engine.url)

with engine.connect() as conn:
    result = conn.exec_driver_sql("""
        SELECT
            column_name,
            data_type,
            udt_name
        FROM information_schema.columns
        WHERE table_name='parcalar'
        ORDER BY ordinal_position
    """)

    for row in result:
        print(row)
    print("=" * 80)
    print(engine.url)
    print("=" * 80)
    print("=" * 60)
    print("PARÇA REPOSITORY TESTİ")
    print("=" * 60)

    session = SessionLocal()

    repo = ParcaRepository(session)

    stok_kodu = f"TST-{uuid4().hex[:8]}"

    # Aynı kayıt varsa temizle
    eski = repo.get_by_stok_kodu(stok_kodu)

    if eski:
        repo.bulk_delete([eski])

    # -------------------------------------------------
    # CREATE
    # -------------------------------------------------

    parca = Parca(
        stok_kodu=stok_kodu,
        orijinal_kod="SKF-6004",
        parca_adi="Test Rulman",
        kategori_id=1,
        marka_id=1,
        model="6004 ZZ",
        tedarikci_id=1,
        birim="Kg",
        fotograf=None,
        aciklama="Repository Testi",
    )

    repo.create(parca)

    print("✅ CREATE")

    # -------------------------------------------------
    # GET BY STOK KODU
    # -------------------------------------------------

    p = repo.get_by_stok_kodu(stok_kodu)

    assert p is not None

    print("✅ GET BY STOK KODU")

    # -------------------------------------------------
    # GET BY KATEGORİ
    # -------------------------------------------------

    sonuc = repo.get_by_kategori(1)

    assert isinstance(sonuc, list)

    print("✅ GET BY KATEGORİ")

    # -------------------------------------------------
    # GET BY MARKA
    # -------------------------------------------------

    sonuc = repo.get_by_marka(1)

    assert isinstance(sonuc, list)

    print("✅ GET BY MARKA")

    # -------------------------------------------------
    # GET BY TEDARİKÇİ
    # -------------------------------------------------

    sonuc = repo.get_by_tedarikci(1)

    assert isinstance(sonuc, list)

    print("✅ GET BY TEDARİKÇİ")

    # -------------------------------------------------
    # SEARCH
    # -------------------------------------------------

    sonuc = repo.search("Rulman")

    assert len(sonuc) > 0

    print("✅ SEARCH")

    # -------------------------------------------------
    # RELATION
    # -------------------------------------------------

    sonuc = repo.get_with_relations(p.id)

    assert sonuc is not None

    print("✅ RELATION")

    # -------------------------------------------------
    # UPDATE
    # -------------------------------------------------

    repo.update_fields(
        p,
        {
            "parca_adi": "Test Rulman Güncel"
        }
    )

    print("✅ UPDATE")

    # -------------------------------------------------
    # SOFT DELETE
    # -------------------------------------------------

    repo.soft_delete(p)

    print("✅ SOFT DELETE")

    # -------------------------------------------------
    # BULK DELETE
    # -------------------------------------------------

    repo.bulk_delete([p])

    print("✅ BULK DELETE")

    session.close()

    print("=" * 60)
    print("TÜM TESTLER BAŞARILI")
    print("=" * 60)


if __name__ == "__main__":
    main()