file_name = input("What is the filename?? ")
content = input("What content you want to write?? ")

with open(file_name,'w') as file:
    file.write(content)


opn_file = input("Do you want to read the file?")
if opn_file in ['y','yes']:
    with open(file_name,'r') as file:
        print(file.read())

else:
    exit()
