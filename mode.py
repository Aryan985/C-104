import csv
with open("height-weight.csv") as CSV:
    rd = csv.reader(CSV)
    data = list(rd)
data.pop(0)
height = []
for i in range(0,len(data)):
    num = data[i][1]
    height.append(float(num))
    
import statistics
mode = statistics.mode(height)
print(mode)
mean = statistics.mean(height)
print(mean)
median = statistics.median(height)
print(median)