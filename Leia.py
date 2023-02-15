from graphics import *
from Han import *


Falcon = GraphWin("Millennium Falcon Browser", 500, 250)
top_r = Point (0,0)
Background_rect = Rectangle(top_r, Point(500,250))
Background_rect.setFill("dark blue")
Background_rect.draw(Falcon)
div_rect = Rectangle(Point (60, 30), Point(440,220))
div_rect.setFill("dark grey")
div_rect.draw(Falcon)

Question_box = Text(Point(250,80), questions[question_index])
Question_box.draw(Falcon)

#user_answer = Entry(Point(250,120), 20)
#user_answer.draw(Falcon)
