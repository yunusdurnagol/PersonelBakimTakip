"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : test_orm.py
Açıklama   : ORM modelleri bağlantı testi
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from sqlalchemy import text

from core.database import get_session



# Personel
from orm.personel import Personel

# İnsan Kaynakları
from orm.pozisyon import Pozisyon
 


# Bakım / Stok
from orm.parca import Parca
from orm.parca_kategori import ParcaKategori
from orm.parca_marka import ParcaMarka
from orm.tedarikci import Tedarikci
from orm.parca_hareket import ParcaHareket
from orm.parca_muadili import ParcaMuadili
from orm.personel_evrak import PersonelEvrak
from orm.makine_bolumu import MakineBolumu
from orm.makine import Makine
from orm.parca_kullanim_bolumu import ParcaKullanimBolumu

def test_model(model, isim):

    try:
        with get_session() as db:
        
            kayitlar = db.query(model).all()

            print(
                f"✅ {isim:<25} OK "
                f"({len(kayitlar)} kayıt)"
            )

            db.close()


    except Exception as e:

        print(
            f"❌ {isim:<25} HATA"
        )

        print(e)



def main():


    print("=" * 60)
    print("ORM TEST BAŞLADI")
    print("=" * 60)



    modeller = [

        (Personel, "Personel"),

        (Pozisyon, "Pozisyon"),

        (Parca, "Parça"),

        (ParcaKategori, "Parça Kategori"),

        (ParcaMarka, "Parça Marka"),

        (Tedarikci, "Tedarikçi"),

        (ParcaHareket, "Parça Hareket"),

        (ParcaMuadili, "Parça Muadili"),

        (ParcaKategori,"Parça Kategori"),
        
        (PersonelEvrak,"Personel Evrak"),

        (Makine,"Makineler"),
        
        (MakineBolumu,"Makine Bölümü"),

        (ParcaKullanimBolumu,"Parça Kullanım Bölümü"),
    ]


    for model, isim in modeller:

        test_model(
            model,
            isim
        )



    print("=" * 60)
    print("ORM TEST BİTTİ")
    print("=" * 60)



if __name__ == "__main__":

    main()