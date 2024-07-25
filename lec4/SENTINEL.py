keep_going = "y"
while keep_going =="y" :

      wholesale = float(input("Enter the item's wholesale cost: "))

      retail_price = wholesale * 2.5

      print(f"Retail price is ${retail_price:.2f}")

      kepp_going = input("Do you have another item?" + " (Enter y for yes):")