#July_11_Magic8BallV2

import random as r#as r changes when you need to grab a random function

messages = ["It is certain",'Most Likely',"Signs point to yes","I don't think so","Ask again later", "Concentrate and ask again","Outlook not so good","My reply is no"]

while True:
    user_question = input("Enter a yes or no question: ")
    if user_question == "quit":
        print("bye bye")
        break
    
    #random_number = r.randint(1,8)#r = random module name
    
    message = r.choice(messages)
    
    print(message)
        
        
    
