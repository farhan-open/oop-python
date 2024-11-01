'''
Inheritance (warisan) pada OOP Python adalah konsep di mana sebuah kelas dapat "MEWARISI" ATRIBUT DAN METHOD dari kelas lain. Kita dapat membuat kelas baru yang merupakan versi lebih khusus dari kelas yang sudah ada. Kelas yang mewariskan atribut dan metode disebut kelas induk atau kelas dasar atau SUPER CLASS, sedangkan kelas yang menerima warisan disebut kelas anak atau kelas turunan (derived class) atau SUB CLASS.
'''

class Hero:
    def __init__(self, inputName, inputHealth):
        self.name = inputName
        self.health = inputHealth


class HeroIntelligent(Hero): # class HeroIntelligent menjadi sub class dari class Hero
    pass

class HeroStrength(Hero): # class HeroStrength menjadi sub class dari class Hero
    pass

lina = Hero('Lina', 100)
techies = HeroIntelligent('Techies', 100)
axe = HeroStrength('Axe', 200)

print(help(techies))
print('\n')
print(help(axe))
print('\n')
print(lina.__dict__)
print('\n')
print(techies.__dict__)
print('\n')
print(axe.__dict__)

