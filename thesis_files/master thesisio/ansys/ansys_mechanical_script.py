######Easy notation for all the objects in the project tree
model=ExtAPI.DataModel.Project.Model
geom=model.Geometry
mesh=model.Mesh
coordinate_systems=model.CoordinateSystems
connections=model.Connections
materials=model.Materials
analysis=model.Analyses[0]
solution=analysis.Solution
###end########

###CAD model parameters
Extrusion_length=model.Geometry.LengthX
height=model.Geometry.LengthY
breadth=model.Geometry.LengthZ

###material list and assignment##
material_list=model.Materials.Children  ###list of material
geom.Children[0].Children[0].Material=model.Materials.Children[1].Name      #setting material to the first body in list of geometry

###coordinate system created in Spaceclaim
list_of_coordinates=coordinate_systems.Children

###adding construction geometry and paths to plot results##
construction_geometry=model.AddConstructionGeometry() #adding construction geometry to the project tree

    #adding top.face path through plane of symmetry of geometry
Top_face_path=construction_geometry.AddPath()
Top_face_path.StartCoordinateSystem=list_of_coordinates[2]
Top_face_path.EndCoordinateSystem=list_of_coordinates[2]
Top_face_path.EndXCoordinate = Quantity(str(Extrusion_length))
Top_face_path.Name="Top face path"

    #adding neutral axis/surface path
neutral_axis_path=construction_geometry.AddPath()
neutral_axis_path.StartCoordinateSystem=list_of_coordinates[1]
neutral_axis_path.EndCoordinateSystem=list_of_coordinates[1]
neutral_axis_path.EndXCoordinate = Quantity(str(Extrusion_length))
neutral_axis_path.Name="Neutral axis"

    #adding bottom.face path through plane of symmetry of geometry
Bottom_face_path=construction_geometry.AddPath()
Bottom_face_path.StartCoordinateSystem=list_of_coordinates[3]
Bottom_face_path.EndCoordinateSystem=list_of_coordinates[3]
Bottom_face_path.EndXCoordinate = Quantity(str(Extrusion_length))
Bottom_face_path.Name="Bottom face path"

###Adding boundary conditions

