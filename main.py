import random

# INPUT VALIDATION
# Checks if user input is a valid lowercase later, else allows them to try again
# Also allows the program to end if user chose 'q' for quit
def input_validation(selection):
    '''Validates user input and allows user to quit the program'''
    while True:
        if selection in ['f', 'p', 's','l','o']:
            return selection
        elif selection == 'q':
            print('Have a nice day!')
            quit()
        else:
            print('Please enter a lowercase letter:')
            selection = input()
            continue

# MOOD FUNCTIONS
# Use random.choice to print random text hinting at current mood
# Prompt user input and display options
# Accept user input, validate it, check it, print a result, and return to main while loop
	# incorrect action, reduce the mood by 1
	# correct action, mood increases by 1
def mad(mood):
    '''Called whenever the mood value is set to 1'''
    # a random hint text is chosen and printed
    print()
    print(random.choice([
        'Neko seems to be easily agitated and aloof right now.',
        'Neko is vocalizing less frequently than usual and seems uninterested in your attempts to engage with her.',
        'Neko is grooming herself excessively and doesn\'t seem interested in interacting with you.'
        ])) 
    print(action_choice) # prints the action choice string defined on line 132
    user_selection = input() # accepts user input
    action = input_validation(user_selection) # passes input to the input validation function and names the returning result 'action'
    if action == 'f': # user actions affect the mood of Neko, new mood values passed back to main loop
        print('Neko ignores your attempts at domestication and escapes at the first opportunity.')
        return mood -1 # incorrect action
    elif action == 'p':
        print('Neko simply blinks at you with an air of superiority before stalking out of the room.')
        return mood -1 # incorrect action
    elif action == 's':
        print('Neko bit your outstretched hand before turning away, ouch!')
        return mood - 1 # incorrect action
    elif action == 'l':
        print('Neko is pleased that you respected her boundaries. (Mood improved)')
        return mood + 1 # correct action
    elif action == 'o':
        print('Neko gladly steps outside when you offer, but doesn\'t return!')
        return mood - 1 # incorrect action

def wild(mood):
    '''Called whenever the mood value is set to 2'''
    print()
    print(random.choice([
        'Neko\'s eyes are dilated with a crazy look while she chases shadows and reflections.',
        'Neko has the zoomies! She\'s running back and forth around the house like a maniac.',
        'Neko is jumping on and off furniture and knocking things over while stalking imaginary prey.']))
    print(action_choice)
    user_selection = input()
    action = input_validation(user_selection)
    if action == 'f':
        print('Neko knocks over the food dish while zooming past it! (Mood decreased)')
        return mood - 1 # incorrect action
    if action == 'p':
        print('Neko is a little rough. It\'s hard to tell if this is "playing" so much as "preying" on you. (Mood decreased)')
        return mood - 1 # incorrect action
    if action == 's':
        print('Neko wriggles out of your grasp, leaving behind a trail of scratch marks. Ouch! (Mood decreased)')
        return mood - 1 # incorrect action
    if action == 'l':
        print('Neko jumps onto a table and knocks over a lamp. She has too much pent-up energy for the indoors! (Mood decreased)')
        return mood - 1 # incorrect action
    if action == 'o':
        print('You let Neko onto the patio. She speeds past you and lets out her pent-up energy while chasing bugs and sniffing at the breeze. (Mood increased)')
        return mood + 1 # correct action

def hungry(mood):
    '''Called whenever the mood value is set to 3'''
    print()
    print(random.choice([
        'Neko keeps following you around and meowing for... something?',
        'Neko seems to be trying to open up the cabinets in the kitchen.',
        'Neko keeps pawing at your leg and looking up at you expectantly.']))
    print(action_choice)
    user_selection = input() 
    action = input_validation(user_selection) 
    if action == 'f':
        print('Neko gratefully eats all of the food or treats you offered her! (Mood improved)')
        return mood + 1 # correct action
    elif action == 'p':
        print('Neko gnaws on the toy a bit more than usual! I wonder what it tastes like? (Mood decreased)')
        return mood -1 # incorrect action
    elif action == 's':
        print('Neko immediately jumps down from your lap and walks towards the kitchen, howling. (Mood decreased)')
        return mood -1 # incorrect action
    elif action == 'l':
        print('Neko nips your ankle with persistence! (Mood decreased)')
        return mood -1 # incorrect action
    elif action == 'o':
        print('Neko steps out the door and looks for prey to hunt for food on her own. (Mood decreased)')
        return mood - 1 # incorrect action

