from Hero import HeroIntelligent, HeroStrength


lina = HeroIntelligent('Lina')
slardar = HeroStrength('Slardar')

lina.show_info()
slardar.show_info()

lina.gainExp = 200
slardar.gainExp = 250

print('')
lina.show_info()
slardar.show_info()