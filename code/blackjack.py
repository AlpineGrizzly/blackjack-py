"""
blackjack.py

implementation of the cardgame blackjack in python

@author Dalton Kinney
@date July 11th, 2024

blackjack resource https://bicyclecards.com/how-to-play/blackjack
"""
import random
import sys

# Card type declarations
# suits = ["spade", "heart", "diamond", "club"]
# faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
# 
# def create_deck():
#     """ Creates 52 card deck """
#     deck = []
#     for suit in suits:
#         for face in faces:
#             deck.append((face, suit))
#     return deck

class Player:
    """ Instance of a player in the game, aka you """
    def __init__(self, moolah):
        self.money = moolah # Initial money amount to bet
        self.hand = [] # Hand of cards held by player will be array of string tuples of suit and face
    
    def get_score(self):
        """ Returns current score of players hand """
        return get_hand_score(self.hand)

    def bet(self):
        """ Declare amount bet on a round """
        pass

class Game:
    """ Game instance that will control all aspects an instance of a game taking place """
    def __init__(self):
        """ Instantiate game variables """
        self.deck = self.shuffle()
        self.num_players = 1  # hardcoded for now; will add support for more players later
        #self.draw_count = 0   # indicates how many cards have been drawn so far
        self.shuffle()        # init with shuffled deck

    def shuffle(self):
        """ Shuffles the card deck and returns string of shuffled deck """
        # Card type declarations
        suits = ["spade", "heart", "diamond", "club"]
        faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

        deck = [] # Creates 52 card deck
        
        for suit in suits:
            for face in faces:
                deck.append((face, suit))

        random.shuffle(deck) 
        return deck

    def deal(self, player):
        """ Deal card to a player """
        card2deal = self.deck.pop()
        player.hand.append(card2deal)

    def draw_dealer_idle(self):
        """ TODO Draw the dealer in the terminal when idle (sounds coool) """
        pass

    def draw_dealer_deal(self):
        """ TODO Draw the dealer in the terminal when dealing card (sounds coool) """
        pass

def get_hand_score(hand):
    """ Given a hand, determine the number score """
    """ TODO will need to account for an A being a 1 or 11 """
    score = 0
    naces = 0 # Number of aces held by player
    for card in hand:
        face, _ = card
        match face: 
            case "A":
               naces += 1
            case "K":
                score += 12
            case "Q":
                score += 11 
            case "J":
                score += 10
            case _: 
                score += int(face)
    
    for i in range(0, naces):
        if score + 11 > 21:
            score += 1
        else:
            score += 11

    return score
    
def main():
    print("Welcome to blackjack-py")

    # Initialize game and shuffle deck with random order
    print("Initializing game...")
    game = Game()
    player1 = Player(500)
    dealer = Player(1000)

    print("Your deck is ready sir...")
   
    # Main game loop 
    while True: # will change to check for 0 amount on bettable money by player
        # Deal card to dealer, player, and second to dealer 
        game.deal(dealer)
        game.deal(player1)
        game.deal(dealer) 

        # Get score of hand from dealer and player and ask player if they would like to hit or stand
        print("Getting score for dealers hand...", get_hand_score(dealer.hand))     
        print("Score of dealer is %d\n\n" % get_hand_score(dealer.hand))

        while player1.get_score() <= 21:
            # Get players score and query to hit or stand 
            print("Getting score for players hand...", player1.hand)     
            print("Score of player is %d\n\n" % get_hand_score(player1.hand))
            print("Hit or stand? (hit/stand): ")
            decision = input()
            match decision:
                case "hit":
                    print("Player has chosen to %s" % decision)
                    game.deal(player1) # deal another card
                case "stand":
                    print("Player has chosen to %s" % decision)
                    break

        print("Player final score %d" % player1.get_score())
        print("Player hand ", player1.hand)
        print("Dealer hand ", dealer.hand)
        if player1.get_score() > 21:
            print("You busted!")
            break

        # TODO dealer loop where they will hit until they have at least 17 
        print("\nDealers turn\n")
        while dealer.get_score() < 17:
            game.deal(dealer)
            print("Dealer hit::score -> %s = %d" % (dealer.hand, dealer.get_score()))
        print("Dealer final score %d\n" % dealer.get_score())
        if dealer.get_score() > 21: 
            if player1.get_score() == 21:
                print("3 to 2 paid on dealers bust!")
            else:
                print("dealer busted! all hands returned!")
        elif dealer.get_score() > player1.get_score():
            print("You lost to the dealers hand of %d!" % dealer.get_score())
        elif dealer.get_score() == player1.get_score():
            print("Draw!")
        else:
            print("You won!")
        
        break
            

if __name__ == "__main__":
    main()
