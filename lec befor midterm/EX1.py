
# Get the number of employee record to create
num_emps = int(input("How many employee records do you want to create? "))

#open a file for writing using with statement
with open("employee.txt", "w") as emp_file:

    #get each employee's data and write it to the file
    for count in range(1, num_emps + 1):

        #get data for an employee
        print("Enter data for employee #", count, sep="")
        name = input("Name: ")
        id_num = input("ID: ")
        dept = input("Depar: ")

        #write the data as a record to the file
        emp_file.write( name + "\n")
        emp_file.write(id_num + "\n")
        emp_file.write( dept + "\n")
        #display a blank line.
        print()




