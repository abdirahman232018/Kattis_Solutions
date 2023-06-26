import random

# Read the number of set menus
num_menus = int(input())

# Read the details of each set menu
menus = []
for _ in range(num_menus):
    menu_details = input().split()
    num_dishes = int(menu_details[0])
    dishes = menu_details[1:]
    assert num_dishes == len(dishes)
    menus.append(dishes)

# Randomly select a set menu
recommended_menu = random.choice(menus)

# Print the recommended menu
print(len(recommended_menu))
for dish in recommended_menu:
    print(dish)