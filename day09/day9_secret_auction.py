from os import system

print("Welcome to the secret auction program!")

other_bidders = True
auction_info = {}

while other_bidders:

    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ")

    auction_info[name] = bid

    if other_bidders == "yes":
        print(f"\n" * 100)

    else:

        bidder = max(auction_info, key=auction_info.get)
        
        # highest_bid = 0

        # for name in auction_info:
        #     if auction_info[name] > highest_bid:
        #         highest_bid = auction_info[name]
        #         bidder = name
        
        other_bidders = False

print(f"The winner is {bidder.capitalize()} with a bid of ${auction_info[bidder]}")
#print(f"The winner is {bidder.capitalize()} with a bid of ${highest_bid}!")


