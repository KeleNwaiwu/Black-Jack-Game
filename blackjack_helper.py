from random import randint

def print_card_name(card_rank):
    if card_rank == 1:
        card_name = "Ace"
    elif card_rank == 11:
        card_name = "Jack"
    elif card_rank == 12:
        card_name = "Queen"
    elif card_rank == 13:
            card_name = "King"
    else:
        card_name = str(card_rank)
    
    if card_rank == 1 or card_rank == 8:
        print('Drew an ' + card_name)
    elif card_rank < 1 or card_rank > 13:
        print('BAD CARD')
    else:
        print('Drew a ' + card_name)

def draw_card():
    card_rank=randint(1,13)
    print_card_name(card_rank)
    if card_rank == 11 or card_rank == 12 or card_rank == 13:
        card_value = 10
    elif card_rank == 1:
        card_value = 11
    else:
        card_value = card_rank
    return card_value


def print_header(message):
    print("-----------")
    print(message)
    print("-----------")
  

def draw_starting_hand(name):
    name_turn = name + " TURN"
    print_header(name_turn)

    total_handvalue=0

    for i in range(2):
        card_value = draw_card()

        total_handvalue=total_handvalue+card_value
    return total_handvalue


def print_end_turn_status(hand_value):
    print("Final hand: " + str(hand_value) + ".")
    
    if hand_value==21:
        print("BLACKJACK!")
    elif hand_value>21:
        print("BUST.")




def print_end_game_status(user_hand, dealer_hand):
    print_header('GAME RESULT')
    if user_hand>21:
        print("Dealer wins!")
    elif user_hand<dealer_hand and dealer_hand <= 21:
        print("Dealer wins!")
    elif user_hand<=21 and user_hand>dealer_hand:
        print("You win!")
    elif user_hand<=21 and dealer_hand>21:
        print("You win!")
    elif user_hand<=21 and user_hand==dealer_hand:
        print("Push.")
    


