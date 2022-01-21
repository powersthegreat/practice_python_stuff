import random

def maze_logic():
    directions = ["right", "left", "straight"]
    print("""
    You have now entered a dark maze. To get out
    you must choose three correct directional
    paths. After each incorrect choice, the game
    will restart.\n
    """)

    user_input = input("""
    Choose either right, left, or straight
    for your first direction.\n
    """)
    random_int_1 = random.randint(0,2)
    random_int_2 = random.randint(0,2)
    random_int_3 = random.randint(0,2)

    if user_input == directions[random_int_1]:
        user_input_2 = input("""
        Correct, now choose your next direction.\n
        """)
    
        if user_input_2 == directions[random_int_2]:
            user_input_3 = input("""
            Correct, now choose your next direction.\n
            """)
            
            if user_input_3 == directions[random_int_3]:
                print("""
                Correct, you have now completed the maze.\n
                """)

            else:
                print("""
                Incorrect, the game will restart now.\n
                """)

        else:
            print("""
            Incorrect, the game will restart now.\n
            """)
            pass

    else:
        print("""
        Incorrect, the game will restart now.\n
        """)
        pass

intro_input = input("""
Would you like to place the maze game? Enter 'yes' or 'no'.\n
""")

while intro_input == 'yes':
    maze_logic()
    intro_input = input("""
    Would you like to play again? Enter 'yes' or 'no'.\n
    """)


