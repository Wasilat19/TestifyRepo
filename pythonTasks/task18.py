
from cgi import print_arguments


class Human:

    leg_count = 4
    can_walk = True

    def __init__(self, name): 
        self.name = name

baby = Human("Baby")

print(baby.name)
print("leg_count:", baby.leg_count)
print("can_walk:", baby.can_walk)