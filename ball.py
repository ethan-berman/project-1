import numpy as np
import matplotlib.pyplot as plt
#initial conditions
position = np.asarray([0.0, 1.0])
velocity = np.asarray([1.0, 1.0])

def acceleration(velocity):
  windresist = (-0.1)*np.linalg.norm(velocity)**2
  # unit vector in direction of wind resistance
  windresist = windresist * ((-1*velocity)/np.linalg.norm(velocity))

  #  windresist = 0.1*velocity**2
  return np.asarray([0.0, -9.8]) + windresist

endt = 2.6
#pos_t = 0.5*acceleration()*endt**2 + velocity*endt + position
#vel_t = endt*acceleration() + velocity

#update
dt = 0.0001 #timestep in seconds
times = []
positions = []
for iteration in range(int(endt/dt)):
  
  positions.append(position[1])
  times.append(iteration)
  position = position + velocity*dt
  if position[1] <= 0:
    velocity = velocity * -0.643
  else:
    velocity = velocity + acceleration(velocity)*dt

#Plot the existing simulation: 
plt.plot(times,positions)
plt.show()
print("Final state: pos=", position, "speed=",velocity)
#print("Symbolic answer: pos=", pos_t, "speed=", vel_t)

#Loss of 