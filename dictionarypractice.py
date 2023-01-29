# Declaring a Dictionary with 2 key/value pairs
person = {'name': 'Sketchy John', 'age': 52} # <-----------------------

# asking for a key to lookup in the dictionary and storing it in 'info_type'
print("What do you want to know about me? (name or age) ", end='')
info_type = input().lower().strip()

# accessing the given key from the dictionary and storing it in 'info'
info = person[info_type]  # <-----------------------

# printing the information
print(f"My { info_type } is { info }")

# <<<< 2ND PART (adding info to the dictionary) >>>>

# Empty dictionary for storing information about yourself
yourself = {} # <-----------------------

# Asking for a key
print(f"Enough about me! What information can you tell me about yourself? (for example 'name') ", end='')
info_type = input().lower().strip()

# Asking for the value
print(f"Ok, so what's your {info_type}? ", end='')
info = input().lower().strip()

while True:
    yourself[info_type] = info # <-----------------------

    print("\nSo Is that it, or there's more to you?")
    print('1. "I\'m not finished..."')
    print("2. That\'s it!")
    theres_more = int(input().lower().strip()) == 1

    # If "That's it" then stop the loop
    if not theres_more:
        break

    # Asking for a key and a value again
    print(f"Ok, what other info about yourself will you tell me? ", end='')
    info_type = input().lower().strip()
    print(f"So what's your {info_type}? ", end='')
    new_info = input().lower().strip()

    # Verifying if a key already exist in the dictionary (before it's updated with the new value)
    if info_type in yourself:  # <-----------------------
        print(f"You already told me that your {info_type} was '{info}'. ")
        print(f"So I'm not sure if you're making fun of me, but ok, I'll forget about what you told me before...\n")

    info = new_info

# Iterating over all the keys and values added to the dictionary
print("\n\nOk then. This is what I know about you: ")
for info in yourself.items():
    print(f"\tYour {info_type} is {info}.")

print("With all this information, I can impersonate you. I'll have fun being you! Bye hahhaha, (malicious laughter)")
