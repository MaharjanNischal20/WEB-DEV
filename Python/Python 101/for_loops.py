food_items = ['Samosa','MoMo','Chowmein','Pizza']

for food in food_items:
    print(food)

for food in food_items:
    if food == 'Pizza':
        size = input("What size of pizza would you like to order, sir?? ")
        print(f"You ordered {size} of pizza")


food = "Pizza!"
for letters in food:
    print(letters)


person = {
    'name':'Nischal',
    'age':20,
    'address':'Agnishala'
}

for key,value in person.items():
    print(f"Here the key is {key} and value is {value}")


