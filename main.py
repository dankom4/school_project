from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

event_cycle = ['1', '2', '3']
tree = ('Ты старше 5 класса?', {1: ('Твоя основная цель это заработок на программирование?',
                                    {1: {1: ('Математические вычислений, научная деятельность', ('Хочешь более простой для обучения и понимания, но с меньшими возможностями язык программирования?', {1: 'MATLAB', 0: 'Фортран'})),
                                         2: ('Разработка игр и приложений', ('Хочешь разрабатывать игры и приложения для пк?'), {1: 'c++',
                                                                                                                                 0: ('Хочешь разрабатывать игры для мобильных устройств?',
                                                                                                                                     {1: ('Для андроид',
                                                                                                                                          {1: ('Для айфонов',
                                                                                                                                               {1: 'Swift',
                                                                                                                                                0: "К сожалению я не знаю других платформ для такой деятельности, попробуй поменять свой выбор, либо дождись обновления приложения"})}),
                                                                                                                                      0: 'К сожалению я не знаю других платформ для такой деятельности, попробуй поменять свой выбор, либо дождись обновления приложения '})}),
                                         3: ('Хочешь создание сайтов', ('Хочешь создавать внутреннею часть сайта, отвечать за скорость и безопасность сайта?',
                                                                        {1: ('Хочешь более простой для обучения и понимания, но с меньшими возможностями и более медленный язык?', {1: 'Python ', 0: 'GO'}),
                                                                         0: ('Хочешь писать различные анимации, весь дизайн сайта?', {1: 'JavaScript', 0: 'Вариант появиться с обновлением'})}))},
                                     0: ('Solidity')}),
                                0: tuple('Scratch')})


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(100, 100, 100, 255), stop:1 rgba(50, 50, 50, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        generator = self.text_generator(questions)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 150))
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label.setAlignment(Qt.AlignBottom | Qt.AlignCenter)
        self.label.setFont(QtGui.QFont('Arial', 30))
        self.label.setText('ты старше 12 лет?')
        self.label.setWordWrap(True)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 350, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setCheckable(True)
        self.pushButton.clicked.connect(lambda: next(generator))
        self.pushButton.clicked.connect(lambda: event_cycle.append(1))
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 350, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.clicked.connect(lambda: next(generator))
        self.pushButton_2.clicked.connect(lambda: event_cycle.append(0))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">да</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "да"))
        self.pushButton_2.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">да</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "нет"))

    def text_generator(self, list_questions):
        for element in list_questions:
            self.label.setText(element)
            yield

    def test_def(self, num: int,  hash_table: dict):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
