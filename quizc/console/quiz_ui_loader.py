from json import JSONEncoder


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class Quiz:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

class QuizLoader(object):
    MENU_PROMPT = "> "
    FILE = "Name of the file:"

    # TODO: Fix json encoder error
    # TODO: Retrive information from json
    def save_quiz(self, question, answer):
        print(self.FILE)
        name = input(self.MENU_PROMPT)
        if name != "":
            json = MyEncoder().encode(Quiz(question, answer))
            f = open(f"./quizzes/{name}.json", "w")
            f.write(json)
            f.close()
