from quizc.console.quiz_ui_handler import *


class Menu(object):
    MENU_PROMPT = "> "

    def __init__(self):
        self.quiz = None
        self.quiz_answers = None
        self.functions = {}
        self.initialize_menu()

    def initialize_menu(self):
        self.functions["1"] = self.create_quiz
        self.functions["2"] = self.fill_quiz
        self.functions["3"] = self.show_quiz
        self.functions["4"] = self.save_quiz


    def show_main_menu(self):
        print("""
Quizc - A command quiz utility
======================================
1. Create quiz
2. Fill quiz
3. Show quiz
4. Save quiz
5. Exit
======================================
        """)

    def process(self):
        self.show_main_menu()
        option = input(self.MENU_PROMPT)
        should_exit = False
        self.functions.get(option)()
        if option == "5":
            should_exit = True

        return should_exit

    def create_quiz(self):
        self.quiz = QuizUIHandler.create_quiz()

    def fill_quiz(self):
        if self.quiz is None:
            print("No quiz available, you must create first a quiz")
        else:
            self.quiz_answers = QuizUIHandler.fill_quiz(self.quiz)

    def show_quiz(self):
        if self.quiz_answers is None:
            print("No filled quiz available, you must create first a quiz")
        else:
            QuizUIHandler.show_quiz(self.quiz_answers)

    def save_quiz(self):
        if self.quiz_answers and self.quiz:
            save_quiz(self.quiz, self.quiz_answers)
        else:
            print("No quiz available, you must fill the information of the quiz")

    def exit(self):
        return True
