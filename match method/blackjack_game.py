import random

def blackjack():
    deck = [2,3,4,5,6,7,8,9,10,10,10,10,11] * 4
    random.shuffle(deck)
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    
    def hand_value(hand):
        value = sum(hand)
        aces = hand.count(11)
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value
    
    while True:
        print(f"\nYour hand: {player_hand} (Total: {hand_value(player_hand)})")
        print(f"Dealer shows: {dealer_hand[0]}")
        
        match input("Hit or stand? ").lower():
            case "hit":
                player_hand.append(deck.pop())
                if hand_value(player_hand) > 21:
                    print(f"Bust! Your hand: {player_hand} (Total: {hand_value(player_hand)})")
                    return
            case "stand":
                break
            case _:
                print("Please enter 'hit' or 'stand'")
    
    dealer_value = hand_value(dealer_hand)
    while dealer_value < 17:
        dealer_hand.append(deck.pop())
        dealer_value = hand_value(dealer_hand)
    
    print(f"\nYour hand: {player_hand} (Total: {hand_value(player_hand)})")
    print(f"Dealer hand: {dealer_hand} (Total: {dealer_value})")
    
    match (hand_value(player_hand), dealer_value):
        case (p, d) if p > 21:
            print("You busted! Dealer wins.")
        case (p, d) if d > 21:
            print("Dealer busted! You win!")
        case (p, d) if p > d:
            print("You win!")
        case (p, d) if p < d:
            print("Dealer wins!")
        case _:
            print("It's a tie!")
blackjack()