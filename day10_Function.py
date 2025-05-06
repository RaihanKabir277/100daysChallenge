
# def my_function():
#     result = 3*2
#     return result


# result = my_function()
# print(result)

# def format_name(f_name,l_name):
#     name = f_name.title() + " " + l_name.title()

#     return name

# f_name = "raihan"
# l_name = "kabir"

# format_name = format_name(f_name,l_name)
# print(format_name)

# ---------------------- nested Function ---------

def function1(text):
    return text + " " + text

def function2(text):
    return text.title()


output = function2(function1("hello"))
print(output)