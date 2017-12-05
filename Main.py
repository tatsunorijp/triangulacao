import numpy as np
import matplotlib.pyplot as plt
import math


receptores = [[1.55, 17.63, 1.35], [-4.02, 0.00, 1.35], [-4.40, 9.6, 1.35], [9.27, 4.64, 1.35], [9.15, 12.00, 1.35]]
po = [-26.0, -33.8, -29.8, -31.2, -33.0]
lk = [2.1, 1.8, 1.3, 1.4, 1.5]
dkk = [[0.0], [0.0], [0.0], [0.0], [0,0]]

def dk(pk):
    for i in range(3):
        dkk[i][0] = float( math.pow(10.0, ((po[i] - pk[i])/(10.0 * lk[i]) )))


def mmq():
    a = np.matrix([[5.57, -17.63], [13.67, -4.96], [-0.12, 7.36]])
    b = np.matrix([[0.0], [0.0], [0.0]])
    aux = [0.0, 0.0, 0.0, 0.0, 0.0]
    for i in range(5):
        aux[i] = (receptores[i][0]*receptores[i][0]) + (receptores[i][1]*receptores[i][1]) - dkk[i][0]

    b[0][0] = aux[1] - aux[0]
    b[1][0] = aux[3] - aux[2]
    b[2][0] = aux[4] - aux[3]
    a = 2 * a

    return np.linalg.inv(a.transpose() * a) * a.transpose() * b
def main():
    pk = list(map(float, input().split()))
    dk(pk)
    resp = mmq()
    print(resp)

    plot_receiver1 = plt.Circle((1.55, 17.63), dkk[0], color='r', alpha=.6)
    plot_receiver2 = plt.Circle((-4.02, 0.0), dkk[1], color='b', alpha=.6)
    plot_receiver3 = plt.Circle((-4.4, 9.6), dkk[2], color='m', alpha=.6)
    plot_receiver4 = plt.Circle((9.27, 4.64), dkk[3], color='y', alpha=.6)
    plot_receiver5 = plt.Circle((9.15, 12.0), dkk[4], color='k', alpha=.6)
    plt.plot([0.0], [9.0], 'go')
    plt.plot([resp[0, 0]], [resp[1, 0]], 'ro')
    ax = plt.gca()
    ax.add_artist(plot_receiver1)
    ax.add_artist(plot_receiver2)
    ax.add_artist(plot_receiver3)
    ax.add_artist(plot_receiver4)
    ax.add_artist(plot_receiver5)
    ax.set_xlim(-30, 30)
    ax.set_ylim(-30, 30)
    plt.plot()
    plt.show()


main()
