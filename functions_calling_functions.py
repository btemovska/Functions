def is_palindrome(string):
    return string[::-1].casefold() == string.casefold()

def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string) #dogeeseseegod
    # return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)

word = input("Please enter word to check: ")
if palindrome_sentence(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))

    