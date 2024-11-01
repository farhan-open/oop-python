class Hero:
    #constructor
    def __init__(self, inputName, inputHealth, inputPower, inputArmor): # bagian pertama kali yang akan dijalankan ketika proses istansiasi objek dilakukan. parameter 'self' akan merujuk pada objek yang dibuat (mirip dengan 'this' pada java)
        # instance variable/atribut -> akan menempel ke objek hasil instansiasi
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

        # name, health, power, dan armor di atas adalah atribut dari class Hero


hero1 = Hero('Sniper', 100, 10, 4) # instansiasi objek
hero2 = Hero('Mirana', 100, 15, 1) # instansiasi objek
hero3 = Hero('Ucup', 100, 100, 0) # instansiasi objek

print(f'Identitas dari hero1 adalah sebagai berikut:\nNama: {hero1.name}\nHealth: {hero1.health}\nPower: {hero1.power}\nArmor: {hero1.armor}\n')
print(f'Identitas dari hero2 adalah sebagai berikut:\nNama: {hero2.name}\nHealth: {hero2.health}\nPower: {hero2.power}\nArmor: {hero2.armor}\n')
print(f'Identitas dari hero3 adalah sebagai berikut:\nNama: {hero3.name}\nHealth: {hero3.health}\nPower: {hero3.power}\nArmor: {hero3.armor}\n')

# atau cara lain untuk melihat identitas/rincian dari sebuah objek yang dibuat, dapat dilakukan sebagai berikut:
print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)