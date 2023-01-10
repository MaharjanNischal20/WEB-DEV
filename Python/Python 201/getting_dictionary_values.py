courses = {
    "js":"JS 101",
    "Html":["HTML 101", "HTML 201"],
    "python":["python 101", "python 201"]
}

if courses.get('python',None): #here 'None' is a default value,If there is no Html present in the dict, then it is assigned.
    print("You are enrolled")


if courses.get('CSS',None): #since CSS is not in dict so None is assigned
    print("You are enrolled")
