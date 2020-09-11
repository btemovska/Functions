# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


# print(RED,"this would be in red")
# print("and so is this")
# #even though we did not specify, it takes the color from above
# print(MAGENTA, "This is a different color")
# print(CYAN, "this is another color")


def colour_print(text: str, effect: str) -> None:
    """
    Print `text` using hte ANSI sequences to change colour, etc
    :param text: Text to print.
    :param effect: The effect we want. One of the constants
        defined at the start of this module.
    """
    output_string = "{0}{1}{2}".format(effect, text, RESET)
    print(output_string)


colour_print("Hello, Red", RED)
print("This should be in the default terminal colour")
colour_print("Hello Blue", BLUE)
colour_print("Hello Yellow", YELLOW)
colour_print("Hello Bold", BOLD)

