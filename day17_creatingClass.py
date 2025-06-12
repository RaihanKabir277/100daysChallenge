
# class User:
#     pass

# user_1 = User()
# user_1.id = "218"
# user_1.name = "Kabir"

# print(user_1.name)

# user_2 = User()
# user_2.id = "219"
# user_2.name = "nabil"
# print(user_2.id)

# this is okay but if there is more than 100 of users then it will make complexity
# so , overcome this complexity and make the code more easier we will use constructor...



# ---------------- Constructor -----------------

# class User:
#     def __init__(self, user_id, user_name):
#         self.id = user_id
#         self.name = user_name
#         self.followers = 0   # its a default value and should not pass the parameter , when we create a new object , by default we get this value if we need


# user_1 = User("218", "Kabir")
# print(user_1.id)

# user_2 = User("219", "Nabil")
# print(user_2.name)

# now its more convinient then prevoius ..... it take few lines of code and remove complexity


# --------- Adding methods now in the class as before you added constructor and attribute in the classp-------------


class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.followers = 0   # its a default value and should not pass the parameter , when we create a new object , by default we get this value if we need
        self.following = 0
    def follow(self, user):
        user.followers += 1
        self.following += 1



user_1 = User("218", "Kabir")
print(user_1.name)

user_2 = User("219", "Nabil")
print(user_2.name)

print()

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

