def user():
    global username
    username = input("What shall I call you? ")
    print(f"{username} it is then.")

def conversation():
    global affirmative
    affirmative = ["Yes", "yes"]
    global negative
    negative = ["No", "no"]
    response = input("Is this your first time coding a script that speaks to you? ")
    if response in affirmative:
        print("Well you have to start somewhere.")
    elif response in negative:
        argument = input("Are you sure about that? ")
        if argument in affirmative:
            print("Whatever you say...")
            print("Anyways...")
        elif argument in negative:
            print("That's what I figured.")
        else:
            print("Well if your so good at coding you would have made me able to respond well to that but here we are,")
            print("Anyways...")
    else:
        print("Well I don't know how to respond to that or repeat the question so we will just move on.")
    print("I'd say I'm a pretty good coder myself but I'm a computer and that wouldn't be quite fair. Google being built in and all.")

def ending():
    global repeat
    repeat = input("Well that's about all I have for now. If you want to have this riveting conversation again: type \"Yes\" otherwise type \"No\".")
    if repeat in affirmative:
        global final_response
        final_response = input("Do you want to pick a new user name? ")
        if final_response in affirmative:
            print("Starting from the tippy top then.")
            print("Now as if I aquired amnesia.....")
            print("...")
        elif final_response in negative:
            print(f"Alrighty. Another riviting conversation coming right up {username}.")
        else:
            print("I don't know how to respond to that so I'll ask again.")
            ending()
    elif repeat in negative:
        print("Alrighty. Well until next time.")
        print(f"Au revoir {username}")
    else:
        print("I don't know how to respond to that so I'll ask again.")
        ending()
        
exit = 0
def main():
    user()
    conversation()
    ending()

def partial():
    conversation()
    ending()

while exit < 1:
    main()
    if repeat in affirmative:
        if final_response in affirmative:
            main()
        elif final_response in negative:
            partial()
    elif repeat in negative:
        exit += 1
