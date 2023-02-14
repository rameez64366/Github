model=ExtAPI.DataModel.Project.Model
geom=model.Geometry
mesh=model.Mesh
cross_section=model.CrossSections
coordinate_systems=model.CoordinateSystems
named_selection=model.NamedSelections
materials=model.Materials
analysis=model.Analyses[0]
solution=analysis.Solution

##parameters
Extrusion_length=geom.LengthX
section=cross_section.Children[0]
rectangle_breadth=section.Width         #quantity format
rectangle_height=section.Height         #quantity format

###material list and assignment##
material_list=model.Materials.Children  ###list of material
geom.Children[0].Children[0].Material=model.Materials.Children[0].Name      #setting material to the first body in list of geometry

###coordinate system created in Spaceclaim
list_of_coordinates=coordinate_systems.Children

def construction_geometry():
    ###adding construction geometry and paths to plot results##
    construction_geometry=model.AddConstructionGeometry() #adding construction geometry to the project tree
    
    if len(construction_geometry.Children)==0:
        #adding neutral axis/surface path
        neutral_axis_path=construction_geometry.AddPath()
        neutral_axis_path.PathType=PathScopingType.Edge
        neutral_axis_path.Location=named_selection.Children[0]
        neutral_axis_path.Name="Neutral axis"
    
    else:
        pass


def Boundary_conditions():
    ###Adding boundary conditions
    
    if len(analysis.Children) == 2:
        #adding simply support on left end of the beam
        simply_support=analysis.AddSimplySupported()
        simply_support.Location=named_selection.Children[3]
        
        #adding fixed rotation on left end of the beam
        fixed_rotation=analysis.AddFixedRotation()
        fixed_rotation.Location=named_selection.Children[3]
        fixed_rotation.RotationY=FixedOrFree.Free
        fixed_rotation.RotationZ=FixedOrFree.Free
        
        #adding displacement support on right end of the beam
        displacement=analysis.AddDisplacement()
        displacement.Location=named_selection.Children[5]
        displacement.DefineBy=LoadDefineBy.Components
        displacement.YComponent.Output.DiscreteValues=[Quantity("0 [mm]")]
        displacement.ZComponent.Output.DiscreteValues=[Quantity("0 [mm]")]
        
        #adding distributed force
        force=analysis.AddForce()
        force.Location=named_selection.Children[2]
        force.DefineBy=LoadDefineBy.Components
        force.YComponent.Output.DiscreteValues=[Quantity(-5000,"N")]
        force.Name="concentrated_load"
    else:
        pass
    
#adding required analysis
def analysis_objects():
    if len(solution.Children)==1:
        #adding directional deformation on neutral axis
        deformation_Y=solution.AddDirectionalDeformation()
        deformation_Y.Location=named_selection.Children[0]
        deformation_Y.NormalOrientation = NormalOrientationType.YAxis
        deformation_Y.Name="Deformation of beam neutral axis"
        
        #adding beam tool
        beam_tool=solution.AddBeamTool()
        max_bending_stress=beam_tool.AddMaximumBendingStress()
        
        #adding total shear moment diagram
        total_shear_moment_diagram=solution.AddShearMomentDiagramMSUM()
        total_shear_moment_diagram.Location=model.ConstructionGeometry.Children[0]
        
    else:
        pass

def results():
    result=solution.Children
    shear_moment_diagram_result=result[2].PlotData
    
    total_displacement=[-i*10**3 for i in shear_moment_diagram_result["USUM"]]    #list converted from m to mm
    total_bending_moment=[i*10**3 for i in shear_moment_diagram_result["MSUM"]]  #list converted from m to mm
    shear_force_Y=[i for i in shear_moment_diagram_result["SFY"]]
    length=[i*10**3 for i in shear_moment_diagram_result["X Coordinate"]]        #list converted from m to mm and aligning to -Y axis
    
    # with open(r'C:\Users\Admin\Desktop\Shear_moment_result(line body simply supported rect-concentratedload).txt','w') as testfile:
    #     wrt=str("Index")+'\t'+str("length of beam[mm]")+'\t'+str("shear force in Y[N]")+"\t"+str("total bending moment[N.mm]")+"\t"+str("deformation[mm]")+"\n"
    #     count=0
    #     for i in range(len(length)):
    #         a=length[i]
    #         b=shear_force_Y[i]
    #         c=total_bending_moment[i]
    #         d=total_displacement[i]
    #         if count==0:
    #             wrt+=str(i)+'\t'+str(a)+"\t"+str(b)+'\t'+str(c)+"\t"+str(d)+"\n"
    #         else:
    #             wrt=str(i)+'\t'+str(a)+"\t"+str(b)+'\t'+str(c)+"\t"+str(d)+"\n"
    #         count+=1
    #         testfile.write(wrt)

def parameterize():
    load=analysis.Children[4]
    load.CreateParameter("YComponent")
    mesh.CreateParameter("ElementSize")
    mesh.CreateParameter("Nodes")
    mesh.CreateParameter("Elements")
    defor=solution.Children[1]
    defor.CreateParameter("Minimum")
    min_combined=solution.Children[3].Children[1]
    min_combined.CreateParameter("Minimum")
    max_combined=solution.Children[3].Children[2]
    max_combined.CreateParameter("Maximum")


mesh.ElementSize =Quantity("10 [mm]")
mesh.GenerateMesh()    

construction_geometry()
mesh_creation()
Boundary_conditions()
analysis_objects()
solution.Solve(True)   #solve the analysis
parameterize()         #comment this line after running script once
#results()              #only to export results for analysis comparison


