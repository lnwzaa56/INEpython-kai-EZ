import matplotlid.pyplot as plt 

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y, market="0", linestyle="-", color="b")

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Plot")

plt.show()

