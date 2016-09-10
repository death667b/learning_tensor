

scores = [3.0, 1.0, 0.2]

import numpy as np 

def softmax(x):
	"""Compute softmax values for each sets of scores in x."""
	return (np.exp(x)) / (np.sum(np.exp(x)))

print (softmax(scores))

# Plot softmax curves
import matplotlib.pyplot as plt 

plt.plot([1.0, 2.0, 3.0], softmax(scores), linewidth=2)
plt.show()