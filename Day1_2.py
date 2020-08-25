import csv
import math
sum = 0

with open("Input_day1.txt", newline="") as file:
    reader = csv.reader(file, delimiter=" ")
    for row in reader:
        mass = int(row[0])

        def calculateFuel(inputMass):
            fuel = math.floor(inputMass/3) - 2
            if fuel>0:
                global sum
                sum += fuel
                calculateFuel(fuel)
        
        calculateFuel(mass)


print(sum)


