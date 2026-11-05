def say_hello():
    return "hello world"


count = int(input("How many greetings? "))

if count >= 1:
    for _ in range(count):
        print(say_hello())
else:
    print("Nothing to print")
