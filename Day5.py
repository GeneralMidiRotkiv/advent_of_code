import csv
puzzleInput = None

with open("C:\\Users\\ViktorDingelmaier\\OneDrive - tu-dresden.de\\Coding\\Python\\Projects\\Advent_of_code\\Input_Day5.txt", newline="") as file:
    reader = csv.reader(file, delimiter=",")
    def get_puzzleInput():
        for line in reader:
            return line
    
    puzzleInput = get_puzzleInput()

puzzleInput = [int(number) for number in puzzleInput]

puzzleInput[1] = 12
puzzleInput[2] = 2

#print("Original:\n", puzzleInput)
i = 0
#while i<len(puzzleInput):
for instruction in puzzleInput:
    opcode = puzzleInput[i]
    if opcode != 99:
        if opcode == 1:
            """" Opcode 1: addition - the first two numbers (called puzzleInputs) after the opcode indicate the positions from which the puzzleInput values should be read. 
            The third one indicates the position at which the output should be stored """
            puzzleInput[puzzleInput[i+3]] = puzzleInput[puzzleInput[i+1]] + puzzleInput[puzzleInput[i+2]]
            i += 4
        elif opcode == 2:
            """ Opcode 2: multiplication -  multiply the two puzzleInput numbers and store the result at the output position given by the third number"""
            puzzleInput[puzzleInput[i+3]] = puzzleInput[puzzleInput[i+1]] * puzzleInput[puzzleInput[i+2]]
            i += 4
        elif opcode == 3:
            """ Opcode 3: save a given puzzleInput at the position specified by the following number """
            systemID = int(input("Please enter the ID of the system to test: "))
            puzzleInput[i+1] = systemID
            i += 2
        elif opcode == 4:
            """ Opcode 4: output the value at the position specified by the following number """
            print("Opcode 4 print:", puzzleInput[i+1])
            i += 2
        else:
            i += 4
            print("Opcode '{}' could not be recognized".format(opcode))

    else:
        #If opcode 99 is encountered, halt the program
        print("Program ended at position", i, "because the value", puzzleInput[i], "occured")
        break

print("New:\n", puzzleInput)