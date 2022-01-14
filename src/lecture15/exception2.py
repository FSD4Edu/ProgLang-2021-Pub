import sys    # sysモジュール（ライブラリ）の読み込み
try:
    score = int(input("点数を入力してください："))
except:
    print("数値を入力してくださいよ...")
    sys.exit()    # 関数exit()を利用してプログラムを終了
if score >= 80:
    print("合格です！")
else:
    print("不合格です
