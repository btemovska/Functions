def multiply(x, y):
    result = x * y
    # return result  >> this makes is None


def is_palindrome(string):
    return string[::-1].casefld() == string.casefold()

def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    return is_palindrome(string)

answer = multiply(18,3)
print(answer) #54

