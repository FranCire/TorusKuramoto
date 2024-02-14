from timeit import repeat
from Visualizer import Visualizer
from Network import Network
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
from matplotlib.colors import hsv_to_rgb
from matplotlib import cm

class Visualizer3D(Visualizer):
    
    def graph_network_evolution(self,t :float = 1,dt: float = 0.01, circle_radius: float = None,line_width:float = None,color_distribution = "rainbow",filename = None):
        steps = int(t / dt)
        output = self.network.simulate(t,dt)
        output = np.array(output)
        points  = self.network.positions
        A = self.network.A

        X = np.zeros(len(points))
        Y = np.zeros(len(points))
        Z = np.zeros(len(points))

        for i in range(len(points)):
            X[i] = points[i][0]
            Y[i] = points[i][1]
            Z[i] = points[i][2]

        #rango = np.where((np.abs(X) < 0.2))
        #X = X[rango]
        #Y = Y[rango]
        #Z = Z[rango]
        #output = output[:,rango[0]]
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

        ax.set_xlim((-1.5,1.5))
        ax.set_ylim((-1.5,1.5))
        ax.set_zlim((-1.5,1.5))

        ax.axis('off')


        if line_width is not None:
            for i,j in np.transpose(np.nonzero(A)):
                ax.plot([points[i][0],points[j][0]],[points[i][1],points[j][1]],[points[i][2],points[j][2]],color="black",zorder=-1,linewidth=line_width)
            
        values = (np.fmod(np.fmod(output[0],2*np.pi) + 2*np.pi,2*np.pi)) / (2*np.pi)
        if color_distribution == "rainbow":
            colors = np.array([np.fmod(np.abs(hsv_to_rgb((value,1,0.7))),1) for value in values])
            scat = ax.scatter3D(X,Y,Z,facecolors=colors,s = circle_radius)

        if color_distribution == "firefly":

            colors = np.abs(values - 0.5)
            colors[colors >= 0.1] = 0
            colors = 1 - colors * 10
            colors[colors == 1] = 0
            scat = ax.scatter3D(X,Y,Z,facecolors=cm.hot(colors),s = circle_radius)



        
        def animate(i):
            values = (np.fmod(np.fmod(output[i],2*np.pi) + 2*np.pi,2*np.pi)) / (2*np.pi)
            if color_distribution == "rainbow":
                colors = np.array([np.fmod(np.abs(hsv_to_rgb((value,1,0.7))),1) for value in values])
                scat.set_facecolors(colors)

            if color_distribution == "firefly":
                colors = np.abs(values - 0.5)
                colors[colors >= 0.1] = 0
                colors = 1 - colors * 10
                colors[colors == 1] = 0
                scat.set_facecolors(cm.hot(colors))

            return scat,
        
        ani = animation.FuncAnimation(fig,animate,frames=len(output),interval=42)

        if filename is None:
            plt.tight_layout()
            plt.show(block = True)
        
        else:
            ani.save(f"{filename}.mp4")
    

    def __init__(self, network: Network) -> None:
        super().__init__(network)

     
    
