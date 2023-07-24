from matplotlib import pyplot as plt
import csv
plt.clf()
#visualize the graph with x-axis is time_stamp and y-axis is APS
# create x list contain from 0 to 72 seconds with 3 second interval
x = []
for i in range(0, 72, 3):
    x.append(i)
y1 = []
y2 = []
y3 = []
y4 = []

with open('evaluation.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        y1.append(float(row[0]))
        y2.append(float(row[1]))    
        y3.append(float(row[2]))
        y4.append(float(row[3]))


#plot the graph with 4 subplots

plt.subplot(2, 2, 1)
plt.plot(x, y1, marker='o')
plt.title('APS')
plt.xlabel('Time')
plt.text(30, 30, "Normal", fontsize=12, color='green')
plt.text(45, 30, "Attack", fontsize=12, color='red')

plt.subplot(2, 2, 2)
plt.plot(x, y2, marker='o')
plt.title('ABPS')
plt.xlabel('Time')
plt.text(30, 1.5, "Normal", fontsize=12, color='green')
plt.text(45, 1.5, "Attack", fontsize=12, color='red')

plt.subplot(2, 2, 3)
plt.plot(x, y3, marker='o')
plt.title('SUBARP')
plt.xlabel('Time')
plt.text(25, 0.5, "Normal", fontsize=12, color='green')
plt.text(42, 0.5, "Attack", fontsize=12, color='red')

plt.subplot(2, 2, 4)
plt.plot(x, y4, marker='o')
plt.title('MISS_MAC')
plt.xlabel('Time')
plt.text(30, 0.5, "Normal", fontsize=12, color='green')
plt.text(42, 0.5, "Attack", fontsize=12, color='red')
plt.show()

        
        
#clear all plt figure



