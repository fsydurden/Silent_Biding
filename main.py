from art import logo
print(logo)
# print(user_data)
user_data = {}
def add_bid():
    name = input("Enter your name \n")
    bid = int(input("Enter your bid\n$"))
    user_data[name] = bid
add_bid()
players_left = input("Type yes if there are players left \n").lower()
while players_left == 'yes':
    print("\n" * 100)
    add_bid()
    players_left = input("Type yes if there are players left \n").lower()
winner = ""
if players_left == "no":
    print("\n" * 100)
    highest_bid = 0
    for bidder in user_data:
        bid_amount = user_data[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"{winner} has the highest bid ${highest_bid}")
