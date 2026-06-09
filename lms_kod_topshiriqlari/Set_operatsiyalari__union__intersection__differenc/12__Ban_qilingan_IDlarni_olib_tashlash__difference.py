ids = set(map(int, input().split()))
banned = set(map(int, input().split()))
_ = input()  # extra line (ignore)
allowed = ids - banned
if allowed:
    print(*(sorted(allowed)))
else:
    print("BO'SH")
