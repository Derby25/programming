import time
import random 
import os

name_question=[ 
    " What is your name ?: ",
    " Can you tell me your full name please ?: ",
    " How should i address you formally? : ",

]
nickname_questions=[
    " What would you like me to call you ?: ",
    " Do you have a nickname you prefer?: ",
    " How do your friends usually call you?: ",
]
age_questions=[
    " How old are you?: ",
    " Whats your age?: ",
    " May i know your age ?: ",
]
place_questions=[ 
    "Where do you currently live ? : ",
    "Which city or town do you live in ?: ",
    "Where do you call home ?: ",
]
school_questions=[
    " Whats your highest of education?: ",
    " How far have you gone in school?: ",
    " Whats your highest class or degree you have completed?: ", 
]
shs_questions=[
    "Can you tell me the name of your shs?: ",
    " Which Senior High school did you attend ?: ",
    " Which region is is located?: ",
]
colour_questions=[
    " Do you have a favourite colour?: ",
    " what is your favourite colour?: ",
    " Why is it your favourite colour?:  ",
]
hobby_questions=[ 
    " Do you have any hobbies?: ",
    " What is your favourite thing to do ?: ",
    " How do you feel after doing that ?: ",
]

print( "Hi there !")
print( " Im your personal assistant , here to learn little about you so i can help make your \n"
" experience here smarter and more personalised.\n ")
print("This will take only a moment. Ready when you are. \n")

while True:
    Full_name=input(random.choice(name_question))
    user_name=input(random.choice(nickname_questions))

    user_age=int(input(random.choice(age_questions)))
    if user_age<=0:
      print( "Your age cannot be less than or equal to 0.")
      break
    place=input(random.choice(place_questions))
    school_level=input(random.choice(school_questions))
    shs_level=input(random.choice(shs_questions))
    favourite_colour=input(random.choice(colour_questions))
    hobby=input(random.choice(hobby_questions))
    

    summary = (
    f"Hello {user_name}! \n Its a great pleasure to get to know you a little.\n"
    f" you shared that your full name is {Full_name}, and you are { user_age } years old.\n"
    f" You currently live in  {place}, and you have reached { school_level } in your country.\n"
    f" You also went to {shs_level}, for Senior High school, Nice! .\n"
    f"I love that your favourite colour is {favourite_colour}, and in your free time you like to { hobby}.\n"
    f" Thats awesome , hobbies are such a great way to unwind .\n"
    f" Thanks for telling me about yourself !\n I am here to help however i can. Thank you. \n")

    print("\n")
    print (summary)
    

    save = input(" Do you want to save this document ( yes/no): ")
    if save.lower()=="yes":
        filename=f"{user_name}.txt"
        

    while True:
        rating=int( input("Just for fun! How would you like to rate your assistant from 1 to 5:"))
        if 1 <= rating <= 5:
            stars="✨"* rating

            print(f"Thanks for the {stars} rating !")
            break
        else:
            print(" Please enter a number between 1 to 5" )
        with open (file.name,"w",encoding=utf-8)as file:                                                                        
             file.write(summary)
             file.write(f" \nAssistant Rating:{stars} ({rating}/5)")

        print(f" \n Your summary has been saved to {user_name}.txt") 
        print(f"location:{os.path.abspath(filename)}")
        break

    restart= input( "\nWould you like to restart (yes/no):") 
        
    
    if restart==" yes": 
        for i in range(1,4):
           print("Restarting.......")
           time.sleep(1)
        print("\n")
        continue
    else:
        print("\nAlriight thanks for chatting,see you next time !")
        break 
