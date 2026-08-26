import numpy as np

f1= int(input("Digite f1: "))
f2= int(input("Digite f2: "))
escalar = int(input("Digite valor escalar: "))
f= np.array ([f1,f2])
f= escalar * f
print("produto", f)
