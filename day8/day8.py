import time, math

def main(lines):

    moves = lines[0]
    map = {}
    lines.pop(0) # Remove the first line
    for line in lines:
        # Skip empty lines
        if not line:
            continue
        # node = 
        node = line.split(" = ")[0]
        # [1:-1] removes the first and last parenthesis
        elements = line.split(" = ")[1][1:-1].split(', ')
        map[node] = elements
        
    # Map items
    # print("Map items")
    # for k, v in map.items():
    #     print(k,":",  v[0], v[1])

    def part1(INI, END):

        found = False
        steps = 0
        while not found:
            for move in moves:
                if steps == 0:
                    # The first node is AAA, curr_node is the current node = (BBB, CCC)
                    curr_node = map[INI]
                else:
                    curr_node = map[curr_node]
                    
                # Take the left element
                if move == "L":
                    curr_node = curr_node[0]
                # Take the right element
                elif move == "R":
                    curr_node = curr_node[1]
                
                steps += 1
                if curr_node == END:
                    found = True
                    break
                elif END is None and curr_node.endswith("Z"):
                    found = True
                    break
                
        return steps
        
    # PART 1
    sol = part1(INI="AAA", END="ZZZ")
    
    print("Part 1:", sol)
    
    
    def part2():
        def find_inital_nodes():
            initial_nodes = []
            for k, v in map.items():
                #If the last letter of the node is A, it is an initial node
                if k[-1] == "A":
                    initial_nodes.append(k)
            return initial_nodes
        
        initial_nodes = find_inital_nodes()
        # print("Initial nodes:", initial_nodes)
        
        steps_list = []
        for node in initial_nodes:
            steps = part1(INI=node, END=None)
            steps_list.append(steps)

        # print("steps_list:", steps_list)
        print("Part 2:", math.lcm(*steps_list))
            
        
        """
        # For always run code... DONT USE THIS
        found = False
        steps = 0
        while not found:
            for move in moves:
                if steps == 0:
                    # The firsts nodes are the ones finishing with an "A", like 11A, 22A,..
                    current_nodes = find_inital_nodes()
                else:
                    # Reset the current nodes
                    # current_nodes = []
                    pass
                
                
                # Save the current nodes for the next iteration
                # Current nodes = [(11B, XXX), (22B, XXX), ...] (input)
                # Current nodes = ["11B", "22B", ...] (exiting the for loop)
                next_nodes = []
                for node in current_nodes:
                    # Take the left element
                    if move == "L":
                        curr_node = node[0]
                        # Replace (11B, XXX) por los elementos que tiene el nodo 11B
                        index = current_nodes.index(node)
                        current_nodes.remove(node)
                        current_nodes.insert(index, map[curr_node])
                        next_nodes.insert(index, curr_node)
                    # Take the right element
                    elif move == "R":
                        curr_node = node[1]
                        # Replace (XXX, 11Z) por los elementos que tiene el nodo 11Z
                        index = current_nodes.index(node)
                        current_nodes.remove(node)
                        current_nodes.insert(index, map[curr_node])
                        next_nodes.insert(index, curr_node)
                        
                # print("Next nodes:", next_nodes)
                steps += 1
                # Check if all the nodes ends with a Z        
                found = all(node.endswith("Z") for node in next_nodes)
        """
                
    # PART 2
    part2()
   
if __name__ == "__main__":
    # Record the start time
    start_time = time.time()
    # file = open("test.txt", "r")
    # file = open("test2.txt", "r") # test for part 2
    file = open("input.txt", "r")
    lines = file.read().split("\n")
    main(lines)
    # Record the end time
    end_time = time.time()
    # print("Time:", end_time - start_time)


