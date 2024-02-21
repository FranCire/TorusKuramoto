import numpy as np
import matplotlib.pyplot as plt


def draw_color_wheel():
    fig = plt.figure()
    ax = fig.add_subplot(projection='polar')

    rho = np.linspace(0,1,100)
    phi = np.linspace(0,2*np.pi,1000)

    RHO,PHI = np.meshgrid(rho,phi)
    colors = np.abs((PHI / (2*np.pi)) - 0.5)
    PHI += np.pi
    colors[colors >= 0.1] = 0
    colors = 1 - colors * 10
    colors[colors == 1] = 0
    ax.set_theta_zero_location('N', offset=0)
    ax.scatter(PHI,RHO,c=colors,cmap='hot')
    plt.grid(False)
    plt.yticks([])
    plt.savefig("screenshots/color_wheel.png")
    plt.clear()


if __name__ == "__main__":
    draw_color_wheel()