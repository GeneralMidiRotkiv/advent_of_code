import csv
input = None

with open("C:\\Users\\ViktorDingelmaier\\OneDrive - tu-dresden.de\\Coding\\Python\\Projects\\Advent_of_code\\Input_Day5.txt", newline="") as file:
    reader = csv.reader(file, delimiter=",")
    def get_input():
        for line in reader:
            return line
    
    input = get_input()

input = [int(number) for number in input]

input[1] = 12
input[2] = 2

print("Original:\n", input)
i = 0
while i<len(input)-4:
    opcode = input[i]
    inputValue = -1000
    if opcode != 99:
        if opcode == 1:
            input[input[i+3]] = input[input[i+1]] + input[input[i+2]]
            i += 4
        elif opcode == 2:
            input[input[i+3]] = input[input[i+1]] * input[input[i+2]]
            i += 4
        elif opcode == 3:
            input[i+1] = inputValue
            i += 2
        elif opcode == 4:
            print("Opcode 4 print:", input[i+1])
            i += 2
        """ else:
            print("Opcode '{}' could not be recognized".format(opcode)) """

    else:
        print("Program ended at position", i, "because the value", input[i], "occured")
        break
    

print("New:\n", input)