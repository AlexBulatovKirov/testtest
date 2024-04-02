#создай приложение для запоминания информации

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,QRadioButton,QHBoxLayout,QGroupBox


#СОЗДАНИЕ ПРИЛОЖЕНИЯ И ОКНА ПРОГРАММЫ
app = QApplication([])
main_win = QWidget()
main_win.resize(400,200)

#СОЗДАНИЕ ВИДЖЕТОВ
RadioGroupButtom = QGroupBox('Вариант ответа')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чульмцы')
rbtn_4 = QRadioButton('Алеуты')
layout1 = QVBoxLayout()
layout1.addWidget(rbtn_1)
layout1.addWidget(rbtn_2)
layout1.addWidget(rbtn_3)
layout1.addWidget(rbtn_4)
RadioGroupButtom.setLayout(layout1)


#СОЗДАНИЕ НАПРАВЛЯЮЩЕЙ И РАЗМЕЩЕНИЕ НА НЕЙ КНОПОК
layout_main = QVBoxLayout()
layout1 = QHBoxLayout()
layout2 = QHBoxLayout()
label = QLabel('SUUUUUUUUUUUUUUUUUUUUUUUUUU')


layout_main.addWidget(label, alignment = Qt.AlignCenter)
layout_main.addLayout(layout1)
layout_main.addLayout(layout2)
layout_main.addWidget(RadioGroupButtom)


#ОТОБРАЖЕНИЕ НАПРАВЛЯЮЩЕЙ В ОКНЕ ПРОГРАММЫ И ОТОБРАЖЕНИЕ ОКНА НА ЭКРАНЕ МОНИТОРА
main_win.setLayout(layout_main)
main_win.show()
app.exec_()