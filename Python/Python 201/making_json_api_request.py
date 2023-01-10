import requests

req = requests.get('https://swapi.dev/api/people/2/')
person = req.json()                                     #JSON ma encoded bhako lai decode garera person ma value pass gardinxa
print(f"The name of person is:\t\t\t{person['name']}") 
print(f"The eye_color of person is:\t\t{person['eye_color']}") 
print(f"The height of person is:\t\t{person['height']}") 

print("The films involved are")
for film in person['films']:  # yo loop ma bhako 'film' word le counter ko kaam garxa, ani jati ota films hunxa tyati choti request garxa,yo request ko counter film banidinxa.
    req=requests.get(film)   #films bhanne sab link bhako hunale tyaslai pani feri request garera json ma convert gareko ho.
    film = req.json()  #feri json ma convert gareko kinaki tyo link pani euta json file nai ho
    print("Flim is:     ",film['title'])  #tyo films ko link ma thiche paxi link ko title hunxa, ho tyai title yusma print gareko.
