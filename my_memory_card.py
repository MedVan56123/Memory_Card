from random import shuffle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox, QRadioButton, QHBoxLayout, QGroupBox, QButtonGroup

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3





def show_result():
    RadioGroupBox.hide() #временное скрытие окна
    AnsGroupBox.show()
    button.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    button.setText('Ответить')
    RadioGroup = QButtonGroup()
    RadioGroup.addButton(rbtn_1)
    RadioGroup.addButton(rbtn_2)
    RadioGroup.addButton(rbtn_3)
    RadioGroup.addButton(rbtn_4)

    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def start_test():
    if 'Ответить' == button.text():
        show_result()
    else:
        show_question()


app = QApplication([])
window = QWidget()
button = QPushButton('Ответить')
window.setWindowTitle('Memory Card')
RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')

layout1 = QHBoxLayout()
layout2 = QVBoxLayout()
layout3 = QVBoxLayout()

layout2.addWidget(rbtn_1)
layout2.addWidget(rbtn_2)
layout3.addWidget(rbtn_3)
layout3.addWidget(rbtn_4)
layout1.addLayout(layout2)
layout1.addLayout(layout3)

RadioGroupBox.setLayout(layout1)

button
window.score = 0
window.total = 0

AnsGroupBox = QGroupBox('Результат теста')
text_result = QLabel('Правильный ответ:')
text_itog = QLabel('Тут будет верный ответ')


layout_res = QVBoxLayout()
layout_res.addWidget(text_result)
layout_res.addWidget(text_itog, Qt.AlignHCenter | Qt.AlignVCenter)
AnsGroupBox.setLayout(layout_res)

text = QLabel('Какой национальности не существует?')
line1 = QHBoxLayout()
line1.addWidget(text, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
line2 = QVBoxLayout()
line2.addWidget(RadioGroupBox)
line2.addWidget(AnsGroupBox)
line3 = QHBoxLayout()
line3.addWidget(button, alignment=(Qt.AlignHCenter | Qt.AlignVCenter), stretch = 2)



answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    text.setText(q.question)
    text_itog.setText(q.right_answer)
    show_question()

def show_correct(res):
    text_result.setText(res)
    show_result()
def check_answer(): #проверка ответа
    if answer[0].isChecked():
        show_correct('Правильно')
        window.score +=1
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Неверно!')


question_list = []
question_list.append(Question('Как называется столица Франции?', 'Париж', 'Нью-Йорк', 'Лондон', 'Москва'))
question_list.append(Question('Какой химический элемент обозначается символом "O"?', 'Кислород', 'Калий', 'Водород', 'Железо'))
question_list.append(Question('Кто является автором романа "Война и мир"?', 'Толстой', 'Пушкин', 'Ломоносов', 'Крылов'))
question_list.append(Question('В каком году произошло первое кругосветное путешествие?', '1522', '1808', '1432', '1552'))
question_list.append(Question('Сколько планет в Солнечной системе?', '8', '7', '6', '5'))
question_list.append(Question('Когда был основан город Москва?', '1147', '1200', '1100', '1257'))
question_list.append(Question('Какой химический элемент обозначается символом "Fe"?', 'Железо', 'Водород', 'Кислород', 'Свинец'))
question_list.append(Question('Когда была основана компания Apple?', '1976', '1850', '1745', '1978'))
question_list.append(Question('Какой самый большой океан на планете?', 'Тихий', 'Атлантический', 'Индийский', 'Северно-Ледовитый'))
question_list.append(Question('Какая самая высокая гора в мире?', 'Эверест', 'Эльюрус', 'Уральские Горы', 'Саухох'))

q = Question('Из скольки строк состоит эта викторина?', '100+', '<50', '<100', '1000+')
ask(q)
glav = QVBoxLayout()
glav.addLayout(line1)
glav.addLayout(line2)
glav.addLayout(line3)

def next_question():
    window.cur_question +=1 #переход к следующему вопросу
    if window.cur_question >= len(question_list):
        window.cur_question = 0  #если список вопросов закончился
    q = question_list[window.cur_question] #взяли вопрос
    window.total +=1
    ask(q)

def click_ok():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()


window.cur_question = -1
next_question()
window.setLayout(glav)
AnsGroupBox.hide()
button.clicked.connect(click_ok)
window.show()
app.exec()