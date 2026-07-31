"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : exceptions/business_exception.py
Açıklama   : Business Exception
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from exceptions.application_exception import (
    ApplicationException,
)


class BusinessException(ApplicationException):
    """
    İş kurallarına aykırı durumlarda oluşur.

    Örnek:

        - Kullanımda olan parçanın silinmesi
        - İzin gününün aşılması
        - Stok eksiye düşmesi
    """

    pass