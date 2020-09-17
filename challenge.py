def sum_numbers(*values: float) -> float:
    """ calculates the sum of all the numbers passed as arguments """
    result = 0
    for number in values:
        result += number
    return result


print(sum_numbers(1, 2, 3)) #6
print(sum_numbers(8, 20, 2)) #30
print(sum_numbers(12.5, 3.147, 98.1)) #113.747
print(sum_numbers(1.1, 2.2, 5.5)) #8.8

print()


def sum_numbers_2(*values: float) -> float:
    """ calculates the sum of all the numbers passed as arguments """
    return sum(values)


print(sum_numbers_2(1, 2, 3))
print(sum_numbers_2(8, 20, 2))
print(sum_numbers_2(12.5, 3.147, 98.1))
print(sum_numbers_2(1.1, 2.2, 5.5))