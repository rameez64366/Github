import numpy as np
import matplotlib.pyplot as plt
F=1 #unit load
A=1 #unit area

x = np.linspace(-90, 90, 100) #x axis values from -90 to 90 degrees#
y1=np.cos(np.deg2rad(x))**2 #normal stress for unit force and unit area#
y2=np.cos(np.deg2rad(x))*np.sin(np.deg2rad(x))#shear force for unit force and unit area#

plt.ylim(-0.5,1)
plt.yticks(np.arange(-0.5, 1.5, 0.5))
plt.xlim(-100,100)
plt.xticks(np.arange(-100, 101, 20))
plt.ylabel(r'Stress in $\frac{N}{mm^2}$ ')
plt.xlabel(r'Angle of section, $\theta$[degrees]')
plt.plot(x,y1, label=r'$\sigma(\theta)$')
plt.plot(x,y2, label=r'$\tau(\theta)$')
plt.annotate(r'$\frac{F}{A_0}$',xy=(0,1),xytext=(-3,0.9),weight='bold',fontsize="15")
plt.annotate(r'$-\frac{F}{2A_0}$',xy=(-45,-0.5),xytext=(-58,-0.4),weight='bold',fontsize="15")
plt.annotate(r'$\frac{F}{2A_0}$',xy=(45,0.5),xytext=(45,0.55),weight='bold',fontsize="15")
plt.legend()
plt.title('Stress on oblique section for unit load and area', weight='bold')
plt.show()