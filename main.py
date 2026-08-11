"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : main.py
Açıklama   : Program Başlangıç Noktası
Yazar      : Yunus Durnagöl
Sürüm      : 1.1.0
---------------------------------------------------------
"""

from __future__ import annotations

import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication

from core.container import AppContainer
from ui.main_window import MainWindow


def main() -> None:
    """
    Uygulama başlangıç noktası.
    """

    app = QApplication(sys.argv)

    # =====================================================
    # Tema (QSS)
    # =====================================================

    qss_path = (
        Path(__file__).parent
        / "ui"
        / "resources"
        / "style.qss"
    )

    if qss_path.exists():
        app.setStyleSheet(
            qss_path.read_text(
                encoding="utf-8"
            )
        )

    # =====================================================
    # Dependency Injection Container
    # =====================================================

    container = AppContainer()

    # =====================================================
    # Ana Pencere
    # =====================================================

    window = MainWindow(container)
    window.show()

    exit_code = app.exec()

    # =====================================================
    # Veritabanı bağlantısını kapat
    # =====================================================

    container.close()

    sys.exit(exit_code)


if __name__ == "__main__":
    main()