'''
Class abstract pada OOP Python adalah sebuah kelas yang tidak dapat diinisialisasi menjadi objek secara langsung. Artinya, Anda tidak dapat membuat objek langsung dari kelas abstract tersebut. Sebaliknya, kelas abstract digunakan sebagai kerangka atau blueprint untuk kelas turunannya.

Kelas abstract hanya berisi definisi metode tanpa implementasi (tanpa isi atau body metode). Metode-metode tersebut akan diimplementasikan oleh kelas-kelas turunannya. Oleh karena itu, kelas abstract tidak memiliki objek yang sebenarnya, melainkan hanya berfungsi sebagai panduan bagi kelas turunannya untuk mengimplementasikan metode-metode tersebut.

Untuk membuat kelas abstract di Python, Anda perlu mengimpor modul abc (Abstract Base Classes) dan mendefinisikan kelas tersebut sebagai subclass dari ABC (Abstract Base Class) atau menggunakan decorator @abstractmethod pada metode yang ingin dijadikan abstract.
'''
from abc import ABC, abstractmethod

class Button(ABC): # class Button ini menjadi class Abstract karena meng-inherit ABC. Dengan begini, kita tidak dapat membuat objek dari class Button
    @abstractmethod # decorator ini akan memaksa method click untuk diimplementasikan pada class turunan dari class Button
    def click(self):
        pass

class PushButton(Button):
    def click(self):
        print('Push button click')

class RadioButton(Button):
    def click(self):
        print('Radio button click')


tombol1 = PushButton()
tombol2 = RadioButton()
tombol1.click()
tombol2.click()