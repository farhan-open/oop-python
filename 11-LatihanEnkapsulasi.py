class Hero:
    # class variabel
    __jumlah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.__name = inputName
        self.__healthStandar = inputHealth
        self.__powerStandar = inputPower
        self.__armorStandar = inputArmor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthStandar * self.__level
        self.__attPower = self.__powerStandar * self.__level
        self.__armor = self.__armorStandar *self.__level
        self.__health = self.__healthMax

        Hero.__jumlah += 1

    @property
    def info(self):
        return "{}: \n\tLevel = {}\n\tHealth = {}/{}\n\tAttack = {}\n\tArmor = {}".format(self.__name, self.__level, self.__health, self.__healthMax, self.__attPower, self.__armor)
    
    @property # semacam inisialisasi untuk membuat getter dan setter  dengan nama yang sama dalam hal ini adalah gainExp
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp
        if(self.__exp >= 100):
            print(f'{self.__name} naik level')
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__healthStandar * self.__level
            self.__attPower = self.__powerStandar * self.__level
            self.__armor = self.__armorStandar *self.__level

    def attack(self, musuh):
        print(f'{self.__name} menyerang {musuh.__name}')
        self.gainExp = 50


slardar = Hero('Slardar', 100, 5, 10)
axe = Hero('Axe', 100, 5, 10)
print(slardar.info)
print(slardar.__dict__)

print('\n')
slardar.attack(axe)
print(slardar.info)
print(slardar.__dict__)

print('\n')
slardar.attack(axe)
print(slardar.info)
print(slardar.__dict__)

print('\n')
slardar.attack(axe)
print(slardar.info)
print(slardar.__dict__)
