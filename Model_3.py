import numpy as np
import matplotlib.pyplot as plt
plt.style.use(['dark_background'])

# define parameters
life_time = 80  # average lifetime [years]
f = 1.5/life_time  # fertility [1/years]
m = 1/life_time  # mortality [1/years]
r = 0.01  # restauration rate [1/years]
h = 0.001 # harvest rate [resource/person * year]
dt = 1  # timestep [years]
T_end = 5000  # length of simulation [years]

# define initial conditions
R_0 = 1000
P_0 = 10

# Initialise arrays
P = np.zeros(int(T_end/dt))  # Population
P[0] = P_0
R = np.zeros(int(T_end/dt))  # Resource
R[0] = R_0
T = np.arange(0, T_end, dt)  # Time

# Define differential equation of problem:
def dP_dt(P, R):
    m_r = m * (1 + ((R_0 - R)/R_0))
    return (f - m_r) * P

def dR_dt(P, R):
    return r * (R_0 - R) - h * P


# Sove with explicit Euler algorithm
for i in np.arange(0, int(T_end / dt)-1):
    P[i+1] =P[i] + dP_dt(P[i], R[i]) * dt
    R[i+1] = R[i] + dR_dt(P[i], R[i]) * dt



# Plot results
fig, ax = plt.subplots()
ax.plot(T, P, label='Population')
ax.plot(T, R, label='Resource')
ax.set_xlabel('Time [years]')
ax.set_ylabel('Units')
ax.legend()
plt.savefig('Plots/model3.jpg')
plt.show()

