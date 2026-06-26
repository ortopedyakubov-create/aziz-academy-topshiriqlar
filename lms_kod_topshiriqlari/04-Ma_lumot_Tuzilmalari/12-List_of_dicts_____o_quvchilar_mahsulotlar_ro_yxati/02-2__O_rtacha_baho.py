n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
total_score = sum(student['score'] for student in students)
average_score = total_score / n
print(average_score)
