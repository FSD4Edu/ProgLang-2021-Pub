import os, sys, random
if len(sys.argv) != 2:
    print("ファイル名をひとつ指定してください")
    sys.exit()
path = sys.argv[1]
if os.path.exists(path):
    if input("上書きしますか？[y/n]：") != "y":
        sys.exit()
kuji = ["大吉", "中吉", "凶"]
with open(path, "w", encoding = "utf_8") as file:
    file.write(kuji[random.randrange(len(kuji))] + "∖n")
