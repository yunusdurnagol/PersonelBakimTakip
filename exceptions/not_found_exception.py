"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : exceptions/not_found_exception.py
Açıklama   : Not Found Exception
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from exceptions.application_exception import (
    ApplicationException,
)


class NotFoundException(ApplicationException):
    """
    Aranan kayıt bulunamadığında oluşur.
    """

    pass