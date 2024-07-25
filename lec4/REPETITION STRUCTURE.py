keep_going = "y"
while keep_going =="y" :

      sales = float(input("Enter the amount of salaes: "))
      comm_rate = float(input("Enter the commission rate: "))

      commision = sales * comm_rate

      print(f"The commision is ${commision:.2f}")

      kepp_going = input("Do you want to calculate another" + " commission (Enter y for yes):")