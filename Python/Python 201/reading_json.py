import json

C3PO = '''{
    "name": "C-3PO", 
    "height": "167", 
    "mass": "75", 
    "hair_color": "n/a", 
    "skin_color": "gold", 
    "eye_color": "yellow", 
    "birth_year": "112BBY", 
    "gender": "n/a", 
    "homeworld": "https://swapi.dev/api/planets/1/", 
    "films": [
        "https://swapi.dev/api/films/1/", 
        "https://swapi.dev/api/films/2/", 
        "https://swapi.dev/api/films/3/", 
        "https://swapi.dev/api/films/4/", 
        "https://swapi.dev/api/films/5/", 
        "https://swapi.dev/api/films/6/"
    ], 
    "species": [
        "https://swapi.dev/api/species/2/"
    ], 
    "vehicles": [], 
    "starships": [], 
    "created": "2014-12-10T15:10:51.357000Z", 
    "edited": "2014-12-20T21:17:50.309000Z", 
    "url": "https://swapi.dev/api/people/2/"
}'''

C3PO = json.loads(C3PO)  #loads stands for load string
print(C3PO['name'])
C3PO['name'] ="Nischal Maharjan"
C3PO_str =  json.dumps(C3PO)        #dump string
print(C3PO)         #dumps() method allows you to convert a python object into JSON and additionally allows you to store the information into a file (text file)