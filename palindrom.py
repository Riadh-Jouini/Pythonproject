#python program : determine if palindrom

user_input = str(input("Hey user, enter anything and we'll let you know if it's a palindrom :)\n"))
user_input_reversed = user_input[::-1]

def ispalindrom():
    if user_input==user_input_reversed:
        print(f"Yep, it's a palindrom")
    else:
        print(f"Nope")

ispalindrom()

print("thanks for trying my simple code")
