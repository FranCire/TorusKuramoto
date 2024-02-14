
from Network import Network
import numpy as np
from scipy.spatial import Delaunay

class TorusNetwork3D(Network):

    def __generate_torus_random_positions(self):
        positions = np.zeros((self.size,3))
        i = 0
        r = self.torus_inner_radius
        R = self.torus_outer_radius
        phis = []
        thetas = []
        while i < self.size:
            U = np.random.uniform()
            V = np.random.uniform()
            W = np.random.uniform()
            theta = 2*np.pi*U
            phi = 2*np.pi*V
            if W <= (R + r * np.cos(theta))/(r + R):
                positions[i] = np.array([(R + r*np.cos(theta))*np.cos(phi),(R + r*np.cos(theta))*np.sin(phi),r*np.sin(theta)])
                phis.append(phi)
                thetas.append(theta)
                i += 1
        

        
        return positions
    
    def __generate_square_random_positions(self):
        positions = np.zeros((self.size,3))
        r = self.torus_inner_radius
        R = self.torus_outer_radius
        for i in range(self.size):
            phi = np.random.uniform() * 2 * np.pi
            theta = np.random.uniform() * 2 * np.pi
            positions[i] = np.array([(R + r*np.cos(theta))*np.cos(phi),(R + r*np.cos(theta))*np.sin(phi),r*np.sin(theta)])
        return positions
    def __create_distance_adjacency(self,positions):
        A = np.zeros((self.size,self.size))
        for i in range(self.size):
            for j in range(self.size):
                if i != j and np.linalg.norm(positions[i] - positions[j]) < self.eps:
                    A[i,j] = 1
        
        return A
    
    def __create_delauney_adjacency(self, positions):
        A = np.zeros((self.size,self.size))
        tri = Delaunay(positions)
        for triangle in tri.vertices:
            a,b,c,d = triangle
            A[a][b] = A[b][a] = A[a][c] = A[c][a] = A[b][c] = A[c][b] = A[a][d] = A[d][a] = A[b][d] = A[d][b] = A[c][d] = A[d][c] = 1

        
        return A
    
    def __create_k_nearest_neighbours(self,positions,k):
        A = np.zeros((self.size,self.size))
        for i,pos in enumerate(positions):
            dists = np.argsort(np.linalg.norm(positions - pos,axis=1))
            for j in range(1,k+1):
                A[i][dists[j]] = A[dists[j]][i] = 1

        return A
    
    def __init__(self, w: float = 1, size: int = 20, connection_type="dist", initial_thetas: np.array = None, torus_outer_radius: float = 1, torus_inner_radius: float = 0.5, theta_function=None, eps: float = 0.5, k: int = None, positions = None, position_type = "torus_random") -> None:
        self.size = size
        self.torus_outer_radius = torus_outer_radius
        self.torus_inner_radius = torus_inner_radius
        if positions is None:
            if position_type == "torus_random":
                positions = self.__generate_torus_random_positions()
            if position_type == "square_random":
                positions = self.__generate_square_random_positions()
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
                initial_thetas = theta_function(positions,self.torus_inner_radius,self.torus_outer_radius)

        super().__init__(A, initial_thetas, w, positions)
    


        

