import random

print("Welcome to Blackjack Game!")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def calculate_score(cards_list):
    score = sum(cards_list)
    # If there is an 11 and the total exceeds 21, change the 11 to 1.
    if score > 21 and 11 in cards_list:
        cards_list[cards_list.index(11)] = 1
        score = sum(cards_list)
    return score


#starting cards
player_cards = [deal_card(), deal_card()]
dealer_cards = [deal_card(), deal_card()]

game_over = False

while not game_over:
    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)

    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Dealer's first card: {dealer_cards[0]}")

    if player_score > 21:
        print("You went over 21! Dealer wins.")
        game_over = True
        break

    player_choice = input("Type 'hit' to get another card, type 'stand' to pass: ").lower()
    if player_choice == "hit":
        player_cards.append(deal_card())
    else:
        game_over = True

# The dealer draws cards until reaching 17.
while dealer_score < 17 and player_score <= 21:
    dealer_cards.append(deal_card())
    dealer_score = calculate_score(dealer_cards)

#Results
print(f"\nYour final hand: {player_cards}, final score: {player_score}")
print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")

if player_score > 21:
    print("Dealer wins!")
elif dealer_score > 21:
    print("Player wins!")
elif dealer_score > player_score:
    print("Dealer wins!")
elif dealer_score < player_score:
    print("Player wins!")
else:
    print("It's a draw!")