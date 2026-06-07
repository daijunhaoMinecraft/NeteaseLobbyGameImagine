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

for i in range(10):
    if 10 - i <= 9 and 10 - i >= 6:
        time.sleep(1)
        continue
    print(SDJ_TEMPLATE.format(TIME = str(10 - i)))
    time.sleep(1)
print(f"{colorama.Fore.WHITE}[{colorama.Fore.RED}扫地机{colorama.Fore.WHITE}] 掉落物清理完毕")