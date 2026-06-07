import os
import time

import colorama
colorama.init(autoreset=True)

TEMPLATE = f"""
 {colorama.Fore.CYAN}『雪球菜单』
▶==================◀{colorama.Fore.LIGHTYELLOW_EX}
  {{S1}}①.『传送主城』
  {{S2}}②.『原地去世』
  {{S3}}③.『生存模式』
  {{S4}}④.『设重生点』
  {{S5}}⑤.『发起传送』
  {{S6}}⑥.『接受传送』
{colorama.Fore.CYAN}▶==================◀
{colorama.Fore.GREEN}抬头确定✔{colorama.Fore.RED}低头关闭✘{colorama.Fore.RESET}
"""

SDJ_TEMPLATE = f"""
{colorama.Fore.WHITE}[{colorama.Fore.LIGHTYELLOW_EX}扫地机{colorama.Fore.WHITE}] 还有 {colorama.Fore.RED}{{TIME}} {colorama.Fore.WHITE}秒就要清理掉落物了{colorama.Fore.RESET}
"""

TEMPLATE_TP = f"""
{colorama.Fore.WHITE}〈{colorama.Fore.CYAN}世界公告{colorama.Fore.WHITE}〉玩家{colorama.Fore.WHITE} <Player> {colorama.Fore.WHITE}发起了传送请求
{colorama.Fore.WHITE}----------------------------
{colorama.Fore.CYAN}● {colorama.Fore.WHITE}打开雪球菜单接受传送请求
{colorama.Fore.CYAN}● {colorama.Fore.WHITE}60秒后无人同意自动取消传送
{colorama.Fore.CYAN}● {colorama.Fore.WHITE}发起传送者低头可取消传送
----------------------------{colorama.Fore.RESET}
"""
def MainSelect(selectId: int):
    print(TEMPLATE.format(
        S1 = f"{colorama.Fore.LIGHTYELLOW_EX} " if selectId != 1 else f"{colorama.Fore.YELLOW}",
        S2 = f"{colorama.Fore.LIGHTYELLOW_EX} " if selectId != 2 else f"{colorama.Fore.YELLOW}",
        S3 = f"{colorama.Fore.LIGHTYELLOW_EX} " if selectId != 3 else f"{colorama.Fore.YELLOW}",
        S4 = f"{colorama.Fore.LIGHTYELLOW_EX} " if selectId != 4 else f"{colorama.Fore.YELLOW}",
        S5 = f"{colorama.Fore.LIGHTYELLOW_EX} " if selectId != 5 else f"{colorama.Fore.YELLOW}",
        S6 = f"{colorama.Fore.LIGHTYELLOW_EX} " if selectId != 6 else f"{colorama.Fore.YELLOW}",
    ))
nowSelect = 1

while True:
    os.system("cls")
    MainSelect(nowSelect)
    choice = int(input("请选择动作: 1. 扔雪球, 2. 抬头, 3. 低头: "))
    if choice == 1:
        nowSelect += 1
        if nowSelect > 6:
            nowSelect = 1
    elif choice == 2:
        if nowSelect == 1:
            print("你已被tp到 -22.46 122.00 -47.45")
        elif nowSelect == 2:
            print("你被击败了")
        elif nowSelect == 3:
            print("你已切换至 生存模式")
        elif nowSelect == 4:
            print("你已设置重生点")
        elif nowSelect == 5:
            print(TEMPLATE_TP)
            open("hyw.txt", "w", encoding="utf-8").write("1")
        elif nowSelect == 6:
            try:
                if open("hyw.txt", "r", encoding="utf-8").read() == "1":
                    print(f"{colorama.Fore.WHITE}〈{colorama.Fore.MAGENTA}世界公告{colorama.Fore.WHITE}〉已成功将玩家{colorama.Fore.CYAN}<Player>{colorama.Fore.WHITE}传送至{colorama.Fore.WHITE}<Player>{colorama.Fore.RESET}")
                os.remove("hyw.txt")
            except Exception:
                pass
        exit(0)
    elif choice == 3:
        exit(0)