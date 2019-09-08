guests = ['1', '2', '3', '5', '6', '7']
# print(guests)
# for a in guests:
#     message = a + ", please come to my house for dinner"
#     print(message)
# print(guests)
# print('\nscott can not make the dinner party')
# not_coming = 'scott'
# guests.remove(not_coming)
# guests.append('tom')
# print(guests)
# for a in guests:
#     message = a + ", please come to my house for dinner"
#     print(message)
# print(guests)
#
# print("\nI have found a bigger table for us. I'm going to invite more people!")
# guests.insert(0, "Jane")
# guests.insert(2, "Ozzy")
# guests.append("Me")
# print(guests)
# for a in guests:
#     message = a + ", please come to my house for dinner"
#     print(message)
# print(guests)

print("\nOur Table won't arrive in time for all the guests. I'm sorry but I must cancel the dinner and only invite "
      "two people")
print(guests)

# for a in guests:
#     print("guest = " + a)
#     popped_guest = guests.pop()
#     print("popped_guest = " + popped_guest)
#     print(guests)

while len(guests) > 2:
    guest_popped = guests.pop()
    print("I'm sorry, " + guest_popped + ", the restaurant is out of seating. I will invite you to my next dinner.")
    print(guests)

while len(guests) >= 1:
    guest_popped = guests.pop()
    print("Don't worry, " + guest_popped + ", You're my favs so you are still invited!")
    print(guest_popped)
    print(guests)
