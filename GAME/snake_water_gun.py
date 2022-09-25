import random


print("hello everybody welcome to snake water gun game")
print("choose s for snake w for water g for gun")
def gettime():
    import datetime
    return datetime.datetime.now()
def snake_water_gun_game():
    opt=["s","w","g"]
    you=input("type here:\n")
    comp=random.choice(opt)
    if you=="s":
        if comp=="s":
           print("game tie,computer also chooses snake")
           with open("score.txt","a") as sc:
            sc.write(str(str(gettime())+"   :tie\n"))
        elif comp=="w":
            print("you win, computer chooses water")
            with open("score.txt","a") as sc:
             sc.write(str(str(gettime())+"  :win\n"))
        elif comp=="g":
            print("computer wins, computer chooses gun")
            with open("score.txt","a") as sc:
             sc.write(str(str(gettime())+"  :loose\n"))
        else:
            print("enter the valid game option")
    elif you=="w":
        if comp=="s":
            print("computer win, computer chooses snake")
            with open("score.txt","a") as sc:
             sc.write(str(str(gettime())+"  :loose\n"))
        elif comp=="w":
            print("game tie, computer also chooses water ")
            with open("score.txt","a") as sc:
             sc.write(str(str(gettime())+"  :tie\n"))
        elif comp=="g":
            print("you win , computer chooses gun")
            with open("score.txt","a") as sc:
             sc.write(str(str(gettime())+"  :win\n"))
        else:
            print("choose valid option")
    elif you=="g":
        if comp=="s":
            print("you win, computer chooses snake")
            with open("score.txt","a") as sc:
             sc.write(str(str(gettime())+"  :win\n"))
        elif comp=="w":
            print("computer wins, computer  chooses water ")
            with open("score.txt","a") as sc:
             sc.write(str(str(gettime())+"  :loose\n"))
        elif comp=="g":
            print("game tie , computer chooses gun")
            with open("score.txt","a") as sc:
             sc.write(str(str(gettime())+"  :tie\n"))
        else:
            print("choose valid option")
    print("thanks for playing \nnext round\nyour score is recoreded in score.txt file ")                                               

snake_water_gun_game()
snake_water_gun_game()
snake_water_gun_game()
snake_water_gun_game()
snake_water_gun_game()