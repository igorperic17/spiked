
import pyNN.nest as sim
from encoders import ScalarEncoder
from spiked.defaults import *

import pdb

class MemoryBuilder:

	def __init__(self):
		pass

	@classmethod
	def InitMemoryUnit(self):
		sim.ResetKernel()

	@classmethod
	def CreateColumn(self, numOfCells, localInhibitionRadius=0):

		column = sim.create(numOfCells, NEURON_MODEL, self.column_neuron_params, label='blabla')

		# connect column with inhibitory connections
		inhColumnConnector = sim.FixedProbabilityConnector(0.9, weigths=-10.0)
		for neuron in column:
			sim.projection(neuron, column, syn_spec = self.syn_local_inh)
		return column

	@classmethod
	def ConnectProximalDendrite(self, column, in_neuron=None):

		if in_neuron is None:
			in_neuron = nest.Create('iaf_neuron', params = {'I_e' : self.I_e_OFF})
		nest.Connect(in_neuron, column, 'all_to_all', syn_spec = self.syn_prox_in)
		return in_neuron

	@classmethod
	def ConnectBasalDendrite(self, neuron, in_neuron=None):
		if in_neuron is None:
			in_neuron = nest.Create('iaf_neuron', params = {'I_e' : self.I_e_OFF})
		
		#pdb.set_trace()
		nest.Connect(in_neuron, [neuron], 'all_to_all', self.syn_basal_in)
		return in_neuron

	@classmethod
	def SetProximalInput(self, neuron, val):
		v = self.I_e_OFF
		if val is True:
			v = self.I_e_ON
		nest.SetStatus(neuron, params = {'I_e' : v})

	############## RECORDING #################

	@classmethod
	def RecordColumnVoltages(self, column):
		vd = nest.Create('multimeter', len(column), params={'record_from': ['V_m'], 'interval' :0.1})

		# pdb.set_trace()
		nest.Connect(vd, column, 'one_to_one')
		return vd

	@classmethod
	def RecordColumnSpikes(self, column):
		sd = nest.Create('spike_detector', len(column))
		nest.Connect(column, sd, 'one_to_one')
		return sd

	@classmethod
	def FetchColumnEvents(self, sd):
		spikes = nest.GetStatus(sd, 'events')
		return spikes

	############## LAYERS (UNITS) #################

	@classmethod
	def CreateUnit(self, 
		numOfColumns,
		cellsPerColumn, 
		localInhibitionRadius=0,
		localConnectivityRadius=0):
		
		unit = []
		# create columns
		for i in range(numOfColumns):
			c = self.CreateColumn(cellsPerColumn)
			unit.append(c)
			# connect neighboring columns
			for k in range(-localConnectivityRadius, 1, 1):
				idx = i + k # index of column to connect to
				print(idx)
				if idx < 0:
					continue 
				# connect every cell to every other cell
				for p in range(cellsPerColumn):
					for q in range(cellsPerColumn):
						print(p)
						print(q)
						self.ConnectBasalDendrite(unit[i][p], unit[idx][q])

		return unit
