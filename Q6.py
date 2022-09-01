def printWords(l):
    # for loop for iterating
    for i in l:
        print(i)

# Given Sentence
str = "I am a teacher and I love to inspire and teach people"

# storing string in the form of list of words
s = set(str.split(" "))

# passing list to print words function
printWords(s)