from abc import ABC, abstractmethod

class Button(ABC): 
    def __init__(self, set_link):
        self.link = set_link

    @abstractmethod 
    def click(self):
        pass

    @property
    @abstractmethod
    def link(self): # method ini akan terhubung dengan self.link pada constructor di atas (dan harus diimplementasikan di class PushButton sebagai class turunan dari class Abstrak Button)
        pass

class PushButton(Button):
    def click(self):
        print(f'Go to: {self.__tautan}')

    @Button.link.setter # keyword 'Button' berfungsi untuk menandakan bahwa 'link.setter' yang dibuat mengarah pada method link pada class abstract Button. Karena method 'link' pada class abstract Button ditandai sebagai property
    def link(self, input):
        self.__tautan = input

    @link.getter # pada getter di samping, tidak perlu dipasang keyword 'Button' lagi karena program sudah paham bahwa 'link' yang dimaksud mengarah pada method link pada class abstract Button berdasarkan pada perintah baris 20
    def link(self):
        return self.__tautan


tombol1 = PushButton('www.example.com')
tombol1.click()
print(tombol1.__dict__)

# INTI DARI PROGRAM DI ATAS ADALAH KITA COBA MENGHUBUNGKAN ATRIBUT YANG ADA DI ABSTRACT CLASS UNTUK DIIMPLEMENTASIKAN PADA KELAS TURUNAN DARI CLASS ABSTRACT DENGAN CARA MENDUPLIKASI ATRIBUT TERSEBUR SEBAGAI ABSTRACT METHOD (NAMA METHOD-NYA HARUS SAMA DENGAN NAMA ATRIBUTNYA). KEMUDIAN ABSTRACT METHOD TERSEBUT DIIMPLEMENTASIKAN PADA KELAS TURUNAN DARI CLASS ABSTRACT DENGAN CARA MEMBUAT GETTER DAN SETTER UNTUK ABSTRACT METHOD TERSEBUT.

# KEMUDIAN KETIKA KITA MELAKUKAN INSTANSIASI OBJEK SEPERTI PADA BARIS 29, NILAI 'www.example.com' AKAN MASUK MENGISI self.link, DAN KARENA self.link TERHUBUNG DENGAN METHOD ABSTRACT link PADA CLASS BUTTON YANG DIIMPLEMENTASIKAN SETTERNYA PADA CLASS PUSHBUTTON PADA BARIS 20, MAKA NILAI 'www.example.com' TERSEBUT AKAN MASUK MENGISI NILAI PARAMETER 'input' PADA IMPLEMENTASI SETTER METHOD ABSTRAK LINK TERSEBUT. KONSEKUENSINYA, NILAI self.__tautan = input = self.link.

