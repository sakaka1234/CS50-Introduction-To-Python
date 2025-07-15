import re
name = input("What's your name ? ").strip()

if matches := re.fullmatch(r"(.+), *(.+)",name):
    last , first = matches.groups()
    #last = matches.group(1)
    #first = matches.group(2)
    name = f"{first} {last}"
print(name)