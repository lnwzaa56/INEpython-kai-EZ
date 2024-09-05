#this program prompts the user foe sales amounts
#and writes those amount to the sales.txt file.
#get the number of days
num_day = int(input("For how many day do you have sales? "))

#open a new file named sales.txt using  with statement
with open("sales.txt", "w") as sales_file:

#get the amount of sales for each day write it to the file
    for count in range(1, num_day + 1):

#get the sales for a day
        sales = float(input(f"Enter the sales for day #{count}: "))
      
        

#write the sales amount to the file
        sales_file.write(str(sales)+ "\n")

print("Data written to sales.txt")