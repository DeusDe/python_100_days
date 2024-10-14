import random

pos = ["rock","paper","scissors"]
pl_c = pos[int(input("Stein: 1, Papier: 2, Schere: 3"))-1]
pc_c = pos[random.randint(0,2)]

