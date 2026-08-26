import numpy as np

u1= int(input("Digite u1: "))
u2= int(input("Digite u2: "))
v1= int(input("Digite v1: "))
v2= int(input("Digite v2: "))

U= np.array([u1,u2])
V= np.array([v1,v2])

retorno = V - U
print("Retorno", retorno)
