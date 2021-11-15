import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

widgets = {
    "logo": [],
    "button": [],
    "score": [],
    "question": [],
    "confirm": []
}    

app = QApplication(sys.argv)

#window and settings
window = QWidget()
window.setWindowTitle("QUIZ GAME")
window.setFixedWidth(1000)
#place window in (x,y) coordinates
#window.move(2700, 200)
window.setStyleSheet("background: #D6EAF8;")

grid = QGridLayout()

def clear_widgets():
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()

def show_frame1():
    clear_widgets()
    frame1()

def start_game():
    clear_widgets()
    frame2()


'''def create_button(confirm):
    button = QPushButton(confirm)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    #button.setAlignment(QtCore.Qt.AlignCenter)
    #button.setFixedWidth(485)
    button.setStyleSheet(
        "*{border: 4px solid '#AE5DF6';" + 
        "border-radius: 45px;" +
        "font-size: 35px;" +
        "color: 'white';" +
        "padding: 25px 0;" +
        "margin: 100px 200px;}" +
        "*:hover{background: '#AE5DF6';};"
    )
    return button'''

def frame1():
#logo
    image =QPixmap("welcome.png")
    logo = QLabel()
    logo.setPixmap(image)

    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 100px")
    widgets["logo"].append(logo)

    button = QPushButton("PLAY")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
        "*{border: 4px solid '#AE5DF6';" + 
        "border-radius: 45px;" +
        "font-size: 35px;" +
        "color: 'white';" +
        "padding: 25px 0;" +
        "margin: 100px 200px;}" +
        "*:hover{background: '#AE5DF6';};"
    )
    button.clicked.connect(start_game)
    widgets["button"].append(button)

    grid.addWidget(widgets["logo"][-1], 0, 0, 1, 2)
    grid.addWidget(widgets["button"][-1], 1, 0, 1, 2)

def frame2():
    score = QLabel("80")
    score.setAlignment(QtCore.Qt.AlignRight)
    score.setStyleSheet(
        "font-size: 35px;" +
        "color: 'white';" +
        "padding: 25px 20px 20px 20px;" +
        "margin: 20px 200px;" +
        "background: '#AE5DF6';"  +
        "border: 6px solid '#AE5DF6';" + 
        "border-radius: 45px;" 
        
    )
    widgets["score"].append(score)

    question = QLabel("Text Text PLay")
    question.setAlignment(QtCore.Qt.AlignCenter)
    question.setWordWrap(True)
    question.setStyleSheet(
        "font-family: Shanti;" +
        "font-size: 25px;" +
        "color: 'black';" +
        "padding: 75px;"
    )
    widgets["question"].append(question)

    button = QPushButton("confirm")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
        "*{border: 4px solid '#AE5DF6';" + 
        "border-radius: 45px;" +
        "font-size: 35px;" +
        "color: 'white';" +
        "padding: 25px 0;" +
        "margin: 100px 200px;}" +
        "*:hover{background: '#AE5DF6';};"
    )
    button.clicked.connect(show_frame1)
    widgets["confirm"].append(button)

    image =QPixmap("logo_small.png")
    logo = QLabel()
    logo.setPixmap(image)

    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-bottom: 0px;")
    widgets["logo"].append(logo)    


    grid.addWidget(widgets["score"][-1], 0, 1)
    grid.addWidget(widgets["question"][-1], 1, 0, 1, 2)
    grid.addWidget(widgets["confirm"][-1], 2, 0, 1, 2)
    grid.addWidget(widgets["logo"][-1], 4, 0, 1, 2)
     


frame1()


window.setLayout(grid)

window.show()
sys.exit(app.exec()) #terminate the app
