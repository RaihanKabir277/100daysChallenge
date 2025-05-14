

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

word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)