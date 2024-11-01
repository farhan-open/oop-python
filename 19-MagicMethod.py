'''
Magic method pada Python adalah metode khusus yang dimulai dan diakhiri dengan double underscore (dunder), contohnya __init__, __str__, __add__, dll. Magic method memungkinkan Anda untuk mendefinisikan perilaku khusus pada objek yang dibuat dari kelas tertentu. Ketika Anda menggunakan operator atau fungsi tertentu pada objek, Python akan mencari dan menggunakan magic method terkait jika didefinisikan dalam kelas tersebut.
'''

class Mangga:
    # magic method yang pertama
    def __init__(self, nama, jumlah): # sebagai constructor
        self.nama = nama
        self.jumlah = jumlah

    # magic method yang kedua
    def __repr__(self): # biasanya digunakan dalam proses DEBUG (dapat digunakan hanya dengan langsung mencetak objeknya [print(nama_objek)])
        return f"DEBUG\nMangga: {self.nama} dengan jumlah = {self.jumlah}"
    
    # magic method yang ketiga
    def __str__(self): # biasanya digunakan ketika program sudah jadi (dapat digunakan hanya dengan langsung mencetak objeknya [print(nama_objek)] dan lebih sering digunakan jika dibandingkan dengan __repr__)
        return f"\nPROGRAM SUDAH JADI\nMangga: {self.nama} dengan jumlah = {self.jumlah}"
    
    # magic maethod yang keempat
    def __add__(self, objek): # menjumlahkan dua buah objek
        return self.jumlah + objek.jumlah
    

belanja1 = Mangga('Arumanis', 10)
belanja2 = Mangga('Kue', 17)
print(repr(belanja1)) # testing __repr__
print(belanja1) # testinf __str__

print('\n')
print(belanja1 + belanja2) # testing __add__