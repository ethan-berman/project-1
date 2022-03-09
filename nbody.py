import numpy as np

G = 6.67e-11

datafile = open("planets.txt")

numobjects = int(datafile.readline())
universesize_m = float(datafile.readline())  #Size of universe in meters

# Data for points / planets / objects
#objects = {} #keys are names, values are dictionaries with field names

#def class planet:
#  def __init__(self, s):
  #   self.x_pos = 
  #...

#Separate arrays
#x_pos = np.zeros(numobjects)
#y_pos = np.zeros(numobjects)
#x_vel = np.zeros(numobjects)
#y_vel = np.zeros(numobjects)

#Combined 2-D array for all fields
x_pos = 0
y_pos = 1
x_vel = 2
y_vel = 3
mass = 4
objects = np.zeros((5,numobjects))

#Read planet data from file
for object in range(numobjects):
  data = datafile.readline()
  planetfields = data.split()
  for field in range(5):
    objects[field][object] = float(planetfields[field])

def calculateGravity(objects):
  """Returns a 2xN array of acceleration values."""
  #For every object, calculate and accumulate the gravity pull from each 
  # other object
  accel = np.zeros((2,numobjects))
  for index in range(numobjects):
    #for other_index in range(numobjects):
    #  if index == other_index:
    #    continue
    dx = objects[x_pos][index] - objects[x_pos][:]
    dy = objects[y_pos][index] - objects[y_pos][:]
    dist2 = dx**2 + dy**2
    f_mag = G*objects[mass]/dist2
    f_mag = np.delete(f_mag,index)
    dx = np.delete(dx,index)
    dy = np.delete(dy,index)
    dist2 = np.delete(dist2, index)
    accel[0][index] = np.sum(f_mag*dx/np.sqrt(dist2))
    accel[1][index] = np.sum(f_mag*dy/np.sqrt(dist2))
  
  return accel

def angularMomentum(objects):
  #Calculate the angular momentum of the System
  centerofmass = np.sum(objects[mass]*objects[x_pos:y_pos+1,:]) / np.sum(objects[mass])
  displacements = objects[x_pos:y_pos+1] - centerofmass
  angular_moments = np.cross(displacements, objects[x_vel:y_vel+1,:], axisa=0, axisb=0)
  angular_momenta = angular_moments*objects[mass]
  print(angular_momenta)
  return np.sum(angular_momenta)

endt = 100
t = 0
dt = 0.1

print("Angular momentum start", angularMomentum(objects))
while t < endt:
  t += dt
  accel = calculateGravity(objects)
  objects[x_pos] += objects[x_vel] * dt
  objects[y_pos] += objects[y_vel] * dt
  objects[x_vel] += accel[0] * dt
  objects[y_vel] += accel[1] * dt

print("Final state")
print(objects)

print("Angular momentum end", angularMomentum(objects))

#Justification of Parameters
#We use the gravitational constant of 'G = 6.67e-11', because this is well defined by physical sciences
#To update the position of all of the planets, we use Newton's equation for gravity:
#F = G* ((m1*m2) / r^2) 
#We calculate this force of gravity for each planet based on all of the other planets and their relative locations
#This calculates the force due to gravity, which is then applied to the direction that the planet is moving to find the acceleration and velocity
# We also use a universe size of  2.50e+11 meters.  The size of the visible universe (in real life) is  8.7e+26 meters.
# However, in this simulation we view the "universe" as just the solar system.  The solar system has a width of 287.46 billion KM, which is roughly the size we are given
# We should use the solar system size instead of the overall universe size as the rest of our universe is empty, but it doesn't affect the computations anyway
# 