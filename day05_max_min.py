

n = int(input("Give me the number of number you want to add here : "))

scores = []
temp = 0

for i in range(n):

    scores.append(int((input(f"give me the {i + 1} score : "))))
#    take = input(f"Give me the {i+1} scores : ")
#    scores.append(take)


print(scores)

for score in scores :
        if score > temp :
               temp = score
    
print(temp)
    