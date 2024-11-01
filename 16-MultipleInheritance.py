class A: 
    def method_A(self):
        print('Ini adalah method A')

class B:
    def method_B(self):
        print('Ini adalah method B')

class Sesuatu(A, B): # class Sesuatu merupakan sub class dari class A dan class B (Class Sesuatu meng-inherit dua class dalam hal ini adalah class A dan class B)
    pass


objek = Sesuatu() # melakukan instansiasi objek  dari class Sesuatu yang merupakan sub class dari class A dan class B
objek.method_A() # menggunakan method yang ada di class A
objek.method_B() # menggunakan method yang ada di class B