x = input("Provide an int b/w -50 and 50: ")

try:
    a = int(x)

    if a < 51 and a > -51:
        if a % 15 == 0 and a != 0: 
            print("Fizzbuzz")
        elif a % 3 == 0 and a != 0: 
            print("fizz")
        elif a % 5 == 0 and a != 0:
            print("buzz")
        else:
            print(a)
    else:
        print("NOT IN RANGE")

except:
    print ("NOT AN INT")