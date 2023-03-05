import random

#MOODS
#print current mood
#prompt user input and display options
#accept user input, then check it, print a result, and return to while loop
	#incorrect action, reduce the mood by 1
	#correct action, mood increases by 1

def input_validation(selection):
    while True:
        if selection in ['f', 'p', 's','l']:
            return selection
        elif selection == 'q':
            print('Have a nice day!')
            quit()
        else:
            print('Please enter a lowercase letter:')
            selection = input()
            continue

def mad(mood):
    print('Neko seems to be easily agitated and aloof right now.') 
    print(action_choice)
    user_selection = input() 
    action = input_validation(user_selection) 
    if action == 'f':
        print('Neko walked away with disinterest! (Mood decreased)')
        return mood -1
    elif action == 'p':
        print('Neko simply blinks at you with an air of superiority! Silly human. (Mood decreased)')
        return mood -1
    elif action == 's':
        print('Neko bit you, ouch! (Mood decreased)')
        return mood - 1
    elif action == 'l':
        print('Neko is pleased that you respected their boundaries. (Mood improved)')
        return mood + 1 

def hungry(mood):
    print('Neko keeps following you around and meowing for... something?')
    print(action_choice)
    user_selection = input() 
    action = input_validation(user_selection) 
    if action == 'f':
        print('Neko eats all of the food! (Mood improved)')
        return mood + 1
    elif action == 'p':
        print('Neko gnaws on the toy! I wonder what it tastes like? (Mood decreased)')
        return mood -1
    elif action == 's':
        print('Neko stares daggers at you! (Mood decreased)')
        return mood -1
    elif action == 'l':
        print('Neko nips your ankle! (Mood decreased)')
        return mood -1

def bored(mood):
    print('Neko seems to have a lot of excess energy right now.')
    print(action_choice) 
    user_selection = input() 
    action = input_validation(user_selection) 
    if action == 'f':
        print('Neko plays with the food and makes a mess! (Mood decreased)')
        return mood -1
    elif action == 'p':
        print('Neko pounces on the toy with glee! (Mood improved)')
        return mood + 1 
    elif action == 's':
        print('Neko offers a belly... but its a trap! (Mood decreased)')
        return mood -1
    elif action == 'l':
        print('Neko scratches at the furniture! (Mood decreased)')
        return mood -1

def sleepy(mood): 
    print('Neko seems to have low energy right now.') 
    print(action_choice) 
    user_selection = input() 
    action = input_validation(user_selection) 
    if action == 'f':
        print('Neko sniffs at the food before deciding it would take too much energy to eat now. (Mood decreased)')
        return mood -1
    elif action == 'p':
        print('Neko lazily bats at the toy a few times before ignoring you! (Mood decreased)')
        return mood -1
    elif action == 's':
        print('Neko purrs contentedly and drifts off to sleep in your lap. (Mood improved)')
        return mood + 1 
    elif action == 'l':
        print('Neko hides under the bed and naps alone! (Mood decreased)')
        return mood -1

# check what the current mood value is and pass it to the correct function
# if the correct action is taken within a fuction, the mood will increase value
# if mood reaches 5 (happy), the program ends
while True: # main game loop
    print('NEKO-NEKO: a text-based adventure about taking care of a needy cat ^_^')
    print('Can you make Neko happy?')
    print('Respond to her mood by choosing actions. Be careful, too many incorrect actions may make her run away!')
    print(' ')
    
    # generate a random number that correlates to different moods
    mood = random.randrange(1, 5)
    action_choice = 'Choose an action: (f)eed, (p)lay, (s)nuggle, (l)eave alone or (q)uit'

    while True:
        if mood == 1:
         mood = mad(mood)
        elif mood == 2:
            mood = hungry(mood)
        elif mood == 3:
            mood = bored(mood)
        elif mood == 4:
            mood = sleepy(mood)
        elif mood == 0: # if mood reaches 0, Neko runs awaw and game ends
            print('Oh no! It looks like Neko ran away...')
            break
        else: # if mood reaches 5, Neko is happy and game ends
            print('Great! You were able to make Neko happy.')
            break
    
    print('Would you like to play again? y/n')
    replay = input()
    if replay == 'y':
        continue
    if replay == 'n':
        print('Thanks for playing!')
        quit()
