"""
Notes on current issues:

1) Everything will run through smoothly if user sticks to 'Yes' or 'No' responses but if either conversation or user is recalled; it will only run that function and end. I'm sure a loop needs implemented or maybe a while. I'll have to study those more.

2) The 'or' inclusions don't seem to do anything because the lower case versions result in 'else'. This must be an incorrect way of implementing acceptable options. Look into creating a list or distionary to reference.

"""

def user():
    global username
    username = input("What shall I call you? ")
    print(f"{username} it is then.")

user()

def conversation():
    global affirmative
    affirmative = "Yes" or "yes"
    global negative
    negative = "No" or "no"
    response = input("Is this your first time coding a script that speaks to you? ")
    if response == affirmative:
        print("Well you have to start somewhere.")
    elif response == negative:
        argument = input("Are you sure about that? ")
        if argument == affirmative:
            print("Whatever you say...")
            print("Anyways...")
        elif argument == negative:
            print("That's what I figured.")
        else:
            print("Well if your so good at coding you would have made me able to respond well to that but here we are,")
            print("Anyways...")
    else:
        print("Well I don't know how to respond to that or repeat the question so we will just move on.")

conversation()

print("I'd say I'm a pretty good coder myself but I'm a computer and that wouldn't be quite fair. Google being built in and all.")

repeat = input("Well that's about all I have for now. If you want to have this riveting conversation again: type \"Yes\" otherwise type \"No\".")
if repeat == affirmative:
    comp_response = input("Do you want to pick a new user name? ")
    if comp_response == affirmative:
        print("Starting from the tippy top then.")
        print("Now as if I aquired amnesia.....")
        print("...")
        user()
    elif comp_response == negative:
        print(f"Alrighty. Another riviting conversation coming right up {username}.")
        conversation()
    else:
        print("Yup. Don't know how to respond to that so I've decided your keeping the name.")
        conversation()
elif repeat == negative:
    print("Alrighty. Well until next time.")
    print(f"Au revoir {username}")
else:
    print("Well I don't have a response for that answer so I'mma just end it right here.")
    print(f"Au revoir {username}. Hope you get better at this sooner rather than later!")

# Learning to upadate on GitHub