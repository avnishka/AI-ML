import matplotlib.pyplot as plt
#line plot
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.xlabel('x')
plt.ylabel('y')
plt.title('Line Plot')
plt.plot(x, y, color='red', linestyle='--', marker='o',markersize=5 ,linewidth=2)
plt.show()

#subplots
x1 = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
plt.figure(figsize=(10, 5))

plt.subplot(2,2,1)
plt.plot(x1, y1, color='red', linestyle='--', marker='o',markersize=5 ,linewidth=2)
plt.title('Subplot 1')

plt.subplot(2,2,2)
plt.plot(x1, y1, color='blue', linestyle='-', marker='s',markersize=5 ,linewidth=2)
plt.title('Subplot 2')

plt.subplot(2,2,3)
plt.plot(x1, y1, color='green', linestyle='-.', marker='^',markersize=5 ,linewidth=2)
plt.title('Subplot 3')

plt.subplot(2,2,4)
plt.plot(x1, y1, color='purple', linestyle=':', marker='*',markersize=5 ,linewidth=2)
plt.title('Subplot 4')

plt.show()

#BAR PLOT
x2 = [1, 2, 3, 4, 5]
y2 = [1, 4, 9, 16, 25]
plt.bar(x2, y2, color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Bar Plot')

plt.show()
