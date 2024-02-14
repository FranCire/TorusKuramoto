
from Network import Network
from Visualizer import Visualizer
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib import animation
from matplotlib.colors import hsv_to_rgb
from matplotlib.patches import Rectangle
from matplotlib import cm
class PlanarVisualizer3D(Visualizer):
    network: Network

    def __init__(self,network: Network) -> None:
        self.network = network
    
    def get_angles(self,positions,r,R):
        Y = positions[:,1]
        X = positions[:,0]
        Z = positions[:,2]
        norm = np.sqrt(X**2 + Y**2)
        cos_phi = X/norm
        sin_phi = Y/norm
        cos_theta = (norm - R)/r
        sin_theta = Z/r
        phis,thetas = np.arctan2(sin_phi,cos_phi),np.arctan2(sin_theta,cos_theta)
        phi_negatives = np.where(phis < 0)
        phis[phi_negatives] += 2*np.pi
        theta_negatives = np.where(thetas < 0)
        thetas[theta_negatives] += 2*np.pi
        return phis,thetas

    def graph_network_evolution(self,t :float = 1,dt: float = 0.01, circle_radius: float = 0.1,line_width:float = None,xlim = (-0.1,2*np.pi + 0.1),ylim=(-0.1,2*np.pi + 0.1),color_distribution = "rainbow",filename = None):
        steps = int(t / dt)
        output = self.network.simulate(t,dt) 
        three_d_positions  = self.network.positions
        phis,thetas = self.get_angles(three_d_positions,self.network.torus_inner_radius,self.network.torus_outer_radius)
        points = []
        for phi,theta in zip(phis,thetas):
            points.append(np.array([phi,theta]))
        points = np.array(points)
        A = self.network.A

        fig,ax = plt.subplots()

        ax.set_xlim(xlim)
        ax.set_ylim(ylim)

        ax.axis('off')
        ax.set_aspect('equal',adjustable='box')
        
        ax.add_patch(Rectangle((0,0),2*np.pi,2*np.pi,edgecolor = 'black',fill=False))

        values = (np.fmod(np.fmod(output[0],2*np.pi) + 2*np.pi,2*np.pi)) / (2*np.pi)
        

        patches = [plt.Circle(point,circle_radius) for point in points]  

        if color_distribution == "rainbow":
            colors = np.array([np.fmod(np.abs(hsv_to_rgb((value,1,0.7))),1) for value in values])
            p = PatchCollection(patches,facecolors=colors,alpha=1) 


        if color_distribution == "firefly":

            colors = np.abs(values - 0.5)
            colors[colors >= 0.1] = 0
            colors = 1 - colors * 10
            colors[colors == 1] = 0
            p = PatchCollection(patches,facecolors=cm.hot(colors),alpha=1) 


        time_label = ax.text(0.1,1,"t = 0",fontsize=16,transform=ax.transAxes)
        
        
        if line_width is not None:
            for i,j in np.transpose(np.nonzero(A)):
                ax.plot([points[i][0],points[j][0]],[points[i][1],points[j][1]],color="black",zorder=-1,linewidth=line_width)

        
        ax.add_collection(p)

        def animate(i):
            time_label.set_text(f"t = {round(dt*i,3)}")
            values = (np.fmod(np.fmod(output[i],2*np.pi) + 2*np.pi,2*np.pi)) / (2*np.pi)
            if color_distribution == "rainbow":
                colors = np.array([np.fmod(np.abs(hsv_to_rgb((value,1,0.7))),1) for value in values])
                p.set_facecolors(colors)

            if color_distribution == "firefly":
                colors = np.abs(values - 0.5)
                colors[colors >= 0.1] = 0
                colors = 1 - colors * 10
                colors[colors == 1] = 0
                p.set_facecolors(cm.hot(colors))

            return p,
        
        ani = animation.FuncAnimation(fig,animate, frames=steps,interval = 42)

        if filename is None:
            plt.tight_layout()
            plt.show(block = True)
        else:
            ani.save(f"{filename}.mp4")
        
