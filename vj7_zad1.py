import matplotlib.pyplot as plt
import numpy as np
def sgn(number):
    if number<0:
        return(-1)
    else:
        return(1)
class projectile:
    def __init__(self, x_0, y_0, v_0x, v_0y, A, gust, masa, C_d,t):

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

        #funkcija numeričkog računanja kosog hitca sa otporom zraka
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

                    
bon_jovi = projectile(0, 0, 17, 25, 0.02, 0.6, 4, 0.1, 20)
bon_jovi.num_rjesenje()           

    



