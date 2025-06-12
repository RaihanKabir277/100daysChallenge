
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

class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name

user_1 = User("218", "Kabir")
print(user_1.id)

user_2 = User("219", "Nabil")
print(user_2.name)


