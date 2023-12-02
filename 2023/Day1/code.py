# Advent of Code 2023

def recursive_check_same_character(line, char_to_check, val_to_replace):
    found = line.find(char_to_check)
    if found == -1:
        return line
    else:
        line = line[: found + 1] + str(val_to_replace) + line[found + 2 :]
        return recursive_check_same_character(line, char_to_check, val_to_replace)
    

def replace_characters(line_to_replace, all_chars):
    for char in all_chars:
        line_to_replace = recursive_check_same_character(line_to_replace, char, all_chars[char])
    return line_to_replace
            

def sliding_window_left_and_right(input):
    answer = False
    left = 0
    left_value = None
    right_value = None
    right = len(input) - 1
    while not answer:
        if input[left].isdigit() and left_value is None:
            left_value = input[left]
        if input[right].isdigit() and right_value is None:
            right_value = input[right]
        if right_value and left_value:
            return int(left_value + right_value)
        left += 1
        right -= 1
        
if __name__ == "__main__":
    input_string = open('puzzle.txt')
    # for line in input_string.readlines():
    #     print(sliding_window_left_and_right(line))
    # q 2
    vals = {
            "eight": 8,
            "seven": 7,
            "three": 3,
            "four": 4,
            "five": 5,
            "nine": 9,
            "one": 1,
            "two": 2,
            "six": 6
            }
    ttl_sum = []
    
    for line in input_string.readlines():
        print(line)
        new_line = replace_characters(line, vals)
        print(new_line)
        val = (sliding_window_left_and_right(new_line))
        print(val)
        ttl_sum.append(val)
    print(sum(ttl_sum))