import csv
import math
sum = 0

with open('Input_day1.txt', newline="") as file:
    reader = csv.reader(file, delimiter=" ")
    for row in reader:
        mass= int(row[0])
        sum += math.floor(mass/3) - 2

print(sum)


