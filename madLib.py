"""madLib.py

    Dylan Grandjean
    September 19th, 2016

    This program manipulates lists.

    Enter the parts of speech asked for and the program will put them into a mad lib for you
"""
"""
# List instantiation and decleration
sentences = ["There once lived %s %s who wanted more than anything to be %s"]   # Sentence to be displayed on screen
vowels = ["a", "e", "i", "o", "u"]                                              # Check values for words starting with a vowel

words = []                                                                      # List of user input

# Prompt user for an adjective and tests it
word = raw_input("Please enter an adjective > ").lower()
if word[0] in vowels:
    words.append("an " + word)
else:
    words.append("a " + word)

#Prompt user for a noun and stores it into words[]    
words.append(raw_input("Please enter a noun > "))

# Prompt user for a noun and tests it
word = raw_input("Please enter a noun > ").lower()
if word[0] in vowels:
    words.append("an " + word)
else:
    words.append("a " + word)

# Print sentence to consol
print sentences[0] %(words[0], words[1], words[2])


""""""------------------------------------------------------------------------------------------
"""# Import the random class
import random
# Initialize random module
random.seed()

# List of pre-made sentences to use in this program
sentences = ["There once lived %s %s who wanted more than anything to be %s",
             "Did you know that being %s was the only similarity between %s and %s?",
             "%s %s is just as untrustworthy as %s!"]

# List of vowels for test
vowels = ["a", "e", "i", "o", "u"] 

# List of words given by the user
words = []

playing = True

while playing:
    adj = raw_input("Please enter an adjective > ").rstrip()
    noun1= raw_input("Please enter a noun > ").rstrip()
    noun2 = raw_input("Please enter a noun > ").rstrip()

    num = random.randint(0, 2)
    sentence = sentences[num]

    if num == 0:
        if adj[0] in vowels:
            words.append("an " + adj)
        else:
            words.append("a " + adj)      
        words.append(noun1)    
        if noun2[0] in vowels:
            words.append("an " + noun2)
        else:
             words.append("a " + noun2)
             
    elif num == 1:
        words.append(adj)  
        if noun1[0] in vowels:
            words.append("an " + noun1)
        else:
            words.append("a " + noun1)     
        if noun2[0] in vowels:
            words.append("an " + noun2)
        else:
            words.append("a " + noun2)
            
    elif num == 2:
        if adj[0] in vowels:
            words.append("An " + adj)
        else:
            words.append("A " + adj)
        words.append(noun1)
        if noun2[0] in vowels:
            words.append("an " + noun2)
        else:
             words.append("a " + noun2)

    print sentence %(words[len(words) - 3], words[len(words) - 2], words[len(words) - 1])
    answer = raw_input("\nWanna go again? (Y/N) ").lower()
    while answer != "y" and answer != "n":
        answer = raw_input("Please, enter a valid answer.")
    if answer[0] == "n":
        playing = False
        print "Just for fun, let's look at all the crazy words you gave me:"
        x = 0
        y = 1
        for word in words:
            print str(y) + ". " + word
            x = x + 1
            y = y + 1
            if x == 3:
                print "\n"
                x = 0
""""""
