from random import shuffle
import time

def my_shuffle(my_list):
    shuffle(my_list)
    results = my_list
    return results

def game():
    print("Welcome to Three Cup Monte!")
    time.sleep(1)
    print("Please place your guess! Left, Middle or Right!")
    player_input = input()
    new_input = player_input.lower()
    cup_of_monte = [1,0,0]
    options = ['left', 'right', 'middle']
    shuffle_string = 'Shuffling'
    time.sleep(1)
    if new_input == 'end':
        time.sleep(1)
        print('Ending Game')
        return 0
    if new_input in options:
        for element in range(5):
            shuffle_string += '.'
            time.sleep(1)
            print(shuffle_string)
            my_shuffle(cup_of_monte)
            time.sleep(1) 
        if(new_input == 'left' and cup_of_monte[0] == 1):
            print('You have guessed correctly!')
        elif(new_input == 'middle' and cup_of_monte[1] == 1):
            print('You have guessed correctly!')
        elif(new_input == 'right' and cup_of_monte[2] == 1):
            print('You have guessed correctly!')
        else:
            print('You have guessed incorrectly! Please try again!')
            game()
    else:
        print('please enter a valid option')
        game()

game()