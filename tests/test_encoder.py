from spiked.encoders import ScalarEncoder
import logging
import numpy as np
import pyNN.nest as sim

import matplotlib.pyplot as plt
import pyNN.utility.plotting as pynnplt

import pdb

LOG = logging.getLogger(__name__)
LOG.addHandler(logging.StreamHandler())
LOG.setLevel(logging.INFO)

def plot_signal(signal, index, colour='b'):
    
    plt.plot(signal.times, signal[:, index], colour)
    plt.setp(plt.gca().get_xticklabels(), visible=False)
    plt.show()
    
def test_default_params():
    """
    Checking if creating encoder with defualt values works.
    """
    encoder = ScalarEncoder.ScalarEncoder()
    LOG.info('Encoder created: {}'.format(encoder))

def test_encoder_rate_1():
    """
    Checks if encoder is properly encoding provided values.
    """

    encoder = ScalarEncoder.ScalarEncoder(
        size=10, width=1, min_val=0, max_val=10)
    encoder.encode(5.0)

    sim.run(100)

    rate = encoder.population.getSpikes()
    voltages = encoder.population.get_v().segments[0]
    
    pdb.set_trace()
    
    plot_signal(voltages, 1)
    
    # get index of maximum rate neuron
    idx_max = np.argmax(rate)
    LOG.info(rate)
    LOG.info('Max firing rate: {}'.format(idx_max))

    assert idx_max == 4  # indexing starts from zero

if __name__ == '__main__':

    # run tests
    sim.setup()

    test_default_params()
    test_encoder_rate_1()
    