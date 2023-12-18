import time
import numpy as np

def main(lines):
    
    # PIPES
    vertical_pipe = "|"
    horizontal_pipe = "-"
    # CORNERS
    pipe_L = "L"
    pipe_J = "J"
    pipe_7 = "7"
    pipe_F = "F"
    
    corners = [pipe_L, pipe_J, pipe_7, pipe_F]
    # OTHERS
    ground = "."
    start = "S"
    
    # CONDITIONS
    valid_up = [vertical_pipe, pipe_F, pipe_7, start]
    valid_right = [horizontal_pipe, pipe_J, pipe_7, start]
    valid_down = [vertical_pipe, pipe_L, pipe_J, start]
    valid_left = [horizontal_pipe, pipe_L, pipe_F, start]
    
    grid = []
    for line in lines:
        grid.append([x for x in line])
    
    np_grid = np.array(grid)
    
    # print(np_grid)
    
    # Get "S" coordinates
    x, y = np.where(np_grid == start)
    start_coords = (x[0], y[0])
    
    
    def connects(pipe, adj_pipe, dir):
        # Return if two pipes can be connected
        if adj_pipe == ground:
            return False
        
        # Check the start pipe
        if pipe == "S":
            if dir == "up":
                if adj_pipe in valid_up:
                    return True
            elif dir == "right":
                if adj_pipe in valid_right:
                    return True
            elif dir == "down":
                if adj_pipe in valid_down:
                    return True
            elif dir == "left":
                if adj_pipe in valid_left:
                    return True
        

        # If S if found but not connected, return False
        if adj_pipe == "S":
            if dir == "up" and pipe in ["J", "|", "L"]:
                return True
            if dir == "down" and pipe in ["7", "|", "F"]:
                return True
            if dir == "left" and pipe in ["L", "-", "F"]:
                return True
            if dir == "right" and pipe in ["J", "-", "7"]:
                return True
            
        
        # Check if the pipe connects with the adjacent pipe
        if pipe == horizontal_pipe:
            if dir == "left":
                if adj_pipe in valid_left:
                    return True
            elif dir == "right":
                if adj_pipe in valid_right:
                    return True
            else:
                return False
        elif pipe == vertical_pipe:
            if dir == "up":
                if adj_pipe in valid_up:
                    return True
            elif dir == "down":
                if adj_pipe in valid_down:
                    return True
            else:
                return False
        elif pipe == pipe_L:
            if dir == "up":
                if adj_pipe in valid_up:
                    return True
            elif dir == "right":
                if adj_pipe in valid_right:
                    return True
            else:
                return False
        elif pipe == pipe_J:
            if dir == "up":
                if adj_pipe in valid_up:
                    return True
            elif dir == "left":
                if adj_pipe in valid_left:
                    return True
            else:
                return False
        elif pipe == pipe_7:
            if dir == "down":
                if adj_pipe in valid_down:
                    return True
            elif dir == "left":
                if adj_pipe in valid_left:
                    return True
            else:
                return False
        elif pipe == pipe_F:
            if dir == "down":
                if adj_pipe in valid_down:
                    return True
            elif dir == "right":
                if adj_pipe in valid_right:
                    return True
            else:
                return False
    
    visited_pipes = []
    found = False
    start_position = True
    # Current pipe
    pipe = "S"
    while not found:
        
        if start_position:
            coords = start_coords
            visited_pipes.append(coords)
            start_position = False
        
        # Adjacent pipes with possible out of bounds coordinates
        adjacent_pipes_ini = {
            "up": (coords[0] - 1, coords[1]), # Up
            "right": (coords[0], coords[1] + 1), # Right
            "down": (coords[0] + 1, coords[1]), # Down
            "left": (coords[0], coords[1] - 1), # Left
        }
        
        # Adjacent pipes with valid coordinates
        adjacent_pipes = {}
        # Ignore out of bounds coordinates
        for dir, adj in adjacent_pipes_ini.items():
            if adj[0] < 0 or adj[1] < 0 or adj[0] >= len(np_grid) or adj[1] >= len(np_grid[0]):
                # print("Out of bounds")
                continue
            else:
                adjacent_pipes[dir] = adj
        
        
        # print("Adjacents coords of", coords, adjacent_pipes)
            
        # Search for the next pipe up, down, left or right
        for dir, adj_pipe_coord in adjacent_pipes.items():
            adj_pipe = np_grid[adj_pipe_coord]
            # print(adj_pipe)
            
            # If S is found, stop (>3 so it doesnt catch the "S" at the beginning)
            if adj_pipe == "S" and len(visited_pipes) > 3:
                if connects(pipe, adj_pipe, dir):
                    print("Found start")
                    found = True
                    break
            
            if adj_pipe == ground:
                continue
            
            # print("Connects?", pipe, adj_pipe, dir)
            if connects(pipe, adj_pipe, dir) and adj_pipe_coord not in visited_pipes:
                # print("Found adj_pipe", dir , adj_pipe_coord, adj_pipe)
                coords = adj_pipe_coord
                pipe = adj_pipe
                # print(pipe, end="")
                visited_pipes.append(coords)
                break
        
    # print("Visited pipes", visited_pipes)
    
    sol = len(visited_pipes)
    
    print(sol)
    print("Solution:", sol/2) # Sol = 6927


      
if __name__ == "__main__":
    # Record the start time
    start_time = time.time()
    file = open("test.txt", "r")
    # file = open("input.txt", "r")
    lines = file.read().split("\n")
    main(lines)
    # Record the end time
    end_time = time.time()
    # print("Time:", end_time - start_time)
