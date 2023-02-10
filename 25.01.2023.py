#                           OOP

class Pet(object):
    def __init__(self, name, species, description):
        self.name = name

        self.species = species

        self.description = description

    def get_name(self):
        return self.name
    def get_species(self):
        return self.species
    def get_description(self):
        return self.description
    def describe (self):
      print (self.name, "is a", self.species, "and is a", self.description)
    def set_name(self):
      name = input(("enter name"))
      self.name = name
    def set_species(self):
      species = input(("enter species"))
      self.species = species  
    def set_description(self):
      description = input(("enter description"))
      self.description = description
			

Pika = Pet("Pikablue", "budgie", "smol birb")
Pika.set_name()
Pika.set_species()
Pika.set_description()
Pika.describe()
