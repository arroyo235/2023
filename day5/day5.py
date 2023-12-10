import re
from tqdm import tqdm

def main(lines):

    # maps = [
        # [destination_range_start, source_range_start, range_length],
        # [destination_range_start, source_range_start, range_length],
        # [...], ... ]
        
    seeds = []
    seed_to_soil = []
    soil_to_fertilizer = []
    fertilizer_to_water = []
    water_to_light = []
    light_to_temperature = []
    temperature_to_humidity = []
    humidity_to_location = []
    
    # Read the rest of the input (Almanac)
    current_map = None
    
    for line in lines:
        # Skip empty lines
        if not line:
            continue
        
        if line.startswith("seeds"):
            seeds = [int(x) for x in lines[0].split(":")[1].split()]
        elif line.startswith("seed-to-soil"):
            current_map = seed_to_soil
        elif line.startswith("soil-to-fertilizer"):
            current_map = soil_to_fertilizer
        elif line.startswith("fertilizer-to-water"):
            current_map = fertilizer_to_water
        elif line.startswith("water-to-light"):
            current_map = water_to_light
        elif line.startswith("light-to-temperature"):
            current_map = light_to_temperature
        elif line.startswith("temperature-to-humidity"):
            current_map = temperature_to_humidity
        elif line.startswith("humidity-to-location"):
            current_map = humidity_to_location
        elif current_map is not None:
            # Add the mapping to the current map
            current_map.append([int(x) for x in line.split()])

    # print("Seeds:", seeds)
    # print("Seed-to-Soil List:", seed_to_soil)
    # print("Soil-to-Fertilizer List:", soil_to_fertilizer)
    # print("Fertilizer-to-Water List:", fertilizer_to_water)
    # print("Water-to-Light List:", water_to_light)
    # print("Light-to-Temperature List:", light_to_temperature)
    # print("Temperature-to-Humidity List:", temperature_to_humidity)
    # print("Humidity-to-Location List:", humidity_to_location)

    # Save the results after all the mappings
    results = []
    # All maps
    maps = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location]
    # Iterate through the seeds
    for seed in seeds:
        # print("Seed:", seed)
        source = seed
        
        # Iterate through all the maps
        for map in maps:
            # print("Source:", source)
            source = mapping(source, map)
        # print("Last source:", source)
            
        results.append(source)
    
    min_location = min(results)
    print("Solution part 1:", min_location)
    
    # Part 2, reverse mapping
    # Seeds for part 2
    temp_seeds = seeds
    seeds = []
    # Calculate seeds for part 2 (ranges of seed numbers)
    for i in range(0, len(temp_seeds), 2):
        pair = [temp_seeds[i], temp_seeds[i+1]]
        seeds.append(range(pair[0], pair[0] + pair[1]))
    
    # print("Seeds:", seeds)
    found = False
    # Start reverse mapping from 0 to min_location
    # for location in tqdm(range(min_location), desc="Reverse mapping"):
    for location in range(min_location+1):
        destination = location
        # Iterate through all the maps in reverse order
        for map in reversed(maps):
            # Last destination will be a seed
            destination = reversed_mapping(destination, map)
        if found:
            break
        else:
            for range_seed in seeds:
                if destination in range_seed:
                    # print("Seed:", destination)
                    found = True
                    break
    print("Solution part 2:", location)
    print("Seed:", destination)
        
def mapping(source,  map):
    # Iterate each line inside the map
    for line in map:
        destination_range_start = line[0]
        source_range_start = line[1]
        range_length = line[2]
        
        source_range = range(source_range_start, source_range_start + range_length)
        # print(source_range)
        destination_range = range(destination_range_start, destination_range_start + range_length)
        # print(destination_range)
        
        # Calculate the new source value
        if source in source_range:
            # Get the index of the source value in the source range
            index = source_range.index(source)
            # Get the value in the destination range at the same index
            source = destination_range[index]
            break
        
    # If source value is not in the source range, the source value is the same
    return source
        
def reversed_mapping(destination,  map):
    # Iterate each line inside the map
    for line in map:
        # For reverse mapping, the destination is the source and the source is the destination
        destination_range_start = line[0]
        source_range_start = line[1]
        range_length = line[2]
        
        source_range = range(source_range_start, source_range_start + range_length)
        # print(source_range)
        destination_range = range(destination_range_start, destination_range_start + range_length)
        # print(destination_range)
        
        # Calculate the new destination value
        if destination in destination_range:
            # Get the index of the destination value in the destination range
            index = destination_range.index(destination)
            # Get the value in the destination range at the same index
            destination = source_range[index]
            break
        
    # If destination value is not in the destination range, the destination value is the same
    return destination

if __name__ == "__main__":
    file = open("test.txt", "r")
    # file = open("input.txt", "r") # 125742457
    lines = file.read().split("\n")
    main(lines)

