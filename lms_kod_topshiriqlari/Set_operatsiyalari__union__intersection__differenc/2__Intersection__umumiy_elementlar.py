a = set(map(int, input().split()))
b = set(map(int, input().split()))
intersection = sorted (a & b) 
if intersection:
    print(*intersection)
else:
    print("BO'SH")