recipes = [['fire', 'water', 'smoke'],  ['water', 'earth', 'plant'], ]

elements = ['fire', 'water', 'earth']

print('Which two elements:')
print('Element 1: ', end='')
elem1 = input().lower().strip()
print('Element 2: ', end='')
elem2 = input().lower().strip()

if elem1 in elements:
    if elem2 in elements:
        print("Ok, let me mix them and see the result")
    else:
        raise ValueError(f"Sorry, you're missing {elem2}")
else:
    raise ValueError(f"Sorry, you're missing {elem1}")

result_element = None

for recipe in recipes:
    if (elem1 == recipe[0] and elem2 == recipe[1]) or (elem2 == recipe[0] and elem1 == recipe[1]):
        result_element = recipe[2]
        break

if result_element:
    print(f"Great, you discovered {result_element}")
else:
    print("Sorry, that didn't worked")

