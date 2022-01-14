import sys
while True:
    try:
        score = int(input("点数を入力してください："))
        print("入力ありがとうございます")
        print("点数は" + score + "ですね")
        break
    except ValueError:
        print("数値を入力してくださいよ")
    except:
        print("ValueError以外のエラーが発生しました")
        sys.exit()
if score >= 80:
    print("合格です！")
else:
    print("不合格です！")
