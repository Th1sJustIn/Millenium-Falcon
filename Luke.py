from graphics import *
from Han import *
from Leia import *

user_answer = Entry(Point(250,120), 20)
user_answer.draw(Falcon)
##-----------------------Switch Questions---------------------------------
def run_loop():
    global question_index
    if question_index >= len(questions):
        RightorWrong = ("All questions have been answered.")
        return
    #user_answer = input(questions[question_index])
    user_answer = Entry(Point(250,120), 20)
    user_answer.draw(Falcon)

    if user_answer == answers[question_index]:
        answer_is_correct = True
        question_index += 1
        print = ("Correct")
    else:
        answer_is_correct = False
        print = ("Incorrect")
while True:
    Falcon.getMouse()
    run_loop()
