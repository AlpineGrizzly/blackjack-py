# blackjack-py
Implemetation of the blackjack cardgame in python

## TODO 
- [ ] Allow the player to be able to bet and play until you're broke
- [ ] Dealer is still missing some logic based on how its actually played
- [ ] Make it prettier??
- [ ] Make dealers second card hidden to the player until all players have gone
- [ ] Allow multiple Ai's to play with the player
- [ ] Better terminal display so its not just a stream of text

## To play
```
python3 blackjack.py 

Welcome to blackjack-py
Initializing game...
Your deck is ready sir...
Getting score for dealers hand... 6
Score of dealer is 6


Getting score for players hand... [('K', 'club')]
Score of player is 12


Hit or stand? (hit/stand): 
hit
Player has chosen to hit
Getting score for players hand... [('K', 'club'), ('5', 'heart')]
Score of player is 17


Hit or stand? (hit/stand): 
stand
Player has chosen to stand
Player final score 17
Player hand  [('K', 'club'), ('5', 'heart')]
Dealer hand  [('3', 'club'), ('3', 'heart')]

Dealers turn

Dealer hit::score -> [('3', 'club'), ('3', 'heart'), ('7', 'heart')] = 13
Dealer hit::score -> [('3', 'club'), ('3', 'heart'), ('7', 'heart'), ('8', 'diamond')] = 21
You lost to the dealers hand of 21!
```
