import numpy as np
import time

def main(lines):
    
    # Springs: operational (.) or damaged (#) or unknown (?)
    
    springs = []
    groups = []
    
    for line in lines:
        springs_line = line.split()[0]
        group = [int(x) for x in line.split()[1].split(",")]
        
        springs.append(springs_line)
        groups.append(group)
        
    records = list(zip(springs, groups))
    
    for record in records:
        print(record)
    
    def eval_springs(springs):
        
        # Evaluate springs an return the list of spring groups
        for spring in springs:
            if spring == "?":
                # Sustitute the unknow spping with operational or damaged
                continue    
    
      
if __name__ == "__main__":
    # start = time.time()
    file = open("test.txt", "r")
    # file = open("input.txt", "r")
    lines = file.read().split("\n")
    main(lines)
    # end = time.time()
    # print("Time:", end-start)