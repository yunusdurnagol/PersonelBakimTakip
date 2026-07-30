"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : repositories/__init__.py
---------------------------------------------------------
"""

from repositories.base_repository import BaseRepository
from repositories.personel_repository import PersonelRepository
from repositories.pozisyon_repository import PozisyonRepository
from repositories.parca_repository import ParcaRepository
from repositories.parca_kategori_repository import ParcaKategoriRepository
from repositories.parca_marka_repository import ParcaMarkaRepository
from repositories.tedarikci_repository import TedarikciRepository
from repositories.makine_repository import MakineRepository
from repositories.makine_bolumu_repository import MakineBolumuRepository
from repositories.parca_hareket_repository import ParcaHareketRepository
from repositories.parca_kullanim_bolumu_repository import ParcaKullanimBolumuRepository
from repositories.parca_muadili_repository import ParcaMuadiliRepository
from repositories.personel_izin_repository import PersonelIzinRepository
from repositories.personel_evrak_repository import PersonelEvrakRepository

__all__ = [
    "BaseRepository",
    "PersonelRepository",
    "PozisyonRepository",
    "ParcaRepository",
    "ParcaKategoriRepository",
    "ParcaMarkaRepository",
    "TedarikciRepository",
    "MakineRepository",
    "MakineBolumuRepository",
    "ParcaHareketRepository",
    "ParcaKullanimBolumuRepository",
    "ParcaMuadiliRepository",
    "PersonelIzinRepository",
    "PersonelEvrakRepository",
]