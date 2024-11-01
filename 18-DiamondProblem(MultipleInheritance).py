class A: 
    def method(self): 
        print('Ini adalah method A')

class B(A):
    def method(self): 
        print('Ini adalah method B')

class C(A): 
    def method(self): 
        print('Ini adalah method C')

class D(B, C):
    pass


objek = D()
objek.method() # akan mengambil method dari B karena didasarkan pada aturan urutan di bawah ini untuk diamond problem
help(objek) # untuk melihat urutan pada diamond problem (dalam hal ini urutannya adalah D -> B -> C -> A)