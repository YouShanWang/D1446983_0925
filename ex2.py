# 取得使用者輸入
a = int(input("請輸入第一個整數 (0~9): "))
b = int(input("請輸入第二個整數 (0~9): "))

# 檢查輸入範圍
if not (0 <= a <= 9 and 0 <= b <= 9):
    print("輸入數字必須在 0~9 之間")
else:
    # 位元運算結果
    print(f"a AND b = {a & b}")
    print(f"a OR b = {a | b}")
    print(f"a XOR b = {a ^ b}")
    print(f"NOT a = {~a}")
    print(f"(a AND b) AND b = {(a & b) & b}")
    print(f"(a OR b) OR b = {(a | b) | b}")
    print(f"(a XOR b) XOR a = {(a ^ b) ^ a}")
