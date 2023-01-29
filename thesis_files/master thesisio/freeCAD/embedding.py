
def Fixed_wall_sketch():
	rectangle_dimension_tuple=tuple(converted_dimension_rectangle)
	wall_length=str(float(rectangle_dimension_tuple[0]) + 50)
	wall_breadth=str(float(rectangle_dimension_tuple[1]) + 50)
	App.activeDocument().getObject('Body').newObject('Sketcher::SketchObject','Sketch001')
	App.activeDocument().getObject('Sketch001').Support = (App.activeDocument().getObject('Pad'),['Face6',])
	App.activeDocument().getObject('Sketch001').MapMode = 'FlatFace'

	ActiveSketch = App.activeDocument().getObject('Sketch001')

	Geometric_List = []
	Geometric_List.append(Part.LineSegment(App.Vector(-25,25,0),App.Vector(-25,-25,0)))
	Geometric_List.append(Part.LineSegment(App.Vector(-25,-25,0),App.Vector(25,-25,0)))
	Geometric_List.append(Part.LineSegment(App.Vector(25,-25,0),App.Vector(25,25,0)))
	Geometric_List.append(Part.LineSegment(App.Vector(25,25,0),App.Vector(-25,25,0)))
	Geometric_List.append(Part.Point(App.Vector(0.000000,0.000000,0)))

	App.activeDocument().getObject('Sketch001').addGeometry(Geometric_List,False)
	#########creation of constraint list################
	constraint_List = []
	constraint_List.append(Sketcher.Constraint('Coincident',0,2,1,1))
	constraint_List.append(Sketcher.Constraint('Coincident',1,2,2,1))
	constraint_List.append(Sketcher.Constraint('Coincident',2,2,3,1))
	constraint_List.append(Sketcher.Constraint('Coincident',3,2,0,1))
	constraint_List.append(Sketcher.Constraint('Horizontal',1))
	constraint_List.append(Sketcher.Constraint('Horizontal',3))
	constraint_List.append(Sketcher.Constraint('Vertical',0))
	constraint_List.append(Sketcher.Constraint('Vertical',2))
	constraint_List.append(Sketcher.Constraint('Symmetric',1,2,0,1,4,1))
	constraint_List.append(Sketcher.Constraint('Coincident',4,1,-1,1))
	constraint_List.append(Sketcher.Constraint('DistanceX',1,1,1,2,60.988636))
	constraint_List.append(Sketcher.Constraint('DistanceY',0,2,0,1,70.154580))
	##############adding constraint list to the sketch#############
	App.activeDocument().getObject('Sketch001').addConstraint(constraint_List)
	################setting dimensions################
	App.activeDocument().getObject('Sketch001').setDatum(10,App.Units.Quantity(f'{wall_breadth}mm'))
	App.activeDocument().getObject('Sketch001').setDatum(11,App.Units.Quantity(f'{wall_length} mm'))
	#############renaming sketch for wall########
	ActiveSketch.Label="Sketch_of_fixed_wall"
	App.activeDocument().getObject('Sketch001').Visibility=False
	###########check for fully constrained/not######
	full_constrained=ActiveSketch.FullyConstrained
	if full_constrained==True:
		print("The sketch for fixed wall is fully constrained")
	else:
		print("The sketch for fixed wall is not fully constrained. Making a sketch fully constrained is better for unwanted descrepancies in the results.")
	############compute#########
	App.ActiveDocument.recompute()

