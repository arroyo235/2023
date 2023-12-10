def is_adjacent(num_coord, symbols_coords):
    x, y = num_coord
    adjacents = [(x-1, y-1), (x, y-1), (x+1, y-1),
                 (x-1, y),             (x+1, y),
                 (x-1, y+1), (x, y+1), (x+1, y+1)]
    
    for adj in adjacents:
        if adj in symbols_coords:
            return True
        
    return False
    
def is_gear_adjacent(num_coord, all_gear_coords):
    x, y = num_coord
    adjacents = [(x-1, y-1), (x, y-1), (x+1, y-1),
                 (x-1, y),             (x+1, y),
                 (x-1, y+1), (x, y+1), (x+1, y+1)]
    
    has_gear = False
    gears_adjacents = []  
    for adj in adjacents:
        if adj in all_gear_coords:
            # print(adj, all_gear_coords)
            gears_adjacents.append(adj)
            has_gear = True
            
    if has_gear:
        return True, gears_adjacents
    else:        
        return False, None
    
    
def main(lines):
    # numbers = [[467, [(0,0),(1,0),(2,0)]], [114, [(5,0), (6,0), (7,0)]], [35, [(2, 2), (3, 2)]], ...]
    numbers = []
    x, y = 0, 0
    
    symbols_coords = [] 
    all_gear_coords = []
    
    for line in lines:
        num = ""
        num_coords = []
        for char in line:
            if char.isdigit():
                num += char
                num_coords.append((x, y))
            else:
                if num != "":
                    numbers.append([int(num), num_coords])
                    num_coords = []
                if char == ".":
                    num = ""
                else: # Es un simbolo
                    if char == "*": # Es un gear, añadimos sus coordenadas
                        all_gear_coords.append((x, y))
                    symbols_coords.append((x, y))
                    num = ""
            x += 1
        
        # Al finalizar la linea, resetear x e incrementar y, añadimos los numeros al final de la linea
        if num != "":
            numbers.append([int(num), num_coords])
            num_coords = []
        x = 0
        y += 1
    # print(numbers)
    # print(symbols_coords)
    # print(all_gear_coords)
    
    # Comprbamos si las coordenadas de los numeros tienen un simbolo adayacente
    adjacents = []
    # gear_adjacents = {gear_coords: [num1, num2, ...], ...}
    gear_adjacents = {}
    for num in numbers:
        for coords in num[1]:
            if is_adjacent(coords, symbols_coords):
                # print("Tiene adyacente: ", num[0], coords)
                adjacents.append(num[0])
                has_gear, gear_coords = is_gear_adjacent(coords, all_gear_coords)
                if has_gear:
                    # print("Tiene gear adyacente: ", num[0], " con gears: ", gear_coords)
                    for gear_coord in gear_coords:
                        if gear_coord not in gear_adjacents:
                            gear_adjacents[gear_coord] = []
                        gear_adjacents[gear_coord].append(num[0])     
                break
            
    # print(adjacents)        
    print("Part 1:", sum(adjacents)) # 540212

    # Part 2            
    # for k, v in gear_adjacents.items():
    #     print(k, v)
        
    gear_ratio = 1
    total_gear_ratio = []
    for k, v in gear_adjacents.items():
        if(len(v) == 2):
            for num in v:
                gear_ratio *= num
            total_gear_ratio.append(gear_ratio)
        gear_ratio = 1
            
    print("Part 2:", sum(total_gear_ratio)) # 87605697
        
if __name__ == "__main__":
    # file = open("test.txt", "r")
    file = open("input.txt", "r")
    lines = file.read().split("\n")
    main(lines)

