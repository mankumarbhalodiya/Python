
import matplotlib.pyplot as plt
x1 = [1, 2, 3]
y1 = [1, 4, 9]
x2 = [1, 2, 3]
y2 = [1, 2, 3]
plt.plot(x1, y1, label='Line 1: y=x^2')
plt.plot(x2, y2, label='Line 2: y=x')
plt.title("Multiple Lines on Same Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.legend()
plt.show()