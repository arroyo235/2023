from functools import reduce
import time

def main(lines):
    # Times the races last
    str_times = lines[0].split(":")[1].split()
    times = [int(x) for x in str_times]
    # Records of distance of the races
    str_records = lines[1].split(":")[1].split()
    records = [int(x) for x in str_records]
    
    # print("Times:", times)
    # print("Records:", records)
    
    races = list(zip(times, records))
    
    # Try all the posibilities to win the race
    def race(races): 
        wins = []
        wins_race = []
        for race in races:
            race_time = race[0]
            record = race[1]
            for hold_time in range(1, race_time + 1):
                # Calculate the distance traveled
                # speed = hold_time
                # time = race_time - hold_time 
                # distance = time * speed
                if (race_time - hold_time) * (hold_time)  > record:
                    wins_race.append(hold_time)
            wins.append(len(wins_race))
            wins_race = []
        return wins
    
    print("Part 1: ", reduce(lambda x, y: x * y, race(races)))

    
    # Part 2
    time = int(''.join(str_times))
    record = int(''.join(str_records))
    
    # print([time, record])
    
    print("Part 2: ", reduce(lambda x, y: x * y, race([[time, record]])))
    
    
   
if __name__ == "__main__":
    # Record the start time
    start_time = time.time()
    # file = open("test.txt", "r")
    file = open("input.txt", "r")
    lines = file.read().split("\n")
    main(lines)
    # Record the end time
    end_time = time.time()
    print("Time:", end_time - start_time)


