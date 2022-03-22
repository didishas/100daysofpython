from os import system

# HINT: You can call clear() to clear the output in the console.
from art import logo


print(logo)
print("Welcom to the secret auction program.")

auctions = {}
still_bidders = True
while still_bidders:
    system("cls")
    bidder = input("What is your name?: ")
    auction = input("What is your bid?: $")
    auctions[bidder] = auction

    response = input("Are there any other bidders? Type 'yes' or 'no'.")
    if response == "no":
        still_bidders = False


max_bid = 0
max_auctionner = ""
for name, bid in auctions.items():
    if max_bid < int(bid):
        max_bid = int(bid)
        max_auctionner = name

print(f"The winner is {max_auctionner} with a bid of ${max_bid}.")
