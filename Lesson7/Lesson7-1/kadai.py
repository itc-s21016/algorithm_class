def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a % b)


print("a≧bとなる自然数を入力してください")
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
if b == 0:  # 0のときエラーを出す
    print("0はだめです")
    print("もう一度入力してください")
    b = int(input("b="))
if c == 0:  # 0のときエラーを出す
    print("0はだめです")
    print("もう一度入力してください")
    c = int(input("c="))

ab = euclid(a, b)


def euclid2(ab, c):
    if c == 0:
        return ab
    else:
        return euclid2(c, ab % c)


print("それらの数の最大公約数は", euclid2(ab, c))
