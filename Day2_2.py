import csv

for x in range(100):
    for y in range(100):

        input = None

        # with open("C:\\Users\\vigga\\OneDrive - tu-dresden.de\\Python\\Advent_of_code\\Input_day2.txt", newline="") as file:
        with open("Input_day2.txt", newline="") as file:
            reader = csv.reader(file, delimiter=",")
            def get_input():
                for line in reader:
                    return line
            
            input = get_input()

        reference = [input[i:i + 4] for i in range(0, len(input), 4)]

        input = [int(number) for number in input]

        input[1] = x
        input[2] = y

        i = 0
        while i<len(input)-4:
            if input[i] != 99:
                if input[i] == 1:
                    input[input[i+3]] = input[input[i+1]] + input[input[i+2]]
                if input[i] == 2:
                    input[input[i+3]] = input[input[i+1]] * input[input[i+2]]

            i += 4
        
        if input[0] == 19690720:
            print("Noun: ", x, "Verb:", y)
            print("Enter:", 100*x+y)