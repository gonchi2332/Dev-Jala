from json import JSONEncoder


class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.asdf = {"asdf": 15, 16: Some()}


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class Some:
    def __init__(self):
        self.x = 123

myclass = MyClass(4, 5)
json = MyEncoder().encode(myclass)
f = open("myform.json", "w")
f.write(json)
f.close()
