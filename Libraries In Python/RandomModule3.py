import random
print(random.randint(1,10))
cards = ["Ace","1","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
random.shuffle(cards)
for i in cards :
    print(i,sep = "  ")