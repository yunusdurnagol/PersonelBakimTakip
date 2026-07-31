"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : exceptions/validation_exception.py
Açıklama   : Validation Exception
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from exceptions.application_exception import (
    ApplicationException,
)


class ValidationException(ApplicationException):
    """
    Doğrulama hatalarında kullanılır.

    Örnek:

        - Boş alan
        - Hatalı telefon
        - Hatalı e-posta
        - Negatif stok
        - Geçersiz tarih
    """

    pass