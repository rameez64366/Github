###enter parameters in mm
#I shape sketch parameters
Flange_breadth=300
Flange_height=50
Web_thickness=40
Web_height=400
total_height=Web_height+(2*Flange_height)
#distance from fixed end for the application of concentrated load
a=2000         
b=4000
#Beam extrusion length
Extrusion_length=6000

def sketch_I_Beam():
   #set sketch plane
    ViewHelper.SetSketchPlane( Plane.PlaneYZ, None)

    # Sketch Web Rectangle
    point1 = Point2D.Create(MM(7),MM(4))
    point2 = Point2D.Create(MM(-10),MM(4))
    point3 = Point2D.Create(MM(-10),MM(-4))
    result = SketchRectangle.Create(point1, point2, point3)

    # Symmetric Constraint of web geometry with origin coordinates
    Symmetry_options = SymmetricConstraintOptions()
    Symmetry_options.SymmetricEnds = True
    Constraint.CreateSymmetric(SelectionPoint.Create(GetRootPart().DatumPlanes[0].GetChildren[IDatumLine]()[0]),Selection.Create([GetRootPart().DatumPlanes[0].Curves[0],
        GetRootPart().DatumPlanes[0].Curves[2]]), Symmetry_options)
    Constraint.CreateSymmetric(SelectionPoint.Create(GetRootPart().DatumPlanes[0].GetChildren[IDatumLine]()[1]), Selection.Create([GetRootPart().DatumPlanes[0].Curves[1],
        GetRootPart().DatumPlanes[0].Curves[3]]), Symmetry_options)

    # Create web dimensions
    Dimension.CreateDistance(Selection.Create(GetRootPart().DatumPlanes[0].Curves[2]), Selection.Create(GetRootPart().DatumPlanes[0].Curves[0]), DimensionAlignment.Aligned, DimensionSpan.MinMin)
    Dimension.Modify(Selection.Create(GetRootPart().DatumPlanes[0].GetChildren[IDimension]()[0]), MM(Web_thickness))
    Dimension.CreateDistance(Selection.Create(GetRootPart().DatumPlanes[0].Curves[3]),  Selection.Create(GetRootPart().DatumPlanes[0].Curves[1]), DimensionAlignment.Aligned, DimensionSpan.MinMin)
    Dimension.Modify(Selection.Create(GetRootPart().DatumPlanes[0].GetChildren[IDimension]()[1]), MM(Web_height))
    
    #create top flange rectangle
    point1 = Point2D.Create(MM(222),MM(49))
    point2 = Point2D.Create(MM(205),MM(49))
    point3 = Point2D.Create(MM(205),MM(-42))
    SketchRectangle.Create(point1, point2, point3)

    # Constraints of top flange and connect to web
    Constraint.CreateSymmetric(SelectionPoint.Create(GetRootPart().DatumPlanes[0].GetChildren[IDatumLine]()[0]),Selection.Create([GetRootPart().DatumPlanes[0].Curves[4],
        GetRootPart().DatumPlanes[0].Curves[6]]), Symmetry_options)
    Constraint.CreateCoincident(SelectionPoint.Create(GetRootPart().DatumPlanes[0].Curves[5], 0.0874727757571565), SelectionPoint.Create(GetRootPart().DatumPlanes[0].Curves[3], 0.00874122145089259))

    # Create top flange height dimension
    Dimension.CreateLength(Selection.Create(GetRootPart().DatumPlanes[0].Curves[6]), DimensionAlignment.Aligned)
    Dimension.Modify(Selection.Create(GetRootPart().DatumPlanes[0].GetChildren[IDimension]()[2]), MM(Flange_height))

    # Create top flange breadth dimension
    Dimension.CreateDistance(Selection.Create(GetRootPart().DatumPlanes[0].Curves[4]), Selection.Create(GetRootPart().DatumPlanes[0].Curves[6]), DimensionAlignment.Aligned,DimensionSpan.MinMin)
    Dimension.Modify(Selection.Create(GetRootPart().DatumPlanes[0].GetChildren[IDimension]()[3]), MM(Flange_breadth))

    # Sketch Flange Rectangle bottom
    point1 = Point2D.Create(MM(-219),MM(150))
    point2 = Point2D.Create(MM(-254),MM(150))
    point3 = Point2D.Create(MM(-254),MM(-150))
    SketchRectangle.Create(point1, point2, point3)

    # Coincident Constraint of bottom flange to web
    Constraint.CreateCoincident( SelectionPoint.Create(GetRootPart().DatumPlanes[0].Curves[11], 0.0878529291320592), SelectionPoint.Create(GetRootPart().DatumPlanes[0].Curves[1], 0.0279414971553861))

    # Create bottom flange height dimension
    Dimension.CreateLength(Selection.Create(GetRootPart().DatumPlanes[0].Curves[10]),DimensionAlignment.Aligned)
    Dimension.Modify(Selection.Create(GetRootPart().DatumPlanes[0].GetChildren[IDimension]()[4]), MM(Flange_height))

    # Trim Sketch to create I shape
    TrimSketchCurve.Execute( SelectionPoint.Create(GetRootPart().DatumPlanes[0].Curves[3], 0.0241041858918482))
    TrimSketchCurve.Execute( SelectionPoint.Create(GetRootPart().DatumPlanes[0].Curves[4], 0.139012566652589))
    TrimSketchCurve.Execute(SelectionPoint.Create(GetRootPart().DatumPlanes[0].Curves[1], 0.00987297258453456))
    TrimSketchCurve.Execute( SelectionPoint.Create(GetRootPart().DatumPlanes[0].Curves[8], 0.154104185891848))

    # Create I shape dimension after trim to fully constraint
    Dimension.CreateLength(Selection.Create(GetRootPart().DatumPlanes[0].Curves[0]), DimensionAlignment.Aligned)
    Dimension.Modify(Selection.Create(GetRootPart().DatumPlanes[0].GetChildren[IDimension]()[4]),MM(Web_height))
    Dimension.CreateDistance(Selection.Create(GetRootPart().DatumPlanes[0].Curves[9]), Selection.Create(GetRootPart().DatumPlanes[0].GetChildren[IDatumLine]()[1]), DimensionAlignment.Aligned, DimensionSpan.MinMin)
    Dimension.Modify(Selection.Create(GetRootPart().DatumPlanes[0].GetChildren[IDimension]()[5]), MM(Web_height/2))
    Dimension.CreateDistance( Selection.Create(GetRootPart().DatumPlanes[0].Curves[5]), Selection.Create(GetRootPart().DatumPlanes[0].Curves[7]), DimensionAlignment.Aligned, DimensionSpan.MinMin)
    Dimension.Modify(Selection.Create(GetRootPart().DatumPlanes[0].GetChildren[IDimension]()[6]),  MM(Flange_breadth))
    # Symmetric Constraint
    Constraint.CreateSymmetric(SelectionPoint.Create(GetRootPart().DatumPlanes[0].GetChildren[IDatumLine]()[0]), Selection.Create([GetRootPart().DatumPlanes[0].Curves[5],
        GetRootPart().DatumPlanes[0].Curves[7]]), Symmetry_options)

    # Solidify Sketch
    ViewHelper.SetViewMode(InteractionMode.Solid, None)

