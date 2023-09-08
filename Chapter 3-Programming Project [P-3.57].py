import time
import numpy as np
import matplotlib.pylab as plt

def do_sorted(n):
  bignum = 1E6
  A = np.random.randint(0,bignum,n)
  A = sorted(A)

plot_n = []
plot_walltime = []
for j in np.linspace(1E3,1E5,50):

  n = int(j)

  start = time.perf_counter()
  do_sorted(n)
  end = time.perf_counter()

  print("Sorting array of size {0:d} took {1:.6f}".format(n,(end-start)))

  plot_n.append(n)
  plot_walltime.append(end-start)

plt.plot(plot_n,plot_walltime,'o-')
plt.show()
