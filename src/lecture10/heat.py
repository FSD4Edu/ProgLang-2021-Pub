# 最高気温のリスト
max_temp = [22, 26, 21, 23, 27, 24, 22, 25, 24, 26]
# 25以上のデータのみを抽出し夏日の気温リスト（heatday）に追加
heatday = []
for t in max_temp:
    if 25 <= t:
        heatday.append(t)
# 作成したリストを表示
print(heatday)
