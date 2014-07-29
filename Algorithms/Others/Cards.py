class Card():
    suit_list = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_list = ["zero", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

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
        self.deck = []
        for suit in range(len(Card.suit_list)):
            for rank in range(len(Card.rank_list)):
                self.deck.append(Card(suit, rank))

#==> self.deck = [(0,1), (0,2) ....]

    def print_deck(self):
        for card in self.deck:
            print card

# or:

    def __str__(self):
        s = ""
        for card in range(len(self.deck)):
            s = s + str(self.deck[card]) + "\n"
        return s

    def shuffle_deck(self):
        import random

        for i in range(len(self.deck)):
            j = random.randrange(i, len(self.deck)) #their way
            self.deck[i], self.deck[j] = self.deck[j], self.deck[i]

    # returns True if succeesfull False otherwise

    def remove_card(self, card):
        if card in self.deck: # de ce aici nu folosim self.card, ci card???
            self.deck.remove(card)
            return card
        else:
            return False

            # to remove the top card => remove the last element from the deck list - we use "pop" method, does just that

    # pops if deck not empty. prints errr otherwise

    def remove_top_card(self):          # or: return self.deck.pop()
        if len(self.deck) != 0:
            return self.deck.pop()
        else:
            print "No more cards in the deck!"

    def is_empty(self):
        return (len(self.deck) == 0)


c1 = Card(0, 2)
c2 = Card(0, 6)
print c1

# if we modify a class attribute, it affects avery instance of the class

c1.suit_list[0] = "Jon Huaan"
print c2    # ==> it will be 6 of Jon Huaan !!! it is not usually a good thing to modify class atributes!
Card.suit_list[0] = "Clubs"

ada_deck = Deck()
mircea_deck = Deck()

ada_deck.shuffle_deck()
mircea_deck.shuffle_deck()

print ada_deck
mircea_deck.print_deck()

print "\n The Game!!!"

score_ada = 0
score_mircea = 0
for i in range(10):
    top_card_ada = ada_deck.remove_top_card()
    print "Round" + str(i) + "\n" +  "  Ada's:" + str(top_card_ada)
    top_card_mircea = mircea_deck.remove_top_card()
    print "  Mircea's:" + str(top_card_mircea)

    if top_card_ada > top_card_mircea:
        score_ada += 10
    else:
        score_mircea += 10

if score_ada == score_mircea:
    print "Egalitate, fraternitate!;)"
elif score_ada > score_mircea:
    print "Ada is the winner with %d points!" % score_ada
else:
    print "Mircea is the winner with %d points!" % score_mircea







