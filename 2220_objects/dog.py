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
print(toby)
toby.bark()

hotDog = Dog("HotDog", 10, 3)
print(hotDog)
hotDog.bark()


class AssistanceDog(Dog):
    def __init__(self, name, age, weight, owner):
        Dog.__init__(self, name, age, weight)
        self.owner = owner     
        # private attribute (__ before name)
        self.__working = False   
    
    def __str__(self):
        return "assistance name: {}, with owner: {}".format(self.name, self.owner)
    
    def walk(self):        
        print("walking with {} :)".format(self.owner))

    def bark(self):
        if self.__working == True:
            print("I cant bark! Im working dude! ¬¬")  
        else:
            Dog.bark(self)

    def working(self, value = None):
        if value == None:
            return self.__working
        else:
            self.__working = value


helper = AssistanceDog("Santa´s Little Helper", 10, 8, "Homer")
print(helper)
helper.bark()
helper.walk()
# setter call
helper.working(True)
helper.bark()
# setter call
helper.working(False)
helper.bark()
# just fail, tha attribute is hidden, well not truly..
# print(helper.__working)
# you can counsult...
print(helper._AssistanceDog__working)
# Or.. correctly, use the getter
# getter call
print(helper.working())
