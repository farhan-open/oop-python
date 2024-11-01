class Hero:

    def __init__(self, inputName, inputHealth, inputArmor):
        # instance variable private
        self.__name = inputName
        self.__health = inputHealth
        self.__armor = inputArmor
        # self.info = 'Name {}: \n\tHealth: {}'.format(self.__name, self.__health)

    @property # merubah sebuah method menjadi seperti variabel/atribut (sehingga cara memanggilnya sama seperti mengakses atribut/variabel)
    def info(self):
        return 'Name {}: \n\tHealth: {}'.format(self.__name, self.__health)
    
    @property # semacam inisialisasi untuk membuat getter dan setter  dengan nama yang sama dalam hal ini adalah armor
    def armor(self):
        pass
    
    # Getter dan setter menggunakan decorator
    @armor.getter
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self, inputArmor):
        self.__armor = inputArmor

    # Dengan menggunakan decorator di atas, untuk mengakses method-nya dapat dilakukan persis seperti mengakses atribut/variabel (SEPERTI PADA BARIS 31-37) -- tidak perlu dengan etode pengaksesan getter setter seperti biasa yang menggunakan tanda '()'.

    @armor.deleter
    def armor(self):
        print('Armor dihapus..')
        self.__armor = None


sniper = Hero('Sniper', 100, 10)
print(sniper.info)
print('')

print('Getter dan Setter untuk __armor:')
print(sniper.armor)
sniper.armor = 50
print(sniper.armor)
print(sniper.__dict__)

print('')
print('Delete Armor')
del sniper.armor # cara mengakses decorator deleter
print(sniper.__dict__)