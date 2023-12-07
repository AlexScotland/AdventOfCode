import math

class Hand():
    
    def __init__(self, card_hand, wager, wild_card = False):
        self.card_hand = card_hand.strip()
        self.wager = wager
        if not wild_card:
            self.card_value = self._get_hand_combo()
        else:
            self.card_value = self._get_hand_combo_wild_card()
        self.highest_card_and_pos = self._highest_card_and_pos()
    
    def _highest_card_and_pos(self):
        values = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
        value_card = '2'
        position_card = len(self.card_hand)
        for index, card in enumerate(self.card_hand):
            if values.index(card) < values.index(value_card):
                value_card = card
                position_card = index + 1
        return value_card, position_card

    def _get_card_occurences(self):
        occurences = {}
        for card in self.card_hand:
            if occurences.get(card):
                occurences[card] += 1
            else:
                occurences[card] = 1
        return occurences
    
    def _get_hand_combo_wild_card(self):
        # Your logic for handling "J" as a wild card goes here
        # Modify this method accordingly
        # For example, you can replace "J" with the highest possible card
        print("Pre adjustment")
        print(self.card_hand)
        print("POST")
        self.card_hand = self.card_hand.replace("J", max(self.card_hand))
        print(self.card_hand)
        return self._get_hand_combo()

    def _get_hand_combo(self):
        rules = {
            'five_of_a_kind': 7,
            'four_of_a_kind': 6,
            'full_house': 5,
            'three_of_a_kind': 4,
            'two_pair': 3,
            'one_pair': 2,
            'high_card': 1
        }
        if self.card_hand == self.card_hand[0]*5:
            return (self.card_hand[0], rules['five_of_a_kind'])
        card_occurences = self._get_card_occurences()
        highest_repeating = max(card_occurences, key=lambda key: card_occurences[key])
        if len(card_occurences) == 2 and \
              card_occurences[highest_repeating] == 3:
            # KKKQQ
            return (highest_repeating, rules['full_house'])
        elif len(card_occurences) == 2:
            # KKKKQ
            return (highest_repeating, rules['four_of_a_kind'])
        elif len(card_occurences) == 3 and card_occurences[highest_repeating] == 3:
            # TTT1Q
            # T55J5
            return (highest_repeating, rules['three_of_a_kind'])
        elif len(card_occurences) == 3:
            # TT22Q
            return (highest_repeating, rules['two_pair'])
        elif len(card_occurences) == 4:
            return (highest_repeating, rules['one_pair'])
        return (None, rules['high_card'])

class HandFactorySol1():

    @staticmethod
    def create_hand(hand):
        hand_and_point = hand.split()
        return Hand(hand_and_point[0], int(hand_and_point[1]))

class HandFactorySol2():

    @staticmethod
    def create_hand(hand):
        hand_and_point = hand.split()
        return Hand(hand_and_point[0], int(hand_and_point[1]), True)

def return_winner(hand1, hand2):
    if hand1.card_value[1] == hand2.card_value[1]:
        ## TIE, USE HIGHEST CARD AT CLOSEST FRONT
        card_compare = {
            'A': 14,
            'K': 13,
            'Q': 12,
            'J': 11,
            'T': 10,
            '9': 9,
            '8': 8,
            '7': 7,
            '6': 6,
            '5': 5,
            '4': 4,
            '3': 3,
            '2': 2
        }
        for index, card_value in enumerate(hand1.card_hand):
            if card_compare[card_value] > card_compare[hand2.card_hand[index]]:
                return True
            elif card_compare[card_value] < card_compare[hand2.card_hand[index]]:
                return False
    elif hand1.card_value[1] > hand2.card_value[1]:
        return True
    return False

def append_to_list_sorted(hand_list, hand_to_compare):
    if not hand_list:
        hand_list.append(hand_to_compare)
        return hand_list

    low, high = 0, len(hand_list) - 1

    while low <= high:
        mid = (low + high) // 2
        comparison_result = return_winner(hand_to_compare, hand_list[mid])

        if comparison_result:
            high = mid - 1
        else:
            low = mid + 1

    hand_list.insert(low, hand_to_compare)
    return hand_list

def calc_sum(list_of_hands):
    ttl = 0
    for index, hand in enumerate(list_of_hands):
        ttl += (hand.wager * (index + 1))
    return ttl


def sol(file, factory):
    all_hands_sorted = []
    for hand in file.readlines():
        all_hands_sorted = append_to_list_sorted(all_hands_sorted, factory.create_hand(hand))
    all_hands_sorted.reverse()
    return calc_sum(all_hands_sorted)


if __name__ == "__main__":
    file = open("puzzle.txt")
    # print(sol(file, HandFactorySol1))
    print(sol(file, HandFactorySol2))
