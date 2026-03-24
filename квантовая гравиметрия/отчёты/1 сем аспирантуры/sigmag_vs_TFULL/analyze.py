import numpy as np 
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit
import math

def sins(x, A, w, ph, s):
    return A*np.sin(w*x+ph) + s

def roott(t, s):
    return s/np.sqrt(t)

def fitt(chirp_rate, intensity):
    initial_guess = [(np.max(intensity) - np.min(intensity))/2, 2*np.pi*T*T, 0, np.min(intensity)] 
    par, cov = curve_fit(sins, chirp_rate, intensity, p0=initial_guess, maxfev=5000)
    A, w, ph, s = par
    dw, dph, dA = np.sqrt(cov[1,1]), np.sqrt(cov[2,2]), np.sqrt(cov[0,0])
    dg = 1/k/T**2/(A/dA)
    return abs(dg)

def fitt1(t, dg_m):
    initial_guess = 1
    par, cov = curve_fit(roott, t, dg_m, p0=initial_guess)
    s = par
    return s

def sd_t(filepath):

    # чтение csv P(a)
    data = np.genfromtxt(filepath, delimiter=',', dtype=None, skip_header=1)
    data = np.array(data.tolist())

    chirp_rate = data[:-1,0]
    intensity = data[:-1,1]

    chirp_rate = chirp_rate[c0:]
    intensity = intensity[c0:]


    plt.figure(1)
    plt.title("inteference picture")
    plt.plot(chirp_rate, intensity)
    plt.xlabel("chirprate")
    plt.ylabel("Amplitude")

    t = np.arange(i0, len(chirp_rate))*TF
    dg_m = []

    for i in range(i0, len(chirp_rate)):
        print(i)
        dg = fitt(chirp_rate[:i], intensity[:i])
        if math.isfinite(dg):
            dg_m.append(dg)
        else:
            dg_m.append(dg_m[-1])    

    dg_m = np.array(dg_m)

    plt.figure(2)
    plt.plot(t, dg_m*r, label="data")   

    plt.xlabel("time, [s]")
    plt.ylabel("standart deviation, [mGal]") 
    plt.title(f"T = {T}, Tc = {TF}")

    s = fitt1(t, dg_m)
    plt.plot(t, roott(t, s)*r, label = "fit")
    plt.title(f"T = {T*1e3} ms, Tc = {TF*1e3} ms, sensetivity = {s*r} mGal/Hz^1/2")

    np.save(f"t_T9100MOT{Tpause}.npy", t)
    np.save(f"dg_T9100MOT{Tpause}.npy", dg_m)
    print(s)

    plt.legend()
    plt.show()




c = 3*1e8
k =  (384.2304844685*1e12 + 4.27167663181519*1e9 - 229.8518*1e6 - 1e9)/c + (384.2304844685*1e12 + 4.27167663181519*1e9 - 229.8518*1e6 - 1e9 - 6.83468261090429*1e9)/c
k = k*2*np.pi
T = 9100e-6 # s временной интервал между пи импульсами
Tf = 31448*1e-6 # время в таймре без интерференции
ty = 7e-6 # s длительность pi/2 импульса

r = 1e5
c0 = 0
i0 = 70

Tpause = 500
filepath = rf'25-12-17\T9100MOT{Tpause}.csv'
TF = Tf+2*T + Tpause*1e-3+4*ty # point time

sd_t(filepath)
