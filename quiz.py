import random

correct=0
again=False
print("\n\tWelcome to the quiz show-down")
question=["What global event caused a significant disruption to supply chain and le dto a shortage of various goods in 2021 and 2022?"
          ,"Which countries hosted the circket tournament 'Asia cup 2023'?"
          ,"Who is the 46 th president of USA?"
          ,"Who has won the tittle of english football league 'carabao cup 20023'?"
          ,"Which country has become the world's biggest 'narco-state'? "]
answer=["covid 19","Pakistan and sirlanka","Joe Biden","manchester united","Syria"]
    #   qn  index  ,    x is an question

while again==False:
    x=random.choice(question)
    qn = question.index(x)
    ans=answer[qn]
        # print(x,qn,ans)

    
    print("\nQuestion:",x)
    fromuser=str(input("Enter your answer:\n "))
    fromuser=fromuser.lower()
        
    if fromuser==ans:
        print("congralutaion your answer is correct!!")
        correct+=1
        # print("Your point is ",correct)
    else:
        print("Sorry you answer is incorrect")
    
    print("Your point is ",correct,"\n")
    error=False
    while error==False:
        quit=str(input("Enter 'q' to quit otherwise,\npress 'n' for next question: "))
    
        if quit=="q":
            again=True
            error=True
        elif quit=="n":
            again=False
            error=True
        else:
            print("Invalid input!!\n")
            error=False
print("Thank you for playing ,\n You had scored: ",correct)