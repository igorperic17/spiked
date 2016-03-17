import pyNN.nest as sim
import numpy as np
import scipy
import pdb
import spiked.encoders as encoders

class Ensemble(object):
    """
    Ensemble manager object, providing function encoding in a population.
    """
    
    NEURON_PARAMS = { 
		'v_thresh' : -61.0, # mV 
		'tau_refrac' : 2.0, # ms
		'tau_syn_E' : 2.0, # ms
		'tau_syn_I' : 2.0
	}
    NEURON_MODEL = sim.IF_cond_exp
    SYN_PROX_IN = sim.StaticSynapse(
		delay = 1.0,
		weight = 100.0
    )
    SYN_PROX_OUT = sim.STDPMechanism(
                timing_dependence=sim.SpikePairRule(tau_plus=20.0, tau_minus=20.0,
                                                    A_plus=0.01, A_minus=0.012),
                weight_dependence=sim.AdditiveWeightDependence(w_min=0, w_max=0.0000001),
                weight=0.00000005,
                delay=0.1)
    
    def __init__(self, input_encoder, output_decoder, ensemble_size = 100):
        """
        Contructor of neural ensemble layer.
        
        @param ScalarEncoder Encoding layer for input.
        @param ScalarEncoder Decoding layer for output.
        """
        
        # TODO: assert types for encoders (in/out)
        
        self.ensemble_size = ensemble_size
        self.input_encoder = input_encoder
        self.output_decoder = output_decoder
        
        # create ensemble population
        self.cells = sim.Population(ensemble_size, self.NEURON_MODEL, self.NEURON_PARAMS)
        
        # connect encoder
        sim.Projection(self.input_encoder.population, self.cells, sim.AllToAllConnector(), self.SYN_PROX_IN)
        #pdb.set_trace()
        # connect decoder
        sim.Projection(self.cells, self.output_decoder.population, sim.AllToAllConnector(), self.SYN_PROX_IN)
        

    def Train(self):
        
        pass
        
        