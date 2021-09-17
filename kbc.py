


print("     Welcome to Kaun Banega Crorpati    "  )

question_list=["How many continents are there?","What is the capital of India?",
               "NG mei kaun se course padhaya jaata hai?" ]
options_list = [["Four", "Nine", "Seven", "Eight"],
                  ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
                ["Software Engineering", "Counseling", "Tourism", "Agriculture"]]

solution_list = [3, 4, 1]
answer5050=[["(1).Four","(3).seven"],
          ["(2).Bhopal","(4).delhi"],
          ["(1).Software Engineering","(3).Tourism"]]


start=input("can we start the game(yes/no) :")
if start=="yes":
    print("Aapka sawal hai : ")
    print()
    i=0
    count=0
    while i<len(question_list):
        print("Aapka sawal hai : ")
        print(question_list[i])
        print("Aapke option hai : ")
        n=0
        while n<len(options_list[i]):

            print(n+1,options_list[i][n])
            n=n+1
        
        

        choose_lifeline=input("do you want to use (50-50)lifeline :")
        if choose_lifeline=="yes":
            count=count+1
            if count==1:
                print("your option are:")
                
                p=0
                while p < len(answer5050[i]):
                    print(answer5050[i][p])
                    p=p+1
                answer=int(input("Please enter your answer  : "))
                if answer==solution_list[i]:
                    print("Congrats ! Your answer is correct.")
                else:
                    print("sorry your answer is wrong. ")
                    print("you lost your game")
                    break   
            else:
                print("you alraedy use the life line")
                m=0
                while m<len(options_list[i]):
                    print(m+1,options_list[i][m])
                    m=m+1
                answer=int(input("Please enter your answer  : "))
                if answer==solution_list[i]:
                    print("Congrats ! Your answer is correct.")
                else:
                    print("sorry your answer is wrong. ")
                    print("you loss your game")
                    break
            
        else:
            n=0
            while n<len(options_list[i]):
                print(n+1,options_list[i][n])
                n=n+1
            answer=int(input("Please enter your answer  : "))
            if answer==solution_list[i]:
                print("Congrats ! Your answer is correct.")
            else:
                print("sorry your answer is wrong. ")
                print("you loss your game")
                break
        i=i+1
    print("thank you to participating Kaun Banega Crorepati")
    print("Thank you")

