import threading 

class Seed():
    def __init__(self, value) -> None:
        self.original_value = int(value)
        self.adjusted_value = int(value)

class SeedFactory():
    
    @staticmethod
    def create_seeds(seed_line):
        seed_line = seed_line.split(":")[1]
        list_of_seeds = []
        
        for line in seed_line.split(" "):
            if line.strip().isdigit():
                list_of_seeds.append(Seed(int(line)))
        return list_of_seeds
    

    @staticmethod
    def create_seeds_part_2(seed_line, stages):
        seed_line = seed_line.split(":")[1]
        all_seed_values = seed_line.split(" ")
        del all_seed_values[0]
        lowest = None
        for index in range(len(all_seed_values)):
            if index % 2 != 0:
                continue
            seed_start = all_seed_values[index].strip()
            seed_end = all_seed_values[index + 1].strip()
            if seed_start.isdigit() and seed_end.isdigit():
                for seed_val in range(int(seed_start), int(seed_start) + int(seed_end)):
                    adjusted = adjust_seed(Seed(int(seed_val)), stages)
                    if not lowest:
                        lowest = adjusted.adjusted_value
                    elif adjusted.adjusted_value < lowest:
                        lowest = adjusted.adjusted_value

                
        return lowest

class DifferenceCalculator():
    def __init__(self, destination, source, range_val):
        self.source = int(source)
        self.destination = int(destination)
        self.range = int(range_val)
        self.offset = self.destination - self.source
        self.end = (self.source + self.range) - 1

    def in_offset(self, value):
        return self.source <= value <= self.end

    def adjust(self, value):
        return value + self.offset

def extract_map(lines, index):
    vals = []
    for line in lines[index+1:]:
        if line == "\n" or line == " ":
            break
        all_vals =  line.split(" ")
        appender = []
        for val in all_vals:
            appender.append(val.replace("\n",""))
        vals.append(appender)
    return vals

def set_up(lines):
    all_seeds = SeedFactory.create_seeds(lines[0])
    stages = {}
    for index, line in enumerate(lines):
        if "map" in line:
            key = lines[index].replace("\n", "")
            stages[key] = []
            for val in extract_map(lines, index):
                stages[key].append(DifferenceCalculator(val[0], val[1], val[2]))
    return all_seeds, stages

def set_up_part_2(lines):
    stages = {}
    for index, line in enumerate(lines):
        if "map" in line:
            key = lines[index].replace("\n", "")
            stages[key] = []
            for val in extract_map(lines, index):
                stages[key].append(DifferenceCalculator(val[0], val[1], val[2]))
    return SeedFactory.create_seeds_part_2(lines[0], stages)

def adjust_all_seeds(all_seeds, stages):
    for seed in all_seeds:
        for stage in stages:
            seed_changed = False
            for difference_cal in stages[stage]:
                if difference_cal.in_offset(seed.adjusted_value):
                    seed_changed = True
                    seed.adjusted_value = (seed.adjusted_value - difference_cal.source) + difference_cal.destination
                if seed_changed:
                    break
    return all_seeds

def adjust_seed(seed, stages):
    for stage in stages:
        seed_changed = False
        for difference_cal in stages[stage]:
            if difference_cal.in_offset(seed.adjusted_value):
                seed_changed = True
                seed.adjusted_value = (seed.adjusted_value - difference_cal.source) + difference_cal.destination
            if seed_changed:
                break
    return seed

def solution_1(lines):
    all_seeds, stages = set_up(lines)
    # (num (if in range) - Source) + destination
    all_seeds = adjust_all_seeds(all_seeds, stages)
    return min(seed.adjusted_value for seed in all_seeds)

def solution_2(lines):
    return set_up_part_2(lines)

if __name__ == "__main__":
    file = open('puzzle.txt')
    # print(solution_1(file.readlines()))
    print(solution_2(file.readlines()))