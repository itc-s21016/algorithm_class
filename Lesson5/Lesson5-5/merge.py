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


a = [1, 3, 4, 7, 8, 9]
b = [0, 2, 5, 6]
na = len(a)
nb = len(b)
c = [0] * (na + nb)
i = 0
j = 0
p = 0

print(f"{Color.RED}データA", a, f"{Color.RESET}")
print(f"{Color.BLUE}データB", b, f"{Color.RESET}")

while i < na and j < nb:
    if a[i] <= b[j]:
        c[p] = a[i]
        i += 1
        p += 1

    else:
        c[p] = b[j]
        j += 1
        p += 1

while i < na:
    c[p] = a[i]
    i += 1
    p += 1

while j < nb:
    c[p] = b[j]
    j += 1
    p += 1

print(f"{Color.YELLOW}マージ後のデータ", c, f"{Color.RESET}")
