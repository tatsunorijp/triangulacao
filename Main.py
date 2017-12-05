import numpy as np
import matplotlib.pyplot as plt
import math


receptores = ((-3.99, 0, 1.35), (5.55, 1.28, 1.35), (0.35, -6.94, 1.35), (0.16, 7.35, 1.35), (-7.35, 4.55, 1.35))
po = (-26.0, -33.8, -29.8, -31.2, -33.0)
lk = (2.1, 1.8, 1.3, 1.4, 1.5)
dk = (0.0, 0.0, 0.0, 0.0, 0.0)

def dk(pk):
    for i in range(5):
        dk[i] = math.pow(10.0, ((po[i] - pk[i])/(10.0*lk[i]) ))



def main():
    pk = input().split()
    resposta = dk(pk)