import pyNN.nest as sim
import numpy as np
import scipy
import pdb
import spiked.memory.Column as MemoryColumn

class Layer(object):
    """
    Column manager, takes care about spatial organization of memory layer, 
    connectivity of columns in it and attached encoders and decoders.
    """
    
    def __init__(self, layer_size = (10, 10, 6), inhibition_radius = 2):
        """
        Contructor of memory layer.
        
        @param layer_size (X,Y,Z) size of the layer, where:
            - Z is the number of cells each column and 
            - (X,Y) is 2D grid size of memory, so total number of columns is X * Y
        @param inhibition_radius
        """
        self.layer_size = layer_size
        self.inhibition_radius = inhibition_radius
        self.N = layer_size[0]
        self.M = layer_size[1]
        self.num_of_columns = self.N * self.M
        self.cells_per_column = layer_size[2]
        
        # create columns
        self.columns = [ MemoryColumn.Column(self.cells_per_column) ] * self.num_of_columns
        
        # connect local inhibition
        for i in range(self.N):
            for j in range(self.M):
                pass
    
    def ConnectEncoder(self, input_encoder):
        """
        Sets provided encoder as input to the current memory layer.
        
        Encoder has to be of size (X*Y).
        """
        
        
        
        