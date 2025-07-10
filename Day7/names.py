# name = input("What's your name ? ")
# with open("names.txt","a") as file:
#     file.write(f"{name}\n")
names = []
with open("names.txt") as file: # default reading the file 
#     lines = file.readlines()
# for line in lines:
#     print("hello,",line.rstrip())

#     for line in file:
#         names.append(line.rstrip())

# for name in sorted(names):
#     print(name)
    for line in sorted(file,reverse=True):
        print("hello,",line.rstrip())
    