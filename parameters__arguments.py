def multiply(x, y):  #x & y are parameters
    result = x * y
    return result


answer = multiply(10.5, 4)  #10.4 and 4 are the arguments passed to the parameter
print(answer) #42.0

forty_two = multiply(6, 7)
print(forty_two) #42

for val in range(1,5):
    two_times = multiply(2, val)
    print(two_times)
# 2
# 4
# 6
# 8
