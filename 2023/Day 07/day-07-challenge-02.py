import enum
from typing import List, Optional

int_mapping = {
    "J": 0x1,
    "2": 0x2,
    "3": 0x3,
    "4": 0x4,
    "5": 0x5,
    "6": 0x6,
    "7": 0x7,
    "8": 0x8,
    "9": 0x9,
    "T": 0xA,
    "Q": 0xC,
    "K": 0xD,
    "A": 0xE,
}
str_mapping = {
    0x1: "J",
    0x2: "2",
    0x3: "3",
    0x4: "4",
    0x5: "5",
    0x6: "6",
    0x7: "7",
    0x8: "8",
    0x9: "9",
    0xA: "T",
    0xC: "Q",
    0xD: "K",
    0xE: "A",
}


class HandType(enum.IntEnum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_A_KIND = 5
    FIVE_OF_A_KIND = 6


class Hand:
    @staticmethod
    def compute_type(cards: List[int]):
        types = {}

        for card in cards:
            if not types.get(card):
                types[card] = 1
            else:
                types[card] += 1

        if 1 in cards and len(types) > 1:
            jokers = types.pop(1)
            
            for card, count in types.items():
                if count == len(cards) - jokers:
                    types[card] += jokers
                elif len(cards) == len(types) + jokers:
                    types[max(types.keys())] += jokers
                    break
                elif count > len(types) - count:
                    types[card] += jokers
                    break
                elif count < len(types) - count:
                    continue

        if len(types) == 1:
            return HandType.FIVE_OF_A_KIND
        elif len(types) == 2:
            if 4 in types.values() and 1 in types.values():
                return HandType.FOUR_OF_A_KIND
            else:
                return HandType.FULL_HOUSE
        elif len(types) == 3:
            if 3 in types.values():
                return HandType.THREE_OF_A_KIND
            else:
                return HandType.TWO_PAIR
        elif len(types) == 4:
            return HandType.ONE_PAIR
        elif len(types) == 5:
            return HandType.HIGH_CARD
        else:
            raise ValueError(f"Unknown hand type, {cards}")

    def __init__(self, cards: List[int], bid: int):
        self.cards = cards

        self.type = Hand.compute_type(self.cards)

        self.bid = bid

    def __lt__(self, other) -> bool:
        if self.type < other.type:
            return True
        elif self.type == other.type:
            for i in range(min(len(self.cards), len(other.cards))):
                if self.cards[i] < other.cards[i]:
                    return True
                elif self.cards[i] == other.cards[i]:
                    continue
                elif self.cards[i] > other.cards[i]:
                    return False
        elif self.type > other.type:
            return False

    def __repr__(self) -> str:
        return f"{self.cards}, {self.type.name} {self.bid}"


with open("day-07-input.txt", "r") as infile:
    input = infile.readlines()

hands = []

for line in input:
    hand_str, bid = line.strip().split()

    cards = [int_mapping[card] for card in hand_str]
    hand = Hand(cards, int(bid))

    hands.append(hand)

hands.sort()

winnings = 0

for i in range(len(hands)):
    winnings += hands[i].bid * (i + 1)

print(f"Challenge 02: {winnings}")
