#July_11_HangMan
import random
words = ["computer","fan","lamp","phone","calculator"]

chosen_word = random.choice(words)
print(chosen_word)

health_symbol = "\u2764"
#print(health_symbol)

health = 5

hint = []

for index in range(len(chosen_word)):
        hint.append("?")

def update_hint(letter):
    for index in range(len(chosen_word)):
        if letter == chosen_word[index]:
            hint[index] = letter
            
while True:
    print()
    print(hint) #Displaying the Hint
    print(health_symbol*health) #Displaying the Health
    
    
    user_input = input("Enter a letter or a word: ")
    if user_input.lower() == chosen_word:
        #Winning Condition
        print("You guessed the word! You Win!")
        break
    
    elif user_input.lower() in chosen_word:
        update_hint(user_input.lower())
        if "?" not in hint:#Filled out entire hint, should win
            #Winning Condition
            print("You guessed the word! You Win!")
            break
    else:
        print(f"{user_input} is not correct! Please Try Again")
        
        health -= 1
        if health<1:
            #Losing Condition
            print(f"You ran out of Lives! The word was {chosen_word}")
            break
    
"""
make the game continuously do this:

Get input from shell asking for a letter or word
if the user input is = to the secret word, break from the loop
Print out lives through the symbols

"""
