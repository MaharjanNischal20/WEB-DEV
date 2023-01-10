#normal method
number = []

for num in [1,2,3,4,5]:
    number.append(num**2)
print(number)



#list comprehensions process
numbers = []

numbers = [num**2 for num in [1,2,3,4,5]] #this method is known as list comprehension.
print(numbers)