from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QGroupBox, QLabel, QVBoxLayout,QRadioButton,QHBoxLayout,QMessageBox
from random import shuffle

#СОЗДАНИЕ ПРИЛОЖЕНИЯ И ОКНА ПРОГРАММЫ
app = QApplication([])
main_win = QWidget()
main_win.resize(400,200)
main_win.setWindowTitle('Memory Card')
main_win.setStyleSheet('background-image: url(546.jpg')

btn = QPushButton('Ответить')
btn.setStyleSheet('color: dark blue; background-color : orange')
#СОЗДАНИЕ ВИДЖЕТОВ

label = QLabel('Какой национальности не существует?')
label.setStyleSheet('background-color : black')
total = 0
#ГРУППА c вопросом+
RGB = QGroupBox("Варианты ответов")
btn_answer1 = QRadioButton('Энцы')
btn_answer2 = QRadioButton('Смурфы')
btn_answer3 = QRadioButton('Чулымцы')
btn_answer4 = QRadioButton('Алеуты')
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
#Группа с ответом
RGB2 = QGroupBox('Ваш ответ:')
ans1 = QLabel()
layout2 = QVBoxLayout()
layout2.addWidget(ans1)
RGB2.setLayout(layout2)

#def ask(q, vern, wr1, wr2, wr3):
    
answers = [btn_answer1, btn_answer2, btn_answer3, btn_answer4]

def ask(q, v1, v2, v3, v4):
    shuffle(answers)
    answers[0].setText(v1)
    answers[1].setText(v2)
    answers[2].setText(v3)
    answers[3].setText(v4)

    label.setText(q)
    quest()
def ask2(q, v1, v2, v3, v4):
    shuffle(answers)
    answers[0].setText(v1)
    answers[1].setText(v2)
    answers[2].setText(v3)
    answers[3].setText(v4)

    label.setText(q)
    quest()


def check1():
    if answers[0].isChecked():
        ans1.setText('Правильно')
    elif answers[1].isChecked():
        ans1.setText('Не правильно')
    elif answers[2].isChecked():
        ans1.setText('Не правильно')
    elif answers[3].isChecked():
        ans1.setText('Не правильно')

#СОЗДАНИЕ НАПРАВЛЯЮЩЕЙ И РАЗМЕЩЕНИЕ НА НЕЙ КНОПОК
layout_main = QVBoxLayout()



layout_main.addWidget(label, alignment = Qt.AlignCenter)

layout_main.addWidget(RGB)
layout_main.addWidget(RGB2)

RGB2.hide()
def quest():
    RGB.show()
    RGB2.hide()
total = 0                           
def nextquest(x, y, z, a, b):
    ask2(x, y, z, a, b )
    RGB.show()
    RGB2.hide()
    global total
    if ans1.text() == 'Правильно':
        total+=1

def result():
    RGB.hide()
    RGB2.show()  
count = 0  

def click1():
    global count
    if count != len(vopr):
        check1()
        if btn.text() == 'Ответить':
            result()
            btn.setText('Перейти к следующему вопросу')
        else:
            nextquest(vopr[count], ot1[count], ot2[count], ot3[count], ot4[count])
            btn.setText('Ответить')
            count+=1
    else:
        out()

                                                                                 
label12 = QLabel('Это конец программы')
btn2 = QPushButton('Пройти тест снова')                                                                                                                                                            #
label_total = QLabel()
def out():
    RGB.hide()                                                                      
    RGB2.hide()                                                                  
    label.hide()                                                                    
    #btn.setText('Вернуться назад')                                                  
    #btn.clicked.connect(nextquest(vopr[0], ot1[0], ot2[0], ot3[0], ot4[0]))    
    #layout_main.addWidget(label12, aligment=Qt.AlignCentr)     
    btn.hide()
    layout_main.addWidget(btn2)
    btn2.hide()
    btn2.show()
    print(total)
    label_total.setText(str(total))
    layout_main.addWidget(label_total)
def click2():
    RGB.show()
    btn.show()
    btn2.hide()
    label12.hide()
    label.show()
    global count
    count = 0
    label.setText('Государственный язык Бразилии')
    btn_answer1.setText('Португальский')
    btn_answer2.setText('Бразильский')
    btn_answer3.setText('Испанский')
    btn_answer4.setText('Русский')

layout_main.addWidget(btn)
btn.clicked.connect(click1)
btn2.clicked.connect(click2)
ask('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Русский')
vopr = ['Кто получил золотую кнопку ютуба в 2013?']
vopr1 = ['Кто получил серебрянную кнопку ютуба в 2015?']
ot1 = ['wdwdwd', 'wdwd', 'wd', 'wwd']
ot2 = ['Человек1', 'Арнольд Шварцнегер', 'Артем', '2020']
ot3 = ['Человек2', 'Стив Джоб', 'Николай', '2021']
ot4 = ['Человек3', 'Уорен Баффет', 'Никита', '2022']
#ОТОБРАЖЕНИЕ НАПРАВЛЯЮЩЕЙ В ОКНЕ ПРОГРАММЫ И ОТОБРАЖЕНИЕ ОКНА НА ЭКРАНЕ МОНИТОРА
main_win.setLayout(layout_main)
main_win.show()
app.exec_()



