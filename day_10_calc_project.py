
# ----------------------- different way to use function -----------


# def add(n1, n2):
#     return n1 + n2

# my_fav_function = add  #store the function in a variable

# print(my_fav_function(3, 4))

#  --------- project start from here ---------

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multipy(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def remainder(n1, n2):
    return n1 % n2

calc_dict = {
    "+" : add,
    "-" : subtract,
    "*" : multipy,
    "/" : divide,
    "%" : remainder,
}

# calc_multipy = calc_dict["*"]
# print(calc_multipy(4 , 8))

# another easiest way to run the multipy function and print this..

# print(calc_dict["*"](4, 8))
def calculation():
    again = True
    n1 = float(input("Enter the 1st number : \n"))

    while again:

        for symbol in calc_dict:
            print(symbol)

        operator = input("Enter a choice of operator from '+', '-', '/','*','%' : \n")
        n2 = float(input("Enter the second number : \n"))

# for i in calc_dict:
#     if i == operator:
#         print(calc_dict[i](n1, n2))
#     else:
#         print("You input the wrong operator")

# more easiest to do this calculation -----------

# print(f"{n1} {operator} {n2} = {calc_dict[operator](n1, n2)}")

        answer = calc_dict[operator](n1, n2)
        print(f"{n1} {operator} {n2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation :\n").lower()

        if choice == "y":
            n1 = answer
        else:
            again = False
            print("\n" * 20)
            calculation()


calculation()

        




