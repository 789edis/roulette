#Roulette !
import random 


num =random.randint(0,37)
choice_specific=""
choice_subtype=""
even_odd=""
choice_sub_subtype=""
choice_column=""
color=""
bet=""
money = 100
bet_value = 0
dozen = ""
half_board = ""
num_bracket = ""
lowest_num = ""
play_again = 'f'

while play_again.lower() in ('f','y'):
    print(f'You have ${money} to bet with.')
   
    num =random.randint(0,37)
    choice_specific=""
    choice_subtype=""
    even_odd=""
    choice_sub_subtype=""
    choice_column=""
    color=""
    bet=""
    bet_value=""
    dozen=""
    half_board=""
    num_bracket=""
    lowest_num=""

    def test_integer(value,value_range):
        if value in value_range:
            return 0
        else: return 1
    
    while test_integer(bet_value,tuple(map(str,range(1,money+1)))) !=0:
        bet_value = input(f'How much would you like to bet? (1 to {money})\n')
    bet_value = int(bet_value)
    money -= bet_value

    def win_value(bet_ratio,bet_value):
        win = bet_ratio * bet_value + bet_value + money
        print(f'You win! You now have ${win}.')
        return win
    while test_integer(choice_specific,("1","2")) !=0:
        choice_specific = input('Would you like to bet on a specific number? (1 for yes and 2 for no) \n')
    if int(choice_specific) == 1:
        while test_integer(bet,tuple(map(str,range(0,37)))) !=0:
            bet = input('Choose a number between 0 and 36\n')    
    elif int(choice_specific) == 2:
        while test_integer(choice_subtype,("1","2","3")) !=0:
            choice_subtype = input('Would you rather bet on even/odd(1), on number brackets(2) or on color(3)?\n')
        if int(choice_subtype) == 1:
            while test_integer(even_odd,('1','2'))!=0:
                even_odd = input('Even(1) or odd(2)?\n')
            if int(even_odd) == 1:
                bet = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
            elif int(even_odd) == 2:
                bet = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]            
        elif int(choice_subtype) == 2:
            while test_integer(choice_sub_subtype,('1','2','3','4','5','6'))!= 0:
                choice_sub_subtype = input("A dozen(1), a half-board(2), a column(3) or on adjacent numbers(4)?\n")
            match choice_sub_subtype:
                case '1':
                    while test_integer(dozen,('1','2','3'))!=0:
                        dozen = input('First(1), second(2), or third(3) dozen?\n')
                        match dozen:
                            case '1':
                                bet = list(range(1,13))
                            case '2':
                                bet = list(range(13,25))
                            case '3':
                                bet = list(range(25,37))
                case '2':
                    while test_integer(half_board,('1','2'))!=0:
                        half_board = input('First half (1-18)(1) or second half (19-36)(2)?\n')
                        match half_board:
                            case '1':
                                bet = list(range(1,19))
                            case '2':
                                bet = list(range(19,37))
                case '3':
                    while test_integer(choice_column,('1','2','3'))!=0:
                        choice_column = input('Column 1, 2, or 3?\n')
                        match choice_column:
                            case '1':
                                bet = [1,4,7,10,13,16,19,22,25,28,31,34]
                            case '2':
                                bet = [2,5,8,11,14,17,20,23,26,29,32,35]
                            case '3':
                                bet = [3,6,9,12,15,18,21,24,27,30,33,36]
                case '4':
                    while test_integer(num_bracket,('2','3','4','5','6'))!=0:
                        num_bracket = input('Would you like to bet on 2, 3, 4 or 6 adjacent numbers?\n')
                        match num_bracket:
                            case '2':
                                while test_integer(lowest_num,tuple(map(str,range(0,36))))!=0:
                                    lowest_num = input('Enter the lowest number in the bracket:\n')
                                    bet = [int(lowest_num),int(lowest_num)+1]
                            case '3':
                                while test_integer(lowest_num,('1','4','7','10','13','16','19','22','25','28','31','34'))!=0:
                                    lowest_num = input('Enter the number of the first column from your choice:\n')
                                    bet = [int(lowest_num),int(lowest_num)+1,int(lowest_num)+2]
                            case '4':
                                while test_integer(lowest_num,('1','2','4','5','7','8','10','11','13','14','16','17','19','20','22','23','25','26','28','29','31','32','34','35'))!=0:
                                    lowest_num = input('Enter the upper left number from your choice:\n')
                                    bet = [int(lowest_num),int(lowest_num)+1,int(lowest_num)+3,int(lowest_num)+4]
                            case '6':
                                while test_integer(lowest_num,('1','4','7','10','13','16','19','22','25','28','31','34'))!=0:
                                    lowest_num = input('Enter the upper left number from your choice:\n')
                                    bet = [int(lowest_num),int(lowest_num)+1,int(lowest_num)+2,int(lowest_num)+3,int(lowest_num)+4,int(lowest_num)+5]
        elif int(choice_subtype) == 3:
            while test_integer(color,('1','2'))!=0:
                color = input('Black(1) or red (2)?\n')
            if int(color) == 1:
                bet = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
            elif int(color) == 2:
                bet = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]


    if (isinstance(bet,list) and num in bet):
        match choice_specific:
            case '2':
                match choice_subtype:
                    case '1':
                        money = win_value(1,bet_value)
                    case '2':
                        match choice_sub_subtype:
                            case '1' | '3':
                                money=win_value(2,bet_value)
                            case '2':
                                money=win_value(1,bet_value)
                            case '4':
                                match num_bracket:
                                    case '2':
                                        money=win_value(17,bet_value)
                                    case '3':
                                        money=win_value(11,bet_value)
                                    case '4':
                                        money=win_value(8,bet_value)
                                    case '6':
                                        money=win_value(5,bet_value)
                    case '3':
                        money=win_value(1,bet_value)

    elif not isinstance(bet,list) and int(bet) == num:
        money=win_value(35,bet_value)

    else:
        print(f'Sorry, you lose. You now have ${money} left.')

    print(f'The winning number was {num}.')

    if money <= 0:
        print("You have run out of money to bet with.")
        break
    
    play_again = ""
    while test_integer(play_again, ('y','n')) != 0:
        play_again = input("Would you like to play again? (y/n)\n")

print("Thanks for playing!")