def Extrusion():
    options = ExtrudeFaceOptions()
    options.ExtrudeType = ExtrudeType.ForceAdd
    ExtrudeFaces.Execute( FaceSelection.Create(GetRootPart().Bodies[0].Faces[0]), MM(Extrusion_length), options)
    RenameObject.Execute(BodySelection.Create(GetRootPart().Bodies[0]),"I_beam")
    
# Create Coordinate system
def coordinate_systems():
    DatumOriginCreator.Create(Point.Create(MM(0), MM(total_height/2), MM(0)), Direction.DirX, Direction.DirY, None)
    RenameObject.Execute(Selection.Create(GetRootPart().CoordinateSystems[0]),"Top center coordinate ")

    DatumOriginCreator.Create( Point.Create(MM(0), MM(-total_height/2), MM(0)), Direction.DirX, Direction.DirY, None)
    RenameObject.Execute(Selection.Create(GetRootPart().CoordinateSystems[1]),"Bottom center coordinate ")

def face_split():
    # Create a plane where the concentrated load 1 is to be applied
    DatumPlaneCreator.Create( FaceSelection.Create(GetRootPart().Bodies[0].Faces[13]), False, None)
    selection = Selection.Create(GetRootPart().DatumPlanes[0])
    direction = Move.GetDirection(selection)
    options = MoveOptions()
    Move.Translate(selection, direction, MM(-a), options)
    RenameObject.Execute(Selection.Create(GetRootPart().DatumPlanes[0]),"Concentrated_load1_split_plane")

    # Create a plane where the concentrated load 2 is to be applied
    DatumPlaneCreator.Create(FaceSelection.Create(GetRootPart().Bodies[0].Faces[13]), False, None)
    selection = Selection.Create(GetRootPart().DatumPlanes[1])
    direction = Move.GetDirection(selection)
    options = MoveOptions()
    Move.Translate(selection, direction, MM(-b), options)
    RenameObject.Execute(Selection.Create(GetRootPart().DatumPlanes[1]),"Concentrated_load2_split_plane")
    
    # Changing plane visibility
    ViewHelper.SetObjectVisibility( Selection.Create(GetRootPart().DatumPlanes[0]),VisibilityType.Hide, False, False)
    ViewHelper.SetObjectVisibility(Selection.Create(GetRootPart().DatumPlanes[1]), VisibilityType.Hide, False, False)

    # Split Faces
    SplitFace.ByCutter(FaceSelection.Create(GetRootPart().Bodies[0].Faces[1]), Selection.Create(GetRootPart().DatumPlanes[0]), SplitFaceOptions())
    SplitFace.ByCutter(FaceSelection.Create(GetRootPart().Bodies[0].Faces[14]), Selection.Create(GetRootPart().DatumPlanes[1]), SplitFaceOptions())

def named_selections():
    NamedSelection.Create(BodySelection.Create(GetRootPart().Bodies[0]), Selection.Empty())
    NamedSelection.Rename("Group1", "Full_body")
    NamedSelection.Create(EdgeSelection.Create(GetRootPart().Bodies[0].Edges[22]), Selection.Empty())
    NamedSelection.Rename("Group1", "Left_beam_edge")
    NamedSelection.Create(EdgeSelection.Create(GetRootPart().Bodies[0].Edges[20]), Selection.Empty())
    NamedSelection.Rename("Group1", "Right_beam_edge")
    NamedSelection.Create(EdgeSelection.Create(GetRootPart().Bodies[0].Edges[34]), Selection.Empty())
    NamedSelection.Rename("Group1", "Concentrated_load1")
    NamedSelection.Create(EdgeSelection.Create(GetRootPart().Bodies[0].Edges[37]), Selection.Empty())
    NamedSelection.Rename("Group1", "Concentrated_load2")


sketch_I_Beam()
Extrusion()
coordinate_systems()
face_split()
named_selections()