def bored(mood):
    '''Called whenever the mood value is set to 4'''
    print()
    print(random.choice([
        'Neko is restlessly looking around, as if searching for something to do.',
        'Neko\'s tail is twitching impatiently, as if she\'s waiting for something to happen.',
        'Neko is prowling around the room and batting at things.'
        ]))
    print(action_choice) 
    user_selection = input() 
    action = input_validation(user_selection) 
    if action == 'f':
        print('Neko plays with the food and makes a mess! (Mood decreased)')
        return mood -1 # incorrect action
    elif action == 'p':
        print('Neko pounces on the toy you offer with murderous glee! (Mood improved)')
        return mood + 1 # correct action
    elif action == 's':
        print('Neko offers a belly... but its a trap! (Mood decreased)')
        return mood -1 # incorrect action
    elif action == 'l':
        print('Neko scratches at the furniture with frustration! (Mood decreased)')
        return mood -1 # incorrect action
    elif action == 'o':
        print('Neko makes one circle around the patio before planting herself in front of the door and scratching to be let back in. (Mood decreased)')
        return mood - 1 # incorrect action

def sleepy(mood): 
    '''Called whenever the mood value is set to 5'''
    print()
    print(random.choice([
        'Neko curls up in a small ball and starts to close her eyes, looking very peaceful.',
        'Neko\'s movements are slow and sluggish, almost as if she\'s struggling to stay awake.',
        'Neko nuzzles your leg and lets out a contented chirp, as if she\'s seeking comfort.'])) 
    print(action_choice) 
    user_selection = input() 
    action = input_validation(user_selection) 
    if action == 'f':
        print('Neko sniffs at the food before deciding it would take too much energy to eat now. (Mood decreased)')
        return mood -1 # incorrect action
    elif action == 'p':
        print('Neko lazily bats at the toy you offer once or twice before rolling over. (Mood decreased)')
        return mood -1 # incorrect action
    elif action == 's':
        print('You pick up Neko and pet her in your lap. She purrs contentedly and drifts off to sleep. (Ultimate happiness achieved!)')
        return mood + 1 # correct action
    elif action == 'l':
        print('Neko slowly makes her way into the bedroom, where she falls asleep under the bed alone. (Mood decreased)')
        return mood -1 # incorrect action
    elif action == 'o':
        print('Neko curls up just outside the door and dozes off, waiting to be let back inside. (Mood decreased)')
        return mood - 1 # incorrect action

# MAIN GAME LOOP
# Print game instructions
# Check what the current mood value is and pass it to the correct function
# User increases or decreases the mood value based on action choices
    # If mood reaches 6 (happy), the game ends
    # If mood reachs 0, the game ends
    # User can choose to replay or exit game
while True:
    print('NEKO-NEKO: a text-based adventure about taking care of a needy cat ^_^')
    print('Can you make Neko happy?')
    print('Respond to her mood by choosing actions.')
    
    # generate a random starting mood, each integer correlates to a different mood below
    mood = random.randrange(1, 6)
    # action_choice will be printed each time a mood function is called
    action_choice = 'Choose an action: (f)eed, (l)eave alone, let (o)utside, (p)lay with, (s)nuggle, or (q)uit'

    # checks current mood value and passes it to the correct function
    while True:
        if mood == 1:
            mood = mad(mood)
        elif mood == 2:
            mood = wild(mood)
        elif mood == 3:
            mood = hungry(mood)
        elif mood == 4:
            mood = bored(mood)
        elif mood == 5:
            mood = sleepy(mood)
        elif mood == 0: # if mood reaches 0, Neko runs away and game ends
            print()
            print('Oh no! It looks like Neko ran away...Game over!')
            break
        else: # mood == 6, Neko is happy and game ends
            print()
            print('Neko is happy - you win!')
            break
    
    # gives user the option to replay or quit
    print()
    print('Would you like to play again? y/n')
    replay = input()
    if replay == 'y':
        continue
    if replay == 'n':
        print('Thanks for playing!')
        quit()