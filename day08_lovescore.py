def calculate_love_score(name1, name2):
    name = name1 + name2
    name3 = name.lower()
    Love_Score = ""
    t = 0
    r = 0
    u = 0
    e = 0
    for i in name3:
        if i == "t":
            t +=1
        elif i == "r":
            r += 1
        elif i == "u":
            u += 1
        elif i == "e":
            e += 1
    Total = (t+r+u+e)  
    
    l = name3.count('l')
    o = name3.count('o')
    v = name3.count('v')
    e1 = name3.count('e')
    Total1 = (l+o+v+e1)
    
   
    print(f"T occurs {t} times")
    print(f"R occurs {r} times")
    print(f"U occurs {u} times")
    print(f"E occurs {e} times")
    print(f"Total={Total}")
    
    print(f"L occurs {l} times")
    print(f"O occurs {o} times")
    print(f"V occurs {v} times")
    print(f"E occurs {e1} times")
    print(f"Total={Total1}")
    
    Love_Score = str(Total) + str(Total1)
    
    print(f"Love Score={Love_Score}")
    


calculate_love_score("Kanye West", "Kim Kardashian")

