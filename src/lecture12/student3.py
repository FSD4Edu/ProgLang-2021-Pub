class Student:
    lecture = "ProgLang"
    def __init__(self, id, name, score=0):
        self.id = id
        self.name = name
        self.score = score
# クラス変数の値を表示
print("講義名: {}".format(Student.lecture))
# インスタンスの生成
taro = Student(2020028, "立命館太郎", 86)
riko = Student(2020014, "情報理子", 92)
# クラス変数の値を変更
Student.lecture = "Programming Language"
print("{} -> 講義名: {}".format(taro.name, taro.lecture))
print("{} -> 講義名: {}".format(riko.name, riko.lecture))
