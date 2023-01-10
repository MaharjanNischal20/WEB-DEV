with open('new_file','w') as file:
    file.write("Line 1")
    file.write("\nLine 2")

with open('new_file','a') as file:
    file.write("Appended")