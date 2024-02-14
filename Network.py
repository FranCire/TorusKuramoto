import numpy as np
from scipy.integrate import odeint


class Network:
    w: float   
    A: np.array        
    thetas: np.array   
    positions: np.array

    def __init__(self,A: np.array,initial_thetas: np.array,w: float = 0,positions = None) -> None:
        self.w = w                  #Frequency of Nodes
        self.A = A                  #Adjacency Matrix
        if positions is None:
            n = len(A)
            size = 2 * np.pi / n
            angles = [x * size for x in range(n)]
            positions = np.array([(np.cos(angle),np.sin(angle)) for angle in angles])
        
        self.initial_thetas = initial_thetas        #Initial Angles


        
        self.positions = positions      #Positions purely for display purposes. If no positions are given, defaults to circle distribution

        self.density = np.sum(A.astype(bool)) / (len(A)*(len(A) - 1))
 
        def __dthetadt(thetas,t,A,w):
            dthetadt = w + np.array([A[i] @ np.sin(thetas - theta_i) for i,theta_i in enumerate(thetas)])
            return dthetadt
        
        self.__dthetadt = __dthetadt   #Derivative Function
    
    def set_initial_thetas(self,initial_thetas):
        self.initial_thetas = initial_thetas
    

    def simulate(self,t :float = 1,dt :float = 0.01,full_output :bool = True):
        steps = int(t / dt)
        t = np.linspace(0,t,steps,endpoint=False)
        
        solution = odeint(self.__dthetadt,self.initial_thetas,t,args=(self.A,self.w))
        if not full_output:
            solution = solution[-1]
        
        return solution
    
    

        


     

   
