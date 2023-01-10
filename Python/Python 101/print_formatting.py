name = "Nischal"

#method 1
welcome_message = "Hi {}, How are you??".format(name)

print(welcome_message)

#method 2
welcome_message = f"Hi {name}, How are you??"

print(welcome_message)

#method 3 (old method)
welcome_message = "Hi %s, How are you??"% name

print(welcome_message)
