import csv
input = None

with open("C:\\Users\\vigga\\OneDrive - tu-dresden.de\\Python\\Advent_of_code\\Input_day2.txt", newline="") as file:
    reader = csv.reader(file, delimiter=",")
    def get_input():
        for line in reader:
            return line
    
    input = get_input()

reference = [input[i:i + 4] for i in range(0, len(input), 4)]

input = [int(number) for number in input]

input[1] = 12
input[2] = 2

print("Original:\n", input)
i = 0
while i<len(input)-4:
    if input[i] != 99:
        if input[i] == 1:
            input[input[i+3]] = input[input[i+1]] + input[input[i+2]]
        if input[i] == 2:
            input[input[i+3]] = input[input[i+1]] * input[input[i+2]]
    else:
        print("Program ended at position", i, "because the value", input[i], "occured")
        break
    i += 4

print("New:\n", input)