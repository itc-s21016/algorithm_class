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


"""print(f'黒:{Color.py.BLACK}●ABC{Color.py.RESET}')
print(f'赤:{Color.py.RED}●ABC{Color.py.RESET}')
print(f'緑:{Color.py.GREEN}●ABC{Color.py.RESET}')
print(f'黄:{Color.py.YELLOW}●ABC{Color.py.RESET}')
print(f'青:{Color.py.BLUE}●ABC{Color.py.RESET}')
print(f'マゼンタ:{Color.py.MAGENTA}●ABC{Color.py.RESET}')
print(f'シアン:{Color.py.CYAN}●ABC{Color.py.RESET}')
print(f'白:{Color.py.WHITE}●ABC{Color.py.RESET}')
print(f'下線:{Color.py.UNDERLINE}●ABC{Color.py.RESET}')
print(f'太字:{Color.py.BOLD}●ABC{Color.py.RESET}')
print(f'不可視:{Color.py.INVISIBLE}●ABC{Color.py.RESET}')
print(f'反転:{Color.py.REVERCE}●ABC{Color.py.RESET}')
print(f'背景黒:{Color.py.BG_BLACK}●ABC{Color.py.RESET}')
print(f'背景赤:{Color.py.BG_RED}●ABC{Color.py.RESET}')
print(f'背景緑:{Color.py.BG_GREEN}●ABC{Color.py.RESET}')
print(f'背景黄:{Color.py.BG_YELLOW}●ABC{Color.py.RESET}')
print(f'背景青:{Color.py.BG_BLUE}●ABC{Color.py.RESET}')
print(f'背景マゼンタ:{Color.py.BG_MAGENTA}●ABC{Color.py.RESET}')
print(f'背景シアン:{Color.py.BG_CYAN}●ABC{Color.py.RESET}')
print(f'背景白:{Color.py.BG_WHITE}●ABC{Color.py.RESET}')
# 文字色と背景色を変える
print(f'文字赤+背景緑:{Color.py.RED}{Color.py.BG_GREEN}●ABC{Color.py.RESET}')"""


data = ["yosiya","ryuki","seiga","yuu","syunta","asahi","kouiti","seika","kyousuke","haruya","tokiya"]
n = len(data)
print(data, "元のデータ")

for i in range(0, n-1):
    for j in range(n-1, i, -1):
        if data[j-1] > data[j]:
            data[j], data[j-1] = data[j-1], data[j]


print(data, f"{Color.MAGENTA}ソート後のデータ{Color.RESET}")


