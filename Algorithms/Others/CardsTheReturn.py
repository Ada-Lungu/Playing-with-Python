class Card():
    suit_list = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_list = ["Ace", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return str(self.rank_list[self.rank]) + " of " + str(self.suit_list[self.suit])

    def __cmp__(self, other):
        if self.suit > other.suit:
            return 1
        if self.suit < other.suit:
            return -1
        if self.rank > other.rank:
            return 1
        if self.rank < other.rank:
            return -1
        else:
            return 0


class Deck():
    def __init__(self):
        self.cards = []
        for suit in range(len(Card.suit_list)):
            for rank in range(len(Card.rank_list)):
                self.cards.append(Card(suit, rank))
    #==> self.deck = [(0,1), (0,2) ....]

    def print_cards(self):
        for card in self.cards:
            print card

    def __str__(self):
        s = ""
        for card in range(len(self.cards)):
            s = s + str(self.cards[card]) + "\n"
        return s

    def shuffle_cards(self):
        import random
        for i in range(len(self.cards)):
            j = random.randrange(i, len(self.cards)) #their way
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

     # returns True if succeesfull False otherwise

    def remove_card(self, card):
        if card in self.cards: # de ce aici nu folosim self.card, ci card???
            self.cards.remove(card)
            return card
        else:
            return False

    # pops if deck not empty. prints errr otherwise
    def remove_top_card(self):          # or: return self.deck.pop()
        if len(self.cards) != 0:
            # to remove the top card => remove the last element from the cards list - we use "pop" method, does just that
            return self.cards.pop()
        else:
            print "No more cards in the deck!"

    def is_empty(self):
        return (len(self.cards) == 0)


# Cass Hand keeps the cards in hand for each player
class Player():

    def __init__(self, player_name, score = 0):
        self.player_name = player_name
        self.cards = []
        self.score = score

    # since for a hand we start with an empty array of cards
    # we want to be able to add cards to the hand one by one
    # thus,
    def add_card(self, card):
        self.cards.append(card)

    def has_no_cards(self):
        return (len(self.cards) == 0)

    # str returns a string representing the object
    def __str__(self):
        s = "Hand of " + self.player_name + " is\n"
        if self.has_no_cards():
            return s + "empty \n"
        else:
            for card in self.cards:
                s += card.__str__() + "\n"
        return s

    def remove_top_card(self):          # or: return self.deck.pop()
        if len(self.cards) != 0:
            return self.cards.pop()
        else:
            print "No more cards in the deck!"

    #obj.print() -> are nevoie de existentza metodei ... print()
    #print obj -> are nevoie de existentza metodei __str__


class Game():
    def __init__(self, list_players, nr_cards):
        self.list_players = list_players
        self.nr_cards_in_hand = nr_cards
        self.deck = Deck()
        self.deck.shuffle_cards()

    def deal(self):

        for i in range(self.nr_cards_in_hand):
            for each_player in self.list_players:
                upper_card = self.deck.remove_top_card()
                each_player.add_card(upper_card)


class SimpleGame(Game):
        # constructor assumes list of players has only two players
        def __init__(self, list_players, nr_cards):
            self.p1 = list_players[0]
            self.p2 = list_players[1]
            self.list_players = list_players
            self.nr_cards_in_hand = nr_cards
            self.deck = Deck()
            self.deck.shuffle_cards()

        def play(self):
            for i in range(self.nr_cards_in_hand):
                top_card_p1 = self.p1.remove_top_card()
                top_card_p2 = self.p2.remove_top_card()
                if top_card_p1 > top_card_p2:
                    print self.p1.player_name + " 's " + str(top_card_p1) + " > " + self.p2.player_name + " 's " + str(top_card_p2)
                    self.p1.score +=10
                    print "Player " + str(self.p1.player_name) + " won " + str(self.p1.score) + " points\n"
                elif top_card_p1 < top_card_p2:
                    print self.p1.player_name + " 's " + str(top_card_p1) + " < " + self.p2.player_name + " 's " + str(top_card_p2)
                    self.p2.score +=10
                    print "Player " + str(self.p2.player_name) + " won " + str(self.p1.score) + " points\n"
                else:
                    print self.p1.player_name + " 's " + str(top_card_p1) + " = " + self.p2.player_name + " 's " + str(top_card_p2)
                    print "Egalitate!\n"

            if self.p1.score > self.p2.score:
                print "\nThe BIG winner is " + self.p1.player_name + " with " + str(self.p1.score) + " points!"
            elif self.p1.score < self.p2.score:
                print "\nThe BIG winner is " + self.p2.player_name + " with " + str(self.p2.score) + " points!"
            else:
                print "\nYou are equal;)"


player1 = Player("Gigi")
player2 = Player("Lutzi")
players_list = [player1, player2]


game1 = SimpleGame(players_list, 12)
game1.deal()
print player1
print player2
game1.play()


