import random



while True:
    my_ans= input("Choice: rock ,paper or scissors: ")
    bot_ans = random.choice(['rock','paper','scissors'])

    if my_ans == "gg":
        break

    print(f"Computer chose:{bot_ans} ")
    
    
    if my_ans!= "rock" and my_ans!='paper' and my_ans!="scissors":
        print("Please, Enter appropriate answer.")
        continue

    
    if my_ans == bot_ans:
        print("You tied")
        continue

    elif my_ans == "rock" and bot_ans =="scissors":
        print("You won!!")
        break
    
    elif my_ans == "paper" and bot_ans =="rock":
        print("You won!!")
        break
    
    elif my_ans == "scissors" and bot_ans =="paper":
        print("You won!!")
        break
    
    else:
        print("Sorry, Not this time")



    print('')

