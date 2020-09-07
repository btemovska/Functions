#create a new function called palindrome_sentence
#the function should return True if the sentence is a palindrome
#False if otherwise
#Remember that we ignore spaces, punctuation and things like tabs and line feeds.
#We're only interested in alphanumeric characters.
#Check out the String Methods in the documentation, to find out that's suitable
#for identifying if a character is alphanumeric.

#Was it a car, or a cat, I saw?
#Do geese see god?

def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string) #dogeeseseegod
    return string[::-1].casefold() == string.casefold()

word = input("Please enter word to check: ")
if palindrome_sentence(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))
#'was it a car, or a cat i saw' is a palindrome
#'radar' is a palindrome
# 'python' is not a palindrome
#'do geese see god?' is a palindrome

