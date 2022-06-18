## Ex 3-9. 날짜와 시간 표시하기.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QDateTime, Qt


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.datetime = QDateTime.currentDateTime()
        self.initUI()

    def initUI(self):
        # self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))
        self.statusBar().showMessage(self.datetime.toString('yyyy.MM.dd, hh:mm:ss'))

        self.setWindowTitle('Date')
        self.setGeometry(300, 300, 400, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())