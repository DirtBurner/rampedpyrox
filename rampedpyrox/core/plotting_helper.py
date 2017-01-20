'''
This module contains helper functions for plotting rampedpyrox data.
'''


from __future__ import(
	division,
	print_function,
	)

__docformat__ = 'restructuredtext en'
__all__ = ['_plot_dicts', '_rem_dup_leg']

import numpy as np

#define function to pull plotting dicts
def _plot_dicts(case, td):
	'''
	Function to access different plotting dicts.

	Parameters
	----------
	case : str
		The case that defines the dict to pull.
		Acceptable strings:

			'rpo_rd', \n
			'rpo_labs', \n
			'rpo_md'

	td : TimeData or subclass
		``rp.TimeData`` instance containing the data to plot.

	Returns
	-------
	pl_dict : dict
		The resulting dictionary containing plotting info.
	'''

	if case == 'rpo_labs':
		#create a nested dict to keep track of axis labels
		pl_dict = {'time': 
						{'fraction' : ('time (s)', 'g (unitless)'),
						'rate' : ('time (s)', r'fraction/time $(s^{-1})$')
						},
					'temp' : 
						{'fraction' : ('temp (K)', 'g (unitless)'),
						'rate' : ('temp (K)', r'fraction/temp $(K^{-1})$')}
						}
	
	elif case == 'rpo_md':
		#create a nested dict to keep track of cases of modeled data
		pl_dict = {'time': 
						{'fraction' : (td.t, td.ghat),
						'rate' : (td.t, -td.dghatdt)
						},
					'temp': 
						{'fraction' : (td.T, td.ghat),
						'rate' : (td.T, -td.dghatdT)}
						}

	elif case == 'rpo_rd':
		#create a nested dict to keep track of cases for real data
		pl_dict = {'time': 
						{'fraction' : (td.t, td.g),
						'rate' : (td.t, -td.dgdt)
						},
					'temp': 
						{'fraction' : (td.T, td.g),
						'rate' : (td.T, -td.dgdT)}
						}

	return pl_dict

#define function to remove duplicate legend entries
def _rem_dup_leg(ax):
	'''
	Removes duplicate legend entries.

	Parameters
	----------
	ax : plt.axishandle
		Axis handle containing entries to remove.

	Returns
	-------
	han_list : list
		List of axis handles.

	lab_list : list
		List of axis handle labels.
	'''
	han, lab = ax.get_legend_handles_labels()
	han_list, lab_list = [], []
	
	for h, l in zip(han, lab):
		
		if l not in lab_list:
		
			han_list.append(h)
			lab_list.append(l)

	return han_list, lab_list
