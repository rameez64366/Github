import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# import json
# def comparison_3D_model():
#     with open(r"C:\Users\Admin\Desktop\equivalent_stress.txt", "r") as data_file:
#         ANSYS_equivalent_data=pd.read_table(data_file)
#     with open(r"C:\Users\Admin\Desktop\deformation.txt", "r") as data_file:
#         ANSYS_deformation_data=pd.read_table(data_file)
#     with open(r"C:\Users\Admin\Desktop\FreeCADresult.json", "r") as data_file:
#         FreeCAD_data=json.load(data_file)
#
#     ##values exported from ANSYS#
#     ANSYS_deformation_list=[i for i in ANSYS_deformation_data["deformation[mm]"]]
#     ANSYS_deformation_length=[i for i in ANSYS_deformation_data["X_Coordinate length [mm]"]]
#     ANSYS_number_of_nodes_list=[i for i in ANSYS_equivalent_data["Node"]]
#     ANSYS_equivalent_stress_list=[i for i in ANSYS_equivalent_data["von mises stress [Mpa]"]]
#
#     ##values exported from FreeCAD
#     FreeCAD_deformation_list=FreeCAD_data['Results']['Deformation']
#     FreeCAD_node_list=FreeCAD_data['Results']['Nodes']
#     FreeCAD_equivalent_stress=FreeCAD_data['Results']['Von mises']
#
#     ##plots
#     fig,axes=plt.subplots(2,2)
#     axes[0,0].plot(ANSYS_deformation_length,ANSYS_deformation_list)
#     axes[0,0].set_title("ANSYS deformation vs length")
#     axes[0,0].set(xlabel="Length of part [mm]",ylabel="Deformation in Y axis [mm]")
#
#     axes[0,1].plot(ANSYS_number_of_nodes_list,ANSYS_equivalent_stress_list)
#     axes[0,1].set_title("ANSYS Equivalent von mises stress vs nodes")
#     axes[0,1].set(xlabel="nodes",ylabel="stress in [Mpa]")
#
#     axes[1,0].plot(FreeCAD_node_list,FreeCAD_deformation_list)
#     axes[1,0].set_title("FreeCAD deformation vs nodes")
#     axes[1,0].set(xlabel="nodes",ylabel="Deformation in Y axis [mm]")
#
#     axes[1,1].plot(FreeCAD_node_list,FreeCAD_equivalent_stress)
#     axes[1,1].set_title("FreeCAD Equivalent von mises stress vs nodes")
#     axes[1,1].set(xlabel="nodes",ylabel="stress in [Mpa]")
#     fig.tight_layout()
#     plt.show()
#
# def ANSYS_Beam188():
#     with open(r"C:\Users\Admin\Desktop\Shear_moment.txt", "r") as data_file:
#         ANSYS_data = pd.read_table(data_file)
#     print(ANSYS_data)
#     ANSYS_deformation_list = [i for i in ANSYS_data["deformation[mm]"]]
#     ANSYS_length = [i for i in ANSYS_data["length of beam[mm]"]]
#     ANSYS_shear_force_Y = [i for i in ANSYS_data["shear force in Y[N]"]]
#     ANSYS_bending_moment = [i for i in ANSYS_data["total bending moment[N.mm]"]]
#
#     ##plot generation
#     fig, axes = plt.subplots(3)
#     axes[0].plot(ANSYS_length, ANSYS_deformation_list)
#     axes[0].set_title("ANSYS length of beam vs deformation in Y axis ")
#     axes[0].set(xlabel="Length of beam [mm]", ylabel="Deformation in -Y axis [mm]")
#
#     axes[1].plot(ANSYS_length, ANSYS_shear_force_Y, 'tab:orange')
#     axes[1].set_title("ANSYS length of beam vs shear force in Y axis")
#     axes[1].set(xlabel="Length of beam [mm]", ylabel="Shear force [N]")
#
#     axes[2].plot(ANSYS_length, ANSYS_bending_moment,'tab:red')
#     axes[2].set_title("ANSYS length of beam vs bending moment [N.mm]")
#     axes[2].set(xlabel="Length of beam [mm]", ylabel="Bending moment [N.mm]")
#
#     fig.tight_layout()
#     plt.show()
#
# ANSYS_Beam188()
# #comparison_3D_model()
l=[0.0, 10.0, 10.0, 20.0, 20.0, 30.0, 30.0, 40.0, 40.0, 50.0, 50.0, 60.0, 60.0, 70.0, 70.0, 80.0, 80.0, 90.0, 90.0, 100.0, 100.0, 110.0, 110.0, 120.0, 120.0, 130.0, 130.0, 140.0, 140.0, 150.0, 150.0, 160.0, 160.0, 170.0, 170.0, 180.0, 180.0, 190.0, 190.0, 200.0, 200.0, 210.0, 210.0, 220.0, 220.0, 230.0, 230.0, 240.0, 240.0, 250.0, 250.0, 260.0, 260.0, 270.0, 270.0, 280.0, 280.0, 290.0, 290.0, 300.0, 300.0, 310.0, 310.0, 320.0, 320.0, 330.0, 330.0, 340.0, 340.0, 350.0, 350.0, 360.0, 360.0, 370.0, 370.0, 380.0, 380.0, 390.0, 390.0, 400.0, 400.0, 410.0, 410.0, 420.0, 420.0, 430.0, 430.0, 440.0, 440.0, 450.0, 450.0, 460.0, 460.0, 470.0, 470.0, 480.0, 480.0, 490.0, 490.0, 500.0, 500.0, 510.0, 510.0, 520.0, 520.0, 530.0, 530.0, 540.0, 540.0, 550.0, 550.0, 560.0, 560.0, 570.0, 570.0, 580.0, 580.0, 590.0, 590.0, 600.0, 600.0, 610.0, 610.0, 620.0, 620.0, 630.0, 630.0, 640.0, 640.0, 650.0, 650.0, 660.0, 660.0, 670.0, 670.0, 680.0, 680.0, 690.0, 690.0, 700.0, 700.0, 710.0, 710.0, 720.0, 720.0, 730.0, 730.0, 740.0, 740.0, 750.0, 750.0, 760.0, 760.0, 770.0, 770.0, 780.0, 780.0, 790.0, 790.0, 800.0, 800.0, 810.0, 810.0, 820.0, 820.0, 830.0, 830.0, 840.0, 840.0, 850.0, 850.0, 860.0, 860.0, 870.0, 870.0, 880.0, 880.0, 890.0, 890.0, 900.0, 900.0, 910.0, 910.0, 920.0, 920.0, 930.0, 930.0, 940.0, 940.0, 950.0, 950.0, 960.0, 960.0, 970.0, 970.0, 980.0, 980.0, 990.0, 990.0, 1000.0]
x=np.arange(0,l)
print(x)