import random
class Monster(object):
    def __init__(self, name, Health, Dialogue):
        self.name = name

        self.Health = Health

        self.Dialogue = Dialogue

    def get_name(self):
        return self.name
    def get_Health(self):
        return self.Health
    def get_Dialogue(self):
        return self.Dialogue
    def describe (self):
      print("Name:", self.name)
      print("Health:", self.Health)
    def speak(self):
      print("The monster exclaims:", self.Dialogue)
    def damage(self):
       print (self.Health - (random.randint(1,100)))
Monster1 = Monster("Garry", 100, "aaaaa I'm big and scary, fear me human")
Monster1.describe()
Monster1.speak()
Monster1.damage()