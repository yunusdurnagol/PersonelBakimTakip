"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : core/config.py
Açıklama   : Uygulama yapılandırma ayarları (.env)
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Settings(BaseSettings):
    """
    Uygulama ayarları.

    .env dosyasından otomatik okunur.
    """

    # ---------------------------------------------------------
    # PostgreSQL
    # ---------------------------------------------------------

    db_host: str = Field(..., alias="DB_HOST")

    db_port: int = Field(..., alias="DB_PORT")

    db_name: str = Field(..., alias="DB_NAME")

    db_user: str = Field(..., alias="DB_USER")

    db_password: str = Field(..., alias="DB_PASSWORD")

    # ---------------------------------------------------------
    # Uygulama
    # ---------------------------------------------------------

    app_name: str = "Personel ve Bakım Yönetim Sistemi"

    app_version: str = "1.0.0"

    debug: bool = False

    # ---------------------------------------------------------
    # Dosya Klasörleri
    # ---------------------------------------------------------

    upload_folder: str = "uploads"

    export_folder: str = "exports"

    report_folder: str = "reports"

    # ---------------------------------------------------------
    # Pydantic Settings
    # ---------------------------------------------------------

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # ---------------------------------------------------------
    # Database URL
    # ---------------------------------------------------------

    @property
    def database_url(self) -> str:
        """
        SQLAlchemy bağlantı adresi.
        """

        return (
            f"postgresql+psycopg://"
            f"{self.db_user}:"
            f"{self.db_password}@"
            f"{self.db_host}:"
            f"{self.db_port}/"
            f"{self.db_name}"
        )


# ---------------------------------------------------------
# Singleton
# ---------------------------------------------------------

@lru_cache
def get_settings() -> Settings:
    """
    Settings nesnesini tek instance olarak döndürür.
    """

    return Settings()


settings = get_settings()