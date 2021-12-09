year = int(input("入学年を西暦で入力してください："))
name = input("氏名を入力してください：")
course = input("コース名を日本語で入力してください：")
print("令和{}年入学の{}さん({})ですね".format(year-2018, name, course[0:len(course)-3]))  # 西暦→平成の変換，コース名から「コース」削除
