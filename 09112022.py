# test1 = 28
#
# if test1 > 0:
#     print(" Yeah buddy! ")
# else:
#     print(" On the money! ")
#
# age = 21
# name = "Jane"
#
# if age >= 21:
#     print("Congrats" + name + "you can vote")
#
# elif age < 21:
#     print("Sorry" + name + "You are too young")

foods = ['cookies', 'jam', 'orange']
# foods.reverse()
# print(foods)

# for food in foods:
#     print("I love" + food + "!")

# numbers = []
# for value in range(2,6):
#     numbers.append(value)
# print(numbers)

siblings = {'Jessica': 'cookies', 'Christian': 'food', 'Gaby': 'Peanut Butter'}

# print(siblings['Jessica'])

# favorite_foods = []
# for key, value in siblings.items():
#     favorite_foods.append(value)
#     print(favorite_foods)

# sibling_list = []
#
# for name, food in siblings.items():
#     sibling_list.append(name)
#     print(sibling_list)


sibling_1 = {'Jessica': 'cookies', 'age': '30'}
sibling_2 = {'Christian': 'food', 'age': '23'}
sibling_3 = {'Gaby': 'Peanut Butter', 'age': '21'}

siblings = [sibling_1, sibling_2, sibling_3]

# print(siblings)
#
# for sibling in siblings:
#     print(sibling)

# sib = []
# for sibling in siblings:
#    sib.append(sibling.values())
#    print(sib)

pizza = {
    'crust': 'thick',
    'cheese': 'sharp',
    'toppings': ['pineapple', 'extra cheese']
}

# print(pizza['cheese'])
# print(pizza['toppings'][1])

pizza_types = {
    'first_pizza': {
        'crust': 'thick',
        'cheese': 'sharp',
        'toppings': ['pineapple', 'extra cheese']
    }
}


# print(pizza_types['first_pizza']['crust'])
# print(pizza_types['first_pizza']['toppings'])
# print(pizza_types['first_pizza']['toppings'][0])

# print("name")
# name = input("Please enter your name: ")
# print('Hello ' + name)

# responses = {}
# polling_is_active = True
#
# while polling_is_active:
#     name = input("Please enter your name: ")
#     response = input("What country do you want to go to? : ")
#
#     responses[name] = response
#
#     repeat = input("Would you like to add another person? (yes/no) ")
#
#     if repeat == 'no':
#         polling_is_active = False
#
#     for name, response in responses.items():
#         print(name + "would like to go to " + response)

def say_hello(user):
    print("Oh hey!")
    say_hello(user)
