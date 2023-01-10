class animal:
    fur_color="It depends upon the animal"

    def speak(self):
        print("Roaaarrrrr!!")

class tiger(animal):
    fur_color = "Orange and black"

    def speak(self):
        print("roar!")

tgr=tiger()
tgr.speak()