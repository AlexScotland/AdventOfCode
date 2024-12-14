
def parse_input(input_string):
    parsed = input_string.split("\n")
    array_1, array_2 = [], []
    for num_line in parsed:
        sol = num_line.split("   ")
        array_1.append(int(sol[0]))
        array_2.append(int(sol[1]))
    return sorted(array_1), sorted(array_2)
class Solution1():

    def __init__(self):
        from input_1 import INPUT as input
        self.solution = self.solve(input)
    
    def solve(self, input):
        array_1, array_2 = parse_input(input)
        diff_sum = 0
        for index in range(len(array_1)):
            diff = array_1[index] - array_2[index]
            if diff < 0:
                diff = diff * -1
            diff_sum += diff
        return diff_sum


if __name__ == "__main__":
    print(Solution1().solution)
