

def find_highest_bidder(bids):
    winner = ""
    highest = 0
    for bidder in bids:
        bid_amount = bids[bidder]

        if bid_amount > highest:
            highest = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest}")


bids = {}


continue_bidding = True

while continue_bidding:
    name = input("What is your name ? \n")
    price = float(input("What is your bis ? \n"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type yes or no : \n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 10)

