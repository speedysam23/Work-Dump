class Monster(object):
    def __init__(self,Name, HP, Dialogue):
        self.Name = Name

        self.HP = HP

        self.Dialogue = Dialogue

    def get_Name(self):
        return self.Name
    def get_HP(self):
        return self.HP
    def get_Dialogue(self):
        return self.Dialogue
    def describe (self):
      print ("Name:", Monster.Name)
      print("HP:", Monster.HP)
      print("The monster exclaims:", Monster.Dialogue)
    #def set_Name(self):
      Name = input(("enter Name"))
      self.Name = Name
   # def set_HP(self):
      HP = input(("enter HP"))
      self.HP = HP  
    #def set_Dialogue(self):
      Dialogue = input(("enter Dialogue"))
      self.Dialogue = Dialogue
			

Monster1 = Monster("Garry", 100, "aaaaa I'm big and scary, fear me human")

Monster.describe(Monster1)