class Fighter:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 10

    def attack(self, other_guy):
        other_guy.health -= self.damage
        print ("{} attack {} and {} losses {}".format(other_guy.name, self.name, self.name, self.damage))

    def __str__(self):
        return "{} : {}".format(self.name, self.health)

me = Fighter("Me")
you = Fighter("You")

me.attack(you)

print (you.health)
print (me.health)

print (me)
print (you)
print("Ashish Pandey")