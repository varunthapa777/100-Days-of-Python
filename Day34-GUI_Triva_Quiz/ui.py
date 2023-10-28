from tkinter import *
from quiz_brain import QuizBrain
from time import sleep

# from quiz_brain import score

THEME_COLOR = "#375362"
FONT = ("Arial", 15, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Travia Quize")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # self.window.minsize(width=340, height=500)

        self.score = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR, padx=20, pady=20,
                           font=("arial", 15))
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.q_text = self.canvas.create_text(150, 125, text="", width=280, fill="black", font=FONT)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        t_img = PhotoImage(file="./images/true.png")
        f_img = PhotoImage(file="./images/false.png")

        self.t_btn = Button(image=t_img, highlightthickness=0, command=self.click_t)
        self.t_btn.grid(column=0, row=3)
        self.f_btn = Button(image=f_img, highlightthickness=0, command=self.click_f)
        self.f_btn.grid(column=1, row=3)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            next_que = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=next_que)
        else:
            self.canvas.itemconfig(self.q_text, text=f"You've completed the quiz!\nYour Final Score: {self.quiz.score}")
            self.t_btn.config(state="disabled")
            self.f_btn.config(state="disabled")

    def click_t(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def click_f(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
