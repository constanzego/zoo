class Zoo:
    def __init__(self, zoo_name) -> None:
        self.animals = []
        self.name = zoo_name 
    def add_lion(self, name, age=0, happiness=1, health=0, color="brown" ):
        self.animals.append( Lion(name, age, happiness, health, color) )
        
    def add_tiger(self, name, age=0, happiness=1, health=0, size= 200 ):
        self.animals.append( Tiger(name, age, happiness, health, size) )
    def add_zebra(self, name, age=0, happiness=1, health=0, sex = "female"):
        self.animals.append( Zebra(name, age, happiness, health, sex) )
    def feed(self):
        for animal in self.animals:
            animal.eat()
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
            
class Animal:
    def __init__(self, name, age, happiness, health):
        self.animals = []
        self.name = name
        self.age = age
        self.happiness = happiness 
        self.health = health
    
    def eat (self):
        self.health = self.health + 10
        self.happiness =self.happiness + 10  
    
    def display_info(self):
        print("Name: ", self.name, "Age: ", self.age,"Health: ", self.health, "Happiness: ", self.happiness)
        for animal in self.animals:
            animal.display_info()
    
class Lion(Animal):
    def __init__(self, name, age, happiness, health, color):
        super().__init__(name, age, happiness, health)
        self.color = color
    def eat(self):
        self.health = self.health + 20
        self.happiness =self.happiness + 20  
    def groom(self):
        self.health = self.health + 50
        self.happiness = self.happiness + 20
    def display_info(self):
        print("Name: ", self.name, "Age: ", self.age,"Health: ", self.health, "Happiness: ", self.happiness, "Color: ", self.color)
        for animal in self.animals:
            animal.display_info()
    
class Tiger(Animal):
    def __init__(self, name, age, happiness, health, size):
        super().__init__(name, age, happiness, health)
        self.size = size
    def eat(self):
        self.health = self.health + 50
        self.happiness =self.happiness + 50  
    def play(self):
        self.health = self.health + 10
        self.happiness = self.happiness + 40
    def display_info(self):
        print("Name: ", self.name, "Age: ", self.age,"Health: ", self.health, "Happiness: ", self.happiness, "Size: ", self.size)
        for animal in self.animals:
            animal.display_info()
    
        
class Zebra(Animal):
    def __init__(self, name, age, happiness, health, sex):
        super().__init__(name, age, happiness, health)
        self.sex = sex
    def eat(self):
        self.health = self.health + 30
        self.happiness =self.happiness + 30  
    def run(self):
        self.health = self.health -20
        self.happiness = self.happiness + 10
    def display_info(self):
        print("Name: ", self.name, "Age: ", self.age,"Health: ", self.health, "Happiness: ", self.happiness, "sex: ", self.sex)
        for animal in self.animals:
            animal.display_info()

zoo1 = Zoo("Zootopia")
zoo1.add_lion("Nala", 1, 100, 100, "black") 
zoo1.add_lion("Simba", 1, 100, 100, "brown")
zoo1.add_tiger("Rajah", 1, 100, 100, "280 cm" )
zoo1.add_tiger("Shere Khan", 1, 100, 100, "250 cm")
zoo1.add_zebra("Rajah", 1, 100, 100, "male")
zoo1.add_zebra("Shere Khan", 1, 100, 100, "female")
zoo1.print_all_info()

zoo1.feed()
zoo1.print_all_info()

print(zoo1.animals)

zoo1.animals[0].groom()
zoo1.animals[2].play()
zoo1.animals[4].run()
zoo1.print_all_info()
