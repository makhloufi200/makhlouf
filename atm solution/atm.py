__author__ = 'smail'


def give_money(money,request):

    if request<= money:
        while request > 0:
            if request >= 100:
                request -= 100
                print("give 100")
            elif request >= 50:
                request -= 50
                print("give 50")
            elif request >= 10:
                request -= 10
                print("give 10")
            elif request >= 5:
                request -= 5
                print("give 5")
            elif request >= 2:
                request -= 2
                print("give 2")
            elif request >= 1:
                request -= 1
                print("give 1")
    elif money < request:
        x = "Can't Give You Money?"
    

###################################
print give_money(1000,277)