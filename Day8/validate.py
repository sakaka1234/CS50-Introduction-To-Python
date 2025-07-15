import re
email = input("What's your name ?").strip().lower()
#[a-zA-Z0-9] = \w
if re.search(r"^\w+@(\w+\.)?\w+\.(com|gov|edu|net|org)$",email):
    print("Valid")
else:
    print("Invalid")

