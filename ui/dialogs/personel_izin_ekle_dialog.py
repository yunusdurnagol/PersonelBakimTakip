"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : ui/dialogs/personel_izin_ekle_dialog.py
Açıklama   : Personel için yeni izin ekleme dialogu
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from PySide6.QtCore import QDate

from PySide6.QtWidgets import (
    QComboBox,
    QDateEdit,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QGroupBox,
    QLabel,
    QMessageBox,
    QPlainTextEdit,
    QSpinBox,
    QVBoxLayout,
)


class PersonelIzinEkleDialog(QDialog):
    """
    Personel için yeni izin kaydı ekleme dialogu.

    Özellikler
    ----------
    - Başlangıç tarihi
    - Bitiş tarihi
    - Kullanılan izin gün sayısı
    - İzin nedeni
    - Açıklama

    Not
    ---
    İzin gün sayısı sistem tarafından hesaplanmaz.
    Kullanıcının girdiği değer doğrudan kaydedilir.
    """

    # =====================================================
    # INIT
    # =====================================================

    def __init__(
        self,
        personel_izin_service,
        personel,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self.service = personel_izin_service
        self.personel = personel

        self.setWindowTitle(
            "Personel İzin Ekle"
        )

        self.setMinimumWidth(
            520
        )

        self.create_ui()
        self.create_connections()

    # =====================================================
    # UI
    # =====================================================

    def create_ui(self) -> None:

        main_layout = QVBoxLayout(self)

        main_layout.setContentsMargins(
            20,
            20,
            20,
            20,
        )

        main_layout.setSpacing(
            15
        )

        # =================================================
        # PERSONEL
        # =================================================

        personel_group = QGroupBox(
            "Personel"
        )

        personel_layout = QFormLayout(
            personel_group
        )

        personel_layout.setSpacing(
            10
        )

        self.lbl_personel = QLabel(
            self.get_personel_adi()
        )

        self.lbl_personel.setStyleSheet(
            """
            QLabel {
                font-size: 11pt;
                font-weight: 600;
                color: #1E293B;
                padding: 6px;
            }
            """
        )

        personel_layout.addRow(
            "Personel:",
            self.lbl_personel,
        )

        main_layout.addWidget(
            personel_group
        )

        # =================================================
        # İZİN BİLGİLERİ
        # =================================================

        izin_group = QGroupBox(
            "İzin Bilgileri"
        )

        form = QFormLayout(
            izin_group
        )

        form.setSpacing(
            12
        )

        # =================================================
        # BAŞLANGIÇ TARİHİ
        # =================================================

        self.date_baslangic = QDateEdit()

        self.date_baslangic.setCalendarPopup(
            True
        )

        self.date_baslangic.setDisplayFormat(
            "dd.MM.yyyy"
        )

        self.date_baslangic.setDate(
            QDate.currentDate()
        )

        form.addRow(
            "İzin Başlangıç:",
            self.date_baslangic,
        )

        # =================================================
        # BİTİŞ TARİHİ
        # =================================================

        self.date_bitis = QDateEdit()

        self.date_bitis.setCalendarPopup(
            True
        )

        self.date_bitis.setDisplayFormat(
            "dd.MM.yyyy"
        )

        self.date_bitis.setDate(
            QDate.currentDate()
        )

        form.addRow(
            "İzin Bitiş:",
            self.date_bitis,
        )

        # =================================================
        # GÜN SAYISI
        # =================================================

        self.spin_gun = QSpinBox()

        self.spin_gun.setMinimum(
            1
        )

        self.spin_gun.setMaximum(
            365
        )

        self.spin_gun.setValue(
            1
        )

        self.spin_gun.setSuffix(
            " gün"
        )

        form.addRow(
            "Kullanılan İzin:",
            self.spin_gun,
        )

        # =================================================
        # İZİN NEDENİ
        # =================================================

        self.combo_neden = QComboBox()

        self.combo_neden.addItems(
            [
                "Yıllık İzin",
                "Mazeret İzni",
                "Hastalık İzni",
                "Ücretsiz İzin",
                "Diğer",
            ]
        )

        # Varsayılan:
        # Yıllık İzin

        self.combo_neden.setCurrentIndex(
            0
        )

        form.addRow(
            "İzin Nedeni:",
            self.combo_neden,
        )

        # =================================================
        # AÇIKLAMA
        # =================================================

        self.txt_aciklama = QPlainTextEdit()

        self.txt_aciklama.setPlaceholderText(
            "İzin ile ilgili açıklama..."
        )

        self.txt_aciklama.setMinimumHeight(
            90
        )

        form.addRow(
            "Açıklama:",
            self.txt_aciklama,
        )

        main_layout.addWidget(
            izin_group
        )

        # =================================================
        # BUTONLAR
        # =================================================

        self.buttons = QDialogButtonBox(
            QDialogButtonBox.Save
            | QDialogButtonBox.Cancel
        )

        self.buttons.button(
            QDialogButtonBox.Save
        ).setText(
            "Kaydet"
        )

        self.buttons.button(
            QDialogButtonBox.Cancel
        ).setText(
            "İptal"
        )

        main_layout.addWidget(
            self.buttons
        )

        # =================================================
        # STYLE
        # =================================================

        self.setStyleSheet(
            """
            QDialog {
                background: #F8FAFC;
            }

            QGroupBox {
                background: white;
                border: 1px solid #E2E8F0;
                border-radius: 10px;
                margin-top: 10px;
                padding: 15px;
                font-weight: 600;
                color: #334155;
            }

            QGroupBox::title {
                subcontrol-origin: margin;
                left: 12px;
                padding: 0 6px;
                background: #F8FAFC;
            }

            QLabel {
                color: #475569;
            }

            QDateEdit,
            QSpinBox,
            QComboBox,
            QPlainTextEdit {
                background: white;
                border: 1px solid #CBD5E1;
                border-radius: 7px;
                padding: 7px;
                min-height: 20px;
            }

            QDateEdit:focus,
            QSpinBox:focus,
            QComboBox:focus,
            QPlainTextEdit:focus {
                border: 1px solid #2563EB;
            }

            QPushButton {
                min-height: 34px;
                padding: 0 18px;
                border-radius: 7px;
                border: 1px solid #CBD5E1;
                background: white;
                color: #334155;
                font-weight: 600;
            }

            QPushButton:hover {
                background: #F1F5F9;
            }

            QDialogButtonBox QPushButton[text="Kaydet"] {
                background: #2563EB;
                color: white;
                border: none;
            }

            QDialogButtonBox QPushButton[text="Kaydet"]:hover {
                background: #1D4ED8;
            }
            """
        )

    # =====================================================
    # CONNECTIONS
    # =====================================================

    def create_connections(self) -> None:

        self.buttons.accepted.connect(
            self.kaydet
        )

        self.buttons.rejected.connect(
            self.reject
        )

    # =====================================================
    # PERSONEL ADI
    # =====================================================

    def get_personel_adi(self) -> str:

        ad = getattr(
            self.personel,
            "ad",
            "",
        ) or ""

        soyad = getattr(
            self.personel,
            "soyad",
            "",
        ) or ""

        sicil_no = getattr(
            self.personel,
            "sicil_no",
            "",
        ) or ""

        return (
            f"{ad} {soyad}"
            f"  ({sicil_no})"
        ).strip()

    # =====================================================
    # QDATE → DATE
    # =====================================================

    @staticmethod
    def qdate_to_date(
        qdate: QDate,
    ):

        return qdate.toPython()

    # =====================================================
    # KAYDET
    # =====================================================

    def kaydet(self) -> None:

        try:

            personel_id = self.personel.id

            # ---------------------------------------------
            # TARİHLER
            # ---------------------------------------------

            izin_baslangic = (
                self.qdate_to_date(
                    self.date_baslangic.date()
                )
            )

            izin_bitis = (
                self.qdate_to_date(
                    self.date_bitis.date()
                )
            )

            # ---------------------------------------------
            # GÜN SAYISI
            #
            # SİSTEM HESAPLAMIYOR.
            # ---------------------------------------------

            izin_gun_sayisi = (
                self.spin_gun.value()
            )

            # ---------------------------------------------
            # İZİN NEDENİ
            # ---------------------------------------------

            izin_nedeni = (
                self.combo_neden.currentText()
            )

            # ---------------------------------------------
            # AÇIKLAMA
            # ---------------------------------------------

            aciklama = (
                self.txt_aciklama
                .toPlainText()
                .strip()
            )

            if not aciklama:

                aciklama = None

            # ---------------------------------------------
            # SERVICE
            # ---------------------------------------------

            self.service.izin_ekle(
                personel_id=personel_id,
                izin_baslangic=izin_baslangic,
                izin_bitis=izin_bitis,
                izin_gun_sayisi=izin_gun_sayisi,
                izin_nedeni=izin_nedeni,
                aciklama=aciklama,
            )

            QMessageBox.information(
                self,
                "İşlem Başarılı",
                "İzin kaydı başarıyla eklendi.",
            )

            self.accept()

        except Exception as exc:

            QMessageBox.critical(
                self,
                "İzin Eklenemedi",
                str(exc),
            )