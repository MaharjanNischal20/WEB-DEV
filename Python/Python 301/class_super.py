class Animal:

    def chase(self,animal="mouse"):
        print("I am chasing a ",animal)

class HouseCat(Animal):

    def chase(self, animal):
        super().chase(animal)
        print(animal,"was caught")

cat=HouseCat()
cat.chase("cockroach")