a = set(map(int, input().split()))
b = set(map(int, input().split()))
difference = sorted(a - b)
if difference:
    print(*difference)
else:
    print("BO'SH")