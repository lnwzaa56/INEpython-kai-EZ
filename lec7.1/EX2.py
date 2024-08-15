performance_data = {
    "sale":{
        "Alice": [80, 85, 88, 90],
        "Bob":[70, 75, 78, 80],
        "Charlie":[60, 65, 70 ,72]
    },
    "Engineering":{
        "Dvaid": [90, 92, 94, 95],
        "Eve":[85, 88, 87, 90],
        "Frank":[88, 87, 86, 85]
    },
    "HR": {
         "Grace": [70, 72, 74, 76],
         "Heidi":[65, 68, 70, 73],
         "Ivan": [60, 62, 64, 66]
    }
}

#1 Calucate the average performance score for each employee
Average_scores = {}
for department, employees in performance_data.items():
    Average_scores[department] = {}
    for employees, scores in employees.items():
        Average_scores = sum(scores) / len(scores)
        Average_scores[department][employees] = 
     
   