import pyNN.nest as sim
import logging
import pdb

import matplotlib.pyplot as plt

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

logger.info('Starting script.')

sim.setup(timestep=0.1, min_delay=0.1)

cell_params = { 'v_rest': -70.0, 'v_thresh': -52.0 }
pop1 = sim.Population(10, sim.SpikeSourcePoisson, { 'rate' : 20.0 })
pop2 = sim.Population(20, sim.IF_cond_alpha, cell_params)

pop1.record('spikes', to_file=False)
sim.run(1000)

spikes = pop1.getSpikes()
spikes = [int(x) for x in spikes.segments[0].spiketrains[0]] 
# pdb.set_trace()

print('Recorded spikes:')
print(spikes)
x_ax = [1.0] * len(spikes)
print(x_ax)
plt.scatter(spikes, x_ax)
plt.show()
