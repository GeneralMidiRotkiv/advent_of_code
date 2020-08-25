import csv

instructions = []

with open("C:\\Users\\ViktorDingelmaier\\OneDrive - tu-dresden.de\\Coding\\Python\\Projects\\Advent_of_code\\Input_Day3.txt", newline="") as input_file:
    file_reader = csv.reader(input_file, delimiter=",")
    for line in file_reader:
        instructions.append(line)

instructions_wire1 = instructions[0]
instructions_wire2 = instructions[1]

#test1
# instructions_wire1 = ["R75","D30","R83","U83","L12","D49","R71","U7","L72"]
# instructions_wire2 = ["U62","R66","U55","R34","D71","R55","D58","R83"]

#test2
# instructions_wire1 = ["R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"]
# instructions_wire2 = ["U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"]

def formCoords(instructions): 
    coords = {(0,0)}
    current_coords = [0,0]

    for instruction in instructions:
        instruction_distance = int(instruction[1:])+1
        if instruction[0] == "R":
            for x_index in range(1, instruction_distance):
                current_coords[0] = current_coords[0] + 1
                coords.add((current_coords[0], current_coords[1]))
        elif instruction[0] == "L":
            for x_index in range(1, instruction_distance):
                current_coords[0] = current_coords[0] - 1
                coords.add((current_coords[0], current_coords[1]))
        elif instruction[0] == "U":
            for y_index in range(1, instruction_distance):
                current_coords[1] = current_coords[1] + 1
                coords.add((current_coords[0], current_coords[1]))
        elif instruction[0] == "D":
            for y_index in range(1, instruction_distance):
                current_coords[1] = current_coords[1] - 1
                coords.add((current_coords[0], current_coords[1]))
        else: 
            print("Instructions unclear. Dick stuck in stapler")
            break
    
    return coords
    
coordinates_wire1 = formCoords(instructions_wire1)
coordinates_wire2 = formCoords(instructions_wire2)

#Dauert EWIG - Ergebnis deswegen in 'mutual_coordinates' manuell zwischengespeichert
def find_intersections(coordinates1, coordinates2):
    mutual_coordinates = []
    for coordinate in coordinates1:
        if coordinate in coordinates2:
            mutual_coordinates.append(coordinate)
    return mutual_coordinates

mutual_coordinates = find_intersections(coordinates_wire1, coordinates_wire2)
#mutual_coordinates = [(0, 0), (2712, 1515), (2787, 1921), (2913, 2146), (2927, 2146), (3045, 2146), (3370, 1878), (3258, 1690), (2951, 1477), (2043, 1984), (1608, 2379), (2242, 1984), (2130, 2416), (2291, 3276), (2712, 2369), (2487, 2297), (2487, 1984), (2712, 1854), (3258, 1854), (3383, 1878), (3045, 1951), (2744, 2297), (2443, 3095), (1864, 3112), (1608, 2696), (1473, 3948), (2047, 3276), (1864, 3027), (1579, 3027), (331, 3006), (-262, 3482), (-262, 3137), (-482, 3137), (-535, 3137), (-1529, 2650), (-1219, 2201), (-1028, 2201), (-2064, 1618), (-1943, 2475), (-1648, 2650), (-1825, 2650), (-1943, 1885)]

print(mutual_coordinates)

def calc_distance(coordinates):
    shortest = 100000
    for coords in coordinates:
        if coords != (0, 0):
            manhattan_dist = abs(coords[0]) + abs(coords[1])
            if manhattan_dist < shortest:
                shortest = manhattan_dist
    
    print(shortest)

calc_distance(mutual_coordinates)