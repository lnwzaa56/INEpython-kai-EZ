with open("sales.txt", "r") as sales_file:

#read the first line rom the file, but don't conver to a number yet
#we stile need to test for an empty string
    line = sales_file.readline()

#read until the empty string is return
    while line != "":
#convert line to a float
        amount = float(line)

#format and display the amount 
        print(format(amount, ".2f"))

#read the next line
        line = sales_file.readline()