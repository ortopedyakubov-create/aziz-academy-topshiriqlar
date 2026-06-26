n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
count_above_80 = sum(1 for student in students if student['score'] > 80)
print(count_above_80)
