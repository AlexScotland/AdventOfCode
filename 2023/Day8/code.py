class Position():
    
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

class PositionFactory():
    
    @staticmethod
    def create(line):
        line_broken = line.split("=")
        path_name = line_broken[0].strip()
        next_paths = line_broken[1].replace("(","").replace(")","").split(",")
        return Position(path_name, next_paths[0].strip(), next_paths[1].strip())

class RLNavigatorStrategy():
    
    def __init__(self):
        self.start = "AAA"
        self.end = "ZZZ"
    
    def __find_index_for_position(self, position_name, positions):
        for index, position in enumerate(positions):
            if position_name == position.name:
                return index

    def navigate(self, instructions, positions):
        instruction_index = 0
        position_index = self.__find_index_for_position(self.start, positions)
        steps = 0
        MAX = 19185263738118
        while steps < MAX:
            if instruction_index == len(instructions):
                instruction_index = 0
            current_position = positions[position_index]
            next_step = instructions[instruction_index]
            if current_position.name == self.end:
                return steps
            if next_step == "L":
                next_position_name = current_position.left
            else:
                next_position_name = current_position.right
            position_index = self.__find_index_for_position(next_position_name, positions)
            instruction_index += 1
            steps += 1

class SimultaneousRLNavigatorStrategy():
    
    def __init__(self):
        self.start = "A"
        self.end = "Z"
        self.position_dict = {}
    
    def _setup_dict(self, positions):
        for position in positions:
            if self.position_dict.get(position.name[-1], None):
                self.position_dict[position.name[-1]].append(position)
            else:
                self.position_dict[position.name[-1]] = [position]
    
    def _all_are_z(self, positions):
        return all(pos.name.endswith('Z') for pos in positions)

    def _find_position_in_dict(self, next_pos):
        for pos in self.position_dict[next_pos[-1]]:
            if pos.name == next_pos:
                return pos

    def _move_all_positions(self, positions, current_instruction):
        return [self._find_position_in_dict(position.left if current_instruction == "L" else position.right) for position in positions]
        # ret_list_of_pos = []
        # for position in positions:
        #     if current_instruction == "L":
        #         next_pos = position.left
        #     else:
        #         next_pos = position.right
        #     ret_list_of_pos.append(self._find_position_in_dict(next_pos))
        
        # return ret_list_of_pos

    def navigate(self, instructions, positions):
        self._setup_dict(positions)
        current_positions = self.position_dict['A']
        instruction_index = 0
        steps = 0
        MAX = 19185263738118
        while not self._all_are_z(current_positions):
            if steps > MAX:
                print("SOMETHING IS WRONG")
                break
            if instruction_index == len(instructions):
                instruction_index = 0
            current_instruction = instructions[instruction_index]
            current_positions = self._move_all_positions(current_positions, current_instruction)
            instruction_index += 1
            steps += 1
        return steps


def sol1(instructions, positions):
    return RLNavigatorStrategy().navigate(instructions, positions)

def sol2(instructions, positions):
    return SimultaneousRLNavigatorStrategy().navigate(instructions, positions)

if __name__ == "__main__":
    file = open('puzzle.txt')
    all_lines = file.readlines()
    l_r_instructions = all_lines[0]
    positions = []
    for line in all_lines[2:]:
        positions.append(PositionFactory.create(line.strip()))
    
    print(sol2(l_r_instructions.strip(), positions))