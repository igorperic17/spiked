from spiked.memory import Column
import logging
import numpy as np
import pyNN.nest as sim
import nest

LOG = logging.getLogger(__name__)
LOG.addHandler(logging.StreamHandler())
LOG.setLevel(logging.INFO)

def test_default_params():
    """
    Checking if creating encoder with defualt values works.
    """
    
    # reset the simulator
    nest.reset()
    
    column = Column.Column()
    LOG.info('Column created: {}'.format(column))


def test_column_input():
    """
    Tests whether all neurons receive the same feedforward input from
    common proximal dendrite.
    """
    
    LOG.info('Testing column input...')
    
    # reset the simulator
    sim.reset()
    
    column = Column.Column()
    sim.run(1000)
    spikes = column.FetchSpikes()
    print('Spikes before: {}'.format(spikes))
    
    # now stream some input into the column
    column.SetFeedforwardDendrite(1000.0)
    sim.run(1000)
    spikes = column.FetchSpikes().segments[0]
    print('Spikes after: {}'.format(spikes))
    
    LOG.info('Test complete.')
    

def test_column_inhibition():
    """
    Checks if only a single cell fires in the column
    """
    
    LOG.info('Testing inter-column inhibition...')
    
    # reset the simulator
    sim.reset()
    
    LOG.info('Test complete.')
    
    
if __name__ == '__main__':
    
    # setup the simulator
    sim.setup()

    # run tests
    #test_default_params()
    test_column_input()
    #test_column_inhibition()
    