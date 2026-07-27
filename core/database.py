"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : core/database.py
Açıklama   : SQLAlchemy veritabanı bağlantısı
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

from core.config import settings


# ---------------------------------------------------------
# SQLAlchemy Base
# ---------------------------------------------------------

class Base(DeclarativeBase):
    """
    ORM Base sınıfı.
    """
    pass


# ---------------------------------------------------------
# Engine
# ---------------------------------------------------------

engine = create_engine(
    settings.database_url,
    echo=False,           # SQL sorgularını görmek istersen True yapabilirsin.
    future=True,
    pool_pre_ping=True,
)


# ---------------------------------------------------------
# Session Factory
# ---------------------------------------------------------

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)


# ---------------------------------------------------------
# Session Helper
# ---------------------------------------------------------

def get_session():
    """
    Yeni bir veritabanı oturumu oluşturur.

    Kullanım:

    with get_session() as db:
        ...
    """

    return SessionLocal()