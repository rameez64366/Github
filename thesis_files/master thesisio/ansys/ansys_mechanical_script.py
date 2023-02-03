######Easy notation for all the objects in the project tree
model=ExtAPI.DataModel.Project.Model
geom=model.Geometry
mesh=model.Mesh
coordinate_systems=model.CoordinateSystems
named_selection=model.NamedSelections
materials=model.Materials
analysis=model.Analyses[0]
solution=analysis.Solution
###end########

###CAD model parameters
Extrusion_length=geom.LengthX
height=geom.LengthY
breadth=geom.LengthZ

###material list and assignment##
material_list=model.Materials.Children  ###list of material
geom.Children[0].Children[0].Material=model.Materials.Children[0].Name      #setting material to the first body in list of geometry

###coordinate system created in Spaceclaim
list_of_coordinates=coordinate_systems.Children

###adding construction geometry and paths to plot results##
construction_geometry=model.AddConstructionGeometry() #adding construction geometry to the project tree

if len(construction_geometry.Children)==0:
    #adding top.face path through plane of symmetry of geometry
    Top_face_path=construction_geometry.AddPath()
    Top_face_path.StartCoordinateSystem=list_of_coordinates[3]
    Top_face_path.EndCoordinateSystem=list_of_coordinates[3]
    Top_face_path.EndXCoordinate = Quantity(str(Extrusion_length))
    Top_face_path.Name="Top face path"

    #adding neutral axis/surface path
    neutral_axis_path=construction_geometry.AddPath()
    neutral_axis_path.StartCoordinateSystem=list_of_coordinates[2]
    neutral_axis_path.EndCoordinateSystem=list_of_coordinates[2]
    neutral_axis_path.EndXCoordinate = Quantity(str(Extrusion_length))
    neutral_axis_path.Name="Neutral axis"

    #adding bottom.face path through plane of symmetry of geometry
    Bottom_face_path=construction_geometry.AddPath()
    Bottom_face_path.StartCoordinateSystem=list_of_coordinates[1]
    Bottom_face_path.EndCoordinateSystem=list_of_coordinates[1]
    Bottom_face_path.EndXCoordinate = Quantity(str(Extrusion_length))
    Bottom_face_path.Name="Bottom face path"
else:
    pass


##Mesh creation##
mesh.ElementSize =Quantity("20 [mm]")
mesh.GenerateMesh()    
###Adding boundary conditions

if len(analysis.Children) == 2:
    #adding fixed support on left end of the beam
    fixed_support=analysis.AddFixedSupport()
    fixed_support.Location=named_selection.Children[3]

    #adding sliding support on right end of the beam
    displacement=analysis.AddDisplacement()
    displacement.Location=named_selection.Children[2]
    displacement.DefineBy=LoadDefineBy.Components
    displacement.YComponent.Output.DiscreteValues=[Quantity("0 [mm]")]
    displacement.ZComponent.Output.DiscreteValues=[Quantity("0 [mm]")]
    '''x component is set to 'Free' by default'''

    #adding distributed force on top face of the beam
    force=analysis.AddForce()
    force.Location=named_selection.Children[1]
    force.DefineBy=LoadDefineBy.Components
    force.YComponent.Output.DiscreteValues=[Quantity("-5000 [N]")]
    force.Name="Distributed_load"
else:
    pass
    #adding required analysis
if len(solution.Children)==1:
    #adding directional deformation on neutral axis
    deformation_Y=solution.AddDirectionalDeformation()
    deformation_Y.ScopingMethod=GeometryDefineByType.Path
    deformation_Y.Location=construction_geometry.Children[1]
    deformation_Y.NormalOrientation = NormalOrientationType.YAxis
    deformation_Y.Name="Deformation of beam neutral axis"
    
    #adding equivalent von mises stress
    equivalent_stress=solution.AddEquivalentStress()
    equivalent_stress.Name="Equivalent von mises stress"
    
    #adding principle stress
    principle_stress=solution.AddMaximumPrincipalStress()
    
    #adding compressive normal stress
    compressive_stress=solution.AddNormalStress()
    compressive_stress.ScopingMethod=GeometryDefineByType.Path
    compressive_stress.Location=construction_geometry.Children[0]
    compressive_stress.NormalOrientation = NormalOrientationType.XAxis
    compressive_stress.Name="Compressive normal stress"
    
    #adding tensile.stress
    tensile_stress=solution.AddNormalStress()
    tensile_stress.ScopingMethod=GeometryDefineByType.Path
    tensile_stress.Location=construction_geometry.Children[2]
    tensile_stress.NormalOrientation = NormalOrientationType.XAxis
    tensile_stress.Name="Tensile normal stress"
    
    # adding force reaction
    force_reaction_fixed_support=solution.AddForceReaction()
    force_reaction_fixed_support.BoundaryConditionSelection=analysis.Children[1]
    force_reaction_fixed_support.ResultSelection =ProbeDisplayFilter.YAxis
    force_reaction_fixed_support.Name="Force reaction at fixed support"
    
    force_reaction_sliding_support=solution.AddForceReaction()
    force_reaction_sliding_support.BoundaryConditionSelection=analysis.Children[2]
    force_reaction_sliding_support.ResultSelection =ProbeDisplayFilter.YAxis
    force_reaction_sliding_support.Name="Force reaction at sliding support"
    
else:
    pass

solution.Solve(True) #solve the analysis

result=solution.Children
deformation_result=result[1].PlotData    #data frame with index,X Coordi,Y Coordi,Z Coordi,Values
von_mises_result=result[2].PlotData      #data frame with index,Node,Values


deformation_list=[i*10**3 for i in deformation_result["Values"]]               #make the result into list and convert each value into mm
deformation_length_list=[i*10**3 for i in deformation_result["X Coordinate"]]  #make the result into list and convert each value into mm
von_mises_node_list=[i for i in von_mises_result["Node"]]                      #make the result into list 
von_mises_stress_list=[i*10**(-6) for i in von_mises_result["Values"]]         #make the result into list and convert each value from Pa to Mpa

#####export results 

with open('C:\Users\Admin\Desktop\equivalent_stress.txt','w') as testfile:
    wrt=str("Index")+'\t'+str("Node")+"\t"+str("von mises stress [Mpa]")+"\n"
    count=0
    for i in range(len(von_mises_node_list)):
        a=von_mises_node_list[i]
        b=von_mises_stress_list[i]
        if count==0:
            wrt+=str(i)+'\t'+str(a)+"\t"+str(b)+"\n"
        else:
            wrt=str(i)+'\t'+str(a)+"\t"+str(b)+"\n"
        count+=1
        testfile.write(wrt)
        
with open('C:\Users\Admin\Desktop\deformation.txt','w') as testfile:
    wrt=str("Index")+'\t'+str("X_Coordinate length [mm]")+"\t"+str("deformation[mm]")+"\n"
    count=0
    for i in range(len(deformation_list)):
        a=deformation_length_list[i]
        b=deformation_list[i]
        if count==0:
            wrt+=str(i)+'\t'+str(a)+"\t"+str(b)+"\n"
        else:
            wrt=str(i)+'\t'+str(a)+"\t"+str(b)+"\n"
        count+=1
        testfile.write(wrt)
    
    

