class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def bark(self):
        if self.weight >= 8:
            print("woof-woof")
        else:
            print("yip-yip")
    
    def __str__(self):
        return "name: {}, age: {} and weight: {}".format(self.name, self.age, self.weight)

def bark(self):
    print("I aint got no dog!") 

toby = Dog("Toby", 8, 12)
toby.bark()
print(toby)

hotDog = Dog("HotDog", 10, 3)
hotDog.bark()
print(hotDog)