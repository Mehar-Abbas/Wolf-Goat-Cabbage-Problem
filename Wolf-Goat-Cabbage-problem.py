
# Algorithm:
# 1 move goat
# 2 move wolf or move cabbage
# 3 move goat back
# 4 move wolf or move cabbage
# 5 move goat

def main():
    print('\n--------------------- Wolf - Goat - Cabbage Problem ------------------------------------\n')
    play = 'y'
    while play == 'y' or play == 'Y':
        move1 = input(
            'INSTRUCTIONS: Enter g for goat, c for cabbage, w for wolf\n\nThis problem gets solved in 5 moves.\nEnter '
            'who to move first? : ')

        if move1 == 'g':
            move2 = input('Enter your second move: ')

            if move2 == 'c' or move2 == 'w':
                move3 = input('Enter your third move: ')

                if move3 == 'g':
                    move4 = input('Enter your fourth move: ')

                    if (move4 == 'w' or move4 == 'c') and (move2 != move4):
                        move5 = input('Enter your fifth move: ')

                        if move5 == 'g':
                            print('Congratulations!!!, You have solved the problem  :) \n')
                            print(
                                'Solution: 1 move goat\n2 move wolf or move cabbage\n3 move goat back\n4 move wolf or '
                                'move cabbage\n5 move goat')


                    else:
                        print('Oops, wrong selection. This item is already on the other side! :(')

                else:
                    print('Oops, wrong selection. :(')

            else:
                print('Oops, wrong selection. :(')

        else:
            print('Oops, wrong selection. :(')
        play = input('\nWant to play again? ( Enter y for yes, any other key to exit.)')


main()
