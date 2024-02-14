
from Network import Network
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib import animation
from matplotlib.colors import hsv_to_rgb
class Visualizer:
    network: Network

    def __init__(self,network: Network) -> None:
        self.network = network
    

    def graph_network_evolution(self,t :float = 1,dt: float = 0.01, circle_radius: float = 0.1,line_width:float = None,xlim = (-1.5,1.5),ylim=(-1.5,1.5),filename = None):
        steps = int(t / dt)
        output = self.network.simulate(t,dt) 
        points  = self.network.positions
        A = self.network.A

        fig,ax = plt.subplots()

        ax.set_xlim(xlim)
        ax.set_ylim(ylim)

        ax.axis('off')
        ax.set_aspect('equal',adjustable='box')

        values = (np.fmod(np.fmod(output[0],2*np.pi) + 2*np.pi,2*np.pi)) / (2*np.pi)
        colors = np.array([np.fmod(np.abs(hsv_to_rgb((value,1,0.7))),1) for value in values])
        patches = [plt.Circle(point,circle_radius) for point in points]  

        p = PatchCollection(patches,facecolors=colors,alpha=1) 

        time_label = ax.text(0.1,1,"t = 0",fontsize=16,transform=ax.transAxes)
        
        
        if line_width is not None:
            for i,j in np.transpose(np.nonzero(A)):
                ax.plot([points[i][0],points[j][0]],[points[i][1],points[j][1]],color="black",zorder=-1,linewidth=line_width)

        
        ax.add_collection(p)

        def animate(i):
            time_label.set_text(f"t = {round(dt*i,3)}")
            values = (np.fmod(np.fmod(output[i],2*np.pi) + 2*np.pi,2*np.pi)) / (2*np.pi)
            colors = np.array([np.fmod(np.abs(hsv_to_rgb((value,1,0.7))),1) for value in values])
            p.set_facecolors(colors)
            return p,
        
        ani = animation.FuncAnimation(fig,animate, frames=steps,interval = 42)

        if filename is None:
            plt.tight_layout()
            plt.show(block = True)
        else:
            ani.save(f"{filename}.mp4")
        

    
    def circle_network_evolution(self,t: float = 1, dt: int = 0.01, circle_radius: float = 0.1, line_width = None, filename = None):
        steps = int(t / dt)
        output = self.network.simulate(t,dt) 
        A = self.network.A
       

        fig,ax = plt.subplots()
        
        ax.set_xlim((-1.5,1.5))
        ax.set_ylim((-1.5,1.5))

        ax.axis('off')
        ax.set_aspect('equal',adjustable='box')

        circles = [plt.Circle(point,circle_radius,color='blue') for point in [(0,0)]*len(A)]

        if line_width is not None:
            lines = [plt.plot([], [],color="black",zorder=-1,linewidth=line_width)[0] for _ in range(len(np.transpose(np.nonzero(A))))]
            patch = lines + circles
        else:
            patch = circles


        def init():
            points = [(x,y) for x,y in zip(np.cos(output[0]),np.sin(output[0]))]
            if line_width is not None:
                for k,p in enumerate(np.transpose(np.nonzero(A))):
                    i = p[0]
                    j = p[1]
                    lines[k].set_data([points[i][0],points[j][0]],[points[i][1],points[j][1]])
            
            for i, circle in enumerate(circles):
                circle.center = points[i]
                ax.add_patch(circle)
            
            return patch
        
        def animate(m):
            points = [(x,y) for x,y in zip(np.cos(output[m]),np.sin(output[m]))]
            if line_width is not None:
                for k,p in enumerate(np.transpose(np.nonzero(A))):
                    i = p[0]
                    j = p[1]
                    lines[k].set_data([points[i][0],points[j][0]],[points[i][1],points[j][1]])
                    lines[k].set_color('black')
            
            for i, circle in enumerate(circles):
                circle.center = points[i]
                ax.add_patch(circle)
            
            return patch

        ani = animation.FuncAnimation(fig,animate,init_func=init, frames=steps,interval = 42)  
        if filename is None:
            plt.tight_layout()
            plt.show(block = True)
        else:
            ani.save(f"{filename}.mp4")
        
        

    
    def phase_plot(self,t: float = 1, dt: float = 0.01,mod = True,filename = None):
        steps = int(t / dt)
        output = self.network.simulate(t,dt)
        if mod:
            output = np.fmod(np.fmod(output,2*np.pi) + 2*np.pi,2*np.pi)
        xs = np.linspace(0,t,steps,endpoint=False)
        for i in range(len(self.network.A)):
            plt.plot(xs,output[:,i])
        
        if filename is None:
            plt.tight_layout()
            plt.show(block = True)
        else:
            filename.savefig(f"{filename}".png)
        

    





        
        
