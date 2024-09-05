with open("sales.txt", "r") as sales_file:

#Read all the lines from the file
    for line in sales_file:

#convert line  to a float
        amount = float(line)

#Format and display the amount
        print(format(amount, ".2f"))