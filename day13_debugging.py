

# from random import randint
# dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_images[dice_num])


# ------------ try - catch block --------

# try:
#     age = int(input("how old are you? "))

# except ValueError:
#     print("You have typed in a invalid number. Please try again with a numerial number")
#     age = int(input("how old are you? "))


# if age > 18:
#     print(f"You can drive at age {age}")


# squash bug with a print --------

# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)


#  ---------------- Debugging  --------------

# import random
# import maths


# def mutate(a_list):
#     b_list = []
#     new_item = 0
#     for item in a_list:
#         new_item = item * 2
#         new_item += random.randint(1, 3)
#         new_item += maths.add(new_item, item)
#         b_list.append(new_item)
#     print(b_list)


# mutate([1, 2, 3, 5, 8, 13])

# debug the fizzbuzz game --------

def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0:
            print("Fizz")
        if number % 5 == 0:
            print("Buzz")
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        else:
            print(number)
