import random
class character(object):
   print(" ")
class Monster(character):
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

class Ally(character):
  def __init__(self, name, Health, Dialogue):
      

      self.name = name

      self.Health = Health

      self.Dialogue = Dialogue
      
#     Do I really need to define all these methods again????
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
     print("Your companion bellows:", self.Dialogue)
  def damage(self):
     print (self.Health - (random.randint(1,100)))
Monster1 = Monster("Garry", 100, "aaaaa I'm big and scary, fear me human")
Monster1.describe()
Monster1.speak()
Monster1.damage()

Ally1 = Ally("Hercules",1000, "I'LL SAVE YOU")
Ally1.describe()
Ally1.speak()
Ally1.damage()
