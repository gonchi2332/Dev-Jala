import uuid

from quizc.model.question_type import QuestionType


class QuizAnswer(object):
    def __init__(self, quiz):
        self.quiz = quiz
        self.id = uuid.uuid4()
        self.answers = []

    def add_answer(self, answer):
        self.answers.append(answer)


class Answer(object):
    def __init__(self, answers, question):
        self.question = question
        self.answers = answers

    def show_answer(self, number):
        print(f"{number}) {self.question.get_title()}?")
        if self.question.type == QuestionType.PICK_ONE:
            for num_ans in range(len(self.answers)):
                print(f"{num_ans}) {self.answers[num_ans]}.")
        else:
            print(f"A) {self.answers[0]}.")

