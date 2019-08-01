#pet = {
    #"name": "Doggo",
    #"animal": "dog",
    #"species": "laborador",
    #"age": 5
#}

#class Pet(object):
    #def __init__(self, name, age):
        #self.name = name
        #self.age = age

#my_pet = Pet ("Fido", 3)
#print("My pet %s is %s years old" % (my_pet.name, my_pet.age))

#my_pet2 = Pet ("Furry", 5)
#print("My pet %s is %s years old" %(my_pet2.name, my_pet2.age))
#my_pet3 = Pet ("cat", 200)
#print("My pet %s is %s years old" %(my_pet3.name, my_pet3.age))

class Pet(object):
    def __init__(self, name, age, animal, location):
        self.name = name
        self.age = age
        self.animal = animal
        self.is_hungry = False
        self.mood = "happy"
        self.location = "room1"


    def eat(self):
        print("> %s is eating...." % self.name)
        if self.is_hungry:
            self.is_hungry = False
        else:
            print("> %s may have eaten too much." % self.name)
            self.mood = "lethargic"

    def move(self):
        print("> %s is moving..." % self.location)
        if self.location = "room1"
            self.location = "room2"
        else:
            self.location = "room2"
            print("> is in %s " % self.name, self.location)


my_pet = Pet("Fido", 3, "dog")

my_pet.is_hungry = True
print("Is my pet hungry? %s" % my_pet.is_hungry)
my_pet.eat()
print("How about now? %s" % my_pet.is_hungry)
print("My pet is feeling %s" % my_pet.mood)
