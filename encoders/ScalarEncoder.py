
import pyNN.nest as sim
import numpy as np
import scipy
import pdb

class ScalarEncoder(object):
    """
    Object for encoding scalar values into population of neurons.

    Creates a Gaussian-shapped rate encoded output,
    ready to be connected to other input layers.

    Local members:
        * encoder_def: Definition of the encoder. Stores:
            - size (in number of neurons)
            - width of sparse part
                (stddev, given from [0,1] as percentage of total size)
            - min and max (edge) values
    """

    NEURON_MODEL = sim.IF_cond_exp
    NEURON_PARAMS = { 
		'v_thresh' : -61.0, # mV 
		'tau_refrac' : 2.0, # ms
		'tau_syn_E' : 2.0, # ms
		'tau_syn_I' : 2.0
	}
    
    def __init__(self, size=10, width=1, min_val=0, max_val=10):

        # TODO: sanity check for params

        # store the encoder params locally
        self.encoder_def = {
			'size' : int(size),
			'width' : int(width),
			'min_val' : float(min_val),
			'max_val' : float(max_val)
		}

        # create the actual population
        self.population = sim.Population(self.encoder_def['size'], \
            self.NEURON_MODEL, self.NEURON_PARAMS)
        self.population.record(['spikes'])
        
        # create teaching stimulus sources
        self.stimulus = sim.Population(self.encoder_def['size'], \
            sim.SpikeSourcePoisson())
        sim.Projection(self.stimulus, self.population, sim.OneToOneConnector(), \
            sim.StaticSynapse(weight=1.0))
        

    def encode(self, value):
        """
        Encodes provided value into rates of local Poisson generators.

        params:
        * value: Scalar value to be encoded.
        """

        # TODO: sanity check for input (fits in [min,max]?)

        # compute histogram of rates
        params = {
            "mu": value,
            "sigma": 0.1
            }
        #limits = (self.encoder_def['min_val'], self.encoder_def['max_val'])
        limits = (0, self.encoder_def['size'])
        bins = np.linspace(*limits, num=self.encoder_def['size'])
        d = scipy.stats.norm(value, scale=self.encoder_def['width'])
        pdf = d.pdf(bins) * self.encoder_def['size']

        # set rates of each Poisson generator in encoder
        self.stimulus.set(rate=pdf)
        #pdb.set_trace()

    def decode(self):
        """
        Decodes the current rate of activations of population.
        """



