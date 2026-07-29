"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : orm/__init__.py
---------------------------------------------------------
"""

from orm.base_model import BaseModel
from orm.pozisyon import Pozisyon
from orm.personel import Personel
from orm.personel_izin import PersonelIzin
from orm.makine import Makine
from orm.makine_bolumu import MakineBolumu
from orm.parca_hareket import ParcaHareket
from orm.parca_kategori import ParcaKategori
from orm.parca_kullanim_bolumu import ParcaKullanimBolumu
from orm.parca import Parca
from orm.personel_evrak import PersonelEvrak
from orm.tedarikci import Tedarikci
from orm.parca_marka import ParcaMarka
from orm.parca_muadili import ParcaMuadili

__all__ = [
    "BaseModel",
    "Pozisyon",
    "Personel",
    "PersonelIzin",
    "Makine",
    "MakineBolumu",
    "ParcaHareket",
    "ParcaKategori",
    "ParcaKullanimBolumu",
    "Parca",
    "PersonelEvrak"
    ,"Tedarikci",
    "ParcaMarka",
    "ParcaMuadili",
]