"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : exceptions/database_exception.py
Açıklama   : Database Exception
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from exceptions.application_exception import (
    ApplicationException,
)


class DatabaseException(ApplicationException):
    """
    Veritabanı işlemleri sırasında oluşan hatalar.
    """

    pass