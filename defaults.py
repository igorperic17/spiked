"""
Contains definition of all constants and default values.
"""

SYN_LOCAL_INH = {
    #'model' : 'tsodyks_synapse',
    #'tau_rec' : 1000.0, # recovery time
    #'tau_psc' : 100.0, # ?
    'delay' : 1.0,
    'weight': -1000.0
}
SYN_PROX_IN = {
    'delay' : 1.0,
    'weight' : 100.0
}
SYN_BASAL_IN = {
    'model' : 'stdp_synapse',
    'delay' : 1.0,
    'weight' : 10.0
}
SOMA_NEURON_PARAMS = { 
    'v_thresh' : -61.0, # mV 
    'tau_refrac' : 2.0, # ms
    'tau_syn_E' : 2.0, # ms
    'tau_syn_I' : 2.0
}

I_E_OFF = 0.0  # boolean False
I_E_ON = 1e4  # boolean True

# default neuron model to use
NEURON_MODEL = sim.IF_curr_exp