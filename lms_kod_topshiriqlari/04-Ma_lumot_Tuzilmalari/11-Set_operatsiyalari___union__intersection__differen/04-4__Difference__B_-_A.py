a = set(map(int, input().split()))
b = set(map(int, input().split()))
result = sorted(b - a)
if result:
    print(*result)
else:
    print("BO'SH")
