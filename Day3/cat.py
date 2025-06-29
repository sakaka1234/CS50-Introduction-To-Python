def main():
    n = get_number()
    meow(n)

def get_number():
    while True:
        n = int(input("What's number? "))
        if n > 0:
            return n
def meow(n):
    for _ in range(n):
        print("Meow")

main()