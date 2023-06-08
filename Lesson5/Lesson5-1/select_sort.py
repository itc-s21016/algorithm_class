data = ["yosiya","ryuki","seiga","yuu","syunta","asahi","kouiti","seika","kyousuke","haruya","tokiya"]
print(data, "元のデータ")

for i in range(0,11):
    m = i
    for j in range(i+1, 11):
        if data[j] < data[m]:

            m = j
    data[i], data[m] = data[m], data[i]
#data.sort(reverse=False)
print(data,"ソート後のデータ")
