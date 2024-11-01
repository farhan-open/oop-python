class Hero:
    # private class variable
    __jumlah = 0

    def __init__(self, inputName):
        # instance variable private
        self.__name = inputName
        Hero.__jumlah += 1

    # method ini hanya berlaku untuk objek karena terdapat keyword 'self' pada parameter method
    def getJumlah1(self): 
        return Hero.__jumlah
    
    # method ini tidak berlaku untuk objek tapi berlaku untuk class karena tidak terdapat keyword 'self' pada parameter method
    def getJumlah2(): 
        return Hero.__jumlah


sniper = Hero('Sniper')
rikimaru = Hero('Rikimaru')
drowranger = Hero('drowranger')

print(sniper.getJumlah1()) # pembuktian berlaku untuk objek
print(Hero.getJumlah2()) # pembuktian berlaku untuk class

# STATIC METHOD
'''
Static method pada OOP Python adalah metode yang TERKAIT DENGAN CLASS, BUKAN DENGAN OBJEK individu yang dibuat dari kelas tersebut. Dengan kata lain, static method TIDAK MEMERLUKAN OBJEK untuk diakses dan dieksekusi. Static method didefinisikan dengan menggunakan dekorator @staticmethod di depan definisi metode.
'''
class MathUtil:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

# Pemanggilan static method tanpa membuat objek terlebih dahulu
result1 = MathUtil.add(5, 3)
print(result1)  # Output: 8

result2 = MathUtil.multiply(4, 6)
print(result2)  # Output: 24

# CLASS METHOD
'''
Class method pada OOP Python adalah metode yang terkait dengan kelas dan diakses melalui kelas itu sendiri, bukan melalui objek yang dibuat dari kelas tersebut. Class method didefinisikan dengan menggunakan dekorator @classmethod di depan definisi metode.

Ciri-ciri class method:

1. Mengambil parameter cls sebagai argumen pertama, yang merujuk pada kelas itu sendiri (mirip dengan self pada instance method).
2. Dapat mengakses dan memodifikasi atribut kelas karena terikat dengan kelas, bukan dengan objek individu.
3. Dapat diakses langsung dari kelas tanpa membuat objek terlebih dahulu.
'''
class Person:
    total_persons = 0

    def __init__(self, name):
        self.name = name
        Person.total_persons += 1

    @classmethod
    def display_total_persons(cls):
        return cls.total_persons

# Membuat beberapa objek Person
person1 = Person("Alice")
person2 = Person("Bob")

# Memanggil class method tanpa membuat objek terlebih dahulu
total_persons = Person.display_total_persons()
print(total_persons)  # Output: 2
