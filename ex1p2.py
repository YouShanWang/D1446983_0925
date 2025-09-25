h = input("輸入十六進制數字: ")
d = int(h, 16)          # 十進制decimal整數，16表示十六進制
b = bin(d)              # 二進制binary會自動加 '0b'
o = oct(d)              # 八進制octal會自動加 '0o'
print(f"{d}")
print(f"{b[2:]}")       # [2:]去掉前兩個字
print(f"{o[2:]}\n")