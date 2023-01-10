class Animal:

    def __init__(self,fur_color): # double underscore means dunder method which will be called first than other functions.
        self.fur_color = fur_color

    def chase(self,animal="mouse"):
        print("I am chasing a ",animal)

class HouseCat(Animal):

    def get_fur_color(self):
        print(f"The color of cat was {self.fur_color}")

    def chase(self, animal):
        super().chase(animal)
        print(animal,"was caught")

cat=HouseCat("Black and White") #once dunder method is applied we can pass the parameter in the class object
cat.chase("cockroach")
cat.get_fur_color()