# cat-adventure
A simple text-based adventure about taking care of a needy cat named Neko.
Can you make Neko happy?

Neko has 4 possible starting moods in this iteration:
1. Mad
2. Hungry
3. Bored
4. Sleepy

When the program first runs, a random starting mood is determined.
Each mood prompts the user to respond with an action:
(f)eed
(p)lay
(s)nuggle
(l)eave alone

Actions return a text-based response from Neko. 
If you use the correct action for the current mood, the mood value will increase by one step.
If you use the incorrect action, then the mood value does not change and the user is prompted to try again.
If the mood ever reaches a value of 5, then Neko is happy and the program ends.

Improvements to be made:
1. Input validation to only accept letters f, p, s and l
2. More moods and actions!
