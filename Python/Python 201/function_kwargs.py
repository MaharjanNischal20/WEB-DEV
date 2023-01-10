def food_delivery(name,address,**kwargs): #here kwargs acts as a item of burger
    print("The name of food is ",name)
    print("The address to be deliver is ",address)
    price= 15.00
    for key,value in kwargs.items():  #kwargs is a dictionary
        price = price + 2.00
    print(f"The total price is {price}")

total_bill = food_delivery('burger','Lalitpur',ham=True,extra_cheese=True)