def Fixed_wall():
	Wall_thickness=QtGui.QInputDialog.getText(None,"Enter the wall thickness for fixed wall","Input any positive number (units are in mm)  ")[0]
	converted_wall_thickness=float(Wall_thickness)
	App.activeDocument().getObject('Body').newObject('PartDesign::Pad','Pad001')
	App.activeDocument().getObject('Pad001').Profile = App.activeDocument().getObject('Sketch001')
	App.activeDocument().getObject('Pad001').Length = converted_wall_thickness
	App.activeDocument().getObject('Pad001').ReferenceAxis = (App.activeDocument().getObject('Sketch001'),['N_Axis'])
	App.activeDocument().getObject('Sketch001').Visibility = False
	
	App.activeDocument().getObject('Pad001').ViewObject.ShapeColor=getattr(App.activeDocument().getObject('Pad').getLinkedObject(True).ViewObject,'ShapeColor',App.activeDocument().getObject('Pad001').ViewObject.ShapeColor)
	App.activeDocument().getObject('Pad001').ViewObject.LineColor=getattr(App.activeDocument().getObject('Pad').getLinkedObject(True).ViewObject,'LineColor',App.activeDocument().getObject('Pad001').ViewObject.LineColor)
	App.activeDocument().getObject('Pad001').ViewObject.PointColor=getattr(App.activeDocument().getObject('Pad').getLinkedObject(True).ViewObject,'PointColor',App.activeDocument().getObject('Pad001').ViewObject.PointColor)
	App.activeDocument().getObject('Pad001').ViewObject.Transparency=getattr(App.activeDocument().getObject('Pad').getLinkedObject(True).ViewObject,'Transparency',App.activeDocument().getObject('Pad001').ViewObject.Transparency)
	App.activeDocument().getObject('Pad001').ViewObject.DisplayMode=getattr(App.activeDocument().getObject('Pad').getLinkedObject(True).ViewObject,'DisplayMode',App.activeDocument().getObject('Pad001').ViewObject.DisplayMode)

	App.activeDocument().getObject('Pad001').TaperAngle = 0.000000
	App.activeDocument().getObject('Pad001').UseCustomVector = 0
	App.activeDocument().getObject('Pad001').Direction = (0, 0, 1)
	App.activeDocument().getObject('Pad001').ReferenceAxis = (App.activeDocument().getObject('Sketch001'), ['N_Axis'])
	App.activeDocument().getObject('Pad001').AlongSketchNormal = 1
	App.activeDocument().getObject('Pad001').Type = 0
	App.activeDocument().getObject('Pad001').UpToFace = None
	App.activeDocument().getObject('Pad001').Reversed = 0
	App.activeDocument().getObject('Pad001').Midplane = 0
	App.activeDocument().getObject('Pad001').Offset = 0
	App.activeDocument().getObject('Pad').Visibility = False
	App.activeDocument().getObject('Sketch001').Visibility = False
	
	App.activeDocument().getObject('Pad001').Label = "Fixed_wall"
	App.ActiveDocument.recompute()
# new document
doc = App.newDocument("Scripted_CalculiX_Cantilever3D")

# part
import Part
box_obj = doc.addObject('Part::Box', 'Box')
box_obj.Height = box_obj.Width = 1000
box_obj.Length = 8000

# see how our part looks like
import FreeCADGui
FreeCADGui.ActiveDocument.activeView().viewAxonometric()
FreeCADGui.SendMsgToActiveView("ViewFit")


import ObjectsFem

# analysis
analysis_object = ObjectsFem.makeAnalysis(doc, "Analysis")

# solver (we gone use the well tested CcxTools solver object)
solver_object = ObjectsFem.makeSolverCalculixCcxTools(doc, "CalculiX")
solver_object.GeometricalNonlinearity = 'linear'
solver_object.ThermoMechSteadyState = True
solver_object.MatrixSolverType = 'default'
solver_object.IterationsControlParameterTimeUse = False
analysis_object.addObject(solver_object)

# material
material_object = ObjectsFem.makeMaterialSolid(doc, "SolidMaterial")
mat = material_object.Material
mat['Name'] = "Steel-Generic"
mat['YoungsModulus'] = "210000 MPa"
mat['PoissonRatio'] = "0.30"
mat['Density'] = "7900 kg/m^3"
material_object.Material = mat
analysis_object.addObject(material_object)

# fixed_constraint
fixed_constraint = ObjectsFem.makeConstraintFixed(doc, "FemConstraintFixed")
fixed_constraint.References = [(doc.Box, "Face1")]
analysis_object.addObject(fixed_constraint)

# force_constraint
force_constraint = ObjectsFem.makeConstraintForce(doc, "FemConstraintForce")
force_constraint.References = [(doc.Box, "Face2")]
force_constraint.Force = 9000000.0
force_constraint.Direction = (doc.Box, ["Edge5"])
force_constraint.Reversed = True
analysis_object.addObject(force_constraint)