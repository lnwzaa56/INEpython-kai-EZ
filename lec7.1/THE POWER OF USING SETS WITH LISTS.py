#Attendance records for a weak (each list represent a day's attendance)
attendance_week = [
    ["Alice", "Bob", "Charlie", "David"], #Day 1
    ["Alice", "Charlie", "David"], # Day 2
    ["Alice", "Bob",  "David"], # Day 3
    ["Alice", "David", "Eve"], # Day 4
    ["Bob", "Charlie", "David"] #Day 5
    #1 find the set of students who where present every day
    #2 Determine the set of students who were absent at least one day
    #3 Create a list of students who were present on the first day but absrnt on the last day
    #4 Calculate the total number of unique studens who attended at least one day
]
# convert each day's attendance list into a set 
attendance_sets = [set(day) for day in attendance_week]
print(attendance_sets)

#1 find the set of students who where present every day
present_every_day = set.intersection(*attendance_sets)
print("Present every day:", present_every_day)
#output: {"David"}

#2 Determine the set of students who were absent at least one day
all_students = set.union(*attendance_sets)
absent_at_least_one_day = all_students - present_every_day
print("Absent at least one day:", absent_at_least_one_day)
#output: {"Alice", "Chalie", "Bob", "Eve"}


#3 Create a list of students who were present on the first day but absent on the last day
first_day_present = attendance_sets[0]
last_day_present = attendance_sets[-1]
first_day_but_not_last = list(first_day_present - last_day_present)
print("Present on first day but absent on last day:", first_day_but_not_last)
#output:["Alice"]

#4 Calculate the total number of unique studens who attended at least one day
unique_students_count = len(all_students)
print("Total unique students", unique_students_count)
#output: 5