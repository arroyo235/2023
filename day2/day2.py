import re

def main(lines):
    # PART 1
    games = {}
    MAX_RED = 12
    MAX_GRREN = 13
    MAX_BLUE = 14
    valid_list = []
    invalid_list = []
    
    # Flag para saltar al siguiente set
    next_set = False
    
    # PART 1
    for line in lines:
        # Obtengo el numero de juego
        num_game = int(re.findall(r"\d+", line)[0])
        # Obtengo el set
        sets = line.split(":")[1].split(";")
        games[num_game] = {"red": 0, "green": 0, "blue": 0}
        for set in sets:
            cubes = re.findall(r"\d+ \w+", set)
            for cube in cubes:
                num_color = int(cube.split(" ")[0])
                color = cube.split(" ")[1]
                if color == "red" and num_color > MAX_RED:
                    invalid_list.append(num_game)
                    next_set = True
                    break
                elif color == "green" and num_color > MAX_GRREN:
                    invalid_list.append(num_game)
                    next_set = True
                    break
                elif color == "blue" and num_color > MAX_BLUE:
                    invalid_list.append(num_game)
                    next_set = True
                    break
            if next_set:
                next_set = False
                break
    
    # PART 1 - Para el input completo
    valid_list = [x for x in range(1, 101) if x not in invalid_list]
    # print(valid_list)
    print("Part 1: ", sum(valid_list)) # Result 2541
    
    # PART 2
    part2 = []
    for line in lines:
        # Obtengo el numero de juego
        num_game = int(re.findall(r"\d+", line)[0])
        # Obtengo el set
        sets = line.split(":")[1].split(";")
        games[num_game] = {"red": 0, "green": 0, "blue": 0}
        num_red = 0
        num_green = 0
        num_blue = 0
        for set in sets:
            cubes = re.findall(r"\d+ \w+", set)
            for cube in cubes:
                num_color = int(cube.split(" ")[0])
                color = cube.split(" ")[1]                
                # PART 2
                if color == "red" and num_color > num_red:
                    num_red = num_color
                elif color == "green" and num_color > num_green:
                    num_green = num_color
                elif color == "blue" and num_color > num_blue:
                    num_blue = num_color
                

        # print(num_game,": ", num_red* num_green* num_blue)
        part2.append(num_red* num_green* num_blue)
        
    print("Part 2: ", sum(part2))
            
if __name__ == "__main__":
    # file = open("test.txt", "r")
    file = open("input.txt", "r")
    lines = file.read().split("\n")
    main(lines)

