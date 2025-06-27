

#ask user for their name 
def main():
    name = input("Enter your name: ").strip().title()
    # Remove any leading or trailing whitespace and title it
    hello()
    hello(name)
    first, last = name.split(" ")
    print("hello, ", end="")
    print(name)
    print(f"hello, {name}")
    print(first)
    print(last)

def hello(to = "world"):
    print("hello",to)

main()