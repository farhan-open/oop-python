'''
Enkapsulasi pada OOP Python adalah konsep yang memungkinkan untuk menyembunyikan detail implementasi suatu objek dari akses langsung oleh kode lain di luar kelas tersebut. Dalam enkapsulasi, variabel dan method di dalam kelas dapat didefinisikan dengan tingkat aksesibilitas tertentu (seperti public, protected, atau private) untuk mengontrol cara bagaimana objek dapat diakses dan diubah.

Dengan enkapsulasi, kita dapat mengatur bahwa hanya method di dalam kelas itu sendiri yang dapat mengakses dan memodifikasi data (variabel) yang ada di dalamnya. Hal ini membantu mencegah perubahan yang tidak diinginkan dari kode lain dan mengurangi kesalahan dalam kode karena akses data yang tidak terkontrol.
'''

class Hero:

    def __init__(self, inputName, inputHealth, inputPower):
        # instance variable private
        self.__name = inputName
        self.__health = inputHealth
        self.__power = inputPower

    # getter (dibuat untuk bisa mengakses atribut objek yang bersifat private)
    def getName(self):
        return self.__name
    
    def getHealth(self):
        return self.__health
    
    # setter (dibuat untuk bisa mengatur nilai atribut objek yang bersifat private)
    def diserang(self, serangPower):
        self.__health -= serangPower

    def setAttPower(self, nilaiBaru):
        self.__health = nilaiBaru


# awal dari game
earthshaker = Hero('Earthshaker', 50, 5)
print(earthshaker.__dict__)

# game berjalan
print(earthshaker.getName())
print(earthshaker.getHealth())
earthshaker.diserang(10)
print(earthshaker.getHealth())