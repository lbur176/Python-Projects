nums_tested = range(-50,51)

for num in nums_tested:
    if num % 15 == 0 and num != 0:
        print("Fizzbuzz")
    elif num % 3 == 0 and num != 0:
        print("Fizz")
    elif num % 5 == 0 and num != 0: 
        print("Buzz")
    else: 
        print(num)