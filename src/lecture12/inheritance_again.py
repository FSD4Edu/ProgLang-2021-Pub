# この上にstudents_m.pyのコードがあるとする
# CalsScoreを継承したクラスの生成
class NeoCalcScore(CalcScore):
    def maxScore(self):
        max = 0
        for st in self.students:
            if (max <= st.getScore()):
                max = st.getScore()
        return max
# NeoCalsScoreを継承したクラスの生成
class SecondNeoCalcScore(NeoCalcScore):
    def maxScore(self):
        max = 100
        for st in self.students:
            if (st.getScore() <= max):
                max = st.getScore()
        return max
# 学生を表すインスタンスを作成
p1 = Student(10, "佐藤")
p1.setScore(80)
p2 = Student(11, "鈴木", score = 79)
p3 = Student(12, "田中", score = 84)
p4 = Student(13, "山田", score = 77)
# 平均点・最低点を計算
calc = SecondNeoCalcScore()
calc.addStudent(p1)
calc.addStudent(p2)
calc.addStudent(p3)
calc.addStudent(p4)
print("平均点=", calc.ave())
print("最低点=", calc.maxScore())
