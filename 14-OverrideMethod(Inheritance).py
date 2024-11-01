class Hero:
    def __init__(self, inputName, inputHealth):
        self.name = inputName
        self.health = inputHealth

    def showInfo(self):
        print('Show Info di super class Hero')
        print(f'Informasi Hero:\n\tNama: {self.name}\n\tHealth: {self.health}')

class HeroIntelligent(Hero): # class HeroIntelligent menjadi sub class dari class Hero
    def __init__(self, inputName):
        super().__init__(inputName, 100)

    def showInfo(self): # method showInfo di sini akan meng-override method showInfo pada super class
        print('Show Info di sub class HeroIntelligent')
        print(f'Informasi Hero:\n\tNama: {self.name}\n\tTipe: Intelligent\n\tHealth: {self.health}')

class HeroStrength(Hero): # class HeroStrength menjadi sub class dari class Hero
    def __init__(self, inputName):
        super().__init__(inputName, 200)


lina = HeroIntelligent('Lina')
axe = HeroStrength('Axe')

lina.showInfo() # implementasi override method
print('\n')
axe.showInfo() # akan menggunakan showInfo pada super class

'''
PENJELASAN TAMBAHAN:

1. super():
    super() adalah sebuah fungsi yang digunakan untuk memanggil metode dari kelas induk (base class).
    Ketika kita menggunakan super(), kita dapat mengakses metode dari kelas induk dan menggunakan implementasi metode yang ada di kelas induk.
    Dengan super(), kita dapat MENAMBAHKAN FUNGSIONALITAS TAMBAHAN pada metode yang sudah ada di kelas induk tanpa harus menuliskan kembali seluruh kode dari metode tersebut di kelas anak.
    Penggunaan super() umumnya terjadi di dalam metode __init__() pada kelas anak untuk melakukan inisialisasi dari kelas induk.

2. Override:
    Override adalah istilah yang digunakan ketika sebuah kelas anak (derived class) mendefinisikan ulang sebuah metode yang sudah ada di kelas induk (base class).
    Ketika kita melakukan override, artinya kita memberikan implementasi baru untuk metode yang sudah ada di kelas induk. Implementasi baru ini akan digunakan oleh kelas anak, bukan implementasi metode dari kelas induk.
    Dengan melakukan override, kelas anak dapat memiliki perilaku yang berbeda atau spesifik sesuai dengan kebutuhan kelas tersebut.
'''