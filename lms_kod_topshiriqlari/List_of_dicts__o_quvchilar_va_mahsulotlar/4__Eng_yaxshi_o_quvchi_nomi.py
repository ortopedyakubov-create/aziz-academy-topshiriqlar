n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
best_student = max(students, key=lambda student: student['score'])
print(best_student['name'])