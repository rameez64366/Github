#Rectangular beam geometrical parameters
rectangle_length=40
rectangle_height=40
extrusion_length=1000

def sketching_rectangular_beam():
    
    # Set Sketch Plane
    sectionPlane = Plane.PlaneYZ
    ViewHelper.SetSketchPlane(sectionPlane, None)
    
    # Sketch Rectangle
    point1 = Point2D.Create(MM(-10),MM(-10))
    point2 = Point2D.Create(MM(12),MM(-10))
    point3 = Point2D.Create(MM(12),MM(16))
    SketchRectangle.Create(point1, point2, point3)
    
    # Create Length Dimension and Edit dimension
    Dimension.CreateLength(Selection.Create(GetRootPart().DatumPlanes[0].Curves[0]), DimensionAlignment.Aligned)
    Dimension.Modify(Selection.Create(GetRootPart().DatumPlanes[0].GetChildren[IDimension]()[0]), MM(rectangle_height))
    
    # Create Length Dimension and Edit dimension
    Dimension.CreateLength( Selection.Create(GetRootPart().DatumPlanes[0].Curves[1]), DimensionAlignment.Aligned)
    Dimension.Modify(Selection.Create(GetRootPart().DatumPlanes[0].GetChildren[IDimension]()[1]), MM(rectangle_length))
    
    # Symmetric Constraint
    options = SymmetricConstraintOptions()
    options.SymmetricEnds = True
    Constraint.CreateSymmetric(SelectionPoint.Create(GetRootPart().DatumPlanes[0].GetChildren[IDatumLine]()[0]),  Selection.Create([GetRootPart().DatumPlanes[0].Curves[2],GetRootPart().DatumPlanes[0].Curves[0]]), options)
    Constraint.CreateSymmetric(SelectionPoint.Create(GetRootPart().DatumPlanes[0].GetChildren[IDatumLine]()[1]), Selection.Create([GetRootPart().DatumPlanes[0].Curves[1],GetRootPart().DatumPlanes[0].Curves[3]]), options)
    
    # Solidify Sketch
    ViewHelper.SetViewMode(InteractionMode.Solid, None)
    # EndBlock
    
def Rectangular_beam():
    # Extrude 1 Face
    options = ExtrudeFaceOptions()
    options.ExtrudeType = ExtrudeType.ForceAdd
    ExtrudeFaces.Execute( FaceSelection.Create(GetRootPart().Bodies[0].Faces[0]), MM(extrusion_length), options)
    # Rename extrusion in structure 
    RenameObject.Execute(BodySelection.Create(GetRootPart().Bodies[0]),"Rectangular Beam")
    # EndBlock
    
def Named_selections():
    #Creating named selection for body
    Selection_of_faces = FaceSelection.Create([GetRootPart().Bodies[0].Faces[3],
    GetRootPart().Bodies[0].Faces[0],
    GetRootPart().Bodies[0].Faces[1],
    GetRootPart().Bodies[0].Faces[4],
    GetRootPart().Bodies[0].Faces[2],
    GetRootPart().Bodies[0].Faces[5]])
    Full_body=NamedSelection.Create(Selection_of_faces,Selection.Empty())
    NamedSelection.Rename("Group1", "Full_Body")
    #creating named selection for top face for force/pressure application and renaming the selection
    NamedSelection.Create( FaceSelection.Create(GetRootPart().Bodies[0].Faces[1]),Selection.Empty())
    NamedSelection.Rename("Group1", "Top_face")
    #creating named selection for rolling support on the right edge of the part and renaming the selection
    NamedSelection.Create(EdgeSelection.Create(GetRootPart().Bodies[0].Edges[10]),Selection.Empty())
    NamedSelection.Rename("Group1", "Right_end_edge")
    #creating named selection for fixed support on the left edge of the part and renaming the selection and renaming selection
    NamedSelection.Create(EdgeSelection.Create(GetRootPart().Bodies[0].Edges[11]), Selection.Empty())
    NamedSelection.Rename("Group1", "Left_end_edge")
# EndBlock


def coordinate_creation():
    # Create Origin and rename coodinate
    DatumOriginCreator.Create( Point.Create(MM(0), MM(0), MM(0)), Direction.DirX,Direction.DirY, None)
    RenameObject.Execute(Selection.Create(GetRootPart().CoordinateSystems[0]),"Centroid")
    
    #create top-center coordinate and rename coodinate
    DatumOriginCreator.Create(Point.Create(MM(0), MM(rectangle_height/2), MM(0)), Direction.DirX, Direction.DirY, None)
    RenameObject.Execute(Selection.Create(GetRootPart().CoordinateSystems[1]),"Top edge-center coordinate")
    
    #create bottom-center coordinate and rename coodinate
    DatumOriginCreator.Create( Point.Create(MM(0), MM(-rectangle_height/2), MM(0)),  Direction.DirX, Direction.DirY, None)
    RenameObject.Execute(Selection.Create(GetRootPart().CoordinateSystems[2]),"Bottom edge-center coordinate")
    
sketching_rectangular_beam()
Rectangular_beam()
Named_selections()
coordinate_creation()
