"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : ui/pages/personel_page.py
Açıklama   : Personel listeleme ve CRUD ekranı
Yazar      : Yunus Durnagöl
Sürüm      : 3.1.0
---------------------------------------------------------
"""

from __future__ import annotations

from PySide6.QtGui import QStandardItem
from PySide6.QtGui import QStandardItemModel

from PySide6.QtWidgets import (
    QDialog,
    QHBoxLayout,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from ui.dialogs.personel_izinler_dialog import PersonelIzinDialog
from ui.dialogs.personel_dialog import PersonelDialog
from ui.widgets.modern_table import ModernTable
from ui.widgets.personel_izin_table import PersonelIzinTable
from ui.dialogs.personel_evrak_dialog import (
        PersonelEvrakDialog,
    )
class PersonelPage(QWidget):
    """
    Personel listeleme ve CRUD ekranı.

    ORM veya Repository ile doğrudan konuşmaz.

    UI
      ↓
    PersonelService
      ↓
    PersonelRepository
      ↓
    ORM
    """

    def __init__(
        self,
        personel_service,
        pozisyon_service,
        personel_evrak_service,
        personel_izin_service,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self.service = personel_service
        self.pozisyon_service = pozisyon_service
        self.personel_evrak_service = personel_evrak_service
        self.personel_izin_service = personel_izin_service
        self.model = QStandardItemModel()

        self.create_ui()
        self.create_connections()
        self.load_personeller()

    # =====================================================
    # UI
    # =====================================================

    def create_ui(self) -> None:

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            15,
            15,
            15,
            15,
        )

        layout.setSpacing(10)

        # -------------------------------------------------
        # ModernTable
        # -------------------------------------------------

        self.table = ModernTable(
            title="Personel Listesi",
            icon="👨",
        )

        layout.addWidget(
            self.table
        )

        # -------------------------------------------------
        # Model
        # -------------------------------------------------

        self.model.setHorizontalHeaderLabels(
            [
                "ID",
                "Sicil No",
                "TC Kimlik No",
                "Ad",
                "Soyad",
                "Cinsiyet",
                "Doğum Tarihi",
                "Doğum Yeri",
                "Uyruk",
                "Medeni Durum",
                "Eğitim Durumu",
                "İşe Giriş Tarihi",
                "İzin Hakkı",
                "Pozisyon",
                "Telefon",
                "E-Posta",
                "Adres",
                "Maaş",
                "IBAN",
                "Fotoğraf",
                "Açıklama",
            ]
        )

        self.table.set_model(
            self.model
        )

        # -------------------------------------------------
        # ID gizle
        # -------------------------------------------------

        self.table.hide_column(0)

        # -------------------------------------------------
        # CRUD butonları
        # -------------------------------------------------

        self.create_action_buttons(
            layout
        )
       
    # =====================================================
    # CRUD BUTONLARI
    # =====================================================

    def create_action_buttons(
        self,
        parent_layout,
    ) -> None:

        layout = QHBoxLayout()

        layout.setSpacing(8)

        # -------------------------------------------------
        # Yeni Personel
        # -------------------------------------------------

        self.btn_yeni = QPushButton(
            "＋ Yeni Personel"
        )

        self.btn_yeni.setObjectName(
            "btnYeni"
        )

        # -------------------------------------------------
        # Düzenle
        # -------------------------------------------------

        self.btn_duzenle = QPushButton(
            "✎ Düzenle"
        )

        self.btn_duzenle.setObjectName(
            "btnDuzenle"
        )

        # -------------------------------------------------
        # İzinler
        # -------------------------------------------------

        self.btn_izinler = QPushButton(
            "📅 İzinler"
        )

        self.btn_izinler.setObjectName(
            "btnIzinler"
        )

        # -------------------------------------------------
        # Evraklar
        # -------------------------------------------------

        self.btn_evraklar = QPushButton(
            "📄 Evraklar"
        )

        self.btn_evraklar.setObjectName(
            "btnEvraklar"
        )

        # -------------------------------------------------
        # Sil
        # -------------------------------------------------

        self.btn_sil = QPushButton(
            "🗑 Sil"
        )

        self.btn_sil.setObjectName(
            "btnSil"
        )

        # -------------------------------------------------
        # Stil
        # -------------------------------------------------

        self.set_button_style()

        # -------------------------------------------------
        # Layout
        # -------------------------------------------------

        layout.addWidget(
            self.btn_yeni
        )

        layout.addWidget(
            self.btn_duzenle
        )

        layout.addWidget(
            self.btn_izinler
        )

        layout.addWidget(
            self.btn_evraklar
        )

        layout.addWidget(
            self.btn_sil
        )

        layout.addStretch()

        parent_layout.addLayout(
            layout
        )

    # =====================================================
    # BUTON STİLİ
    # =====================================================

    def set_button_style(self) -> None:

        self.setStyleSheet(
            """
            QPushButton {
                min-height: 36px;
                padding: 0 16px;
                border-radius: 8px;
                border: 1px solid #E2E8F0;
                background: #FFFFFF;
                color: #334155;
                font-size: 10pt;
                font-weight: 600;
            }

            QPushButton:hover {
                background: #F1F5F9;
            }

            QPushButton#btnYeni {
                background: #2563EB;
                color: white;
                border: none;
            }

            QPushButton#btnYeni:hover {
                background: #1D4ED8;
            }

            QPushButton#btnDuzenle {
                background: #F59E0B;
                color: white;
                border: none;
            }

            QPushButton#btnDuzenle:hover {
                background: #D97706;
            }

            QPushButton#btnSil {
                background: #EF4444;
                color: white;
                border: none;
            }

            QPushButton#btnSil:hover {
                background: #DC2626;
            }

            QPushButton#btnIzinler {
                background: #10B981;
                color: white;
                border: none;
            }

            QPushButton#btnIzinler:hover {
                background: #059669;
            }
            QPushButton#btnIzinler {
                background: #10B981;
                color: white;
                border: none;
            }

            QPushButton#btnIzinler:hover {
                background: #059669;
            }

            QPushButton#btnEvraklar {
                background: #6366F1;
                color: white;
                border: none;
            }

            QPushButton#btnEvraklar:hover {
                background: #4F46E5;
            }
            """
        )

    # =====================================================
    # CONNECTIONS
    # =====================================================

    def create_connections(self) -> None:

        self.btn_yeni.clicked.connect(
            self.yeni_personel
        )

        self.btn_duzenle.clicked.connect(
            self.duzenle_personel
        )

        self.btn_izinler.clicked.connect(
            self.izinler_personel
        )

        self.btn_evraklar.clicked.connect(
            self.evraklar_personel
        )

        self.btn_sil.clicked.connect(
            self.sil_personel
        )

        self.table.refreshRequested.connect(
            self.load_personeller
        )

        self.table.rowDoubleClicked.connect(
            self.personel_double_clicked
        )

    # =====================================================
    # PERSONELLERİ YÜKLE
    # =====================================================

    def load_personeller(self) -> None:

        self.model.removeRows(
            0,
            self.model.rowCount(),
        )

        try:

            personeller = (
                self.service.get_tum_personeller()
            )

            for personel in personeller:

                pozisyon = ""

                if personel.pozisyon:

                    pozisyon = (
                        personel.pozisyon.ad
                    )

                row = [

                    QStandardItem(
                        str(personel.id)
                    ),

                    QStandardItem(
                        personel.sicil_no or ""
                    ),

                    QStandardItem(
                        personel.tc_kimlik_no or ""
                    ),

                    QStandardItem(
                        personel.ad or ""
                    ),

                    QStandardItem(
                        personel.soyad or ""
                    ),

                    QStandardItem(
                        personel.cinsiyet or ""
                    ),

                    QStandardItem(
                        self.format_date(
                            personel.dogum_tarihi
                        )
                    ),

                    QStandardItem(
                        personel.dogum_yeri or ""
                    ),

                    QStandardItem(
                        personel.uyruk or ""
                    ),

                    QStandardItem(
                        personel.medeni_durum or ""
                    ),

                    QStandardItem(
                        personel.egitim_durumu or ""
                    ),

                    QStandardItem(
                        self.format_date(
                            personel.ise_giris_tarihi
                        )
                    ),

                    QStandardItem(
                        str(
                            personel.izin_hakki
                            or 0
                        )
                    ),

                    QStandardItem(
                        pozisyon
                    ),

                    QStandardItem(
                        personel.telefon or ""
                    ),

                    QStandardItem(
                        personel.email or ""
                    ),

                    QStandardItem(
                        personel.adres or ""
                    ),

                    QStandardItem(
                        (
                            f"{personel.maas:.2f}"
                            if personel.maas
                            is not None
                            else ""
                        )
                    ),

                    QStandardItem(
                        personel.iban or ""
                    ),

                    QStandardItem(
                        personel.fotograf or ""
                    ),

                    QStandardItem(
                        personel.aciklama or ""
                    ),
                ]

                self.model.appendRow(
                    row
                )

            self.table.resize_columns()

            self.table.update_footer()

        except Exception as exc:

            QMessageBox.critical(
                self,
                "Personeller Yüklenemedi",
                str(exc),
            )

    # =====================================================
    # TARİH FORMAT
    # =====================================================

    @staticmethod
    def format_date(
        value,
    ) -> str:

        if value is None:
            return ""

        return value.strftime(
            "%d.%m.%Y"
        )

    # =====================================================
    # YENİ PERSONEL
    # =====================================================

    def yeni_personel(self) -> None:

        dialog = PersonelDialog(
            personel_service=self.service,
            pozisyon_service=self.pozisyon_service,
            parent=self,
        )

        result = dialog.exec()

        if result == QDialog.Accepted:

            self.load_personeller()

    # =====================================================
    # SEÇİLİ PERSONEL ID
    # =====================================================

    def selected_personel_id(
        self,
    ) -> int | None:

        return self.table.selected_id()

    # =====================================================
    # SEÇİLİ PERSONEL
    # =====================================================

    def selected_personel(self):

        personel_id = (
            self.selected_personel_id()
        )

        if personel_id is None:

            return None

        return self.service.get_by_id(
            personel_id
        )

    # =====================================================
    # DÜZENLE
    # =====================================================

    def duzenle_personel(self) -> None:

        personel = self.selected_personel()

        if personel is None:

            QMessageBox.information(
                self,
                "Personel Seçilmedi",
                (
                    "Lütfen düzenlemek istediğiniz "
                    "personeli seçin."
                ),
            )

            return

        dialog = PersonelDialog(
            personel_service=self.service,
            pozisyon_service=self.pozisyon_service,
            personel=personel,
            parent=self,
        )

        result = dialog.exec()

        # DÜZELTİLDİ
        if result == QDialog.Accepted:

            self.load_personeller()

    # =====================================================
    # SİL
    # =====================================================

    def sil_personel(self) -> None:

        personel = self.selected_personel()

        if personel is None:

            QMessageBox.information(
                self,
                "Personel Seçilmedi",
                (
                    "Lütfen silmek istediğiniz "
                    "personeli seçin."
                ),
            )

            return

        cevap = QMessageBox.question(
            self,
            "Personel Sil",
            (
                f"{personel.ad_soyad}\n\n"
                "Bu personeli silmek istediğinize "
                "emin misiniz?"
            ),
            QMessageBox.Yes
            | QMessageBox.No,
            QMessageBox.No,
        )

        if cevap != QMessageBox.Yes:

            return

        try:

            self.service.personel_sil(
                personel.id
            )

            QMessageBox.information(
                self,
                "İşlem Başarılı",
                "Personel başarıyla silindi.",
            )

            self.load_personeller()

        except Exception as exc:

            QMessageBox.critical(
                self,
                "Personel Silinemedi",
                str(exc),
            )

    # =====================================================
    # ÇİFT TIK
    # =====================================================

    def personel_double_clicked(
        self,
        row: int,
    ) -> None:

        item = self.model.item(
            row,
            0,
        )

        if item is None:

            return

        try:

            personel_id = int(
                item.text()
            )

        except ValueError:

            return

        personel = self.service.get_by_id(
            personel_id
        )

        if personel is None:

            QMessageBox.warning(
                self,
                "Personel",
                "Personel bulunamadı.",
            )

            return

        dialog = PersonelDialog(
            personel_service=self.service,
            pozisyon_service=self.pozisyon_service,
            personel=personel,
            parent=self,
        )

        result = dialog.exec()

        # DÜZELTİLDİ
        if result == QDialog.Accepted:

            self.load_personeller()

    # =====================================================
    # REFRESH
    # =====================================================

    def refresh(self) -> None:

        self.load_personeller()

    # =====================================================
    # SEARCH
    # =====================================================

    def search(
        self,
        text: str,
    ) -> None:

        self.table.set_search_text(
            text
        )


    def izinleri_goster(self) -> None:

        personel = self.selected_personel()

        if personel is None:

            QMessageBox.information(
                self,
                "Personel Seçilmedi",
                "Lütfen izinlerini görmek istediğiniz "
                "personeli seçin.",
            )

            return

        dialog = QDialog(self)

        dialog.setWindowTitle(
            f"📅 İzinler - "
            f"{personel.ad} {personel.soyad}"
        )

        dialog.resize(
            1000,
            600,
        )

        layout = QVBoxLayout(dialog)

        izin_table = PersonelIzinTable(
            personel_izin_service=self.personel_izin_service,
            personel=personel,
            parent=dialog,
        )

        layout.addWidget(
            izin_table
        )

        dialog.exec()

    # =====================================================
    # PERSONEL İZİNLERİ
    # =====================================================

    def izinler_personel(self) -> None:

        personel = self.selected_personel()

        if personel is None:

            QMessageBox.information(
                self,
                "Personel Seçilmedi",
                "Lütfen izinlerini görmek istediğiniz "
                "personeli seçin.",
            )

            return

        dialog = PersonelIzinDialog(
            personel_izin_service=self.personel_izin_service,
            personel=personel,
            parent=self,
        )

        dialog.exec()

# =====================================================
# PERSONEL EVRAKLARI
# =====================================================

    def evraklar_personel(self) -> None:

        personel = self.selected_personel()

        if personel is None:

            QMessageBox.information(
                self,
                "Personel Seçilmedi",
                "Lütfen evraklarını görmek veya "
                "eklemek istediğiniz personeli seçin.",
            )

            return

    

        dialog = PersonelEvrakDialog(
        personel_evrak_service=self.personel_evrak_service,
        personel_id=personel.id,
        parent=self,
        )

        dialog.exec()