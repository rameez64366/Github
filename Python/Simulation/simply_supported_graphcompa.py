import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

with open(r"C:\Users\Admin\Desktop\Shear_moment_result(line body simply supported rect-concentratedload).txt", "r") as data_file:
    ANSYS_line_body_result=pd.read_table(data_file)

Beam_length_list=[i for i in ANSYS_line_body_result["length of beam[mm]"]]
deformation_list=[i for i in ANSYS_line_body_result["deformation[mm]"]]
shear_force_list=[i for i in ANSYS_line_body_result["shear force in Y[N]"]]
bending_moment_list=[i for i in ANSYS_line_body_result["total bending moment[N.mm]"]]

fig,a=plt.subplots(3,1,sharex=True)

a[0].plot(Beam_length_list,shear_force_list,color='blue', linewidth = 2,
         marker='o', markerfacecolor='orange', markersize=3,label="shear force")
a[0].legend(loc="upper right")
a[0].set_title(r"Beam length in$[mm]$ vs shear force in Y direction $[N]$")
a[0].set_ylabel(r"Shear force in $N$")
a[0].set_yticks(np.arange(min(shear_force_list), max(shear_force_list)+500, 500))
a[0].axhline(y = 0, color = 'black', linestyle='dashed')
a[1].plot(Beam_length_list,bending_moment_list,color='red', linewidth = 2,
         marker='o', markerfacecolor='orange', markersize=3,label="bending moment")
a[1].legend(loc="upper right")
a[1].set_title(r"Beam length in$[mm]$ vs bending moment $[N.mm]$")
a[1].set_ylabel(r"Bending moment in $[N.mm]$")
a[1].axvline(x = 500, color = 'black', linestyle='dashed')
a[1].annotate(f"{max(bending_moment_list)}", xy=(500, 1100000), xytext=(500-25,1100000), fontsize="8")
a[2].plot(Beam_length_list,deformation_list,color='green', linewidth = 2,
         marker='o', markerfacecolor='orange', markersize=3,label="deformed beam axis")
a[2].plot(Beam_length_list,np.zeros(200),color='blue',linestyle='dashed',label="undeformed beam axis")
a[2].legend(loc="lower right")
a[2].set_title(r"Beam length in$[mm]$ vs deformation of beam neutral axis $[mm]$")
a[2].set_yticks(np.arange(round(min(deformation_list))-0.5,0.6,0.5))
a[2].set_xlabel(r"Length of beam in $[mm]$")
a[2].set_ylabel(r"deformation in $[mm]$")
a[2].axvline(x = 500, color = 'black', linestyle='dashed')
a[2].annotate(f"{min(deformation_list):.6f}", xy=(500, -2.3), xytext=(500-25, -2.3), fontsize="8")
a[2].set_xticks(np.arange(0, Beam_length_list[-1]+50, 50))
plt.show()

#elastic curve comparison
E=210000        #young's modulus in N/mm^2
I=213333.333    #Moment of inertia for beam of 40mmx40mm
L=1000          #length of the beam
P=5000          #Concentrated_load
a=500           #distance from left fixed support of beam
if L/a==2:      #check to determine the type of elastic curve
    Theory_curve_list=[]
    Theory_slope_list=[]
    Theory_slope_zero=[]
    for x in Beam_length_list:
        if x<=L/2:
            elastic_check_fn=0
            slope_check_fn=0
        else:
            elastic_check_fn = (x - L / 2) ** 3                                           #macaulay's bracket
            slope_check_fn=(x - L / 2) ** 2
        y=(1/(E*I))*((P/12)*x**3-(P/6)*(elastic_check_fn)-((3*P*L**2*x)/48))              #elastic curve function macaulay's method
        slope=(1/(E*I))*((P/4)*x**2-(P/2)*slope_check_fn-(P*L**2)/16)
        if slope==0:
            Theory_slope_zero.append(x)
            Theory_slope_zero.append(slope)

        Theory_curve_list.append(y)
        Theory_slope_list.append(slope)

    theory_slope_at_start=Theory_slope_list[0]
    theory_slope_at_end=Theory_slope_list[-1]

    plt.plot(Beam_length_list,Theory_curve_list,color='red', linewidth = 2,
         marker='o', markerfacecolor='orange', markersize=3,label="Theoretical beam axis deformation")
    plt.plot(Beam_length_list,np.zeros(200),color='blue',linestyle='dashed',label="undeformed beam axis")
    plt.plot(Beam_length_list,deformation_list,color='green', linewidth = 2,
      marker='o', markerfacecolor='blue', markersize=3,label="deformed beam axis from ANSYS")
    plt.legend(loc="lower right")
    plt.xticks(np.arange(0, Beam_length_list[-1]+50, 50))
    plt.xlabel(r"beam length in [mm]")
    plt.ylabel(r"deformation in[mm]")
    plt.title("comparison of theoretical and simulated elastic curves of simply supported rectangular beam")
    plt.annotate(f"dy/dx={theory_slope_at_start:.6f}", xy=(0,-0.1), xytext=(20, -0.1), fontsize="8")
    plt.annotate(f"dy/dx={Theory_slope_zero[1]:}", xy=(Theory_slope_zero[0], -2.4), xytext=(Theory_slope_zero[0]-25, -2.4), fontsize="8")
    plt.annotate(f"dy/dx={theory_slope_at_end:.6f}", xy=(1000, -0.1), xytext=(900, -0.1), fontsize="8")
plt.show()




