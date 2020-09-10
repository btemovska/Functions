def is_palindrome(string: str) -> bool:
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence: str) -> bool:
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    return is_palindrome(string)


p = palindrome_sentence("hello")

#another example
def fibonacci(n: int) -> int:
    """Return the `n` th Fibonacci number, for positive `n`."""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))

#another example
def multiply(x: float, y: float) -> float:
    result = x * y
    return result
