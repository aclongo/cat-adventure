import random

# INPUT VALIDATION
# Checks if user input is a valid lowercase later, else allows them to try again
# Also allows the program to end if user chose 'q' for quit
def input_validation(selection):
    '''Validates user input and allows user to quit the program'''
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

# MOOD FUNCTIONS
# Print text hinting at current mood
# Prompt user input and display options
# Accept user input, validate it, check it, print a result, and return to main while loop
	# incorrect action, reduce the mood by 1
	# correct action, mood increases by 1
def mad(mood):
    '''Called whenever the mood value is set to 1'''
    print('Neko seems to be easily agitated and aloof right now.') 
    print(action_choice) # prints the action choice string defined on line 109
    user_selection = input() # accepts user input
    action = input_validation(user_selection) # passes input to the input validation function and names the returning result 'action'
    if action == 'f': # user actions affect the mood of Neko, new mood values passed back to main loop
        print('Neko walked away with disinterest! (Mood decreased)')
        return mood -1 # incorrect action
    elif action == 'p':
        print('Neko simply blinks at you with an air of superiority! Silly human. (Mood decreased)')
        return mood -1 # incorrect action
    elif action == 's':
        print('Neko bit you, ouch! (Mood decreased)')
        return mood - 1 # incorrect action
    elif action == 'l':
        print('Neko is pleased that you respected their boundaries. (Mood improved)')
        return mood + 1 # correct action

def hungry(mood):
    '''Called whenever the mood value is set to 2'''
    print('Neko keeps following you around and meowing for... something?')
    print(action_choice)
    user_selection = input() 
    action = input_validation(user_selection) 
    if action == 'f':
        print('Neko eats all of the food! (Mood improved)')
        return mood + 1 # correct action
    elif action == 'p':
        print('Neko gnaws on the toy! I wonder what it tastes like? (Mood decreased)')
        return mood -1 # incorrect action
    elif action == 's':
        print('Neko stares daggers at you! (Mood decreased)')
        return mood -1 # incorrect action
    elif action == 'l':
        print('Neko nips your ankle! (Mood decreased)')
        return mood -1 # incorrect action

def bored(mood):
    '''Called whenever the mood value is set to 3'''
    print('Neko seems to have a lot of excess energy right now.')
    print(action_choice) 
    user_selection = input() 
    action = input_validation(user_selection) 
    if action == 'f':
        print('Neko plays with the food and makes a mess! (Mood decreased)')
        return mood -1 # incorrect action
    elif action == 'p':
        print('Neko pounces on the toy with glee! (Mood improved)')
        return mood + 1 # correct action
    elif action == 's':
        print('Neko offers a belly... but its a trap! (Mood decreased)')
        return mood -1 # incorrect action
    elif action == 'l':
        print('Neko scratches at the furniture! (Mood decreased)')
        return mood -1 # incorrect action

def sleepy(mood): 
    '''Called whenever the mood value is set to 4'''
    print('Neko seems to have low energy right now.') 
    print(action_choice) 
    user_selection = input() 
    action = input_validation(user_selection) 
    if action == 'f':
        print('Neko sniffs at the food before deciding it would take too much energy to eat now. (Mood decreased)')
        return mood -1 # incorrect action
    elif action == 'p':
        print('Neko lazily bats at the toy a few times before ignoring you! (Mood decreased)')
        return mood -1 # incorrect action
    elif action == 's':
        print('Neko purrs contentedly and drifts off to sleep in your lap. (Mood improved)')
        return mood + 1 # correct action
    elif action == 'l':
        print('Neko hides under the bed and naps alone! (Mood decreased)')
        return mood -1 # incorrect action

# MAIN GAME LOOP
# Print game instructions
# Check what the current mood value is and pass it to the correct function
# User increases or decreases the mood value based on action choices
    # If mood reaches 5 (happy), the game ends
    # If mood reachs 0, the game ends
    # User can choose to replay or exit game
while True:
    print('NEKO-NEKO: a text-based adventure about taking care of a needy cat ^_^')
    print('Can you make Neko happy?')
    print('Respond to her mood by choosing actions. Be careful, too many incorrect actions may make her run away!')
    print(' ')
    
    # generate a random starting mood, each integer correlates to a different mood below
    mood = random.randrange(1, 5)
    # action_choice will be printed each time a mood function is called
    action_choice = 'Choose an action: (f)eed, (p)lay, (s)nuggle, (l)eave alone or (q)uit'

    # checks current mood value and passes it to the correct function
    while True:
        if mood == 1:
         mood = mad(mood)
        elif mood == 2:
            mood = hungry(mood)
        elif mood == 3:
            mood = bored(mood)
        elif mood == 4:
            mood = sleepy(mood)
        elif mood == 0: # if mood reaches 0, Neko runs away and game ends
            print('Oh no! It looks like Neko ran away...')
            break
        else: # mood == 5, Neko is happy and game ends
            print('Great! You were able to make Neko happy.')
            break
    
    # gives user the option to replay or quit
    print('Would you like to play again? y/n')
    replay = input()
    if replay == 'y':
        continue
    if replay == 'n':
        print('Thanks for playing!')
        quit()