class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.age = age
        self.breed = breed

class GuardDog(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed, 50)
        # super는 부모(Dog)의 클래스를 참조한다.

    def rrrrr(self):
        print("stay away")

class Puppy(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed, 2)
        # super는 부모(Dog)의 클래스를 참조한다.
    
    def woof_woof(self):
        print("Woof Woof!")


ruffus = Puppy(name = "Ruffus", breed = "Beagle")
bibi = GuardDog(name = "Bibi", breed = "Dalmathian")

ruffus.woof_woof()
# Woof Woof!

bibi.rrrrr()
# stay away
