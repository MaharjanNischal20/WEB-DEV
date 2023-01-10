num = 0

while num<=20:
    num+=1
    if num == 12:
        break
    print(num)


list = ["Banana","Apple","Pommegranate","Avocado","Chicken"]

for food in list:
    if food == "Pommegranate":
        continue   # skip jasari kaam garxa yusle.
    print(food)

num = 0

while num<=20:
    num+=1
    if num % 2==0:
        continue
    print(num)