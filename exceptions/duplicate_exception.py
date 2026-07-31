"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : exceptions/duplicate_exception.py
Açıklama   : Duplicate Exception
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from exceptions.application_exception import (
    ApplicationException,
)


class DuplicateException(ApplicationException):
    """
    Aynı kayıt mevcut olduğunda oluşur.

    Örnek:

        - Aynı stok kodu
        - Aynı sicil numarası
        - Aynı TC Kimlik No
        - Aynı firma adı
    """

    pass