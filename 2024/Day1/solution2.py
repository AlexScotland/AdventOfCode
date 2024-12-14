from solution1 import parse_input

class Solution2():
    def __init__(self):
        from input_1 import INPUT as input
        self.solution = self.solve(input)

    def solve(self, input):
        array_1, array_2 = parse_input(input)
        data_seen = {}
        summed_numbers = 0
        for number in array_1:
            if number not in data_seen:
                data_seen[number] = array_2.count(number)
            summed_numbers += number * data_seen[number]
        return summed_numbers


if __name__ == "__main__":
    print(Solution2().solution)