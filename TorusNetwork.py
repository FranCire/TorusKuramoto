from Network import Network
import numpy as np
from scipy.spatial import Delaunay


class TorusNetwork(Network):
    def __generate_positions(self):
        angles = np.random.uniform(low = 0,high = 2*np.pi,size = self.size)
        radiuses = np.sqrt(np.random.uniform(low = self.torus_inner_radius**2,high = self.torus_outer_radius**2,size = self.size))
        xs = np.cos(angles) * radiuses
        ys = np.sin(angles) * radiuses
        positions = np.stack((xs,ys),axis=1)
        return positions

    def __create_distance_adjacency(self,positions):
        A = np.zeros((self.size,self.size))
        for i in range(self.size):
            for j in range(self.size):
                if i != j and np.linalg.norm(positions[i] - positions[j]) < self.eps:
                    A[i,j] = 1
        
        return A
    
    def __create_delauney_adjacency(self,positions):
        A = np.zeros((self.size,self.size))
        tri = Delaunay(positions)
        for triangle in tri.vertices:
            print(triangle)
            a,b,c = triangle
            A[a][b] = A[b][a] = A[a][c] = A[c][a] = A[b][c] = A[c][b] = 1

        
        return A
    
    def __create_k_nearest_neighbours(self,positions,k):
        A = np.zeros((self.size,self.size))
        for i,pos in enumerate(positions):
            dists = np.argsort(np.linalg.norm(positions - pos,axis=1))
            for j in range(1,k+1):
                A[i][dists[j]] = A[dists[j]][i] = 1

        return A


    def __init__(self,w:float = 1,size: int = 20, connection_type = "dist", initial_thetas: np.array = None,torus_outer_radius: float = 1, torus_inner_radius: float = 0.5,theta_function = None,eps: float = 0.5,k: int = None,positions = None) -> None:
        self.size = size
        self.torus_outer_radius = torus_outer_radius
        self.torus_inner_radius = torus_inner_radius
        if positions is None:
            positions = self.__generate_positions()
        if connection_type == "dist":
            self.eps = eps
            A = self.__create_distance_adjacency(positions)
        elif connection_type == "delauney":
            A = self.__create_delauney_adjacency(positions)
        elif connection_type == "nearest":
            A = self.__create_k_nearest_neighbours(positions,k)
        else:
            raise Exception("Not a valid connection type. Connection type must be either dist, delauney or nearest")
        if initial_thetas is None:
            if theta_function is None:
                initial_thetas = np.random.uniform(low = 0,high = 2*np.pi, size=size)
            else:
                initial_thetas = theta_function(positions)

        super().__init__(A, initial_thetas, w, positions)
