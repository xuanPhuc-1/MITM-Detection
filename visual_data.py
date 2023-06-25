from matplotlib import pyplot as plt
import csv

#load the features-file.csv file and plot the graph 
#sep = ',' 
x = []
y = []

with open('features-file.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        y.append(float(row[1]))
        x.append(row[3])

#plot the graph with x-axis is time_stamp and y-axis is ABPS

plots = plt.plot(x,y, label='Loaded from file!')
plt.show()