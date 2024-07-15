"""
blackjack.py

implementation of the cardgame blackjack in python

@author Dalton Kinney
@date July 11th, 2024

blackjack resource https://bicyclecards.com/how-to-play/blackjack
"""

# Card type declarations
suits = ["spade", "heart", "diamond", "club"]
faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

def create_deck():
    """ Creates 52 card deck """
    deck = []
    for suit in suits:
        for face in faces:
            deck.append((face, suit))
    return deck

class Player:
    """ Instance of a player in the game, aka you """
    def __init__(self, moolah):
        self.money = moolah # Initial money amount to bet
        self.score = 0 # Initial score amount based on sum of all cards currently held
        self.hand = "" # String to represent all cards currently held by a player
    def bet(self):
        """ Declare amount bet on a round """
        pass
    def hit(self):
        """ Be dealt a card """ 
        pass
    def stand(self):
        """ Stand on a deal """
        pass

class Game:
    """ Game instance that will control all aspects an instance of a game taking place """
    def __init__(self):
        """ Instantiate game variables """
        self.deck = create_deck()
        self.num_players = 1 # hardcoded for now

    def shuffle(self):
        """ Shuffles the card deck and returns string of shuffled deck """

    def deal(self):
        """ Deals cards to all players including the dealer """
        pass
    def draw_dealer(self):
        """ Draw the dealer in the terminal (sounds coool) """
        pass

def main():
    print("Welcome to blackjack-py")

    # Initialize game and shuffle deck with random order
    print("initializing game...")
    game = Game()

    print("Your deck is ready sir...")
    for card in game.deck:
        print(card)

    # Game Loop
    #while True:
        # draw cards for the dealer and the player

        # allow player to decide to hit or pass 

if __name__ == "__main__":
    main()
