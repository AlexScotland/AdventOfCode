def find_direction(line, index, multiplier):
    if line[index + multiplier].isdigit():
        return find_direction(line, index + multiplier, multiplier)
    else:
        return index

def get_number_from_unknown_location(line, index_to_start):
    left = find_direction(line, index_to_start, -1)
    right = find_direction(line, index_to_start, 1)
    return (line[left:right+1], left, right)
    
def get_all_numbers_touching(file, index_y, index_x):
    all_nums_touching = []
    try:
        # check up
        if file[index_y - 1][index_x].isdigit():
            full_num = get_number_from_unknown_location(file[index_y - 1], index_x)
            if full_num not in all_nums_touching:
                all_nums_touching.append(full_num)
        # check up left
        if file[index_y - 1][index_x - 1].isdigit():
            full_num = get_number_from_unknown_location(file[index_y - 1], index_x - 1)
            if full_num not in all_nums_touching:
                all_nums_touching.append(full_num)
        # check up right
        if file[index_y - 1][index_x + 1].isdigit():
            full_num = get_number_from_unknown_location(file[index_y - 1], index_x + 1)
            if full_num not in all_nums_touching:
                all_nums_touching.append(full_num)
        # check left
        if file[index_y][index_x - 1].isdigit():
            full_num = get_number_from_unknown_location(file[index_y], index_x - 1)
            if full_num not in all_nums_touching:
                all_nums_touching.append(full_num)
        # check right
        if file[index_y][index_x + 1].isdigit():
            full_num = get_number_from_unknown_location(file[index_y], index_x + 1)
            if full_num not in all_nums_touching:
                all_nums_touching.append(full_num)
        # check down left
        if file[index_y + 1][index_x - 1].isdigit():
            full_num = get_number_from_unknown_location(file[index_y + 1], index_x - 1)
            if full_num not in all_nums_touching:
                all_nums_touching.append(full_num)
        # check down
        if file[index_y + 1][index_x].isdigit():
            full_num = get_number_from_unknown_location(file[index_y + 1], index_x)
            if full_num not in all_nums_touching:
                all_nums_touching.append(full_num)
        # check down right
        if file[index_y + 1][index_x + 1].isdigit():
            full_num = get_number_from_unknown_location(file[index_y + 1], index_x + 1)
            if full_num not in all_nums_touching:
                all_nums_touching.append(full_num)
        
    except Exception:
        print("FAILED")
    return all_nums_touching

if __name__ == "__main__":
    total_sum = 0
    sum_array = []
    file = open("puzzle.txt")
    full_file = file.readlines()
    # Puzzle 1
    for line_index in range(len(full_file)):
        line = full_file[line_index]
        for v_index in range(len(line)):
            if not line[v_index].isdigit() and line[v_index] != "\n" and line[v_index] != ".":
                all_nums = get_all_numbers_touching(full_file, line_index, v_index)
                for num in all_nums:
                    total_sum += int(num[0])
    print(total_sum)
    total_sum = 0
    # Puzzle 2
    for line_index in range(len(full_file)):
        line = full_file[line_index]
        for v_index in range(len(line)):
            if not line[v_index].isdigit() and line[v_index] != "\n" and line[v_index] != ".":
                all_nums = get_all_numbers_touching(full_file, line_index, v_index)
                if line[v_index] == "*":
                    if len(all_nums) == 2:
                        total_sum += (int(all_nums[0][0]) * int(all_nums[1][0]))

    print(total_sum)