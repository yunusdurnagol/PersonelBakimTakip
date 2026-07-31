"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : tests/test_makine_service.py
Açıklama   : Makine Service Testleri
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from core.database import SessionLocal
from repositories.makine_repository import MakineRepository
from services.makine_service import MakineService


def yazdir(baslik: str):

    print("\n" + "=" * 70)
    print(baslik)
    print("=" * 70)


def main():

    db = SessionLocal()

    try:

        repo = MakineRepository(db)
        service = MakineService(repo)

        yazdir("MAKİNE SERVICE TESTLERİ")

        print("\n1) get_by_id()")
        print(
            service.get_by_id(1)
        )

        print("\n2) get_by_makine_kodu()")
        print(
            service.get_by_makine_kodu(
                "MK-001"
            )
        )

        print("\n3) get_tum_makineler()")
        print(
            service.get_tum_makineler()
        )

        print("\n4) search()")
        print(
            service.search(
                "Ram"
            )
        )

        print("\n5) makine_kodu_var_mi()")
        print(
            service.makine_kodu_var_mi(
                "MK-001"
            )
        )

        print("\n6) toplam_makine()")
        print(
            service.toplam_makine()
        )

    finally:

        db.close()


if __name__ == "__main__":
    main()