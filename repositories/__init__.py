"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : repositories/__init__.py
Açıklama   : Repository Paket Tanımları
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from repositories.base_repository import BaseRepository
from repositories.personel_repository import PersonelRepositoryfrom 
from repositories.makine_bolumu_repository import MakineBolumuRepository
from repositories.makine_repository import MakineRepository
from repositories.parca_repository import ParcaRepository
from repositories.parca_marka_repository import ParcaMarkaRepository
from repositories.parca_kategori_repository import ParcaKategoriRepository
from repositories.pozisyon_repository import PozisyonRepository
from repositories.tedarikci_repository import TedarikciRepository
__all__ = [
    "BaseRepository",
    "PersonelRepository",
    "MakineBolumuRepository",
    "MakineRepository",
    "ParcaRepository",
    "ParcaMarkaRepository",
    "ParcaKategoriRepository",
    "PozisyonRepository",
    "TedarikciRepository",
]