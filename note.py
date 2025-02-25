""" x = True
y = True

def GCF(x,y):
    if x == True and y == True:
        print("common factor")
def vote(age, id):
    if age < 18 or id == False:
        print("cannot vote")
    elif age > 18 and id == True:
        print("you can vote")
    
def skins(money, age, isAvailable):
    if money < 10 or age < 18 or isAvailable == False:
        return ("cannot buy")
def skins(money, cost, isAvailable):
    if isAvailable == True:
        if money > 10 or cost == 0:
            print("can purchase")
        else:
            print("Lucas Broke Boy")
    else:
        print("not available")
 """
##############################
def skins(money, cost, isAvailable):
    if isAvailable == True and money >= cost:
        print("You can buy")
skins(11, 5, True)