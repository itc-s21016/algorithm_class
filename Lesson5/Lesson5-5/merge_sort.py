class Color:
    BLACK = '\033[30m'  # (文字)黒
    RED = '\033[31m'  # (文字)赤
    GREEN = '\033[32m'  # (文字)緑
    YELLOW = '\033[33m'  # (文字)黄
    BLUE = '\033[34m'  # (文字)青
    MAGENTA = '\033[35m'  # (文字)マゼンタ
    CYAN = '\033[36m'  # (文字)シアン
    WHITE = '\033[37m'  # (文字)白
    COLOR_DEFAULT = '\033[39m'  # 文字色をデフォルトに戻す
    BOLD = '\033[1m'  # 太字
    UNDERLINE = '\033[4m'  # 下線
    INVISIBLE = '\033[08m'  # 不可視
    REVERCE = '\033[07m'  # 文字色と背景色を反転
    BG_BLACK = '\033[40m'  # (背景)黒
    BG_RED = '\033[41m'  # (背景)赤
    BG_GREEN = '\033[42m'  # (背景)緑
    BG_YELLOW = '\033[43m'  # (背景)黄
    BG_BLUE = '\033[44m'  # (背景)青
    BG_MAGENTA = '\033[45m'  # (背景)マゼンタ
    BG_CYAN = '\033[46m'  # (背景)シアン
    BG_WHITE = '\033[47m'  # (背景)白
    BG_DEFAULT = '\033[49m'  # 背景色をデフォルトに戻す
    RESET = '\033[0m'  # 全てリセット


import random

n = 15
data = [0] * n
for i in range(n):
    data[i] = random.randint(1, 99)


def merge(left, mid, right):
    buff = [0] * (right - left)
    i = left
    j = mid
    p = 0
    while i < mid and j < right:
        if data[i] <= data[j]:
            buff[p] = data[i]
            i += 1
            p += 1
        else:
            buff[p] = data[j]
            j += 1
            p += 1
    while i < mid:
        buff[p] = data[i]
        i += 1
        p += 1

    while j < right:
        buff[p] = data[j]
        j += 1
        p += 1
        for n in range(left, right):
            data[n] = buff[n - left]


print(data, "元のデータ")
s = 2
while s <= n:
    loop = n // s
    fragment = n % s
    for i in range(loop):
        merge(i * s, i * s + (s // 2), i * s + s)
    if fragment > 0:
        merge((loop - 1) * s, loop * s, n)
    s = s * 2
print(data, "ソート後のデータ")
       