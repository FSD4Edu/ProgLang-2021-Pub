results = {}
with open("answer.txt", "r", encoding = "utf_8") as file:
    for line in file:
        country = line.rstrip("∖n")
        if country in results:
            results[country] += 1
        else:
            results[country] = 1
for country, num in results.items():
    print("{}:{}".format(country,num))
