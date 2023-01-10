#process 1: To convert list containing tuple into dictionary
names = [('name','Nischal'),('address','Agnishala')]
d= {}

for key,value in names:
    d[key]=value    #yesari rakhyo bhane thyakkai 'name':'Nischal' hunxa.Pahila bhanda thyakkai opposite.
print(d)

#process 2: To convert list containing tuple into dictionary using dictionary comprehension
d={key:value for key,value in names}
print(d)

#easiest way
d=dict(names)
print(d)

