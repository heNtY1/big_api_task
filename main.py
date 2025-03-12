import io
import os
import sys
import requests

from PyQt6 import uic
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel



class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.server_address = 'https://static-maps.yandex.ru/v1?'
        self.api_key = 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'
        self.initUI()

    def initUI(self):
        uic.loadUi('ui_file.ui', self)
        self.wight_Edit.setText('55.755811')
        self.high_Edit.setText('37.617617')
        self.size_Edit.setText('0.05')
        self.ok_button.clicked.connect(self.getImage)

    def getImage(self):
        server_address = 'https://static-maps.yandex.ru/v1?'
        api_key = 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'
        a = self.wight_Edit.text()
        b = self.high_Edit.text()
        c = self.size_Edit.text()
        self.ll_spn = f'll={b},{a}&spn={c},{c}'
        # Готовим запрос.

        map_request = f"{server_address}{self.ll_spn}&apikey={api_key}"
        response = requests.get(map_request)

        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        # Запишем полученное изображение в файл.
        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(response.content)

        self.imagee()

    def imagee(self):
        self.pixmap = QPixmap(self.map_file)
        self.map_label.resize(640, 300)
        self.map_label.setPixmap(self.pixmap)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
