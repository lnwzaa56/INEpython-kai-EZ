def caculate_stats(numbers):
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return total_sum, average,maximum, minimum

#Example usage
number = [5,10,15,20,25]
total, avg,max_mum,min_num = caculate_stats(number)

print(f"Total sum:{total}")
print(f"Average :{avg}")
print(f"Maxmimum:{max_mum}")
print(f"Minmum :{min_num}")
