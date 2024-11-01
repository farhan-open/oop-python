class Hero:
    def __init__(self, inputName, inputHealth):
        self.name = inputName
        self.health = inputHealth

    def showInfo(self):
        print(f'Informasi Hero:\n\tNama: {self.name}\n\tHealth: {self.health}')

class HeroIntelligent(Hero): # class HeroIntelligent menjadi sub class dari class Hero
    def __init__(self, inputName):
        super().__init__(inputName, 100) # mengambil method init (constructor) dari super class beserta atribut-atributnya
        super().showInfo() # mengambil method showInfo dari super class

class HeroStrength(Hero): # class HeroStrength menjadi sub class dari class Hero
    def __init__(self, inputName):
        super().__init__(inputName, 200) # mengambil method init (constructor) dari super class beserta atribut-atributnya
        super().showInfo() # mengambil method showInfo dari super class


lina = HeroIntelligent('Lina')
axe = HeroStrength('Axe')