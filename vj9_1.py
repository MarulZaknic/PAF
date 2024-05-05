import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Create some random data for demonstration
num_points = 100
x = np.random.rand(num_points)
y = np.random.rand(num_points)
z = np.random.rand(num_points)

# Create a figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the initial points
points, = ax.plot(x, y, z, 'bo')

# Define the update function for the animation
def update(frame):
    # Update the coordinates of the points
    x[:] += 0.01 * np.random.randn(num_points)
    y[:] += 0.01 * np.random.randn(num_points)
    z[:] += 0.01 * np.random.randn(num_points)
    
    # Update the plot with the new coordinates
    points.set_data(x, y)
    points.set_3d_properties(z)
    return points,

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

plt.show()

