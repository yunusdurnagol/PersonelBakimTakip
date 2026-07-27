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

__all__ = [
    "BaseModel",
    "Pozisyon",
    "Personel",
    "PersonelIzin",
]