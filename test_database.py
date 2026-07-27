"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : test_database.py
Açıklama   : PostgreSQL bağlantı ve veri okuma testi
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from sqlalchemy import text

from core.database import get_session


def main():

    try:

        with get_session() as db:

            print("=" * 50)
            print("VERİTABANI BAĞLANTI TESTİ")
            print("=" * 50)

            sonuc = db.execute(
                text("SELECT version();")
            )

            print("\nPostgreSQL Sürümü:")
            print(sonuc.scalar())

            print("\nPersoneller:\n")

            sonuc = db.execute(
                text("""
                    SELECT
                        p.id,
                        p.sicil_no,
                        p.ad,
                        p.soyad,
                        poz.ad AS pozisyon
                    FROM personeller p
                    LEFT JOIN pozisyonlar poz
                        ON poz.id = p.pozisyon_id
                    ORDER BY p.id;
                """)
            )

            satirlar = sonuc.fetchall()

            if not satirlar:

                print("Kayıt bulunamadı.")

            else:

                for satir in satirlar:

                    print(
                        f"{satir.id:3} | "
                        f"{satir.sicil_no:10} | "
                        f"{satir.ad} {satir.soyad} | "
                        f"{satir.pozisyon}"
                    )

            print("\nTest başarılı.")

    except Exception as ex:

        print("\nHATA OLUŞTU\n")
        print(ex)


if __name__ == "__main__":
    main()