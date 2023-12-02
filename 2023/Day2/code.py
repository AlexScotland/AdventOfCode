
class GameRound():
    def __init__(self, game_string):
        self.id = self.get_id(game_string)
        self.games = self._get_game_strings(game_string)
        self.is_game_playable = self.determine_game()
        self.lowest_power = self.determine_lowest_count_of_cubes()
    
    def get_id(self, game_string):
        return int(game_string.split(":")[0].split(" ")[1])

    def _get_game_strings(self, game_string):
        return game_string.split(":")[1].split(";")
    
    def determine_lowest_count_of_cubes(self):
        lowest_count = {
                'red': None,
                'green': None,
                'blue': None
            }
        for full_game in self.games:
            rounds_translated = full_game.replace(",", '').replace("\n", '')
            rounds = rounds_translated.split(' ')
            for color in lowest_count:
                try:
                    round_index = rounds.index(color)
                except ValueError:
                    continue
                else:
                    value = int(rounds[round_index - 1])
                    if lowest_count[color] is None or value > lowest_count[color]:
                        lowest_count[color] = value
        power_for_round = lowest_count['red'] * lowest_count['blue'] * lowest_count['green']
        return power_for_round

    def determine_game(self):
        rules = {
            'red': 12,
            'green': 13,
            'blue': 14,
        }
        for full_game in self.games:
            rounds_translated = full_game.replace(",",'').replace("\n",'')
            rounds = rounds_translated.split(' ')
            for rule in rules:
                # print(rule)
                try:
                    round_index = rounds.index(rule)
                except ValueError:
                    continue
                else:
                    value = rounds[round_index - 1]
                    if int(value) > rules[rule]:
                        # print(f"violation on id {self.id} on color {rule} - {value} > {rules[rule]}")
                        return False
                    pass
        return True
        
        
if __name__ == "__main__":
    file = open("puzzle.txt")
    total_sum = 0 
    total_sum_power = 0
    for line in file.readlines():
        game = GameRound(line)
        total_sum_power += game.lowest_power
        if game.is_game_playable:
            # print(game.id)
            total_sum += game.id
    # Q1
    print(total_sum)
    # Q2
    print(total_sum_power)
        