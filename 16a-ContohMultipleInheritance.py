class Team:
    def setTeam(self, team):
        self.team = team

    def showTeam(self):
        print(self.team)

class Tipe_Hero:
    def setTipe(self, tipe):
        self.tipe = tipe

    def showTipe(self):
        print(self.tipe)

class Hero(Team, Tipe_Hero):
    def __init__(self, name, health):
        self.name = name
        self.health = health


ucup = Hero('Ucup', 100)
ucup.setTeam('Merah') # mengimplementasikan method dari class Team
ucup.setTipe('Intelligent') # mengimplementasikan method dari class Tipe_Hero
ucup.showTeam() # mengimplementasikan method dari class Team
ucup.showTipe() # mengimplementasikan method dari class Tipe_Hero