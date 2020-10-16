
# Loop through the numbers 1 to 100
for num in range(1, 101):
    result = ""
    # First check if it is both a multiple of 3 and 5 and print FizzBuzz if so
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    # If it's not both, check first if it's a multiple of 3 and print Fizz if so
    elif num % 3 == 0:
        print("Fizz")
    # If it's not both or a multiple of three but is a multiple of 5, print Buzz
    elif num % 5 == 0:
        print("Buzz")
    # If it's not a multiple of either, print the number
    else:
        print(num)
