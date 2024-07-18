hours_w = float(input("Enter the number of hourse worked:"))
pay_h   = float(input("Enter the hourly pay rate:"))
if hours_w <= 40 :
   print("the gross pay is:",  hours_w*pay_h)
    
else:
    overtimepay = hours_w - 40
    print ("the gross pay is:", (pay_h*40) + (overtimepay*pay_h*1.5))
    