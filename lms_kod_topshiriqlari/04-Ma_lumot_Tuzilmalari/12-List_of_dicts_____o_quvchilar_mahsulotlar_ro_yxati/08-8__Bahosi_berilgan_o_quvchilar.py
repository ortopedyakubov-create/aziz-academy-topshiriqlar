n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
x = int(input())
count = 0
for student in students:
    if student['score'] == x:
        count += 1
print(count)
