class animal:
    this_is_a_property= {
        'key1':"value1"
    }
    another_property = ['nischal','asmit','amrit','sakshyam']

    def add_name(self,name):
        return self.another_property.append(name)

    
    def this_is_a_method(self):
        print(self.this_is_a_property['key1'])

    @property #decorator use garisakepaxi bracket lekhnu pardaina call garda kheri.
    def get_me(self):
        return self.another_property[0]


the_animal = animal()
the_animal.add_name('maharjan')
print(the_animal.another_property)
the_animal.this_is_a_method()
print(the_animal.get_me)