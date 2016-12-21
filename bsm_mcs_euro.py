import numpy as np
import matplotlib.pyplot as plt

S0 = 100
K = 105
T = 1.0
r = 0.05
sigma = 0.2/250

I = 100000

z = np.random.standard_normal(I)
ST = S0 * np.exp((r-0.5*sigma**2)*T+sigma*np.sqrt(T)*z)

plt.plot(ST)


hT = np.maximum(ST-K, 0)
C0 = np.exp(-r * T)*np.sum(hT) / I

print "Value of the European Call Option %5.3f" % C0
