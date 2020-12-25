"""This programm implements the game Quartett.

- played by 2 - 8 players
- 32 cards with 8 x Quartetts
- if 2 players: every player gets 10 cards and up side down pile with 12 cards
- if 3+ players: the cards are evenly split up
- one player starts and it goes clockwise
- asks random player for specific card
- if he has the card he gives it to the questioner and process repeats
- if he has not the card:
    - 2 players: pick up card from pile and next players turn
    - 3 + players: next players turn
- end: if one player has no cards left
- winner: person with the most quartetts
"""

__author__ = "6628790, Kowalski"
__credits__ = ""
__email__ = "s9781862@stud.uni-frankfurt.de"


import rules
import players



def quartett():
    """Docstring: This Programm does ...

    parameter:
    output:
    """
    
    pass


def main():
    """This function implements the whole game.

    """
    print("\n", 15 * "-", "Quartett",  15 * "-", "\n")
    rules()
    players()
    

if __name__ == "__main__":
    main()


