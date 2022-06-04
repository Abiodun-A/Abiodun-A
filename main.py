import random

is_running= True
print("Rock Paper Scissor")
print("What do you pick?\n Rock=R\n Paper=P\n Scissor=S\n")
while is_running:
    try:
        List=['R', 'P', 'S']
        User= input("Pick your option between 'R' 'P' 'S': ")
        CPU= random. choice(List)
        print(CPU)
    except:
        print("Error")
        continue
    if User=='R' and CPU=='P':
        print("User(Rock):CPU(Paper)\nCPU won")
        is_running=False
    elif User=='R' and CPU=='S':
        print("User(Rock):CPU(Scissor)\nUser won")
        is_running=False
    elif User=='R' and CPU=='R':
        print("User(Rock):CPU(Rock)\nIt is a tie")
        pass
    elif User=='P' and CPU=='P':
        print("User(Paper):CPU(Paper)\nIt is a tie")
        pass
    elif User=='P' and CPU=='S':
        print("User(Paper):CPU(Scissor)\nCPU won")
        is_running=False
    elif User=='P' and CPU=='R':
        print("User(Paper):CPU(Rock)\nUser won")
        is_running=False
    elif User=='S' and CPU=='S':
        print("User(Scissor):CPU(Scissor)\nIt is a tie")
        pass
    elif User=='S' and CPU=='P':
        print("User(Scissor):CPU(Paper)\n User won")
        is_running=False   
    elif User=='S' and CPU=='R':
        print("User(Scissor):CPU(Rock)\n CPU won")
        is_running=False
    else:
        print("Error")
    
