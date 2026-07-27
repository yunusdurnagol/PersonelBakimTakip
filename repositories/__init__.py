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
from repositories.personel_repository import PersonelRepository

__all__ = [
    "BaseRepository",
    "PersonelRepository",
]