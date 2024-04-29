import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d



class cestica:
    def __init__(self, x_0, y_0, z_0, vx_0, vy_0, vz_0, q, m, Bx, By, Bz, Ex, Ey, Ez):

        self.x_0 = x_0
        self.y_0 = y_0
        self.z_0 = z_0
        self.vx_0 = vx_0
        self.vy_0 = vy_0
        self.vz_0 = vz_0
        self.q = q
        self.m = m
        self.Bx = Bx
        self.By = By
        self.Bz = Bz
        self.Ex = Ex
        self.Ey = Ey
        self.Ez = Ez


    def gibanje_euler(self):
        x_0 = self.x_0
        y_0 = self.y_0
        z_0 = self.z_0
        vx_0 = self.vx_0
        vy_0 = self.vy_0
        vz_0 = self.vz_0
        q = self.q
        m = self.m
        Bx = self.Bx
        By = self.By
        Bz = self.Bz
        Ex = self.Ex
        Ey = self.Ey
        Ez = self.Ez
        dt = 0.01
        vremenska_lista = np.arange(0, 40, dt)
        vec_v = np.array([vx_0, vy_0, vz_0])
        vec_b = np.array([Bx, By, Bz])
        vec_e = np.array([Ex, Ey, Ez])
        vec_poz = np.array([x_0, y_0, z_0])
        lista_poz_vec = [vec_poz]
        x_poz = []
        y_poz = []
        z_poz = []

        for aki in vremenska_lista:
            vec_a = (q/m)*(vec_e + np.cross(vec_v, vec_b))
            vec_v = vec_v + vec_a*dt
            vec_poz = vec_poz + vec_v*dt
            lista_poz_vec.append(vec_poz)
        for eli in lista_poz_vec:
            x_poz.append(eli[0])
            y_poz.append(eli[1])
            z_poz.append(eli[2])
       


        ax.plot(x_poz, y_poz, z_poz)
    def gibanje_rgk(self):
        x_0 = self.x_0
        y_0 = self.y_0
        z_0 = self.z_0
        vx_0 = self.vx_0
        vy_0 = self.vy_0
        vz_0 = self.vz_0
        q = self.q
        m = self.m
        Bx = self.Bx
        By = self.By
        Bz = self.Bz
        Ex = self.Ex
        Ey = self.Ey
        Ez = self.Ez
        dt = 0.01
        vremenska_lista = np.arange(0, 40, dt)
        vec_v = np.array([vx_0, vy_0, vz_0])
        vec_b = np.array([Bx, By, Bz])
        vec_e = np.array([Ex, Ey, Ez])
        vec_pol = np.array([x_0, y_0, z_0])
        vec_pol_lista = []
        for kio in vremenska_lista:
            k1_vec_brz = (q/m)*(vec_e + np.cross(vec_v, vec_b))*dt
            k1_vec_pol = vec_v*dt
            k2_vec_brz = (q/m)*(vec_e + np.cross((vec_v + (k1_vec_brz/2)), vec_b))*dt
            k2_vec_pol = (vec_v + (k1_vec_brz/2))*dt
            k3_vec_brz = (q/m)*(vec_e + np.cross((vec_v + (k2_vec_brz/2)), vec_b))*dt
            k3_vec_pol = (vec_v + (k2_vec_brz/2))*dt
            k4_vec_brz = (q/m)*(vec_e + np.cross((vec_v + (k3_vec_brz/2)), vec_b))*dt
            k4_vec_pol = (vec_v + (k3_vec_brz/2))*dt
            vec_v = vec_v + (1/6)*(k1_vec_brz + 2*k2_vec_brz + 2*k3_vec_brz + k4_vec_brz)
            vec_pol = vec_pol + (1/6)*(k1_vec_pol + 2*k2_vec_pol + 2*k3_vec_pol + k4_vec_pol)
            vec_pol_lista.append(vec_pol)
            pol_listax = []
            pol_listay = []
            pol_listaz = []
        for aij in vec_pol_lista:
            pol_listax.append(aij[0])
            pol_listay.append(aij[1])
            pol_listaz.append(aij[2])
        ax.plot(pol_listax,pol_listay,pol_listaz)
        






   






fig = plt.figure()
ax = plt.axes(projection='3d')
elektron = cestica(0, 0, 0, 0.1, 0.1, 0.1, -1, 1, 0, 0, 1, 0, 0, 0)
elektron.gibanje_euler()
elektron.gibanje_rgk()
pozitron = cestica(0, 0, 0, 0.1, 0.1, 0.1, 1, 1, 0, 0, 1, 0, 0, 0)
pozitron.gibanje_euler()
pozitron.gibanje_rgk()
plt.show()

        
    



        
        
