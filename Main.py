import numpy as np
import matplotlib.pyplot as plt
import math


receptores = [[-3.99, 0, 1.35], [5.55, 1.28, 1.35], [0.35, -6.94, 1.35], [0.16, 7.35, 1.35], [-7.35, 4.55, 1.35]]
po = [-26.0, -33.8, -29.8, -31.2, -33.0]
lk = [2.1, 1.8, 1.3, 1.4, 1.5]
dkk = [[0.0], [0.0], [0.0], [0.0], [0.0]]

def dk(pk):
    for i in range(4):
        dkk[i][0] = float( math.pow(10.0, ((po[i] - pk[i])/(10.0 * lk[i]) )))

def mmq():
    a = np.matrix([[5.57, -17.63], [13.67, -4.96], [-0.12, 7.36]])
    b = np.matrix([[0.0], [0.0], [0.0]])
    aux = [0.0, 0.0, 0.0, 0.0, 0.0]
    for i in range(4):
        aux[i] = (receptores[i][0]*receptores[i][0]) + (receptores[i][1]*receptores[i][1]) - dkk[i][0]

    b[0][0] = -aux[0] + aux[1]
    b[1][0] = -aux[2] + aux[3]
    b[2][0] = -aux[3] + aux[4]
    a = 2 * a

    return np.linalg.inv(a.transpose() * a) * a.transpose() * b
def main():
    pk = list(map(float, input().split()))
    dk(pk)
    resp = mmq()
    print(resp)
main()
