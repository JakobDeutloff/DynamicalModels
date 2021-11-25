import numpy as np
import matplotlib.pyplot as plt

# define parameters
life_time = 80  # average lifetime [years]
f = 1.5/life_time  # fertility [1/years]
m = 1/life_time  # mortality [1/years]
dt = 1  # timestep [years]
T_end = 1000  # length of simulation [years]

# define initial conditions
P_0 = 1000  # Total population [peolpe]

# Initialise arrays
P = np.zeros(int(T_end/dt))  # Population
P[0] = P_0
T = np.arange(0, T_end, dt)  # Time


# Define differential equation of problem:
def dW_dt(P):
    return (f-m) * P


# Sove with explicit Euler algorithm
for i in np.arange(0, int(T_end / dt)-1):
    P[i + 1] = P[i] + dW_dt(P[i]) * dt

# Plot results
fig, ax = plt.subplots()
ax.plot(T, P)
ax.set_xlabel('Time [years]')
ax.set_ylabel('Population [people]')
plt.tight_layout()
plt.savefig('Plots/model2_1.jpg')
plt.show()
