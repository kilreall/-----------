import numpy as np 
import matplotlib.pyplot as plt 

plt.rcParams['font.size'] = 16 # Общий размер для всех элементов
plt.rcParams['figure.figsize'] = [6.5, 6.5] # Все новые графики будут 8x5 дюймов

def roott(t, s):
    return s/np.sqrt(t)

r = 1e5

t_T9100MOT50 = np.load("t_T9100MOT50.npy")
t_T9100MOT200 = np.load("t_T9100MOT200.npy")
t_T9100MOT500 = np.load("t_T9100MOT500.npy")

dg_T9100MOT50 = np.load("dg_T9100MOT50.npy")
s_T9100MOT50 = 2.8012087e-05
dg_T9100MOT200 = np.load("dg_T9100MOT200.npy")
s_T9100MOT200 = 4.65936154e-05
dg_T9100MOT500 = np.load("dg_T9100MOT500.npy")
s_T9100MOT500 = 5.73843227e-05

plt.plot(t_T9100MOT50, dg_T9100MOT50*r, color="b", label ="f = 10 Гц, s = 2,8 мГал/√Гц", ls = "dotted", lw = 2)
plt.plot(t_T9100MOT50, roott(t_T9100MOT50, s_T9100MOT50)*r, color="b")
plt.plot(t_T9100MOT200, dg_T9100MOT200*r, color="r", label ="f = 4 Гц, s = 4,7 мГал/√Гц", ls = "dotted", lw = 2)
plt.plot(t_T9100MOT200, roott(t_T9100MOT200, s_T9100MOT200)*r, color="r")
plt.plot(t_T9100MOT500, dg_T9100MOT500*r, color="g", label ="f = 2 Гц, s = 5,7 мГал/√Гц", ls = "dotted", lw = 2)
plt.plot(t_T9100MOT500, roott(t_T9100MOT500, s_T9100MOT500)*r, color="g")

plt.xlabel("время, [с]")
plt.ylabel("стабильность, [мГал]") 

plt.legend()
plt.show()