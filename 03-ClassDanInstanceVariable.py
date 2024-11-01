class Hero:
    jumlah = 0 # ini yang disebut sebagai class variabel atau STATIC variabel dan akan menempel ke CLASS

    def __init__(self, inputName, inputHealth, inputPower, inputArmor): # bagian pertama kali yang akan dijalankan ketika proses istansiasi objek dilakukan. parameter 'self' akan merujuk pada objek yang dibuat (mirip dengan 'this' pada java)
        # instance variable/atribut -> akan menempel ke objek hasil instansiasi
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print('Membuat Hero dengan nama ' + inputName)

        # name, health, power, dan armor di atas adalah atribut dari class Hero


hero1 = Hero('Sniper', 100, 10, 4) # instansiasi objek
print(Hero.jumlah)
hero2 = Hero('Mirana', 100, 15, 1) # instansiasi objek
print(Hero.jumlah)
hero3 = Hero('Ucup', 100, 100, 0) # instansiasi objek
print(Hero.jumlah)

'''
Definisi formal dari class variable adalah sebagai berikut:

Class variable adalah variabel yang didefinisikan di dalam sebuah kelas Python dan dimiliki oleh semua objek yang dibuat dari kelas tersebut. Ini berarti nilai dari class variable akan sama untuk semua objek yang dibuat dari kelas yang sama.
'''