import time, math

def main(lines):
    
    # Report of the history of all the different values
    report = []
    
    for line in lines:
        # Histoty of one value
        history = [int(x) for x in line.split()]
        report.append(history)

    # print(report)
    
    def prediciton(history):
        
        """Calculate the prediction of the next history
        
        [[0,3,6,9,12,15], [3,3,3,3,3], [0,0,0,0]]
        
        Since these values aren't all zero, repeat the process
        
        """
        # If all values are zero, return 0
        if all(x == 0 for x in history):
            return 0
        
        # history = [0,3,6,9,12,15]
        reduced_history = []
        
        for value in range(len(history)-1):
            reduced_history.append((history[value + 1] - history[value]))

        # print("Reduced history:", reduced_history)
        predicted_value = prediciton(reduced_history)
        
        # print("Predicted value:", predicted_value)
        # print("Returned value:", history[-1] + predicted_value)
        return history[-1] + predicted_value
    
    
    # PART 1
    new_values = []
    
    for history in report:
        new_values.append(prediciton(history))
    print("Part 1:", sum(new_values))
    
    # PART 2
    new_values = []
    for history in report:
        rev_history = list(reversed(history))
        new_values.append(prediciton(rev_history))
        
    print("Part 2:", sum(new_values))
   
if __name__ == "__main__":
    # Record the start time
    start_time = time.time()
    # file = open("test.txt", "r")
    file = open("input.txt", "r")
    lines = file.read().split("\n")
    main(lines)
    # Record the end time
    end_time = time.time()
    # print("Time:", end_time - start_time)


