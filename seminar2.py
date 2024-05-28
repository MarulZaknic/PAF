import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

class Svemir:
    def __init__(self):
        self.lista_planeta = []

    def dodavac_planeta(self, x, y, z, vx, vy, vz, masa):
        novi_planet = Planet(x, y, z, vx, vy, vz, masa, self)
        return novi_planet

    def simulacija(self, steps, interval):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_box_aspect([1, 1, 1])  # Aspect ratio is 1:1:1

        def update(frame):
            ax.clear()
            max_range = 0
            for el in self.lista_planeta:
                el.move()
                max_range = max(max_range, np.linalg.norm(el.vec_r))
            max_range += 1  # Padding for visibility
            ax.set_xlim([-max_range, max_range])
            ax.set_ylim([-max_range, max_range])
            ax.set_zlim([-max_range, max_range])
            for el in self.lista_planeta:
                ax.scatter(el.vec_r[0], el.vec_r[1], el.vec_r[2], s=el.m * 100)  # Scale size for visibility
            ax.set_xlabel('X [AU]')
            ax.set_ylabel('Y [AU]')
            ax.set_zlabel('Z [AU]')

        ani = FuncAnimation(fig, update, frames=range(steps), interval=interval)
        plt.show()

class Planet:
    def __init__(self, x_0, y_0, z_0, vx_0, vy_0, vz_0, m, svemir_instance):
        self.vec_r = np.array([x_0, y_0, z_0], dtype=np.float64)
        self.vec_v = np.array([vx_0, vy_0, vz_0], dtype=np.float64)
        self.m = m
        self.svemir_instance = svemir_instance
        self.svemir_instance.lista_planeta.append(self)

    def move(self):
        G = 39.478  # Gravitational constant in AU^3 / (solar mass * day^2)
        dt = 1  # Time step in days
        a = np.zeros(3, dtype=np.float64)

        for el in self.svemir_instance.lista_planeta:
            if el != self:
                r_vec = el.vec_r - self.vec_r
                r_mag = np.linalg.norm(r_vec)
                if r_mag > 0:  # Avoid division by zero
                    a += G * el.m * r_vec / r_mag**3

        self.vec_v += a * dt
        self.vec_r += self.vec_v * dt
        print(f"Position: {self.vec_r}, Velocity: {self.vec_v}")  # Debugging output

# Create the universe instance
uni1 = Svemir()
# Adding Earth with normalized units (1 AU, 0, 0) and velocity (0, 0.0172 AU/day, 0) with mass 3e-6 solar masses
uni1.dodavac_planeta(1, 0, 0, 0, 0.0172, 0, 3e-6)  # Earth
# Adding Sun with normalized units (0, 0, 0) and mass 1 solar mass
uni1.dodavac_planeta(0, 0, 0, 0, 0, 0, 1)  # Sun

# Run the simulation
uni1.simulacija(steps=365, interval=50)  # Simulate for 1 year with 1-day steps
