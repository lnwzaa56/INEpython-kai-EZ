# pop method
grades = [85, 90, 78, 92, 88]
third_grade = grades.pop(2)
grades.append(third_grade)
print(f"Grades after pop: {grades}")
# Output: grades after pop: [85, 90, 92, 88, 78]