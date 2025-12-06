#Roulette !
import random 

num = random.randint(0,37)
choice_specific = int(input('Would you like to bet on a specific number? (1 for yes and 2 for no) \n'))

if choice_specific == 1:
    bet = int(input('On which number would you like to bet? \n'))
    
elif choice_specific == 2:
    choice_subtype = int(input('Would you rather bet on even/odd(1), on number brackets(2) or on color(3)?\n'))
    if choice_subtype == 1:
        even_odd = int(input('Even(1) or odd(2)?\n'))
        if even_odd == 1:
            bet = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
        elif even_odd == 2:
            bet = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]
        else:
            print('Please enter 1 or 2 as a decision')
    elif choice_subtype == 2:
        choice_sub_subtype = int(input('From 1 to 12(1), 1 to 18(2), 12 to 24(3), 19 to 36(4),25 to 36(5) or a column(6)?\n'))
        if choice_sub_subtype == 1:
            bet = list(range(1, 13))
        elif choice_sub_subtype == 2:
            bet = list(range(1,19))
        elif choice_sub_subtype == 3:
            bet = list(range(12,25))
        elif choice_sub_subtype == 4:
            bet = list(range(19,37))
        elif choice_sub_subtype == 5:
            bet = list(range(25,37))
        elif choice_sub_subtype == 6:
            choice_column = int(input('Column 1, 2, or 3?\n'))
            if choice_column == 1:
                bet = [1,4,7,10,13,16,19,22,25,28,31,34]
            elif choice_column == 2:
                bet = [2,5,8,11,14,17,20,23,26,29,32,35]
            elif choice_column == 3:
                bet = [3,6,9,12,15,18,21,24,27,30,33,36]
            else:
                print('Please enter a number from the array')
        else:
            print('Please enter a number as seen in the parenthesis as a decision')
    elif choice_subtype == 3:
        color = int(input('Black(1) or red (2)?\n'))
        if color == 1:
            bet = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
        elif color == 2:
            bet = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
        else:
            print('Please enter 1 or 2 as a decision')
    else:
        print('Please enter a number seen in the parentheses as a decision')
else:
    print('Please enter 1 or 2 as decision')
    

if choice_specific == 2 and num in bet:
    print('You have won!')
elif choice_specific == 2 and num not in bet:
    print('You have unfortunately lost...')
elif choice_specific == 1 and num == bet:
    print('You have won!')   
elif choice_specific == 1 and num != bet:
    print('You have unfortunately lost...')  
    
print(f'The winning number was {num} ')