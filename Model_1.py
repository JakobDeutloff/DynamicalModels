import numpy as np
import matplotlib.pyplot as plt
plt.style.use(['dark_background'])

# define parameters
i = 1  # inflow [l/s]
o = 0.9  # outflow [l/s]
dt = 1  # timestep [s]
T_end = 100  # length of simulation [s]

# define initial conditions
W_0 = 0  # filling of bathtub [l]

# Initialise arrays
W = np.zeros(int(T_end/dt))
W[0] = W_0
T = np.arange(0, T_end, dt)


# Define differential equation of problem:
def dW_dt():
    return i - o


# Sove with explicit Euler algorithm
for j in np.arange(0, int(T_end / dt)-1):
    W[j + 1] = W[j] + (dW_dt() * dt)

# Plot results
fig, ax = plt.subplots()
ax.plot(T, W)
ax.set_xlabel('Time [s]')
ax.set_ylabel('Water [l]')
plt.savefig('Plots/model1.jpg')
plt.show()

