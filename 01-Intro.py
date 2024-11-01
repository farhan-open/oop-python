# class merupakan sebuah blue print untuk membuat objek

class Hero: # template-class paling polos
    pass


hero1 = Hero() # membuat objek yang bernama hero1 (proses instansiasi objek)
hero2 = Hero() # membuat objek yang bernama hero2 (proses instansiasi objek)
hero3 = Hero() # membuat objek yang bernama hero3 (proses instansiasi objek)

hero1.name = 'sniper'
hero1.health = 100

hero2.name = 'sven'
hero2.health = 200

hero3.name = 'ucup'
hero3.health = 1000

print(hero1) # untuk memastikan bahwa hero1 merupakan object
print(hero1.__dict__) # untuk melihat atribut (variabel) yang dimiliki oleh hero1
print(hero1.name) # menampilkan atribut nama dari hero1