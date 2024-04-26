import numpy as np
import matplotlib.pyplot as plt
class har_oscilator:
    def __init__(self,x_0,v_0,masa, k, t, num_t):
        self.x_0 = x_0
        self.num_t = num_t
        self.v_0 = v_0
        self.masa = masa
        self.k = k
        self.t = t
    def ana_xt(self):
        t = self.t
        v_0 = self.v_0
        x_0 = self.x_0
        masa = self.masa
        k = self.k
        w = np.sqrt(k/masa)
        pha = np.arctan((w*x_0) / v_0)
        A = x_0/np.sin(pha)
        timer = np.arange(0, t, 0.01)
        vrij = []
        x_novo = 0
        for tu in timer:
            x_novo = A * np.sin((w*tu) + pha)
            vrij.append(x_novo)
        self.timer = timer
        self.vrij = vrij
    def preciznost (self):
        self.ana_xt()
        t = self.t
        masa = self.masa
        v_0 = self.v_0
        x_0 = self.x_0
        k = self.k
        rjecnik_rjesenja = {}
        d_t_lista = [0.1, 0.01, 0.001]
        for kio in d_t_lista:
            vremenska_lista_num = np.arange(0, t, kio)
            x_num_lista = [x_0]
            x_num = x_0
            v_num = v_0
            for jiu in vremenska_lista_num[1:]:
                a_num = (-k/masa)*x_num_lista[-1]
                v_num = v_num + a_num*kio
                x_num = x_num_lista[-1] + v_num*kio
                x_num_lista.append(x_num)
            rjecnik_rjesenja[round(kio,10)] = {"vremenska_lista_num":vremenska_lista_num, "x_num_lista":x_num_lista}
        for kio, data in rjecnik_rjesenja.items():
            vremenska_lista_num = data["vremenska_lista_num"]
            x_num_lista = data["x_num_lista"]
            plt.scatter(vremenska_lista_num, x_num_lista)
        plt.plot(self.timer, self.vrij)
        plt.show()
    def grafovi_num (self):
        t = self.t
        masa = self.masa
        v_0 = self.v_0
        x_0 = self.x_0
        k = self.k
        num_t = self.num_t
        x_numg_lista = []
        v_numg_lista = []
        a_numg_lista = []
        koli = np.arange(0, t, num_t)
        for aus in koli:
            if aus != 0:
                v_num = v_num + a_num*num_t
                v_numg_lista.append(v_num)
                x_num = x_num + v_num*num_t
                x_numg_lista.append(x_num)
                a_num = (-k/masa)*x_num
                a_numg_lista.append(a_num)
            else:
                x_num = x_0
                x_numg_lista.append(x_num)
                v_num = v_0
                v_numg_lista.append(v_num)
                a_num = (-k/masa)*x_num
                a_numg_lista.append(a_num)

        plt.subplot(3,1,1)
        plt.plot(koli, x_numg_lista)
        plt.title("x/t")
        plt.xlabel('t')
        plt.ylabel('x')

        plt.subplot(3,1,2)
        plt.plot(koli, v_numg_lista)
        plt.title("v/t")
        plt.xlabel('t')
        plt.ylabel('v')

        plt.subplot(3,1,3)
        plt.plot(koli, a_numg_lista)
        plt.title("a/t")
        plt.xlabel('t')
        plt.ylabel('a')
        plt.show()
    def period_titranja (self):
        t = self.t
        masa = self.masa
        v_0 = self.v_0
        x_0 = self.x_0
        k = self.k
        num_t = self.num_t
        num_t_lista_array = np.arange(0.001, 1, 0.001)
        rjecnik_titranja = {}
        analiticki_period = (2*np.pi) * np.sqrt(masa/k)
        for eri in num_t_lista_array:
            x_num_lista = [x_0]
            x_num = x_0
            v_num = v_0
            har_osc_num = True
            t_titranja = 0
            per_supercount = 0
            while har_osc_num:
                a_num = (-k/masa)*x_num_lista[-1]
                v_num = v_num + a_num*num_t
                x_num = x_num_lista[-1] + v_num*eri
                x_num_lista.append(x_num)
                t_titranja = t_titranja + eri
                if (x_num_lista[-1] < x_0 and x_num_lista[-2] > x_0) or (x_num_lista[-1] > x_0 and x_num_lista[-2] < x_0):
                    per_supercount += 1
                if per_supercount == 2:
                    har_osc_num = False
            deviacija_od_rjesenja = t_titranja - analiticki_period
            rjecnik_titranja[round(eri,10)] = {"deviacija_od_rjesenja":deviacija_od_rjesenja}
        for eri, data in rjecnik_titranja.items():
            deviacija_od_rjesenja = data["deviacija_od_rjesenja"]
            plt.scatter(eri, deviacija_od_rjesenja)
        plt.show()
                





        
                    
    

        







            

            

                




jak = har_oscilator(1, 4, 5, 3, 8, 0.01)
#jak.ana_xt()
#jak.preciznost()
#jak.grafovi_num()
#jak.period_titranja()
