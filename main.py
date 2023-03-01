import random

# Moods
def mad(mood):
    print('Neko is mad.') #print current mood
    print('Enter a lowercase letter: (f)eed, (p)lay, (s)nuggle, (l)eave alone') #prompt user input and display options
    action = input() #accept user input, then check it, print a result, and return to while loop
    if action == 'f':
        print('Neko walked away with disinterest! Try again.')
        return mood #incorrect action, return the same mood value to the loop to try again
    elif action == 'p':
        print('Neko simply blinks at you with an air of superiority! Silly human, try again.')
        return mood #incorrect action, return the same mood value to the loop to try again
    elif action == 's':
        print('Neko bit you, ouch! Try again.')
        return mood #incorrect action, return the same mood value to the loop to try again
    elif action == 'l':
        print('Neko is pleased that you respected their boundaries. (Mood has improved.)')
        return mood + 1 #this is the correct action for this mood, mood increases by 1

def hungry(mood):
    print('Neko is hungry.') #print current mood
    print('Enter a lowercase letter: (f)eed, (p)lay, (s)nuggle, (l)eave alone') #prompt user input and display options
    action = input() #accept user input, then check it, print a result, and return to while loop
    if action == 'f':
        print('Neko eats all of the food! (Mood has improved)')
        return mood + 1 #this is the correct action for this mood, mood increases by 1
    elif action == 'p':
        print('Neko gnaws on the toy! I wonder what it tastes like? Try again.')
        return mood #incorrect action, return the same mood value to the loop to try again
    elif action == 's':
        print('Neko stares daggers at you! Try again.')
        return mood #incorrect action, return the same mood value to the loop to try again
    elif action == 'l':
        print('Neko nips your ankle! Try again.')
        return mood #incorrect action, return the same mood value to the loop to try again

def bored(mood):
    print('Neko is bored.') #print current mood
    print('Enter a lowercase letter: (f)eed, (p)lay, (s)nuggle, (l)eave alone') #prompt user input and display options
    action = input() #accept user input, then check it, print a result, and return to while loop
    if action == 'f':
        print('Neko plays with the food and makes a mess! Try again.')
        return mood #incorrect action, return the same mood value to the loop to try again
    elif action == 'p':
        print('Neko pounces on the toy with glee! (Mood has improved.)')
        return mood + 1 #this is the correct action for this mood, mood increases by 1
    elif action == 's':
        print('Neko offers a belly... but its a trap! Try again.')
        return mood #incorrect action, return the same mood value to the loop to try again
    elif action == 'l':
        print('Neko scratches at the furniture! Try again.')
        return mood #incorrect action, return the same mood value to the loop to try again

def sleepy(mood): 
    print('Neko is sleepy.') #print current mood
    print('Enter a lowercase letter: (f)eed, (p)lay, (s)nuggle, (l)eave alone') #prompt user input and display options
    action = input() #accept user input, then check it, print a result, and return to while loop
    if action == 'f':
        print('Neko sniffs at the food before deciding it would take too much energy to eat now. Try again.')
        return mood #incorrect action, return the same mood value to the loop to try again
    elif action == 'p':
        print('Neko lazily bats at the toy a few times before ignoring you! Try again.')
        return mood #incorrect action, return the same mood value to the loop to try again
    elif action == 's':
        print('Neko purrs contentedly and drifts off to sleep in your lap. (Mood has improved.)')
        return mood + 1 #this is the correct action for this mood, mood increases by 1
    elif action == 'l':
        print('Neko hides under the bed and naps alone! Try again.')
        return mood #incorrect action, return the same mood value to the loop to try again

print('Neko neko! ^_^')
print('Can you make Neko happy?')
print('Respond to her mood.')

# generate a random number that correlates to different moods
mood = random.randrange(1, 5)

# check what the current mood value is and pass it to the correct function
# if the correct action is taken within a fuction, the mood will increase value
# if mood reaches 5 (happy), the program ends
while True:
    if mood == 1:
        mood = mad(mood)
    elif mood == 2:
        mood = hungry(mood)
    elif mood == 3:
        mood = bored(mood)
    elif mood == 4:
        mood = sleepy(mood)
    else: # if mood reaches 5, Neko is happy and program ends
        break

print('Yay! Neko is happy!')