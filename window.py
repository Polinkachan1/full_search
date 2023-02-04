from random import choice
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QMainWindow, QLabel,
)
from PyQt5.QtGui import (
    QMouseEvent,
    QKeyEvent,
    QPixmap,
)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self._images = [
            'car_1.jpg',
            'car_2.jpg',
        ]
        self._selected_image = self._images[0]
        self._init_ui()

    def _init_ui(self) -> None:
        self.setGeometry(300, 300, 600, 600)
        self.image = QLabel(self)
        self.image.setGeometry(0, 0, 60, 38)
        self._pixmap = QPixmap(self._selected_image)
        self.image.setPixmap(self._pixmap)
        self.show()
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        self.image.move(event.x(), event.y())

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key_Space:
            self._selected_image = choice(self._images)
            self._paint()

    def _paint(self) -> None:
        self._pixmap.load(self._selected_image)
        self.image.setPixmap(self._pixmap)
