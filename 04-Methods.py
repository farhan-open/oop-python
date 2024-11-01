'''
Dalam OOP (Object-Oriented Programming) Python, method adalah fungsi yang didefinisikan di dalam sebuah kelas dan berfungsi untuk melakukan tindakan atau operasi tertentu pada objek dari kelas tersebut. 
'''

class Hero:
    # class variabel
    jumlah_hero = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1

    # void function atau method tanpa return
    def siapa(self):
        print('Namaku adalah ' + self.name)

    # method dengan argumen
    def healthUp(self, up):
        self.health += up
    # dalam hal ini, 'self' tidak diitung sebagai argumen, karena merupakan parameter wajib yang musti ada dalam sebuah method

    # method dengan return
    def getHealth(self):
        return self.health


hero1 = Hero('Sniper', 100, 10, 5) # objek hero 1

# menggunakan method
hero1.siapa()
print(f'Health dari {hero1.name} = {hero1.health}')
hero1.healthUp(10)
print(f'Health dari {hero1.name} setelah dilakukan penambahan = {hero1.getHealth()}')

print('')

hero2 = Hero('Mario Bros', 90, 5, 10) # objek hero 2
# menggunakan method
hero2.siapa()
print(f'Health dari {hero2.name} = {hero2.health}')
hero2.healthUp(20)
print(f'Health dari {hero2.name} setelah dilakukan penambahan = {hero2.getHealth()}')