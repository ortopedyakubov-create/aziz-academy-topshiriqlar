A = set(map(int, input().split()))
B = set(map(int, input().split()))
intersection_count = len(A & B)
union_count = len(A | B)
jaccard = intersection_count / union_count
print(f"{jaccard:.3f}")