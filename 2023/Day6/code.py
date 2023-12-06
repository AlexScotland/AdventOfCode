import re

class Race():
    def __init__(self, time, distance):
        self.time = int(time)
        self.distance = int(distance)

def calc_better_races(race):
    s = []
    for i in range(0,race.time + 1):
        pot_dist = (race.time - i) * i
        if pot_dist > race.distance:
            s.append(pot_dist)
    return len(s)

def get_all_better_times(all_best_times):
    dick = {}
    for index, race in enumerate(all_best_times):
        dick[index] = calc_better_races(race)
    return dick

def parse_puzzle_into_races(lines):
    array = []
    time =  re.findall(r'\d+', lines[0].strip())
    distance = re.findall(r'\d+', lines[1].strip())
    for i in range(len(time)):
        array.append(Race(time[i], distance[i]))
    return array

def parse_puzzle_into_race(lines):
    time =  ''.join(re.findall(r'\d+', lines[0].strip()))
    distance = ''.join(re.findall(r'\d+', lines[1].strip()))
    array = [Race(time, distance)]
    return array

def sol1(file):
    all_best_times = parse_puzzle_into_races(file.readlines())
    all_better_times = get_all_better_times(all_best_times)
    val = 1
    for x in all_better_times.values():
        val = val * x 
    return val

def sol2(file):
    all_best_times = parse_puzzle_into_race(file.readlines())
    all_better_times = get_all_better_times(all_best_times)
    val = 1
    for x in all_better_times.values():
        val = val * x 
    return val

if __name__ == "__main__":
    file = open("puzzle.txt")
    # print(sol1(file))
    print(sol2(file))
