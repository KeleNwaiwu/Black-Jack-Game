from random import randint
from blackjack_helper import print_header,draw_card,print_end_turn_status,draw_starting_hand,print_end_game_status,print_card_name


name="YOUR"
hand_value=draw_starting_hand(name)
while hand_value < 21:
    should_hit = input('You have ' + str(hand_value) + ". Hit (y/n)? ")
    if should_hit == 'n':
        break
    elif should_hit == 'y':
        user_cardvalue1=draw_card()
        hand_value = hand_value + user_cardvalue1
    else:
        print("Sorry I didn't get that.")

print_end_turn_status(hand_value)


name="DEALER"
dealer_value=draw_starting_hand(name)

while dealer_value<17:

    print("Dealer has " + str(dealer_value) + ".")
    if dealer_value<17:
        dealer_hand=draw_card()
        dealer_value+=dealer_hand
print_end_turn_status(dealer_value)

print_end_game_status(hand_value, dealer_value)



  
















    


      