"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : main.py
Açıklama   : Program Başlangıç Noktası
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

import sys

from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow
from pathlib import Path



def main() -> None:
   

    app = QApplication(sys.argv)
    # =====================================================
    # QSS Tema
    # =====================================================

    qss_path = (
        Path(__file__).parent
        / "ui"
        / "resources"
        / "style.qss"
    )

    if qss_path.exists():
        app.setStyleSheet(
            qss_path.read_text(encoding="utf-8")
        )
    # =====================================================
    # Ana Pencere
    # =====================================================

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()