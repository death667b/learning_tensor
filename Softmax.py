
import numpy as np 
scores = np.array([[1, 2, 3, 6],
		   			[2, 4, 5, 6],
		   			[3, 8 ,7, 6]])



def softmax(x):
	"""Compute softmax values for each sets of scores in x."""
	return np.exp(x) / np.sum(np.exp(x), axis=0)

print (softmax(scores))

# Plot softmax curves
import matplotlib.pyplot as plt 
x = np.arange(-2.0, 6.0, 0.1)
score = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])

print (x.shape)
print (score.shape)

plt.plot(x, softmax(score/10).T, linewidth=2)
plt.show()