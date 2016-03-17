
import pyNN.nest as sim
import numpy as np
import scipy
import pdb

class Column(object):
    """
    Respresentation of column.
    """
    
    NEURON_PARAMS = { 
		'v_thresh' : -61.0, # mV 
		'tau_refrac' : 2.0, # ms
		'tau_syn_E' : 2.0, # ms
		'tau_syn_I' : 2.0
	}
    NEURON_MODEL = sim.IF_curr_exp
    SYN_PROX_IN = sim.StaticSynapse(
		delay = 1.0,
		weight = 100.0
    )
    SYN_LOCAL_INH = sim.StaticSynapse(
		delay = 1.0,
		weight = -1000.0
    )
    
    def __init__(self, num_of_cells = 6, record_spikes = True):
        """
        Creates a column of cells and connects local inhibition to it.
        
        @param num_of_cells Number of cells in the column.
        @param record_spikes Controlls creating of recorder for all cells in the column.
        """

        # store locally
        self.num_of_cells = num_of_cells

        # create the actual Column
        self.cells = sim.Population(num_of_cells, self.NEURON_MODEL, self.NEURON_PARAMS)
        
        # record spikes from cells
        if record_spikes:
            self.cells.record_v()
        
        # connect the common feedforward dendrite
        self.feedforward_dendrite = sim.Population(1, sim.SpikeSourcePoisson())
        sim.Projection(self.feedforward_dendrite, self.cells, sim.AllToAllConnector(), self.SYN_PROX_IN)
        
        # TODO: connect inhibitory inter-neuron connections
        
    
    def SetFeedforwardDendrite(self, value):
        """
        Sets the input of common (shared) feedforward dendrite to provided rate.
        """
        
        self.feedforward_dendrite.set(rate = value)
 

    def FetchSpikes(self):
        """
        Retrieves the spikes for all cells in the column.
        """
        
        return self.cells.get_data()