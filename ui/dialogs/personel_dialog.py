"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : ui/dialogs/personel_dialog.py
Açıklama   : Personel Ekleme / Güncelleme Dialogu
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

import re

from decimal import Decimal

from PySide6.QtCore import Qt, QDate
from PySide6.QtWidgets import (
    QComboBox,
    QDateEdit,
    QDialog,
    QDialogButtonBox,
    QDoubleSpinBox,
    QFileDialog,
    QFormLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QSpinBox,
    QTextEdit,
    QVBoxLayout,
)


class PersonelDialog(QDialog):
    """
    Personel ekleme ve güncelleme penceresi.

    Aynı dialog hem yeni personel oluşturmak
    hem de mevcut personeli düzenlemek için kullanılır.

    ORM işlemleri burada yapılmaz.
    Tüm kayıt işlemleri PersonelService üzerinden yürütülür.
    """

    def __init__(
        self,
        pozisyon_service,
        personel_service,
        personel=None,
        parent=None,
    ) -> None:

        super().__init__(parent)

        # =====================================================
        # SERVICES
        # =====================================================

        self.pozisyon_service = pozisyon_service
        self.personel_service = personel_service

        # =====================================================
        # PERSONEL
        # =====================================================

        self.personel = personel

        # =====================================================
        # MOD
        # =====================================================

        self.is_edit_mode = personel is not None

        # =====================================================
        # PENCERE
        # =====================================================

        self.setWindowTitle(
            "Personel Düzenle"
            if self.is_edit_mode
            else "Yeni Personel"
        )

        # -----------------------------------------------------
        # Dialog boyutu
        # -----------------------------------------------------

        self.resize(
            1100,
            800,
        )

        self.setMinimumSize(
            1000,
            700,
        )

        self.setSizeGripEnabled(
            True
        )

        # =====================================================
        # UI
        # =====================================================

        self.create_ui()

        # =====================================================
        # POZİSYONLAR
        # =====================================================

        self.load_pozisyonlar()

        # =====================================================
        # MEVCUT PERSONEL
        # =====================================================

        if self.personel:
            self.load_personel()

        # =====================================================
        # CONNECTIONS
        # =====================================================

        self.create_connections()

    # =========================================================
    # UI
    # =========================================================

    def create_ui(self) -> None:

        # =====================================================
        # ANA LAYOUT
        # =====================================================

        main_layout = QVBoxLayout(
            self
        )

        main_layout.setContentsMargins(
            25,
            20,
            25,
            20,
        )

        main_layout.setSpacing(
            15
        )

        # =====================================================
        # BAŞLIK
        # =====================================================

        title = QLabel(
            "👨  "
            + (
                "Personel Düzenle"
                if self.is_edit_mode
                else "Yeni Personel"
            )
        )

        title.setStyleSheet(
            """
            QLabel {
                font-size: 21px;
                font-weight: bold;
                color: #1E293B;
                padding-bottom: 5px;
            }
            """
        )

        main_layout.addWidget(
            title
        )

        # =====================================================
        # İKİ SÜTUNLU FORM
        # =====================================================

        columns_layout = QHBoxLayout()

        columns_layout.setSpacing(
            18
        )

        # =====================================================
        # SOL SÜTUN
        # =====================================================

        left_layout = QVBoxLayout()

        left_layout.setSpacing(
            15
        )

        # =====================================================
        # KİMLİK BİLGİLERİ
        # =====================================================

        kimlik_group = QGroupBox(
            "Kimlik Bilgileri"
        )

        kimlik_layout = QFormLayout(
            kimlik_group
        )

        kimlik_layout.setContentsMargins(
            20,
            28,
            20,
            20,
        )

        kimlik_layout.setHorizontalSpacing(
            15
        )

        kimlik_layout.setVerticalSpacing(
            10
        )

        kimlik_layout.setLabelAlignment(
            Qt.AlignRight
        )

        # -----------------------------------------------------
        # Sicil No
        # -----------------------------------------------------

        self.txt_sicil = QLineEdit()

        self.txt_sicil.setPlaceholderText(
            "Örn: A001"
        )

        self.txt_sicil.setMaxLength(
            20
        )

        kimlik_layout.addRow(
            "Sicil No *",
            self.txt_sicil,
        )

        # -----------------------------------------------------
        # TC Kimlik
        # -----------------------------------------------------

        self.txt_tc = QLineEdit()

        self.txt_tc.setMaxLength(
            11
        )

        self.txt_tc.setPlaceholderText(
            "11 haneli TC Kimlik No"
        )

        kimlik_layout.addRow(
            "TC Kimlik No",
            self.txt_tc,
        )

        # -----------------------------------------------------
        # Ad
        # -----------------------------------------------------

        self.txt_ad = QLineEdit()

        self.txt_ad.setPlaceholderText(
            "Ad"
        )

        kimlik_layout.addRow(
            "Ad *",
            self.txt_ad,
        )

        # -----------------------------------------------------
        # Soyad
        # -----------------------------------------------------

        self.txt_soyad = QLineEdit()

        self.txt_soyad.setPlaceholderText(
            "Soyad"
        )

        kimlik_layout.addRow(
            "Soyad *",
            self.txt_soyad,
        )

        # -----------------------------------------------------
        # Cinsiyet
        # -----------------------------------------------------

        self.cmb_cinsiyet = QComboBox()

        self.cmb_cinsiyet.addItems(
            [
                "",
                "Erkek",
                "Kadın",
            ]
        )

        kimlik_layout.addRow(
            "Cinsiyet",
            self.cmb_cinsiyet,
        )

        # -----------------------------------------------------
        # Doğum Tarihi
        # -----------------------------------------------------

        self.date_dogum = QDateEdit()

        self.date_dogum.setCalendarPopup(
            True
        )

        self.date_dogum.setDisplayFormat(
            "dd.MM.yyyy"
        )

        self.date_dogum.setDate(
            QDate(
                2000,
                1,
                1,
            )
        )

        kimlik_layout.addRow(
            "Doğum Tarihi",
            self.date_dogum,
        )

        # -----------------------------------------------------
        # Doğum Yeri
        # -----------------------------------------------------

        self.txt_dogum_yeri = QLineEdit()

        self.txt_dogum_yeri.setPlaceholderText(
            "Doğum yeri"
        )

        kimlik_layout.addRow(
            "Doğum Yeri",
            self.txt_dogum_yeri,
        )

        left_layout.addWidget(
            kimlik_group
        )

        # =====================================================
        # İŞ BİLGİLERİ
        # =====================================================

        is_group = QGroupBox(
            "İş Bilgileri"
        )

        is_layout = QFormLayout(
            is_group
        )

        is_layout.setContentsMargins(
            20,
            28,
            20,
            20,
        )

        is_layout.setHorizontalSpacing(
            15
        )

        is_layout.setVerticalSpacing(
            10
        )

        is_layout.setLabelAlignment(
            Qt.AlignRight
        )

        # -----------------------------------------------------
        # Pozisyon
        # -----------------------------------------------------

        self.cmb_pozisyon = QComboBox()

        self.cmb_pozisyon.setPlaceholderText(
            "Pozisyon seçiniz"
        )

        is_layout.addRow(
            "Pozisyon *",
            self.cmb_pozisyon,
        )

        # -----------------------------------------------------
        # İşe Giriş Tarihi
        # -----------------------------------------------------

        self.date_ise_giris = QDateEdit()

        self.date_ise_giris.setCalendarPopup(
            True
        )

        self.date_ise_giris.setDisplayFormat(
            "dd.MM.yyyy"
        )

        self.date_ise_giris.setDate(
            QDate.currentDate()
        )

        is_layout.addRow(
            "İşe Giriş Tarihi *",
            self.date_ise_giris,
        )

        # -----------------------------------------------------
        # İzin Hakkı
        # -----------------------------------------------------

        self.spin_izin = QSpinBox()

        self.spin_izin.setRange(
            0,
            365,
        )

        self.spin_izin.setValue(
            14
        )

        self.spin_izin.setSuffix(
            " gün"
        )

        is_layout.addRow(
            "İzin Hakkı",
            self.spin_izin,
        )

        left_layout.addWidget(
            is_group
        )

        left_layout.addStretch()

        # =====================================================
        # SAĞ SÜTUN
        # =====================================================

        right_layout = QVBoxLayout()

        right_layout.setSpacing(
            15
        )

        # =====================================================
        # İLETİŞİM BİLGİLERİ
        # =====================================================

        iletisim_group = QGroupBox(
            "İletişim Bilgileri"
        )

        iletisim_layout = QFormLayout(
            iletisim_group
        )

        iletisim_layout.setContentsMargins(
            20,
            28,
            20,
            20,
        )

        iletisim_layout.setHorizontalSpacing(
            15
        )

        iletisim_layout.setVerticalSpacing(
            10
        )

        iletisim_layout.setLabelAlignment(
            Qt.AlignRight
        )

        # -----------------------------------------------------
        # Telefon
        # -----------------------------------------------------

        self.txt_telefon = QLineEdit()

        self.txt_telefon.setPlaceholderText(
            "05xx xxx xx xx"
        )

        self.txt_telefon.setMaxLength(
            30
        )

        iletisim_layout.addRow(
            "Telefon",
            self.txt_telefon,
        )

        # -----------------------------------------------------
        # E-Posta
        # -----------------------------------------------------

        self.txt_email = QLineEdit()

        self.txt_email.setPlaceholderText(
            "ornek@email.com"
        )

        iletisim_layout.addRow(
            "E-Posta",
            self.txt_email,
        )

        # -----------------------------------------------------
        # IBAN
        # -----------------------------------------------------

        self.txt_iban = QLineEdit()

        self.txt_iban.setPlaceholderText(
            "TR00 0000 0000 0000 0000 0000 00"
        )

        self.txt_iban.setMaxLength(
            34
        )

        iletisim_layout.addRow(
            "IBAN",
            self.txt_iban,
        )

        # -----------------------------------------------------
        # Adres
        # -----------------------------------------------------

        self.txt_adres = QTextEdit()

        self.txt_adres.setFixedHeight(
            85
        )

        self.txt_adres.setPlaceholderText(
            "Adres bilgisi"
        )

        iletisim_layout.addRow(
            "Adres",
            self.txt_adres,
        )

        right_layout.addWidget(
            iletisim_group
        )

        # =====================================================
        # DİĞER BİLGİLER
        # =====================================================

        diger_group = QGroupBox(
            "Diğer Bilgiler"
        )

        diger_layout = QFormLayout(
            diger_group
        )

        diger_layout.setContentsMargins(
            20,
            28,
            20,
            20,
        )

        diger_layout.setHorizontalSpacing(
            15
        )

        diger_layout.setVerticalSpacing(
            10
        )

        diger_layout.setLabelAlignment(
            Qt.AlignRight
        )

        # -----------------------------------------------------
        # Uyruk
        # -----------------------------------------------------

        self.cmb_uyruk = QComboBox()

        self.cmb_uyruk.setEditable(
            True
        )

        self.cmb_uyruk.addItems(
            [
                "",
                "Türkiye",
                "Azerbaycan",
                "Türkmenistan",
                "Özbekistan",
                "Diğer",
            ]
        )

        self.cmb_uyruk.setCurrentText(
            "Türkiye"
        )

        diger_layout.addRow(
            "Uyruk",
            self.cmb_uyruk,
        )

        # -----------------------------------------------------
        # Medeni Durum
        # -----------------------------------------------------

        self.cmb_medeni = QComboBox()

        self.cmb_medeni.addItems(
            [
                "",
                "Bekar",
                "Evli",
                "Boşanmış",
                "Dul",
            ]
        )

        diger_layout.addRow(
            "Medeni Durum",
            self.cmb_medeni,
        )

        # -----------------------------------------------------
        # Eğitim
        # -----------------------------------------------------

        self.cmb_egitim = QComboBox()

        self.cmb_egitim.setEditable(
            True
        )

        self.cmb_egitim.addItems(
            [
                "",
                "İlkokul",
                "Ortaokul",
                "Lise",
                "Ön Lisans",
                "Lisans",
                "Yüksek Lisans",
                "Doktora",
            ]
        )

        diger_layout.addRow(
            "Eğitim Durumu",
            self.cmb_egitim,
        )

        # -----------------------------------------------------
        # Maaş
        # -----------------------------------------------------

        self.spin_maas = QDoubleSpinBox()

        self.spin_maas.setRange(
            0,
            999999999,
        )

        self.spin_maas.setDecimals(
            2
        )

        self.spin_maas.setSuffix(
            " TL"
        )

        self.spin_maas.setGroupSeparatorShown(
            True
        )

        diger_layout.addRow(
            "Maaş",
            self.spin_maas,
        )

        # -----------------------------------------------------
        # Fotoğraf
        # -----------------------------------------------------

        photo_layout = QHBoxLayout()

        photo_layout.setSpacing(
            8
        )

        self.txt_fotograf = QLineEdit()

        self.txt_fotograf.setPlaceholderText(
            "Fotoğraf dosya yolu"
        )

        self.btn_fotograf = QPushButton(
            "Dosya Seç"
        )

        self.btn_fotograf.setMinimumWidth(
            90
        )

        photo_layout.addWidget(
            self.txt_fotograf,
            1
        )

        photo_layout.addWidget(
            self.btn_fotograf
        )

        diger_layout.addRow(
            "Fotoğraf",
            photo_layout,
        )

        # -----------------------------------------------------
        # Açıklama
        # -----------------------------------------------------

        self.txt_aciklama = QTextEdit()

        self.txt_aciklama.setFixedHeight(
            85
        )

        self.txt_aciklama.setPlaceholderText(
            "Personel hakkında açıklama..."
        )

        diger_layout.addRow(
            "Açıklama",
            self.txt_aciklama,
        )

        right_layout.addWidget(
            diger_group
        )

        right_layout.addStretch()

        # =====================================================
        # SÜTUNLARI ANA LAYOUT'A EKLE
        # =====================================================

        columns_layout.addLayout(
            left_layout,
            1
        )

        columns_layout.addLayout(
            right_layout,
            1
        )

        main_layout.addLayout(
            columns_layout,
            1
        )

        # =====================================================
        # BUTONLAR
        # =====================================================

        self.buttons = QDialogButtonBox(
            QDialogButtonBox.Save
            | QDialogButtonBox.Cancel
        )

        self.btn_save = self.buttons.button(
            QDialogButtonBox.Save
        )

        self.btn_cancel = self.buttons.button(
            QDialogButtonBox.Cancel
        )

        self.btn_save.setText(
            "Kaydet"
        )

        self.btn_cancel.setText(
            "İptal"
        )

        main_layout.addWidget(
            self.buttons
        )

        # =====================================================
        # STİL
        # =====================================================

        self.setStyleSheet(
            """
            /* =================================================
               ANA DIALOG
               ================================================= */

            QDialog {
                background: #F8FAFC;
            }

            /* =================================================
               GROUPBOX
               ================================================= */

            QGroupBox {
                background: #FFFFFF;

                border: 1px solid #CBD5E1;

                border-radius: 8px;

                margin-top: 12px;

                padding-top: 8px;

                font-size: 13px;

                font-weight: bold;

                color: #1E293B;
            }

            QGroupBox::title {
                subcontrol-origin: margin;

                subcontrol-position: top left;

                left: 15px;

                padding-left: 7px;

                padding-right: 7px;

                color: #1E293B;

                background: #F8FAFC;
            }

            /* =================================================
               LABEL
               ================================================= */

            QLabel {
                color: #334155;

                font-size: 13px;
            }

            /* =================================================
               INPUTLAR
               ================================================= */

            QLineEdit,
            QComboBox,
            QDateEdit,
            QSpinBox,
            QDoubleSpinBox,
            QTextEdit {

                min-height: 32px;

                background: #FFFFFF;

                border: 1px solid #CBD5E1;

                border-radius: 6px;

                padding-left: 8px;

                padding-right: 8px;

                color: #1E293B;
            }

            /* =================================================
               FOCUS
               ================================================= */

            QLineEdit:focus,
            QComboBox:focus,
            QDateEdit:focus,
            QSpinBox:focus,
            QDoubleSpinBox:focus,
            QTextEdit:focus {

                border: 1px solid #2563EB;

                background: #FFFFFF;
            }

            /* =================================================
               COMBOBOX
               ================================================= */

            QComboBox::drop-down {

                width: 28px;

                border: none;
            }

            /* =================================================
               BUTONLAR
               ================================================= */

            QPushButton {

                min-height: 34px;

                min-width: 90px;

                border-radius: 6px;

                padding-left: 16px;

                padding-right: 16px;
            }

            /* =================================================
               FOTOĞRAF BUTONU
               ================================================= */

            QPushButton#photoButton {

                background: #E2E8F0;

                color: #334155;

                border: 1px solid #CBD5E1;
            }

            QPushButton#photoButton:hover {

                background: #CBD5E1;
            }

            /* =================================================
               KAYDET
               ================================================= */

            QDialogButtonBox QPushButton[text="Kaydet"] {

                background: #2563EB;

                color: white;

                border: none;

                font-weight: bold;
            }

            QDialogButtonBox QPushButton[text="Kaydet"]:hover {

                background: #1D4ED8;
            }

            /* =================================================
               İPTAL
               ================================================= */

            QDialogButtonBox QPushButton[text="İptal"] {

                background: #E2E8F0;

                color: #334155;

                border: 1px solid #CBD5E1;
            }

            QDialogButtonBox QPushButton[text="İptal"]:hover {

                background: #CBD5E1;
            }
            """
        )

        # Fotoğraf butonuna object name
        self.btn_fotograf.setObjectName(
            "photoButton"
        )

    # =========================================================
    # CONNECTIONS
    # =========================================================

    def create_connections(self) -> None:

        self.buttons.accepted.connect(
            self.save
        )

        self.buttons.rejected.connect(
            self.reject
        )

        self.btn_fotograf.clicked.connect(
            self.select_photo
        )

    # =========================================================
    # FOTOĞRAF SEÇ
    # =========================================================

    def select_photo(self) -> None:

        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Personel Fotoğrafı Seç",
            "",
            (
                "Resim Dosyaları "
                "(*.png *.jpg *.jpeg *.bmp *.webp)"
            ),
        )

        if file_path:

            self.txt_fotograf.setText(
                file_path
            )

    # =========================================================
    # POZİSYONLARI YÜKLE
    # =========================================================

    def load_pozisyonlar(self) -> None:

        self.cmb_pozisyon.clear()

        try:

            pozisyonlar = (
                self.pozisyon_service
                .get_tum_pozisyonlar()
            )

        except AttributeError:

            try:

                pozisyonlar = (
                    self.pozisyon_service
                    .get_all()
                )

            except AttributeError:

                QMessageBox.warning(
                    self,
                    "Pozisyon",
                    (
                        "PozisyonService içinde "
                        "get_tum_pozisyonlar() veya "
                        "get_all() bulunamadı."
                    ),
                )

                return

        for pozisyon in pozisyonlar:

            self.cmb_pozisyon.addItem(
                pozisyon.ad,
                pozisyon.id,
            )

    # =========================================================
    # PERSONELİ FORMA YÜKLE
    # =========================================================

    def load_personel(self) -> None:

        p = self.personel

        # -----------------------------------------------------
        # Kimlik
        # -----------------------------------------------------

        self.txt_sicil.setText(
            p.sicil_no or ""
        )

        self.txt_tc.setText(
            p.tc_kimlik_no or ""
        )

        self.txt_ad.setText(
            p.ad or ""
        )

        self.txt_soyad.setText(
            p.soyad or ""
        )

        self.cmb_cinsiyet.setCurrentText(
            p.cinsiyet or ""
        )

        # -----------------------------------------------------
        # Doğum
        # -----------------------------------------------------

        if p.dogum_tarihi:

            self.date_dogum.setDate(
                QDate(
                    p.dogum_tarihi.year,
                    p.dogum_tarihi.month,
                    p.dogum_tarihi.day,
                )
            )

        self.txt_dogum_yeri.setText(
            p.dogum_yeri or ""
        )

        # -----------------------------------------------------
        # Diğer
        # -----------------------------------------------------

        self.cmb_uyruk.setCurrentText(
            p.uyruk or ""
        )

        self.cmb_medeni.setCurrentText(
            p.medeni_durum or ""
        )

        self.cmb_egitim.setCurrentText(
            p.egitim_durumu or ""
        )

        # -----------------------------------------------------
        # İş
        # -----------------------------------------------------

        if p.ise_giris_tarihi:

            self.date_ise_giris.setDate(
                QDate(
                    p.ise_giris_tarihi.year,
                    p.ise_giris_tarihi.month,
                    p.ise_giris_tarihi.day,
                )
            )

        self.spin_izin.setValue(
            p.izin_hakki or 14
        )

        # -----------------------------------------------------
        # Pozisyon
        # -----------------------------------------------------

        index = self.cmb_pozisyon.findData(
            p.pozisyon_id
        )

        if index >= 0:

            self.cmb_pozisyon.setCurrentIndex(
                index
            )

        # -----------------------------------------------------
        # İletişim
        # -----------------------------------------------------

        self.txt_telefon.setText(
            p.telefon or ""
        )

        self.txt_email.setText(
            p.email or ""
        )

        self.txt_iban.setText(
            p.iban or ""
        )

        self.txt_adres.setPlainText(
            p.adres or ""
        )

        # -----------------------------------------------------
        # Maaş
        # -----------------------------------------------------

        if p.maas is not None:

            self.spin_maas.setValue(
                float(p.maas)
            )

        # -----------------------------------------------------
        # Diğer
        # -----------------------------------------------------

        self.txt_fotograf.setText(
            p.fotograf or ""
        )

        self.txt_aciklama.setPlainText(
            p.aciklama or ""
        )

    # =========================================================
    # TARİH
    # =========================================================

    @staticmethod
    def get_date(
        widget: QDateEdit,
    ):

        qdate = widget.date()

        if not qdate.isValid():

            return None

        return qdate.toPython()

    # =========================================================
    # DOĞRULAMA
    # =========================================================

    def validate(self) -> bool:

        # =====================================================
        # SİCİL
        # =====================================================

        sicil_no = (
            self.txt_sicil
            .text()
            .strip()
        )

        if not sicil_no:

            QMessageBox.warning(
                self,
                "Eksik Bilgi",
                "Sicil No zorunludur.",
            )

            self.txt_sicil.setFocus()

            return False

        # =====================================================
        # AD
        # =====================================================

        ad = (
            self.txt_ad
            .text()
            .strip()
        )

        if not ad:

            QMessageBox.warning(
                self,
                "Eksik Bilgi",
                "Ad zorunludur.",
            )

            self.txt_ad.setFocus()

            return False

        # =====================================================
        # SOYAD
        # =====================================================

        soyad = (
            self.txt_soyad
            .text()
            .strip()
        )

        if not soyad:

            QMessageBox.warning(
                self,
                "Eksik Bilgi",
                "Soyad zorunludur.",
            )

            self.txt_soyad.setFocus()

            return False

        # =====================================================
        # POZİSYON
        # =====================================================

        pozisyon_id = (
            self.cmb_pozisyon
            .currentData()
        )

        if not pozisyon_id:

            QMessageBox.warning(
                self,
                "Eksik Bilgi",
                "Lütfen bir pozisyon seçin.",
            )

            self.cmb_pozisyon.setFocus()

            return False

        # =====================================================
        # TC KİMLİK
        # =====================================================

        tc = (
            self.txt_tc
            .text()
            .strip()
        )

        if tc:

            if (
                len(tc) != 11
                or not tc.isdigit()
            ):

                QMessageBox.warning(
                    self,
                    "Geçersiz TC Kimlik No",
                    (
                        "TC Kimlik No "
                        "11 haneli olmalıdır."
                    ),
                )

                self.txt_tc.setFocus()

                return False

        # =====================================================
        # E-POSTA
        # =====================================================

        email = (
            self.txt_email
            .text()
            .strip()
        )

        if email:

            email_pattern = (
                r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
            )

            if not re.match(
                email_pattern,
                email,
            ):

                QMessageBox.warning(
                    self,
                    "Geçersiz E-Posta",
                    "Lütfen geçerli bir e-posta adresi girin.",
                )

                self.txt_email.setFocus()

                return False

        # =====================================================
        # IBAN
        # =====================================================

        iban = (
            self.txt_iban
            .text()
            .strip()
            .replace(" ", "")
            .upper()
        )

        if iban:

            if (
                not iban.startswith("TR")
                or len(iban) != 26
                or not iban[2:].isdigit()
            ):

                QMessageBox.warning(
                    self,
                    "Geçersiz IBAN",
                    (
                        "Türkiye IBAN numarası "
                        "TR ile başlamalı ve "
                        "26 karakter olmalıdır."
                    ),
                )

                self.txt_iban.setFocus()

                return False

        return True

    # =========================================================
    # KAYDET
    # =========================================================

    def save(self) -> None:

        # =====================================================
        # VALIDATION
        # =====================================================

        if not self.validate():

            return

        # =====================================================
        # VERİLER
        # =====================================================

        sicil_no = (
            self.txt_sicil
            .text()
            .strip()
        )

        ad = (
            self.txt_ad
            .text()
            .strip()
        )

        soyad = (
            self.txt_soyad
            .text()
            .strip()
        )

        tc_kimlik_no = (
            self.txt_tc
            .text()
            .strip()
            or None
        )

        cinsiyet = (
            self.cmb_cinsiyet
            .currentText()
            .strip()
            or None
        )

        dogum_tarihi = self.get_date(
            self.date_dogum
        )

        dogum_yeri = (
            self.txt_dogum_yeri
            .text()
            .strip()
            or None
        )

        uyruk = (
            self.cmb_uyruk
            .currentText()
            .strip()
            or None
        )

        medeni_durum = (
            self.cmb_medeni
            .currentText()
            .strip()
            or None
        )

        egitim_durumu = (
            self.cmb_egitim
            .currentText()
            .strip()
            or None
        )

        ise_giris_tarihi = self.get_date(
            self.date_ise_giris
        )

        izin_hakki = (
            self.spin_izin.value()
        )

        pozisyon_id = (
            self.cmb_pozisyon
            .currentData()
        )

        telefon = (
            self.txt_telefon
            .text()
            .strip()
            or None
        )

        email = (
            self.txt_email
            .text()
            .strip()
            or None
        )

        adres = (
            self.txt_adres
            .toPlainText()
            .strip()
            or None
        )

        maas = Decimal(
            str(
                self.spin_maas.value()
            )
        )

        iban = (
            self.txt_iban
            .text()
            .strip()
            .replace(" ", "")
            .upper()
            or None
        )

        fotograf = (
            self.txt_fotograf
            .text()
            .strip()
            or None
        )

        aciklama = (
            self.txt_aciklama
            .toPlainText()
            .strip()
            or None
        )

        # =====================================================
        # KAYIT
        # =====================================================

        try:

            # =================================================
            # GÜNCELLEME
            # =================================================

            if self.is_edit_mode:

                self.personel_service.personel_guncelle(
                    self.personel.id,

                    sicil_no=sicil_no,

                    ad=ad,

                    soyad=soyad,

                    ise_giris_tarihi=ise_giris_tarihi,

                    pozisyon_id=pozisyon_id,

                    tc_kimlik_no=tc_kimlik_no,

                    cinsiyet=cinsiyet,

                    dogum_tarihi=dogum_tarihi,

                    dogum_yeri=dogum_yeri,

                    uyruk=uyruk,

                    medeni_durum=medeni_durum,

                    egitim_durumu=egitim_durumu,

                    izin_hakki=izin_hakki,

                    telefon=telefon,

                    email=email,

                    adres=adres,

                    maas=maas,

                    iban=iban,

                    fotograf=fotograf,

                    aciklama=aciklama,
                )

            # =================================================
            # YENİ PERSONEL
            # =================================================

            else:

                self.personel_service.personel_ekle(

                    sicil_no=sicil_no,

                    ad=ad,

                    soyad=soyad,

                    ise_giris_tarihi=ise_giris_tarihi,

                    pozisyon_id=pozisyon_id,

                    tc_kimlik_no=tc_kimlik_no,

                    cinsiyet=cinsiyet,

                    dogum_tarihi=dogum_tarihi,

                    dogum_yeri=dogum_yeri,

                    uyruk=uyruk,

                    medeni_durum=medeni_durum,

                    egitim_durumu=egitim_durumu,

                    izin_hakki=izin_hakki,

                    telefon=telefon,

                    email=email,

                    adres=adres,

                    maas=maas,

                    iban=iban,

                    fotograf=fotograf,

                    aciklama=aciklama,
                )

            # =================================================
            # BAŞARILI
            # =================================================

            self.accept()

        # =====================================================
        # HATA
        # =====================================================

        except Exception as exc:

            QMessageBox.critical(
                self,
                "Personel Kaydedilemedi",
                (
                    "Personel kaydedilirken "
                    "bir hata oluştu.\n\n"
                    f"{exc}"
                ),
            )