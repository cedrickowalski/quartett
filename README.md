# quartett
This repository is for implementing the game "quartett".

The game quartett can be played by 2 - 8 players.
It has 32 cards with 8 x quartetts (numbers: 7, 8, 9, 10, B, D, K, A, symbols: ♠, ♣, ♥, ♦).
4 cards of a kind (f.e. 7, 7, 7, 7) build a quartett.
If a quartett is build, put it down.,
Cards are randomly distributed:
  2 players: every player gets 10 cards and 12 remaining cards are put on a pile
  3 - 8 players: the cards are evenly split up
Active player asks random player for specific card:
  if positiv 2 players: player hands card to the player who asked and process repeats
  if positiv 3 - 8 players: player hands card to the player who asked and process repeats
  if negative 2 players: player takes card from pile and move ends
  if negativ 3- 8 players: end and next player starts move
The game end if one player has no more cards left.
The winner is the one with the most quartetts.

