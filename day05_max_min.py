

# n = int(input("Give me the number of number you want to add here : "))

# scores = []
# temp = 0

# for i in range(n):

#     scores.append(int((input(f"give me the {i + 1} score : "))))
# #    take = input(f"Give me the {i+1} scores : ")
# #    scores.append(take)


# print(scores)

# for score in scores :
#         if score > temp :
#                temp = score
    
# print(temp)
    

#      find min without min function -------------

n = int(input("give me the max number of inputs you want to push : "))

min_scores = []

for i in range(n):
    min_scores.append(float(input(f"Enter the {i+1} scores : ")))

print(min_scores)
temp = min_scores[0]

for score in min_scores : 
    if score <= temp :
        temp = score

print(temp)

