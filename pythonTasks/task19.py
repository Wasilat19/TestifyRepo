
class Human: 

    leg_count = 4
    can_walk = True

    def get_description(self, description):
        return description

    def get_leg_count(self):
        return self.leg_count

man = Human()
print(man.get_description("This is a human"))
print(man.leg_count)
print(man.get_leg_count(), man.can_walk)


