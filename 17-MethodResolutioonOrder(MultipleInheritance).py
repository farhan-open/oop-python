class A: 
    def method(self): # nama methodnya sama dengan yang ada di class B
        print('Ini adalah method A')

class B:
    def method(self): # nama methodnya sama dengan yang ada di class A
        print('Ini adalah method B')

class C(A, B): # class C merupakan sub class dari class A dan class B (Class C meng-inherit dua class dalam hal ini adalah class A dan class B)
    pass


objek = C() # melakukan instansiasi objek  dari class C yang merupakan sub class dari class A dan class B
objek.method() # menggunakan method yang ada di class A pada class B juga ada method yang bernama 'method()'. Ini karena kita mendefinisikan class C mewarisi class A terlebih dahulu baru kemudian mewarisi class B (pada baris 9)
help(objek) # untuk melihan urutan (method resolution order) dalam hal ini urutannya adalah C -> A -> B

'''
PENJELASAN FORMAL

Method Resolution Order (MRO) adalah urutan pencarian dalam hierarki kelas ketika Anda memanggil suatu metode atau atribut pada sebuah objek. Pada OOP Python, setiap kelas dapat memiliki kelas induk (superclass) atau kelas turunan (subclass).

Ketika Anda memanggil metode atau atribut pada objek, Python akan mencari metode atau atribut tersebut mulai dari kelas tersebut, lalu ke kelas turunannya, dan seterusnya hingga mencapai kelas induk tertinggi.
'''