
class Human:
    leg_count = 4
    
    def get_gender(self):
        return "Unknown"

human = Human()
print(human.get_gender())

class Man(Human):
    def get_gender(self):
        return "man"

class Woman(Human):
    def get_gender(self):
        return "woman"

man1 = Man()
woman1 = Woman()
print(man1.get_gender())
print(woman1.get_gender())

       
       

