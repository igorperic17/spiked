import nest
import matplotlib.pyplot as plt

from psmu.core import MemoryBuilder, ScalarEncoder

import pdb

# create a column
col1 = MemoryBuilder.CreateColumn(6)

# create a common proximal dendrite and dedicated input neuron
input_neuron = MemoryBuilder.ConnectProximalDendrite(col1)
basal_neuron = MemoryBuilder.ConnectBasalDendrite(col1[0])
basal_neuron2 = MemoryBuilder.ConnectBasalDendrite(col1[1])

# turn on recording of spikes for this column
sd = MemoryBuilder.RecordColumnSpikes(col1)
vd = MemoryBuilder.RecordColumnVoltages(col1)

# prepare plotting
plt.figure()
#plt.ion()

# run loop
for i in range(50):
	plt.clf()

	if i > 5:
		MemoryBuilder.SetProximalInput(basal_neuron, True)

	if i > 10:
		MemoryBuilder.SetProximalInput(input_neuron, True)

	if i > 22:
		MemoryBuilder.SetProximalInput(basal_neuron, False)
		MemoryBuild0r.SetProximalInput(basal_neuron2, True)

	if i > 30:
		MemoryBuilder.SetProximalInput(basal_neuron2, False)

	column_spikes = MemoryBuilder.FetchColumnEvents(sd)
	column_v = MemoryBuilder.FetchColumnEvents(vd)
	
	for i in range(len(sd)):
		plt.plot(column_v[i]['times'], column_v[i]['V_m'])
		plt2.scatter(column_v[i]['times'], sd[i]) 
	plt.draw()

	nest.Simulate(100)

plt.show()
