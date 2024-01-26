for i in range(1, 20):
    message = ""
    if i % 3 == 0:
        message += "Fizz"
    if i % 5 == 0:
        message += "Buzz"
    print(message)