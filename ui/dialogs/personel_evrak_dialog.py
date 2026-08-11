"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : ui/dialogs/personel_evrak_dialog.py
Açıklama   : Personel Evrak Ekleme Dialogu
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import QDate
from PySide6.QtWidgets import (
    QDateEdit,
    QDialog,
    QDialogButtonBox,
    QFileDialog,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
)


class PersonelEvrakDialog(QDialog):
    """
    Personel için yeni evrak ekleme dialogu.

    UI
        ↓
    PersonelEvrakService
        ↓
    PersonelEvrakRepository
        ↓
    PersonelEvrak ORM
    """

    def __init__(
        self,
        *,
        personel_id: int,
        personel_evrak_service,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self.personel_id = personel_id
        self.service = personel_evrak_service

        # Kullanıcının seçtiği ORİJİNAL dosyanın yolu
        self.selected_file_path: str = ""

        self.setWindowTitle(
            "📄 Personel Evrakı Ekle"
        )

        self.setModal(True)

        self.resize(
            600,
            430,
        )

        self.create_ui()
        self.create_connections()

    # =====================================================
    # UI
    # =====================================================

    def create_ui(self) -> None:

        main_layout = QVBoxLayout(self)

        main_layout.setContentsMargins(
            25,
            25,
            25,
            25,
        )

        main_layout.setSpacing(15)

        # -------------------------------------------------
        # BAŞLIK
        # -------------------------------------------------

        title = QLabel(
            "📄 Personel Evrakı Ekle"
        )

        title.setStyleSheet(
            """
            QLabel {
                font-size: 16pt;
                font-weight: 700;
                color: #1E293B;
            }
            """
        )

        main_layout.addWidget(
            title
        )

        subtitle = QLabel(
            "Personel için yeni bir belge ekleyin."
        )

        subtitle.setStyleSheet(
            """
            QLabel {
                color: #64748B;
                font-size: 10pt;
            }
            """
        )

        main_layout.addWidget(
            subtitle
        )

        # -------------------------------------------------
        # FORM
        # -------------------------------------------------

        form_layout = QFormLayout()

        form_layout.setHorizontalSpacing(
            15
        )

        form_layout.setVerticalSpacing(
            12
        )

        # -------------------------------------------------
        # EVRAK ADI
        # -------------------------------------------------

        self.txt_evrak_adi = QLineEdit()

        self.txt_evrak_adi.setPlaceholderText(
            "Örn: Kimlik, Diploma, İş Sözleşmesi..."
        )

        self.txt_evrak_adi.setMinimumHeight(
            38
        )

        form_layout.addRow(
            "Evrak Adı:",
            self.txt_evrak_adi,
        )

        # -------------------------------------------------
        # DOSYA
        # -------------------------------------------------

        file_layout = QHBoxLayout()

        file_layout.setSpacing(
            8
        )

        self.txt_dosya = QLineEdit()

        self.txt_dosya.setReadOnly(
            True
        )

        self.txt_dosya.setPlaceholderText(
            "Dosya seçilmedi"
        )

        self.txt_dosya.setMinimumHeight(
            38
        )

        self.btn_dosya_sec = QPushButton(
            "📂 Dosya Seç"
        )

        self.btn_dosya_sec.setMinimumHeight(
            38
        )

        self.btn_dosya_sec.setMinimumWidth(
            120
        )

        file_layout.addWidget(
            self.txt_dosya,
            1,
        )

        file_layout.addWidget(
            self.btn_dosya_sec
        )

        form_layout.addRow(
            "Dosya:",
            file_layout,
        )

        # -------------------------------------------------
        # BELGE TARİHİ
        # -------------------------------------------------

        self.date_belge = QDateEdit()

        self.date_belge.setCalendarPopup(
            True
        )

        self.date_belge.setDisplayFormat(
            "dd.MM.yyyy"
        )

        self.date_belge.setDate(
            QDate.currentDate()
        )

        self.date_belge.setMinimumHeight(
            38
        )

        form_layout.addRow(
            "Belge Tarihi:",
            self.date_belge,
        )

        # -------------------------------------------------
        # AÇIKLAMA
        # -------------------------------------------------

        self.txt_aciklama = QTextEdit()

        self.txt_aciklama.setPlaceholderText(
            "Evrak hakkında açıklama..."
        )

        self.txt_aciklama.setMinimumHeight(
            100
        )

        form_layout.addRow(
            "Açıklama:",
            self.txt_aciklama,
        )

        main_layout.addLayout(
            form_layout
        )

        # -------------------------------------------------
        # BUTONLAR
        # -------------------------------------------------

        self.button_box = QDialogButtonBox(
            QDialogButtonBox.Cancel
            | QDialogButtonBox.Save
        )

        self.button_box.button(
            QDialogButtonBox.Save
        ).setText(
            "💾 Kaydet"
        )

        self.button_box.button(
            QDialogButtonBox.Cancel
        ).setText(
            "İptal"
        )

        main_layout.addWidget(
            self.button_box
        )

        # -------------------------------------------------
        # STİL
        # -------------------------------------------------

        self.setStyleSheet(
            """
            QDialog {
                background: #FFFFFF;
            }

            QLineEdit,
            QDateEdit,
            QTextEdit {
                border: 1px solid #CBD5E1;
                border-radius: 7px;
                padding: 7px 10px;
                background: #FFFFFF;
                color: #1E293B;
                font-size: 10pt;
            }

            QLineEdit:focus,
            QDateEdit:focus,
            QTextEdit:focus {
                border: 2px solid #2563EB;
            }

            QPushButton {
                min-height: 36px;
                padding: 0 15px;
                border-radius: 7px;
                border: 1px solid #CBD5E1;
                background: #FFFFFF;
                color: #334155;
                font-weight: 600;
            }

            QPushButton:hover {
                background: #F1F5F9;
            }

            QDialogButtonBox QPushButton {
                min-width: 90px;
            }
            """
        )

    # =====================================================
    # CONNECTIONS
    # =====================================================

    def create_connections(self) -> None:

        self.btn_dosya_sec.clicked.connect(
            self.dosya_sec
        )

        self.button_box.accepted.connect(
            self.kaydet
        )

        self.button_box.rejected.connect(
            self.reject
        )

    # =====================================================
    # DOSYA SEÇ
    # =====================================================

    def dosya_sec(self) -> None:

        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Personel Evrakı Seç",
            "",
            (
                "Tüm Dosyalar (*.*);;"
                "PDF Dosyaları (*.pdf);;"
                "Word Dosyaları (*.doc *.docx);;"
                "Excel Dosyaları (*.xls *.xlsx);;"
                "Resim Dosyaları (*.jpg *.jpeg *.png)"
            ),
        )

        if not file_path:
            return

        self.selected_file_path = file_path

        dosya = Path(
            file_path
        )

        self.txt_dosya.setText(
            dosya.name
        )

        # Evrak adı henüz girilmediyse
        # dosya adından otomatik oluştur.
        if not self.txt_evrak_adi.text().strip():

            self.txt_evrak_adi.setText(
                dosya.stem
            )

    # =====================================================
    # KAYDET
    # =====================================================

    def kaydet(self) -> None:

        # -------------------------------------------------
        # Evrak adı
        # -------------------------------------------------

        evrak_adi = (
            self.txt_evrak_adi
            .text()
            .strip()
        )

        if not evrak_adi:

            QMessageBox.warning(
                self,
                "Eksik Bilgi",
                "Lütfen evrak adını girin.",
            )

            self.txt_evrak_adi.setFocus()

            return

        # -------------------------------------------------
        # Dosya
        # -------------------------------------------------

        if not self.selected_file_path:

            QMessageBox.warning(
                self,
                "Dosya Seçilmedi",
                "Lütfen eklenecek dosyayı seçin.",
            )

            return

        # -------------------------------------------------
        # Dosyanın hala mevcut olup olmadığını kontrol et
        # -------------------------------------------------

        if not Path(
            self.selected_file_path
        ).exists():

            QMessageBox.warning(
                self,
                "Dosya Bulunamadı",
                "Seçilen dosya artık mevcut değil.",
            )

            return

        # -------------------------------------------------
        # Dosya bilgileri
        # -------------------------------------------------

        dosya = Path(
            self.selected_file_path
        )

        dosya_adi = dosya.name

        dosya_yolu = str(
            dosya
        )

        # -------------------------------------------------
        # Belge tarihi
        # -------------------------------------------------

        qdate = self.date_belge.date()

        belge_tarihi = qdate.toPython()

        # -------------------------------------------------
        # Açıklama
        # -------------------------------------------------

        aciklama = (
            self.txt_aciklama
            .toPlainText()
            .strip()
        )

        if not aciklama:
            aciklama = None

        # -------------------------------------------------
        # SERVICE
        # -------------------------------------------------

        try:

            self.service.evrak_ekle(
                personel_id=self.personel_id,
                evrak_adi=evrak_adi,
                dosya_adi=dosya_adi,
                dosya_yolu=dosya_yolu,
                belge_tarihi=belge_tarihi,
                aciklama=aciklama,
            )

        except ValueError as exc:

            QMessageBox.warning(
                self,
                "Evrak Eklenemedi",
                str(exc),
            )

            return

        except Exception as exc:

            QMessageBox.critical(
                self,
                "Evrak Eklenemedi",
                (
                    "Evrak kaydedilirken "
                    "beklenmeyen bir hata oluştu.\n\n"
                    f"{exc}"
                ),
            )

            return

        # -------------------------------------------------
        # BAŞARILI
        # -------------------------------------------------

        QMessageBox.information(
            self,
            "İşlem Başarılı",
            "Personel evrakı başarıyla eklendi.",
        )

        self.accept()