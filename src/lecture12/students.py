# 学生を表すクラス
class Student:
    def __init__(self, id, name, score = 0):
        self.id = id
        self.name = name
        self.score = score
    def getID(self):
        return self.id
    def getName(self):
        return self.name
    def getScore(self):
        return self.score
    def setScore(self,score):
        self.score = score
# 学生を管理し平均点を計算するクラス
class CalcScore:
    def __init__(self):
        self.students = []
    def addStudent(self, student):
        self.students.append(student)
    def ave(self):
        total = 0
        for st in self.students:
            total += st.getScore()
        ave = total / len(self.students)
        return ave
# 学生を表すインスタンスを作成
p1 = Student(10, "佐藤")
p1.setScore(80)
p2 = Student(11, "鈴木", score = 79)
p3 = Student(12, "田中", score = 84)
p4 = Student(13, "山田", score = 77)
# 平均点を計算
calc = CalcScore()
calc.addStudent(p1)
calc.addStudent(p2)
calc.addStudent(p3)
calc.addStudent(p4)
print("平均点=", calc.ave())
