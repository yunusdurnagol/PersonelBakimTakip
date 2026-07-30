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

__all__ = [
    "BaseService",
    "PersonelService",
    "PozisyonService",
    "ParcaService",
    "ParcaKategorService",
]


"""

from services.base_service import BaseService

from services.personel_service import PersonelService
from services.pozisyon_service import PozisyonService

from services.parca_service import ParcaService
from services.parca_hareket_service import ParcaHareketService
from services.parca_kategori_service import ParcaKategoriService
from services.parca_kullanim_bolumu_service import ParcaKullanimBolumuService
from services.parca_marka_service import ParcaMarkaService
from services.parca_muadili_service import ParcaMuadiliService

from services.makine_service import MakineService
from services.makine_bolumu_service import MakineBolumuService

from services.tedarikci_service import TedarikciService

from services.izin_service import IzinService

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