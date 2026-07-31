"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : exceptions/base_exception.py
Açıklama   : Temel Exception Sınıfı
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations


class ApplicationException(Exception):
    """
    Projedeki tüm özel exception sınıflarının temelidir.

    Bütün özel exception'lar bu sınıftan türetilmelidir.
    """

    def __init__(
        self,
        message: str,
        details: str | None = None,
    ) -> None:
        """
        Args:
            message:
                Kullanıcıya gösterilecek hata mesajı.

            details:
                Geliştirici için teknik açıklama.
        """

        self.message = message
        self.details = details

        super().__init__(message)

    def __str__(self) -> str:
        """
        Exception string çıktısı.
        """

        return self.message

    def __repr__(self) -> str:
        """
        Debug çıktısı.
        """

        return (
            f"{self.__class__.__name__}("
            f"message='{self.message}', "
            f"details='{self.details}')"
        )