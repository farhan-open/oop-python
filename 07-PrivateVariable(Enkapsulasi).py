'''
Private variable pada OOP Python adalah variabel yang dinyatakan sebagai "private" di dalam kelas dan HANYA DAPAT DIAKSES dan dimodifikasi oleh method yang ada di dalam kelas tersebut. Variabel private dinyatakan dengan menambahkan dua garis bawah (__) di awal nama variabel.

Menggunakan private variable membantu untuk mencegah akses langsung dari luar kelas dan memastikan bahwa akses dan modifikasi data dilakukan melalui method yang sesuai. Ini membantu dalam mengontrol dan membatasi akses terhadap data kelas, sehingga memungkinkan untuk mengatur tingkat abstraksi dan encapsulation yang lebih baik dalam kode.
'''

class Hero:
    # class variable
    jumlah_hero = 0

    # class variable private
    __privateJumlah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variable public
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        
        # instance variable private
        self.__private = 'Ini adalah variabel private'

        # instance variable protected
        self._protected = 'prootected'

'''
Protected variable pada OOP Python adalah variabel yang dinyatakan sebagai "protected" di dalam kelas. Variabel protected dapat diakses dan dimodifikasi oleh method yang ada di dalam kelas itu sendiri dan juga oleh kelas turunan (subclass) dari kelas tersebut.

Variabel protected dinyatakan dengan menambahkan satu garis bawah (_) di awal nama variabel.
'''