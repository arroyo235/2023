seeds = "950527520 85181200 546703948 123777711 63627802 279111951 1141059215 246466925 1655973293 98210926 3948361820 92804510 2424412143 247735408 4140139679 82572647 2009732824 325159757 3575518161 370114248"
seeds = "79 14 55 13"
seeds = [int(x) for x in seeds.split()]

temp_seeds = seeds
seeds = []
# Calculate seeds for part 2 (ranges of seed numbers)
for i in range(0, len(temp_seeds), 2):
    pair = [temp_seeds[i], temp_seeds[i+1]]
    seeds.append(range(pair[0], pair[0] + pair[1]))
    
for seed in seeds:
    print(seed)

# Convert ranges to tuples for easier manipulation
# seeds = [tuple(seed) for seed in seeds]
print()
start_seed = 0
end_seed = 0
# min_seed = 99999999999999
# max_seed = 0
seeds_list = []

# Convert ranges to tuples for easier manipulation
for i, seed in enumerate(seeds):
    start_seed = seed[0]
    end_seed = seed[-1]
    seeds_list.append((start_seed, end_seed+1))
        
# Sort the seeds based on their starting values
seeds.sort(key=lambda x: x[0])

# Initialize a merged list with the first seed
merged_seeds = [seeds[0]]

# Iterate through the sorted seeds and merge overlapping seeds
for current_seed in seeds[1:]:
    if current_seed[0] <= merged_seeds[-1][1]:
        # If overlapping, merge the seeds by updating the end value
        merged_seeds[-1] = (merged_seeds[-1][0], max(merged_seeds[-1][1], current_seed[1]))
    else:
        # If not overlapping, add the current seed to the merged list
        merged_seeds.append(current_seed)

# Print the merged seed ranges
for merged_seed in merged_seeds:
    print(merged_seed)
    
print(len(merged_seeds))