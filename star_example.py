numbers = (0, 1, 2, 3, 4, 5)

print(numbers) #(0, 1, 2, 3, 4, 5)
print(*numbers) #0 1 2 3 4 5

print(numbers, sep=";") #(0, 1, 2, 3, 4, 5)
print(*numbers, sep=";") #0;1;2;3;4;5

print()

def test_star(*args):
    print(args) #(0, 1, 2, 3, 4, 5)
    for x in args:
        print(x) #puts them in each row


test_star(0, 1, 2, 3, 4, 5)

print()
test_star() #() empty tuple


