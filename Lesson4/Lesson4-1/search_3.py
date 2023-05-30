"""data =[]
f = open("data.txt","r")
data = f.read()
print(data)"""

data = [
    ["佐藤", "000-0000-0000"],
    ["鈴木", "111-1111-1111"],
    ["高橋", "222-2222-2222"],
    ["田中", "333-3333-3333"]
]
n = len(data)
s = input("検索する相手の名字は?")
data.append(s)
i = 0
while i < n and data[i][0] != s:
    i += 1
if i == n:
    print("その名は登録されていません")
    c = input("登録しますか？ yes/no :")
    if c == "yes" or c == "y":
        print("登録したい名前と電話番号を入力してください")
        a = input("名前:")
        b = input("電話番号:")
        #f.write()
        data.append([a, b])
        print("登録されました")
        print(data)
        #f.close()
    else:
        print("またのご利用をお待ちしています")
else:
    print(data[i][0]+"さんの番号は "+data[i][1]+"です")
    #f.close()
