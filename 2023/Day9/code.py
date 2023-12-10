
def get_all_differences(number_list):
    index = 0
    all_differences_in_order = []
    while index < len(number_list)- 1:
        all_differences_in_order.append(
            number_list[index + 1] - number_list[index]
        )
        index += 1
    return all_differences_in_order

def is_not_all_zeroes(numbers_list):
    return any(numbers_list)

def predicted_history(histories):
    histories.reverse()
    index = 1
    histories[0].append(0)
    while index < len(histories):
        last_char_current_row = histories[index][-1]
        last_char_last_row = histories[index - 1][-1]
        added_diff = last_char_current_row + last_char_last_row
        histories[index].append(
            added_diff
        )
        index += 1
    return histories

def sol_2_predicted_history(histories):
    index = 1
    histories[0].insert(0,0)
    while index < len(histories):
        first_char_current_row = histories[index][0]
        first_char_last_row = histories[index - 1][0]
        added_diff = first_char_current_row -first_char_last_row 
        histories[index].insert(
            0,
            added_diff
        )
        index += 1
    return histories

class HistoryFactory():

    @staticmethod
    def create(lines):
        ret_list = []
        for line in lines:
            row = []
            for num in line.split(" "):
                if num.strip() == "":
                    break
                row.append(int(num.strip()))
            ret_list.append(row)
        return ret_list
    
    @staticmethod
    def create_history(history_array, past_history = 0):
        history_array = [history_array]
        difference_array = get_all_differences(history_array[0])
        history_array.append(difference_array)
        while is_not_all_zeroes(difference_array):
            difference_array = get_all_differences(history_array[-1])
            history_array.append(difference_array)
        for num in range(past_history):
            history_array.insert(0, predicted_history(history_array))
        return history_array
    @staticmethod
    def create_history_sol_2(history_array, past_history = 0):
        history_array = [history_array]
        difference_array = get_all_differences(history_array[0])
        history_array.append(difference_array)
        while is_not_all_zeroes(difference_array):
            difference_array = get_all_differences(history_array[-1])
            history_array.append(difference_array)
        history_array.reverse()
        for num in range(past_history):
            history_array.insert(0, sol_2_predicted_history(history_array))
        return history_array

def sol1(tow_array_of_histories):
    for histories in tow_array_of_histories:
        all_history = HistoryFactory.create_history(histories, 1)
    sums = 0
    for hist in tow_array_of_histories:
        sums += hist[-1]
    return sums

def sol2(tow_array_of_histories):
    for histories in tow_array_of_histories:
        all_history = HistoryFactory.create_history_sol_2(histories, 1)
    sums = 0
    for hist in tow_array_of_histories:
        sums += hist[0]
    return sums

if __name__ == "__main__":
    file = open('puzzle.txt')
    all_lines = file.readlines()
    twodimensional_history_array = HistoryFactory.create(all_lines)
    print(sol1(twodimensional_history_array))
    print(sol2(twodimensional_history_array))