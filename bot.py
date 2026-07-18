import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

g = 9.81
rho = 1.225
Cd = 0.42
A = 0.1
m = 50.0

def ucus_dinamigi(durum, t):
    x, y, vx, vy = durum
    v = np.sqrt(vx**2 + vy**2)
    
    Fd = 0.5 * rho * v**2 * Cd * A
    
    ax = -(Fd * (vx / v)) / m
    ay = -g - (Fd * (vy / v)) / m
    
    return [vx, vy, ax, ay]

v_baslangic = 300
aci = np.radians(60)
baslangic_durumu = [0, 0, v_baslangic * np.cos(aci), v_baslangic * np.sin(aci)]

t = np.linspace(0, 60, 1000)

cozum = odeint(ucus_dinamigi, baslangic_durumu, t)
x_pos, y_pos = cozum[:, 0], cozum[:, 1]

x_ucusu = x_pos[y_pos >= 0]
y_ucusu = y_pos[y_pos >= 0]

plt.figure(figsize=(10, 6))
plt.plot(x_ucusu, y_ucusu, label='Sürüklenmeli Yörünge', color='#1f77b4', linewidth=2)
plt.title('2D Uçuş Yörüngesi Analizi')
plt.xlabel('Mesafe (m)')
plt.ylabel('İrtifa (m)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()
