"""
Veritabanı bağlantı testi
"""

from sqlalchemy import text

from core.database import get_session


def main():

    try:

        with get_session() as db:

            result = db.execute(
                text("SELECT version();")
            )

            print("\nBağlantı başarılı.\n")

            print(result.scalar())

    except Exception as ex:

        print()

        print("Bağlantı Hatası")

        print(ex)


if __name__ == "__main__":

    main()