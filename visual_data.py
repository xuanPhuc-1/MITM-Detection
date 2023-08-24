from matplotlib import pyplot as plt
import csv
plt.clf()
#visualize the graph with x-axis is time_stamp and y-axis is APS
# create x list contain from 0 to 72 seconds with 3 second interval

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

number_of_samples = len(y1)
x = []

#use for loop to create x list, each sample has 3 second interval
for i in range(0, number_of_samples):
    x.append(i*3)
    

#plot the graph with 4 subplots


# plt.plot(x, y1, marker='o')
# plt.title('ARP Packets per Second')
# plt.xlabel('Time')
# plt.ylabel('Value')
# # plt.text(30, 30, "Normal", fontsize=12, color='green')
# # plt.text(45, 30, "Attack", fontsize=12, color='red')
# plt.show()

# # plt.subplot(2, 2, 2)
# plt.plot(x, y2, marker='o')
# plt.title('ARP Broadcast Packets per Second')
# plt.xlabel('Time')
# plt.ylabel('Value')
# # plt.text(30, 1.5, "Normal", fontsize=12, color='green')
# # plt.text(45, 1.5, "Attack", fontsize=12, color='red')
# plt.show()

# #plt.subplot(2, 2, 3)
# plt.plot(x, y3, marker='o')
# plt.title('Subtraction of ARP request and ARP reply')
# plt.xlabel('Time')
# plt.ylabel('Value')
# # plt.text(25, 0.5, "Normal", fontsize=12, color='green')
# # plt.text(42, 0.5, "Attack", fontsize=12, color='red')
# plt.show()
#set the font-family is Times New Roman

plt.rcParams["font.family"] = "Times New Roman"
#plt.subplot(2, 2, 4)
# plt.plot(x, y4, marker='o')
# #set the title font-family is Times New Roman

# plt.title('Miss-Match IP and MAC address', size=35, **csfont)
# plt.xticks(fontsize=30)
# plt.yticks(fontsize=30)
# plt.xlabel('Time', size=35)
# # increase xlabel size
# plt.ylabel('Value', size=35)
# # plt.text(30, 0.5, "Normal", fontsize=12, color='green')
# # plt.text(42, 0.5, "Attack", fontsize=12, color='red')
# # increase the font size and the number size on the axis

# plt.show()
plt.title('title')
plt.xlabel('xlabel')
plt.show()

        
        
# #clear all plt figure



