# Programming Exercise 
# Implement a class to represent a playing card
# Implement a class to represent a deck of cards
# Use those two classes to represent 

import random


class Card:
    def __init__(self, value: int, suit: str):
        self.value = value
        self.suit = suit

        if suit == 'Diamonds' or suit == 'Hearts':
            self.color = 'red'

        if suit == 'Spades' or suit == 'Clubs':
            self.color = 'black'

    def __repr__(self) -> str:
        return f"{self.value} of {self.suit}"

    def __str__(self) -> str:
        return f"{self.value} of {self.suit}"

    def show_card(self) -> str:
        return f"{self.value} of {self.suit}"

    def get_value(self):
        return self.value


class Deck:
    def __init__(self):
        self.deck = []
        self.build()
        self.shuffle()

    def build(self):
        for suit in ['Spades', 'Clubs', 'Diamonds', 'Hearts']:
            for value in range(1,14):
                self.deck.append(Card(value, suit))

    # try implementing repr after you finish the game play

    def show_deck(self):
        for card in self.deck:
            print(card)

    def shuffle(self):
        return random.shuffle(self.deck)

    def size(self):
        return len(self.deck)

    def supply_card(self):
        return self.deck.pop()

    def in_deck(self, card):
        if card in self.deck:
            return True
        return False


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.table =[]


    def draw(self, deck, num=1):
        for _ in range(1,(num + 1)):
            self.hand.append(deck.supply_card())


    def show_hand(self):
        return self.hand


    def in_hand(self, check_card):
        for card in self.hand:
            if card.show_card() == check_card:
                return True
        return False


    def discard(self, discard_card = None):
        if discard_card == None:
            i = random.randint(1, len(self.hand))
            self.hand.pop(i)
        else: 
            for i, card in enumerate(self.hand):
                if card.show_card() == discard_card:
                    self.hand.pop(i)

    def hand_size(self):
        return len(self.hand)

  
# d = Deck()
# p1 = Player('laura')
# p1.pick_card()


def play_GoFish(player_1:str, player_2:str):
    # start a new deck
    deck = Deck()
    # initialize two players with given names
    p1 = Player(player_1)
    p2 = Player(player_2)
    turn = p1

    p1.draw(deck, 7)
    p2.draw(deck, 7)

    while deck.size() != 0:
        if turn == p1:
            chosen_card = pick_card(p1)
            value = chosen_card.get_value()
            for card in p2.hand:
                if is_valid(card, value):
                    place_on_table_for(p1, chosen_card, card, )
                    p1.discard(chosen_card)
                    p2.discard(card)
            else:
                p1.draw(deck)

     
            turn = p2

        else: 
            chosen_card = pick_card(p2)
            value = chosen_card.get_value()
            for card in p1.hand:
                if is_valid(card, value):
                    place_on_table_for(p2, chosen_card, card, )
                    p2.discard(chosen_card)
                    p1.discard(card)
            else:
                p2.draw(deck)

            turn = p1

    print(p1.table, '\n\n')
    print(p2.table, '\n\n')
    if len(p1.table) > len(p2.table):
        return f'Laura won with {len(p1.table)}, drew lost with {len(p2.table)}'

    if len(p2.table) > len(p1.table):
        return f'Drew won {len(p2.table)}, but still sucks. Laura was close with {len(p1.table)}'

    if len(p2.table) == len(p1.table):
        return 'Woah! Tie'


def pick_card(lead_player):
    if lead_player.hand_size() == 0:
        return 'empty hand'
    else:
        random_card = random.randint(1, len(lead_player.hand)-1)
        return lead_player.hand[random_card]


def place_on_table_for(lead_player, chosen_card, card):
    return lead_player.table.append((chosen_card, card))


def is_valid(card, value):
    return card.get_value() == value







print(play_GoFish('laura', 'drew'))




        




    

            

