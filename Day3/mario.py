def main():
    print_square(5)
def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#",end="")
        print()
main()