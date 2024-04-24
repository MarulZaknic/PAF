import matplotlib.pyplot as plt
import numpy as np
def sgn(number):
    if number<0:
        return(-1)
    else:
        return(1)
class projectile:
    def __init__(self, x_0, y_0, v_0x, v_0y, A, gust, masa, C_d, t):

        #funkcija definiranja variabli
        self.x_0 = x_0
        self.y_0 = y_0
        self.v_0x = v_0x
        self.v_0y = v_0y
        self.A = A
        self.C_d = C_d
        self.t = t
        self.gust = gust
        self.masa = masa
    def  num_rjesenje(self):

        #funkcija numeričkog računanja kosog hitca sa otporom zraka Eulerovom metodom
        x_0 = self.x_0
        y_0 = self.y_0
        v_0x = self.v_0x
        v_0y = self.v_0y
        A = self.A
        masa = self.masa
        gust = self.gust
        C_d = self.C_d
        t = self.t
        dt = 0.001
        g = 9.8
        konst_oz = (gust*C_d*A)/(2*masa)
        x_num = x_0
        y_num = y_0
        vx_num = v_0x
        vy_num = v_0y
        ay_num = - g - 1*sgn(vy_num)* (konst_oz*vy_num**2) 
        ax_num = - 1*sgn(vx_num)*(konst_oz*vx_num**2)
        y_lista = []
        x_lista = []

        #petlja numeričke iteracije
        while y_num>=0:
            vy_num = vy_num + ay_num*dt
            vx_num = vx_num + ax_num*dt
            ay_num = -g-1*sgn(vy_num)* konst_oz*(vy_num**2) 
            ax_num = -1*sgn(vx_num)*konst_oz*(vx_num**2)
            y_num = y_num + vy_num*dt
            y_lista.append(y_num)
            x_num = x_num + vx_num*dt
            x_lista.append(x_num)
        plt.plot(x_lista, y_lista)
        plt.xlabel("apcisa")
        plt.ylabel("ordinata")
        plt.show()
    def runge_kutta_rjesenje(self):

        #funkcija numeričkog računanja kosog hitca sa otporom zraka Runge-Kutta metodom
        x_0 = self.x_0
        y_0 = self.y_0
        v_0x = self.v_0x
        v_0y = self.v_0y
        A = self.A
        masa = self.masa
        gust = self.gust
        C_d = self.C_d
        t = self.t
        dt = 0.01
        g = 9.8
        konst_oz = (gust*C_d*A)/(2*masa)
        x_num = x_0
        y_num = y_0
        vx_num = v_0x
        vy_num = v_0y
        y_lista = [y_0]
        x_lista = [x_0]
        tt = 0

        #petlje numeričke iteracije
        while y_num>=0:
            k1_vx = -sgn(vx_num)*konst_oz*(vx_num)**2 * dt
            k1_x = vx_num * dt
            k2_vx = -sgn(vx_num + k1_vx)*konst_oz*(vx_num + (k1_vx/2))**2 * dt
            k2_x = (vx_num + (k1_vx/2)) * dt
            k3_vx = -sgn(vx_num + k2_vx)*konst_oz*(vx_num + (k2_vx/2))**2 * dt
            k3_x = (vx_num + (k2_vx/2)) * dt
            k4_vx = -sgn(vx_num + k3_vx)*konst_oz*(vx_num + (k3_vx/2))**2 * dt
            k4_x = (vx_num + (k3_vx/2)) * dt
            vx_num = vx_num + (1/6)*(k1_vx + 2*k2_vx + 2*k3_vx + k4_vx)
            x_num = x_num + (1/6)*(k1_x + 2*k2_x + 2*k3_x + k4_x)
            x_lista.append(x_num)


            k1_vy = (-g -sgn(vy_num)*konst_oz*(vy_num)**2) * dt
            k1_y = vy_num * dt
            k2_vy = (-g -sgn(vy_num + k1_vy)*konst_oz*(vy_num + (k1_vy/2))**2) * dt
            k2_y = (vy_num + (k1_vy/2)) * dt
            k3_vy = (-g -sgn(vy_num + k2_vy)*konst_oz*(vy_num + (k2_vy/2))**2) * dt
            k3_y = (vy_num + (k2_vy/2)) * dt
            k4_vy = (-g -sgn(vy_num + k3_vy)*konst_oz*(vy_num + (k3_vy/2))**2) * dt
            k4_y = (vy_num + (k3_vy/2)) * dt
            vy_num = vy_num + (1/6)*(k1_vy + 2*k2_vy + 2*k3_vy + k4_vy)
            y_num = y_num + (1/6)*(k1_y + 2*k2_y + 2*k3_y + k4_y)
            y_lista.append(y_num)

            plt.plot(x_lista, y_lista)
        def eulerova_metoda(el):
            x_num = x_0
            y_num = y_0
            vx_num = v_0x
            vy_num = v_0y
            ay_num = - g - 1*sgn(vy_num)* (konst_oz*vy_num**2) 
            ax_num = - 1*sgn(vx_num)*(konst_oz*vx_num**2)
            y_lista = []
            x_lista = []
            g = 9.8
            while y_num>=0:
                vy_num = vy_num + ay_num*el
                vx_num = vx_num + ax_num*el
                ay_num = -g-1*sgn(vy_num)* konst_oz*(vy_num**2) 
                ax_num = -1*sgn(vx_num)*konst_oz*(vx_num**2)
                y_num = y_num + vy_num*el
                y_lista.append(y_num)
                x_num = x_num + vx_num*el
                x_lista.append(x_num)
            return y_lista, x_lista

        euler_dt = [0.1, 0.01, 0.001]
        for el in euler_dt:
            eulerova_metoda(el)
            plt.plot(x_lista, y_lista)

        plt.show()

                    
bon_jovi = projectile(0, 0, 17, 25, 0.02, 0.6, 4, 0.1, 20)
bon_jovi.runge_kutta_rjesenje()           

    



