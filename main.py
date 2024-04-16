from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

tree = ('Ты старше 5 класса?', {1: ('Твоя основная цель это заработок на программирование?',
                                    {0: ('выбери что тебе больше нравиться',
                                         {1: ('Хочешь более простой для обучения и понимания, но с меньшими возможностями язык программирования?', {1: ('MATLAB', 'https://www.mathworks.com/', '1'), 0: ('Fortran', 'https://fortran-lang.org/ru/index', '1')}),
                                          0: ('Хочешь разрабатывать игры и приложения для пк?', {1: ('c++', 'https://isocpp.org/', '1'),
                                                                                                 0: ('Хочешь разрабатывать игры для мобильных устройств?',
                                                                                                     {1: ('Для андроид',
                                                                                                          {1: ('Для айфонов',
                                                                                                               {1: ('Swift', 'https://www.swift.org/', '1'),
                                                                                                                0: ('Вариант появиться с обновлением', '', '0')})}),
                                                                                                      0: ('Вариант появиться с обновлением', '', '0')})}),
                                          2:  ('Хочешь создавать внутреннею часть сайта, отвечать за скорость и безопасность сайта?',
                                                                        {1: ('Хочешь более простой для обучения и понимания, но с меньшими возможностями и более медленный язык?', {1: ('Python', 'https://www.python.org/', '1'), 0: ('GO', 'https://go.dev/', '1')}),
                                                                         0: ('Хочешь писать различные анимации, весь дизайн сайта?', {1: ('JavaScript', 'https://www.javascript.com/', '1'), 0: ('Вариант появиться с обновлением', '', '1')})})}),
                                     1: ('Solidity', 'https://soliditylang.org/', '1')}),
                                0: ('Scratch', 'https://scratch.mit.edu/', '1')})


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(
            "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(100, 100, 100, 255), stop:1 rgba(50, 50, 50, 255));")
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

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                 "color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label")
        self.label_2.setAlignment(Qt.AlignBottom | Qt.AlignCenter)
        self.label_2.setFont(QtGui.QFont('Arial', 30))
        self.label_2.setWordWrap(True)
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

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1, 1, 1, 1))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.clicked.connect(lambda: self.test_func2(2, tree))

        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton.setText('да')
        self.pushButton_2.setText('нет')
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def test_func2(self, flag: 0 | 1 | 2, last_tuple):
        global tree
        if len(last_tuple) == 2:
            if last_tuple[0] == 'выбери что тебе больше нравиться':
                self.special_case(0)
            last_dict = last_tuple[1]
            new_tuple = last_dict.get(flag)
            tree = new_tuple
            self.label.setText(new_tuple[0])
            if new_tuple[0] == 'выбери что тебе больше нравиться':
                self.special_case(1)
            if len(new_tuple) == 3:
                self.pushButton.setText('')
                self.pushButton.setGeometry(1, 1, 1, 1)
                self.pushButton_2.setText('')
                self.pushButton_2.setGeometry(1, 1, 1, 1)
                self.label_2.setGeometry(0, 200, 800, 150)
                self.label_2.setText(new_tuple[1])

    def special_case(self, flag:  0 | 1):
        if flag == 1:
            self.pushButton.setGeometry(50, 200, 750, 100)
            self.pushButton_2.setGeometry(50, 320, 750, 100)
            self.pushButton_3.setGeometry(50, 440, 750, 100)
            self.pushButton.setText('Математические вычислений,\n'
                                    'научная деятельность')
            self.pushButton_2.setText('Разработка игр и приложений')
            self.pushButton_3.setText('создание сайтов')
            return

        self.pushButton.setGeometry(150, 350, 100, 100)
        self.pushButton_2.setGeometry(550, 350, 100, 100)
        self.pushButton_3.setGeometry(1, 1, 1, 1)
        self.pushButton.setText('да')
        self.pushButton_2.setText('нет')
        self.pushButton_3.setText('')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
