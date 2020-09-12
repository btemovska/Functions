LOW = 1
HIGH = 1023


def guess_binary(answer, low, high):
    guesses = 1
    while True:
        guess = low + (high - low) // 2
        if guess < answer:
            low = guess + 1
        elif guess > answer:
            high = guess - 1
        elif guess == answer:
            return guesses
        guesses += 1

correct_count = 0
max_guesses = 0
for number in range(LOW, HIGH + 1):
    number_of_guesses = guess_binary(number, LOW, HIGH)
    print("{} guessed in {}".format(number, number_of_guesses))

    if number_of_guesses > max_guesses:
        max_guesses, correct_count = number_of_guesses, 1
    elif number_of_guesses == max_guesses:
        correct_count += 1

print("I guessed without being told {} times. Max {} guesses."
      .format(correct_count, max_guesses))


# 1 guessed in 9
# 2 guessed in 10
# 3 guessed in 8
# 4 guessed in 10
# 5 guessed in 9
# 6 guessed in 10
# 7 guessed in 7
# 8 guessed in 10
# 9 guessed in 9
# 10 guessed in 10
# 11 guessed in 8
# 12 guessed in 10


# 1020 guessed in 8
# 1021 guessed in 10
# 1022 guessed in 9
# 1023 guessed in 10
# I guessed without being told 512 times. Max 10 guesses.