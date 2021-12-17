class Student:
    def __init__(self, id, name, score):
        self.id = id
        self.name = name
        self.score = score
    def getScore(self):
        return self.score
taro = Student(2020028, "立命館太郎", 86)
score = taro.getScore()
print("{}点".format(score))
