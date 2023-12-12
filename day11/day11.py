import numpy as np
import time

def main(lines):
    
    # An image of galaxies (#) and empty space (.)
    image = []
    
    for line in lines:
        image.append([x for x in line])
        
    initial_image = np.array(image)
    
    # print("Initial image:")
    # print(initial_image.shape)
    # print()
    
    # Expand the image where all the row and columns are empty (.)
    
    def expand(matrix, size):
        
        row_indexes = []
        col_indexes = []
        
        # Get indexes of empty rows
        for i, row in enumerate(matrix):
            if np.all(row == "."):
                row_indexes.append(i)

        # Get indexes of empty columns
        for i, col in enumerate(matrix.T):
            if np.all(col == "."):
                col_indexes.append(i)
                
        # Expand the matrix
        matrix = np.insert(matrix, row_indexes*size, ".", axis=0)
        matrix = np.insert(matrix, col_indexes*size, ".", axis=1)
                        
        return matrix
    
    
    # Expand the image
    image = expand(initial_image, size=1)
    # print("Image expanded:")
    # print(image.shape)
    
    # Coordinates of the galaxies after expanding the universe
    x, y = np.where(image == "#")
    galaxies = list(zip(x,y))
    # print(galaxies)
    

    
    def get_distances(galaxies):
        # Distance
        distances = []
        for galaxy in galaxies:
            for galaxy2 in galaxies:
                if galaxy == galaxy2:
                    continue
                
                distance = (abs(galaxy2[0]-galaxy[0]), abs(galaxy2[1]-galaxy[1]))
                distances.append(sum(distance))
                # print("Distance:", galaxy, galaxy2, sum(distance))
        
        # After expanding the universe, the sum of the shortest path between all pairs of galaxies 
        return distances
        
    # Divided by 2 because the distance between A and B is the same as B and A
    solution = int(sum(get_distances(galaxies))/2)
    print("Part 1:", solution)
    
    
    
    
    
    #####################  PART 2 #####################
    
    # Size of the expansion
    size = 1000000 - 1
    
    # Para coordenada de cada galaxia se le suma la expansion en funcion de las veces que se ha expandido previamente
    row_indexes = []
    col_indexes = []
    
    # Get indexes of empty rows
    for i, row in enumerate(initial_image):
        if np.all(row == "."):
            row_indexes.append(i)
    # print("Empty rows:", row_indexes)
    
    # Get indexes of empty columns
    for i, col in enumerate(initial_image.T):
        if np.all(col == "."):
            col_indexes.append(i)
    # print("Empty columns:", col_indexes)
    
    # Coordenadas de las galaxias
    x, y = np.where(initial_image == "#")
    galaxies = list(zip(x,y))
    galaxies = [list(galaxy) for galaxy in galaxies]
                
    # print("Galaxies:", galaxies)
    
    witdh = initial_image.shape[1]
    height = initial_image.shape[0]
    
    # Map to initialise the size of the expanded universe
    row_map = [size] * height
    column_map = [size] * witdh
    
    # The row and columns where there are galaxies are set to 0
    for galaxy in galaxies:
        row_map[galaxy[0]] = 0
        column_map[galaxy[1]] = 0
    
    # print("Row map:", row_map) # [9,9,9,9,9,9...]
    # print("Column map:", column_map) # [9,9,9,9,9,9...]
    
    new_row_map = [0]*len(row_map)
    new_column_map = [0]*len(column_map)
    
    # Calculate the new witdh and height of the universe with the expansion and the galaxies
    for i in range(len(row_map)):
        new_row_map[i] = sum(row_map[:i+1])
        
    for i in range(len(column_map)):
        new_column_map[i] = sum(column_map[:i+1])
    
    # print("Row map:", new_row_map) # example: [0, 0, 9, 9, 9, 18, 18, 18, 27, 27]
    # print("Column map:", new_column_map) # [0, 0, 0, 9, 9, 9, 9, 18, 18, 18]

    # New coords of the galaxies after expanding the universe
    new_galaxies = []
    for x, y in galaxies:
        new_row_index = x + new_row_map[x]
        new_col_index = y + new_column_map[y]
        new_galaxies.append((new_row_index, new_col_index))
        
    solution = int(sum(get_distances(new_galaxies))/2)

    print("Part 2:", solution)
    
      
if __name__ == "__main__":
    # start = time.time()
    file = open("test.txt", "r")
    file = open("input.txt", "r")
    lines = file.read().split("\n")
    main(lines)
    # end = time.time()
    # print("Time:", end-start)