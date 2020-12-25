"""This function creates player profiles.

output: a list with all players
"""

__author__ = "6628790, Kowalski"
__credits__ = ""
__email__ = "s9781862@stud.uni-frankfurt.de"




def players():
    """This function creates player profiles.

    parameter: /
    output: a list with tuples including name and gamertype (computer, human)
    """
    
    players_list = []
    counter = 0
    asker = True

    while asker:

        counter += 1
        print("\n", 10 * "-", "player", counter, 10 * "-", "\n")
        
        # ask for players name 
        player_name = input("Players name: ")

        # ask for players type
        player_type = input("\nPlayed by: [0] Computer or [1] human: ")
        while player_type not in ("0", "1"):
            player_type = input("\nPlayed by: [0] Computer or [1] human: ")

        if player_type == "1":
            player_type = "Human"
        elif player_type == "0":
            player_type = "Computer"

        # create players tuple and add it to players_list
        player_tuple = (player_name, player_type)
        players_list.append(player_tuple)
        
        # starting game is possible between 2 and 8 players
        if counter == 1:
            asker = True
        elif counter > 1 and counter < 8:
            asker = input("\nAnother player: [1] yes, [0] no: ")
            while asker not in ("0", "1"):
                asker = input("\nAnother player: [1] yes, [0] no: ")
            if asker == "1":
                asker = True
            elif asker == "0":
                asker = False 
        elif counter == 8:
            asker = False

    return players_list



