def rock_paper_scissors(player_1, player_2):
    player_1_letters = []
    player_2_letters = []
    for letters in player_1:
        player_1_letters.append(letters)
    for letters in player_2:
        player_2_letters.append(letters)

    if player_1_letters[0] == player_2_letters[0]:
        print("It's a tie.")
    elif player_1_letters[0] == "r" and player_2_letters[0] == "p":
        print("Player 2 wins.")
    elif player_1_letters[0] == "r" and player_2_letters[0] == "s":
        print("Player 1 wins.")
    elif player_1_letters[0] == "p" and player_2_letters[0] == "r":
        print("Player 1 wins.")
    elif player_1_letters[0] == "p" and player_2_letters[0] == "s":
        print("Player 2 wins.")
    elif player_1_letters[0] == "s" and player_2_letters[0] == "r":
        print("Player_2 wins.")
    elif player_1_letters[0] == "s" and player_2_letters[0] == "p":
        print("Player 1 wins.")


user_input = input("type 'start' or 'quit\n")
user_input.lower()

while user_input == "start":
        plays = input("Enter player 1 then player 2.\n")
        player_1_and_2 = plays.split()
        player_1 = player_1_and_2[0]
        player_2 = player_1_and_2[1]
        rock_paper_scissors(player_1, player_2)
