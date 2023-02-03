import pandas as pd
import matplotlib.pyplot as plt
import json
def comparison_3D_model():
    with open(r"C:\Users\Admin\Desktop\equivalent_stress.txt", "r") as data_file:
        ANSYS_equivalent_data=pd.read_table(data_file)
    with open(r"C:\Users\Admin\Desktop\deformation.txt", "r") as data_file:
        ANSYS_deformation_data=pd.read_table(data_file)
    with open(r"C:\Users\Admin\Desktop\FreeCADresult.json", "r") as data_file:
        FreeCAD_data=json.load(data_file)

    ##values exported from ANSYS#
    ANSYS_deformation_list=[i for i in ANSYS_deformation_data["deformation[mm]"]]
    ANSYS_deformation_length=[i for i in ANSYS_deformation_data["X_Coordinate length [mm]"]]
    ANSYS_number_of_nodes_list=[i for i in ANSYS_equivalent_data["Node"]]
    ANSYS_equivalent_stress_list=[i for i in ANSYS_equivalent_data["von mises stress [Mpa]"]]

    ##values exported from FreeCAD
    FreeCAD_deformation_list=FreeCAD_data['Results']['Deformation']
    FreeCAD_node_list=FreeCAD_data['Results']['Nodes']
    FreeCAD_equivalent_stress=FreeCAD_data['Results']['Von mises']

    ##plots
    fig,axes=plt.subplots(2,2)
    axes[0,0].plot(ANSYS_deformation_length,ANSYS_deformation_list)
    axes[0,0].set_title("ANSYS deformation vs length")
    axes[0,0].set(xlabel="Length of part [mm]",ylabel="Deformation in Y axis [mm]")

    axes[0,1].plot(ANSYS_number_of_nodes_list,ANSYS_equivalent_stress_list)
    axes[0,1].set_title("ANSYS Equivalent von mises stress vs nodes")
    axes[0,1].set(xlabel="nodes",ylabel="stress in [Mpa]")

    axes[1,0].plot(FreeCAD_node_list,FreeCAD_deformation_list)
    axes[1,0].set_title("FreeCAD deformation vs nodes")
    axes[1,0].set(xlabel="nodes",ylabel="Deformation in Y axis [mm]")

    axes[1,1].plot(FreeCAD_node_list,FreeCAD_equivalent_stress)
    axes[1,1].set_title("FreeCAD Equivalent von mises stress vs nodes")
    axes[1,1].set(xlabel="nodes",ylabel="stress in [Mpa]")
    fig.tight_layout()
    plt.show()

def ANSYS_Beam188():
    with open(r"C:\Users\Admin\Desktop\Shear_moment.txt", "r") as data_file:
        ANSYS_data = pd.read_table(data_file)
    print(ANSYS_data)
    ANSYS_deformation_list = [i for i in ANSYS_data["deformation[mm]"]]
    ANSYS_length = [i for i in ANSYS_data["length of beam[mm]"]]
    ANSYS_shear_force_Y = [i for i in ANSYS_data["shear force in Y[N]"]]
    ANSYS_bending_moment = [i for i in ANSYS_data["total bending moment[N.mm]"]]

    ##plot generation
    fig, axes = plt.subplots(3)
    axes[0].plot(ANSYS_length, ANSYS_deformation_list)
    axes[0].set_title("ANSYS length of beam vs deformation in Y axis ")
    axes[0].set(xlabel="Length of beam [mm]", ylabel="Deformation in -Y axis [mm]")

    axes[1].plot(ANSYS_length, ANSYS_shear_force_Y, 'tab:orange')
    axes[1].set_title("ANSYS length of beam vs shear force in Y axis")
    axes[1].set(xlabel="Length of beam [mm]", ylabel="Shear force [N]")

    axes[2].plot(ANSYS_length, ANSYS_bending_moment,'tab:red')
    axes[2].set_title("ANSYS length of beam vs bending moment [N.mm]")
    axes[2].set(xlabel="Length of beam [mm]", ylabel="Bending moment [N.mm]")

    fig.tight_layout()
    plt.show()

ANSYS_Beam188()
#comparison_3D_model()