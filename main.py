from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

tree = ('Ты старше 5 класса?', {1: ('Твоя основная цель это заработок на программирование?',
                                    {0: ('выбери что тебе больше нравиться',
                                         {0: ('Математические вычислений, научная деятельность', ('Хочешь более простой для обучения и понимания, но с меньшими возможностями язык программирования?', {1: 'MATLAB', 0: 'Фортран'})),
                                          1: ('Разработка игр и приложений', ('Хочешь разрабатывать игры и приложения для пк?'), {1: 'c++',
                                                                                                                                 0: ('Хочешь разрабатывать игры для мобильных устройств?',
                                                                                                                                     {1: ('Для андроид',
                                                                                                                                          {1: ('Для айфонов',
                                                                                                                                               {1: 'Swift',
                                                                                                                                                0: "К сожалению я не знаю других платформ для такой деятельности, попробуй поменять свой выбор, либо дождись обновления приложения"})}),
                                                                                                                                      0: 'К сожалению я не знаю других платформ для такой деятельности, попробуй поменять свой выбор, либо дождись обновления приложения '})}),
                                          2: ('Хочешь создание сайтов', ('Хочешь создавать внутреннею часть сайта, отвечать за скорость и безопасность сайта?',
                                                                        {1: ('Хочешь более простой для обучения и понимания, но с меньшими возможностями и более медленный язык?', {1: 'Python ', 0: 'GO'}),
                                                                         0: ('Хочешь писать различные анимации, весь дизайн сайта?', {1: 'JavaScript', 0: 'Вариант появиться с обновлением'})}))}),
                                     1: ('Solidity', )}),
                                0: ('Scratch', )})


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(100, 100, 100, 255), stop:1 rgba(50, 50, 50, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 150))
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label.setAlignment(Qt.AlignBottom | Qt.AlignCenter)
        self.label.setFont(QtGui.QFont('Arial', 30))
        self.label.setWordWrap(True)
        self.label.setText('Ты старше 5 класса?')
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 350, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setCheckable(True)
        self.pushButton.clicked.connect(lambda: self.test_func2(1, tree))
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 350, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.clicked.connect(lambda: self.test_func2(0, tree))
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">да</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "да"))
        self.pushButton_2.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">да</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "нет"))

    def test_func2(self, num: int, last_tuple):
        global tree
        if len(last_tuple) == 2:
            last_dict = last_tuple[1]
            new_tuple = last_dict.get(num)
            tree = new_tuple
            self.label.setText(new_tuple[0])
            if new_tuple[0] == 'выбери что тебе больше нравиться':
                pass
                # self.special_case()
            print(tree)
        else:
            self.label.setText(*last_tuple)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
