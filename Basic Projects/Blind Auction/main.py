import os
from art import logo

print(logo)

highest_bidder = {}
bidding_finished = False


def find_highest_bidder(highest_bidder):
    highest_bid = 0
    for bidder in highest_bidder:
        bid_amount = highest_bidder[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


while not bidding_finished:
    name = input("What is your name?: ")
    bid = int(input("How much are you bidding?: $"))

    highest_bidder[name] = bid

    another_bid = input("Are there any other bidders? type 'yes' or 'no'.\n ")
    if another_bid == "no":
        bidding_finished = True
        find_highest_bidder(highest_bidder)
    elif another_bid == "yes":
        os.system('cls')