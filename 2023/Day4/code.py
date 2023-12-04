import copy
from collections import defaultdict
import re

class Card():

    def __init__(self, card):
        self.card_number = self._extract_card_number(card)
        self.winning_numbers = self._extract_numbers(card.split(":")[1].split("|")[0])
        self.picked_numbers = self._extract_numbers(card.split(":")[1].split("|")[1])
        self.won_numbers = self.get_winning_numbers()
        self.score = self.dictate_score()

    def _extract_card_number(self, line):
        return int(line.split(":")[0].split(" ")[-1])

    def _extract_numbers(self, number_string):
        valid_numbers = []
        all_numbers = number_string.split(" ")
        for number in all_numbers:
            if number != " " and number != "":
                valid_numbers.append(int(number.replace("\n","")))
        return valid_numbers

    def get_winning_numbers(self):
        winning = []
        for number in self.picked_numbers:
            if number in self.winning_numbers:
                winning.append(number)
        return winning

    def dictate_score(self):
        counter = 0
        for number in self.won_numbers:
            if counter == 0 :
                counter += 1
            else:
                counter = counter * 2
        return counter

def solution_1(all_lines):
    ttl = 0
    for line in all_lines:
        current_card = Card(line)
        ttl += current_card.score
    return ttl
def solution_2(all_lines):
    d = defaultdict(lambda: 1)
    for i, line in enumerate(all_lines, 1):
        d[i]    # This line is important
        card = line.replace('  ',' ').split(': ')[1]
        ln, yh = card.split(' | ')
        ln = set(map(int, ln.split(' ')))
        yh = set(map(int, yh.split(' ')))
        matches = len(ln.intersection(yh))
        for j in range(i + 1, i + matches + 1):
            d[j] = d[j] + 1 * d[i]
    return sum(d.values())
if __name__ == "__main__":
    file = open('puzzle.txt')
    # print(solution_1(file.readlines()))
    print(solution_2(file.readlines()))