model=ExtAPI.DataModel.Project.Model
geom=model.Geometry
mesh=model.Mesh
coordinate_systems=model.CoordinateSystems
named_selection=model.NamedSelections
materials=model.Materials
analysis=model.Analyses[0]
solution=analysis.Solution

###CAD model parameters
Extrusion_length=geom.LengthX
height=geom.LengthY
breadth=geom.LengthZ

###add distance for shear measurement
distance_from_left=Quantity(1000, "mm")

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
    Top_face_path.StartCoordinateSystem=list_of_coordinates[2]
    Top_face_path.EndCoordinateSystem=list_of_coordinates[2]
    Top_face_path.EndXCoordinate = Quantity(str(Extrusion_length))
    Top_face_path.Name="Top face path"

    #adding neutral axis/surface path
    neutral_axis_path=construction_geometry.AddPath()
    neutral_axis_path.StartCoordinateSystem=list_of_coordinates[0]
    neutral_axis_path.EndCoordinateSystem=list_of_coordinates[0]
    neutral_axis_path.EndXCoordinate = Quantity(str(Extrusion_length))
    neutral_axis_path.Name="Neutral axis"

    #adding bottom.face path through plane of symmetry of geometry
    Bottom_face_path=construction_geometry.AddPath()
    Bottom_face_path.StartCoordinateSystem=list_of_coordinates[1]
    Bottom_face_path.EndCoordinateSystem=list_of_coordinates[1]
    Bottom_face_path.EndXCoordinate = Quantity(str(Extrusion_length))
    Bottom_face_path.Name="Bottom face path"
    
    #adding shear measuring
    shear_path1=construction_geometry.AddPath()
    shear_path1.StartCoordinateSystem=list_of_coordinates[2]
    shear_path1.StartXCoordinate=distance_from_left
    shear_path1.EndCoordinateSystem=list_of_coordinates[1]
    shear_path1.EndXCoordinate=distance_from_left
    shear_path1.Name="Shear measurement path"
else:
    pass

##Mesh creation##
mesh.ElementSize =Quantity("30 [mm]")
mesh.GenerateMesh()    
###Adding boundary conditions


if len(analysis.Children) == 2:
    #adding fixed support on left end of the beam
    fixed_support=analysis.AddFixedSupport()
    fixed_support.Location=named_selection.Children[1]

    #adding sliding support on right end of the beam
    displacement=analysis.AddDisplacement()
    displacement.Location=named_selection.Children[2]
    displacement.DefineBy=LoadDefineBy.Components
    displacement.YComponent.Output.DiscreteValues=[Quantity("0 [mm]")]
    displacement.ZComponent.Output.DiscreteValues=[Quantity("0 [mm]")]
    '''x component is set to 'Free' by default'''

    #adding distributed force on top face of the beam
    Concentrated_load=analysis.AddForce()
    Concentrated_load.Location=named_selection.Children[3]
    Concentrated_load.DefineBy=LoadDefineBy.Components
    Concentrated_load.YComponent.Output.DiscreteValues=[Quantity("-100000 [N]")]
    Concentrated_load.Name="Concentrate_load1"
    
       #adding distributed force on top face of the beam
    Concentrated_load2=analysis.AddForce()
    Concentrated_load2.Location=named_selection.Children[4]
    Concentrated_load2.DefineBy=LoadDefineBy.Components
    Concentrated_load2.YComponent.Output.DiscreteValues=[Quantity("-100000 [N]")]
    Concentrated_load2.Name="Concentrate_load2"
    
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







