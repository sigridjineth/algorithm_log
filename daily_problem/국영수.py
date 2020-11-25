# 국영수
n = int(input())
students = []

# 모든 학생 정보를 입력받기
for _ in range(n):
    students.append(input().split())

students.sort(key = lambda x: (-int(x[1])), (int(x[2])), (-int(x[3]), x[0]))

# 정렬된 학생 정보에서 이름만 출력
for student in students:
    print(student[0])