
# print("Number of letters in your name: " + str(len(input("Enter your name : "))))

print(6 + 4 / 2 - (1 * 2))



print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

total = (bill + (tip / 100)) / people
print(round(total, 2))


