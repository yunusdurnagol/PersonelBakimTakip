from services.personel_service import PersonelService
from services.makine_service import MakineService
from services.parca_service import ParcaService
from services.tedarikci_service import TedarikciService
from services.parca_hareket_service import ParcaHareketService


class DashboardService:

    def __init__(
        self,
        personel_service: PersonelService,
        makine_service: MakineService,
        parca_service: ParcaService,
        tedarikci_service: TedarikciService,
        hareket_service: ParcaHareketService,
    ):

        self.personel_service = personel_service
        self.makine_service = makine_service
        self.parca_service = parca_service
        self.tedarikci_service = tedarikci_service
        self.hareket_service = hareket_service

    def kart_verileri(self):

        return {
            "personel": self.personel_service.toplam_personel(),
            "makine": self.makine_service.toplam_makine(),
            "parca": self.parca_service.toplam_parca(),
            "tedarikci": self.tedarikci_service.toplam_tedarikci(),
        }

    def son_personeller(self):

        return self.personel_service.son_eklenenler(10)


    def son_hareketler(self):

        return self.hareket_service.son_hareketler(10)