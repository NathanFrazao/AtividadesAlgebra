import numpy as np

a1= int(input("Digite a1: "))
a2= int(input("Digite a2: "))
b1= int(input("Digite b1: "))
b2= int(input("Digite b2: "))

a = np.array ([a1,a2])
b = np.array ([b1,b2])
AB = b - a
dist = np.linalg.norm(AB)
print("Distância", dist)
