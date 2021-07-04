import csv
with open("height-weight.csv") as CSV:
    rd = csv.reader(CSV)
    data = list(rd)
data.pop(0)
height = []
for i in range(0,len(data)):
    num = data[i][1]
    height.append(float(num))

height.sort()
n = len(height)
if n % 2 == 0:
    median1 = float(height[n//2])
    median2 = float(height[n//2+1])
    median = (median1+median2)/2
else:
    median = float(height[n//2])
print(median)
