import random

#MOODS
#print current mood
#prompt user input and display options
#accept user input, then check it, print a result, and return to while loop
	#incorrect action, return the same mood value to the loop to try again
	#correct action, mood increases by 1
def mad(mood):
    print('Neko seems to be easily agitated and aloof right now.') 
    print(action_choice) 
    action = input() 
    if action == 'f':
        print('Neko walked away with disinterest! Try again.')
        return mood 
    elif action == 'p':
        print('Neko simply blinks at you with an air of superiority! Silly human, try again.')
        return mood 
    elif action == 's':
        print('Neko bit you, ouch! Try again.')
        return mood - 1
    elif action == 'l':
        print('Neko is pleased that you respected their boundaries. (Mood has improved.)')
        return mood + 1 

def hungry(mood):
    print('Neko keeps following you around and meowing for... somthing?')
    print(action)
    action = input() 
    if action == 'f':
        print('Neko eats all of the food! (Mood has improved)')
        return mood + 1
    elif action == 'p':
        print('Neko gnaws on the toy! I wonder what it tastes like? Try again.')
        return mood 
    elif action == 's':
        print('Neko stares daggers at you! Try again.')
        return mood 
    elif action == 'l':
        print('Neko nips your ankle! Try again.')
        return mood 

def bored(mood):
    print('Neko seems to have a lot of excess energy right now.')
    print(action_choice) 
    action = input() 
    if action == 'f':
        print('Neko plays with the food and makes a mess! Try again.')
        return mood 
    elif action == 'p':
        print('Neko pounces on the toy with glee! (Mood has improved.)')
        return mood + 1 
    elif action == 's':
        print('Neko offers a belly... but its a trap! Try again.')
        return mood
    elif action == 'l':
        print('Neko scratches at the furniture! Try again.')
        return mood

def sleepy(mood): 
    print('Neko seems to have low energy right now.') 
    print(action_choice) 
    action = input()
    if action == 'f':
        print('Neko sniffs at the food before deciding it would take too much energy to eat now.')
        return mood
    elif action == 'p':
        print('Neko lazily bats at the toy a few times before ignoring you!')
        return mood 
    elif action == 's':
        print('Neko purrs contentedly and drifts off to sleep in your lap.')
        return mood + 1 
    elif action == 'l':
        print('Neko hides under the bed and naps alone!')
        return mood

print('Neko-Neko : a text-based adventure about taking care of a needy cat')
print('Can you make Neko happy? All cats are difficult to read, and Neko is no exception.')
print('Respond to her mood by choosing actions. Be careful, too many incorrect actions may make her run away!')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
action_choice = 'Choose an action: (f)eed, (p)lay, (s)nuggle, (l)eave alone'

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
    elif mood == 0: # if mood reaches 0, Neko runs awaw and game ends
        print('Oh no! It looks like Neko ran away...')
        break
    else: # if mood reaches 5, Neko is happy and game ends
        print('Great! You were able to navigate Nekos moods and make her happy.')
        break

print('Would you like to play again? y/n')

