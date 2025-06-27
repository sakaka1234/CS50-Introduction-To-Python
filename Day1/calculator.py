
# x = float(input("What's x ? "))
# y = float(input("What's y ? "))
# z = round(x/y,2)
# k = x / y
# print(z)
# print(f"{k:.2f}")
def main():
    x = int(input("What's x :"))
    print("x squared is", square(x))

def square(x):
    return int(x**2)

main()