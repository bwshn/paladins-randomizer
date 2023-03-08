import random
import numpy as np
from datetime import datetime

Tank = ["Ash", "Atlas", "Azaan", "Barik", "Fernando", "Inara", "Khan",
        "Makoa", "Nyx", "Raum", "Ruckus", "Terminus", "Torvald", "Yagorath"]
Damage = ["Betty la Bomba", "Bomb King", "Cassie", "Dredge", "Drogoz", "Imani", "Kasumi", "Kinessa",
          "Lian", "Octavia", "Saati", "Sha Lin", "Strix", "Tiberius", "Tyra", "Viktor", "Vivian", "Willo"]
Flank = ["Androxus", "Buck", "Caspian", "Evie", "Koga", "Lex",
         "Maeve", "Moji", "Skye", "Talus", "VII", "Vatu", "Vora", "Zhin"]
Support = ["Corvus", "Furia", "Grohk", "Grover", "Io", "Jenos",
           "Lillith", "Mal'Damba", "Pip", "Rei", "Seris", "Ying"]
Total = Tank + Damage + Flank + Support

Talent = ["1.", "2.", "3."]
Card = ["1.", "2.", "3."]

Mode = ["Choose Any", "Onslaught", "Siege"]
if datetime.now().weekday() not in [5, 6]:
    Mode.append("Payload")
else:
    Mode.append("LTM")

print("Welcome to Paladins Hero/Mode Picker!")
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
    print("Talent: " + random.choice(Talent))
    print("Mode: " + random.choice(Mode))
    ans = input("Continue?: ")
    i += 1
