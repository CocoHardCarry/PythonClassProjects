#July_11_Magic8Ball

import random as r#as r changes when you need to grab a random function

while True:
    user_question = input("Enter a yes or no question: ")
    if user_question == "quit":
        print("bye bye")
        break
    
    random_number = r.randint(1,8)#r = random module name
    
    if random_number == 1:
        print("It is certain")
    elif random_number==2:
        print('Most Likely')
    elif random_number==3:
        print('Signs point to yes')
    elif random_number == 4:
        print("I don't think so")
    elif random_number == 5:
        print("Ask again later")
    elif random_number == 6:
        print("Concentrate and ask again")
    elif random_number == 7:
        print("Outlook not so good")
    elif random_number == 8:
        print("My reply is no")
        
        
    
