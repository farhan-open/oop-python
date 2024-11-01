# Game saling serang

class Hero:
    # class variabel
    jumlah_hero = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
    
    def serang(self, lawan): # parameter fungsi/method pada python tidak perlu didefinisikan tipe-nya, nanti yang menentukan nilai dan tipe yang kita masukkan benar atau tidak akan didasarkan pada operasi yang diberlakukan pada parameter tersebut (SAMA SEPERTI R).
        print(self.name + ' menyerang ' + lawan.name)
        lawan.diserang(self, self.power)

    def diserang(self, lawan, attackPowerLawan):
        print(self.name + ' diserang ' + lawan.name)
        attack_diterima = attackPowerLawan/self.armor
        print(f'Efek serangan sebesar {int(attack_diterima)}')
        self.health -= attack_diterima
        print(f'Health {self.name} tersisa {int(self.health)}')


sniper = Hero('Sniper', 100, 10, 5)
rikimaru = Hero('Rikimaru', 100, 20, 10)

sniper.serang(rikimaru)
print('\n')
rikimaru.serang(sniper)