#Rectangular beam geometrical parameters
rectangle_breadth=40
rectangle_height=40
extrusion_length=1000

# Set Sketch Plane
sectionPlane = Plane.PlaneXY
ViewHelper.SetSketchPlane(sectionPlane, None)
# EndBlock

# Sketch Line which represent the neutral axis
SketchLine.Create(Point2D.Create(MM(0), MM(0)), Point2D.Create(MM(extrusion_length), MM(0)))

###constraining the line
#coincident on origin
base = SelectionPoint.Create(GetRootPart().DatumPlanes[0].Curves[0].GetChildren[ICurvePoint]()[0])
target= SelectionPoint.Create(GetRootPart().DatumPlanes[0].GetChildren[IDatumPoint]()[0])
Constraint.CreateCoincident(base, target)

#coincident on x-axis
base= SelectionPoint.Create(GetRootPart().DatumPlanes[0].Curves[0].GetChildren[ICurvePoint]()[1])
target= SelectionPoint.Create(GetRootPart().DatumPlanes[0].GetChildren[IDatumLine]()[0])
Constraint.CreateCoincident(base, target)

#Horizontal relation with X-axis
Constraint.CreateHorizontal(Selection.Create(GetRootPart().DatumPlanes[0].Curves[0]))

#perpendicular relation with Y-axis
base= SelectionPoint.Create(GetRootPart().DatumPlanes[0].Curves[0])
target= SelectionPoint.Create(GetRootPart().DatumPlanes[0].GetChildren[IDatumLine]()[1])
Constraint.CreatePerpendicular(base, target)

# Solidify Sketch
ViewHelper.SetViewMode(InteractionMode.Solid, None)

# Create Named Selection Group
NamedSelection.Create(Selection.Create(GetRootPart().Curves[0]), Selection.Empty())
NamedSelection.Rename("Group1", "Line_body")
NamedSelection.Create(Selection.Create(GetRootPart().Curves[0].GetChildren[ICurvePoint]()[1]), Selection.Empty())
NamedSelection.Rename("Group1", "right_edge_point")
NamedSelection.Create(Selection.Create(GetRootPart().Curves[0].GetChildren[ICurvePoint]()[0]), Selection.Empty())
NamedSelection.Rename("Group1", "left_end_point")

# Insert Beam Profile
BeamProfile.CreateFromFile("Standard\Rect.scdoc", "Rectangle", FileType.Supported)

# Import Component Groups
ComponentHelper.ImportComponentGroups(ComponentSelection.Create(GetRootPart().Components[0]), None)

#setting up cross section driving dimensions
NamedSelection.GetGroup("Rectangle_B").SetDimensionValue(rectangle_breadth*10**(-3)) ##underlying metric unit is m so converting to mm
NamedSelection.GetGroup("Rectangle_H").SetDimensionValue(rectangle_height*10**(-3))  ##underlying metric unit is m so converting to mm

#Create Beam profile and connect to the created line
Beam.Create(Selection.Create(GetRootPart().Curves[0]))
