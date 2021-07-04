import csv
with open("height-weight.csv") as CSV:
    rd = csv.reader(CSV)
    data = list(rd)
data.pop(0)
height = []
for i in range(0,len(data)):
    num = data[i][1]
    height.append(float(num))

sum = 0
for a in height:
    sum = sum+a

mean = sum/len(height)
print(mean)