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

Pika = Pet("Pikablue", "budgie", "smol birb")
print(Pika.name,Pika.species, Pika.description)
    
