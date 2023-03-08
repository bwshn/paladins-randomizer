import random
from datetime import datetime

# TODO: put all the heros in a .txt file for further use

Tank = ["Ash", "Atlas", "Azaan", "Barik", "Fernando", "Inara", "Khan",
        "Makoa", "Nyx", "Raum", "Ruckus", "Terminus", "Torvald", "Yagorath"]
Damage = ["Betty la Bomba", "Bomb King", "Cassie", "Dredge", "Drogoz", "Imani", "Kasumi", "Kinessa",
          "Lian", "Octavia", "Saati", "Sha Lin", "Strix", "Tiberius", "Tyra", "Viktor", "Vivian", "Willo"]
Flank = ["Androxus", "Buck", "Caspian", "Evie", "Koga", "Lex",
         "Maeve", "Moji", "Skye", "Talus", "VII", "Vatu", "Vora", "Zhin"]
Support = ["Corvus", "Furia", "Grohk", "Grover", "Io", "Jenos",
           "Lillith", "Mal'Damba", "Pip", "Rei", "Seris", "Ying"]
Total = Tank + Damage + Flank + Support

# TODO: make a version with name of the talents and cards

Talent = ["1.", "2.", "3."]
Cards = [0] * 16
i = 0
while (i < 5):
    deck = random.randint(0, 15)
    if Cards[deck] == 0:
        Cards[deck] = 1
        i += 1
i = 0
Locs = [i for i, e in enumerate(Cards) if e != 0]
while (i < 10):
    loc = random.choice(Locs)
    if Cards[loc] != 5:
        Cards[loc] += 1
        i += 1
Cards = [Cards[i:i+4] for i in range(0, len(Cards), 4)]
Cards = [Cards[i:i+2] for i in range(0, len(Cards), 2)]

Mode = ["Choose Any", "Onslaught", "Siege"]
if datetime.now().weekday() not in [5, 6]:
    Mode.append("Payload")
else:
    Mode.append("LTM")

print("Welcome to Paladins Complete Randomizer Picker!")
ans = "yes"
i = 1
while (ans.lower() != "n" and ans.lower() != "no" and ans != "0"):
    print("\n")
    print("Trial: " + str(i))
    print("Support: " + random.choice(Support))
    print("Tank: " + random.choice(Tank))
    print("Damage: " + random.choice(Damage))
    print("Flank: " + random.choice(Flank))
    print("Random: " + random.choice(Total))
    print("Mode: " + random.choice(Mode))
    print("Talent: " + random.choice(Talent))
    for j in Cards:
        print("\t".join(map(str, j)))
    ans = input("Continue?: ")
    i += 1