from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QGroupBox, QLabel, QVBoxLayout,QRadioButton,QHBoxLayout,QMessageBox
from random import shuffle
import sqlite3

#СОЗДАНИЕ ПРИЛОЖЕНИЯ И ОКНА ПРОГРАММЫ
app = QApplication([])
main_win = QWidget()
main_win.resize(400,200)
main_win.setWindowTitle('15237125836128739812')
main_win.setStyleSheet('background-image:url(istockphoto-467367026-612x612.jpg)')

#СОЗДАНИЕ ВИДЖЕТОВ
label = QLabel('Ответь на вопрос')
btn = QPushButton('Ответить')

#ГРУППА c вопросом
RGB = QGroupBox("Варианты ответов")
btn_answer1 = QRadioButton('2005')
btn_answer2 = QRadioButton('2007')
btn_answer3 = QRadioButton('2004')
btn_answer4 = QRadioButton('2006')
layout1 = QVBoxLayout()
h1 = QHBoxLayout()
h2 = QHBoxLayout()
h1.addWidget(btn_answer1)
h1.addWidget(btn_answer2)
h2.addWidget(btn_answer3)
h2.addWidget(btn_answer4)
layout1.addLayout(h1)
layout1.addLayout(h2)
RGB.setLayout(layout1)

answers = [btn_answer1, btn_answer2, btn_answer3, btn_answer4]
def ask(q,v1,v2,v3,v4):
    shuffle(answers)
    answers[0].setText(v1)
    answers[1].setText(v2)
    answers[2].setText(v3)
    answers[3].setText(v4)

    label.setText(q)
    quest()

#Группа с ответом
RGB2 = QGroupBox("Ваш ответ:")
lotv1 = QLabel('Правильный/Не правильный')

con = sqlite3.connect()

layout2 = QVBoxLayout()
layout2.addWidget(lotv1)

RGB2.setLayout(layout2)
total = 0
########1 if на elif ... на answers[0]
def check():
    if answers[0].isChecked():
        lotv1.setText('ПРАВИЛЬНО')
    elif answers[1].isChecked():
        lotv1.setText('НЕПРАВИЛЬНО')
    elif answers[2].isChecked():
        lotv1.setText('НЕПРАВИЛЬНО')
    elif answers[3].isChecked():
        lotv1.setText('НЕПРАВИЛЬНО')

#СОЗДАНИЕ НАПРАВЛЯЮЩЕЙ И РАЗМЕЩЕНИЕ НА НЕЙ КНОПОК
layout_main = QVBoxLayout()
layout_main.addWidget(label, alignment = Qt.AlignCenter)
layout_main.addWidget(RGB)
layout_main.addWidget(RGB2)

RGB2.hide()

def quest():
    RGB.show()
    RGB2.hide()

def nextquest(x, y, z, a, b):
    ask(x, y, z, a, b)
    RGB.show()
    RGB2.hide()
    global total
    if lotv1.text() == 'ПРАВИЛЬНО':
        total+=1

def res():
    RGB.hide()
    RGB2.show()

count = 0

def click():
    global count
    if count != len(vopr):
        check()
        if btn.text() == "Ответить":
            res()
            btn.setText('Перейти к след вопросу')
        else:
            nextquest(vopr[count],ot1[count],ot2[count],ot3[count],ot4[count])
            btn.setText('Ответить')
            count+=1
    else:
        out()

label2 = QLabel('Это конец программы')
label3 = QLabel('')

btn2 = QPushButton('Пройти тест снова')
layout_main.addWidget(btn2)

btn2.hide()

def out():
    label3.setText(f'Правильных ответов: {total} из 4')
    label3.show()
    RGB.hide()
    RGB2.hide()
    label.hide()
    btn2.show()
    label2.show()
    layout_main.addWidget(label2, alignment=Qt.AlignCenter)
    layout_main.addWidget(label3, alignment=Qt.AlignCenter)
    btn.hide()


def out2():
    label3.hide()
    label2.hide()
    RGB.show()
    RGB2.hide()
    btn.show()
    btn2.hide()
    label.show()
    global count
    count = 0
    global total
    total = 0
btn2.clicked.connect(out2)

layout_main.addWidget(btn)
btn.clicked.connect(click)
vopr = ['Кликовская битва','Бородинское сражение','1945']
ot1 = ['1380','1812','9 мая']
ot2 = ['1382','1813','10 мая']
ot3 = ['1383','1814','11 мая']
ot4 = ['1384','1815','12 мая']

#ОТОБРАЖЕНИЕ НАПРАВЛЯЮЩЕЙ В ОКНЕ ПРОГРАММЫ И ОТОБРАЖЕНИЕ ОКНА НА ЭКРАНЕ МОНИТОРА
main_win.setLayout(layout_main)
main_win.show()
app.exec_()