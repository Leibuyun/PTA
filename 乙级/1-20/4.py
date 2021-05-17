n = int(input())
min_s_name, min_s_no, min_s_grade = input().split()
max_s_name, max_s_no, max_s_grade = min_s_name, min_s_no, min_s_grade
for i in range(1, n):
    name, no, grade = input().split()
    if int(grade) > int(max_s_grade):
        max_s_name, max_s_no, max_s_grade = name, no, grade
    if int(grade) < int(min_s_grade):
        min_s_name, min_s_no, min_s_grade = name, no, grade
print(max_s_name, max_s_no)
print(min_s_name, min_s_no)

