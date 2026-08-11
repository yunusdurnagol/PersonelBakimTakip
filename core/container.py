"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : core/container.py
Açıklama   : Dependency Injection Container
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from sqlalchemy.orm import Session

from core.database import SessionLocal

# =====================================================
# Repositories
# =====================================================
from repositories.pozisyon_repository import PozisyonRepository
from services.pozisyon_service import PozisyonService
from repositories.personel_repository import PersonelRepository
from repositories.makine_repository import MakineRepository
from repositories.parca_repository import ParcaRepository
from repositories.parca_hareket_repository import (
    ParcaHareketRepository,
)
from repositories.tedarikci_repository import (
    TedarikciRepository,
)
from repositories.personel_izin_repository import (
    PersonelIzinRepository,
)

# =====================================================
# Services
# =====================================================

from services.personel_service import PersonelService
from services.makine_service import MakineService
from services.parca_service import ParcaService
from services.parca_hareket_service import (
    ParcaHareketService,
)
from services.tedarikci_service import (
    TedarikciService,
)
from services.personel_izin_service import (
    PersonelIzinService,
)
from services.dashboard_service import DashboardService

from repositories.personel_evrak_repository import PersonelEvrakRepository
from services.personel_evrak_service import PersonelEvrakService
class AppContainer:
    """
    Uygulamanın bütün servislerini tek merkezden oluşturur.
    """

    def __init__(self) -> None:

        # =============================================
        # Session
        # =============================================

        self.session: Session = SessionLocal()

        # =============================================
        # Repositories
        # =============================================

        self.personel_repository = PersonelRepository(
            self.session
        )
        self.pozisyon_repository = PozisyonRepository(
            self.session
        )

        self.personel_evrak_repository = PersonelEvrakRepository(
            self.session
        )
        self.makine_repository = MakineRepository(
            self.session
        )

        self.parca_repository = ParcaRepository(
            self.session
        )

        self.parca_hareket_repository = (
            ParcaHareketRepository(
                self.session
            )
        )

        self.tedarikci_repository = (
            TedarikciRepository(
                self.session
            )
        )

        self.personel_izin_repository = (
            PersonelIzinRepository(
                self.session
            )
        )
         
        # =============================================
        # Services
        # =============================================

        self.personel_service = PersonelService(
            self.personel_repository
        )
        self.personel_evrak_service = PersonelEvrakService(
        self.personel_evrak_repository
    )
        self.makine_service = MakineService(
            self.makine_repository
        )

        self.parca_service = ParcaService(
            self.parca_repository
        )
        self.pozisyon_service = PozisyonService(
            self.pozisyon_repository
        )
        self.parca_hareket_service = (
            ParcaHareketService(
                self.parca_hareket_repository
            )
        )

        self.tedarikci_service = (
            TedarikciService(
                self.tedarikci_repository
            )
        )

        self.personel_izin_service = (
            PersonelIzinService(
                self.personel_izin_repository
            )
        )
         
        # =============================================
        # Dashboard
        # =============================================

        self.dashboard_service = DashboardService(
            personel_service=self.personel_service,
            makine_service=self.makine_service,
            parca_service=self.parca_service,
            tedarikci_service=self.tedarikci_service,
            parca_hareket_service=self.parca_hareket_service,
        )

    # =====================================================
    # CLOSE
    # =====================================================

    def close(self) -> None:
        """
        Veritabanı oturumunu kapatır.
        """

        self.session.close()