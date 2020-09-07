def is_palindrome(string):
    # backwards = string[::-1] #reverses the original string
    # return backwards == string #check to see if it is the same as the original
    return string[::-1].casefold() == string.casefold()


word = input("Please enter a word to check: ")
if is_palindrome(word.case):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))
#'racecar' is a palindrome
# 'python' is not a palindrome

