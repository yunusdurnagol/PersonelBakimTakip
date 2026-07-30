"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : services/__init__.py
---------------------------------------------------------
"""

from services.base_service import BaseService
from services.personel_service import PersonelService
from services.pozisyon_service import PozisyonService
from services.parca_service import ParcaService
from services.parca_kategori_service import ParcaKategoriService
from services.makine_bolumu_service import MakineBolumuService
from services.parca_hareket_service import ParcaHareketService
from services.parca_kullanim_bolumu_service import ParcaKullanimBolumuService
from services.parca_muadili_service import ParcaMuadiliService
from services.personel_evrak_service import PersonelEvrakService
from services.personel_izin_service import PersonelIzinService
from services.tedarikci_service import TedarikciService

__all__ = [
    "BaseService",
    "PersonelService",
    "PozisyonService",
    "ParcaService",
    "ParcaKategoriService",
    "MakineBolumuService",
    "ParcaHareketService",
    "ParcaKullanimBolumuService",
    "ParcaMuadiliService",
    "PersonelEvrakService",
    "PersonelIzinService",
    "TedarikciService",
]


"""

 

 

__all__ = [
    "BaseService",

    "PersonelService",
    "PozisyonService",

    "ParcaService",
    "ParcaHareketService",
    "ParcaKategoriService",
    "ParcaKullanimBolumuService",
    "ParcaMarkaService",
    "ParcaMuadiliService",

    "MakineService",
    "MakineBolumuService",

    "TedarikciService",

    "IzinService",
]
"""