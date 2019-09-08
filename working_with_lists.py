print('-----slicing a list-----')
players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0:3])
# print(players[1:4])
# print(players[:4])
# print(players[2:])

print('\n-----looping through a slice-----')
print("Here are the first 3 players on my team:")
for players in players[:3]:
    print(players.title())

print('\n-----copying a list-----')

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('canoli')
friend_foods.append('ice cream')

print('My favorite foods are:')
print(my_foods)

print('\nMy friends favorite foods are:')
print(friend_foods)
print('\n-----working with tuples-----')
print('\n\n-----dimensions-----')

dimensions = (200, 50)
# print(dimensions[0])
# print(dimensions[1])
#
# # Looping through all values in a Tuples
# for dimension in dimensions:
#     print(dimension)

print('Original dimensions:')
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print('\nModified dimensions:')
for dimension in dimensions:
    print(dimension)

print('\n-----Tuples Try It Yourself-----')
menu = ('fried eggs', 'hamburgers', 'steak', 'shakes', 'waffles')

print('ORIGINAL MENU:')
for menu in menu:
    print(menu)

print('\nNEW MENU:')
menu = ('grilled cheese', 'hamburgers', 'steak', 'shakes', 'fish')
for menu in menu:
    print(menu)