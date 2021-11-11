#seafood = ["カツオ", "イワシ", "アユ", "ハマチ", "アンコウ", "タイ"]       
seafood = ["カツオ", "イワシ", "アユ", "タコ", "アンコウ", "タイ"]
length = len(seafood)
i = 0
while i < length:
   if (seafood[i] == "イカ" or seafood[i] == "タコ"):
       print(seafood[i] + "は食べられません")
       break
   print(seafood[i] + "は食べられます")
   i += 1
else:
   print("食べられないものはありませんでした")
