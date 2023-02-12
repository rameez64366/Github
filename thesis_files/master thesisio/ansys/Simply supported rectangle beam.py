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

#########################Important to confirm few information before running the script############

'''make sure to input multilinear isotropic hardening behaviour to the material in case of non-linear analysis and specify the analysis type'''
###material list and assignment##
material_list=model.Materials.Children  ###list of material
geom.Children[0].Children[0].Material=model.Materials.Children[1].Name      #setting material to the first body in list of geometry

#selection of analysis type linear or non-linear
Analysis_type="linear"          #Type "Linear" or "Non-linear"

############run the script after completing material assignment and analysis type ###############

###CAD model parameters
Extrusion_length=geom.LengthX
height=geom.LengthY
breadth=geom.LengthZ

##in case of 1 concentrated load
a=Extrusion_length/2  ### units are in m
concentrated_load_value=5000

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
    
    #adding shear path
    shear_path=construction_geometry.AddPath()
    shear_path.StartCoordinateSystem=list_of_coordinates[1]
    shear_path.StartXCoordinate=Quantity(str(a/2))
    shear_path.EndCoordinateSystem=list_of_coordinates[3]
    shear_path.EndXCoordinate = Quantity(str(a/2))
    shear_path.Name="shear path"
    
else:
    pass

def mesh_creation():
    ##Mesh creation##
    mesh.ElementSize =Quantity("10 [mm]")
    #size=mesh.CreateParameter("ElementSize")      #paramterizing mesh size
    mesh.GenerateMesh()    
    
###Adding boundary conditions
def Boundary_conditions():
    if Analysis_type=="Non-linear":
        analysis_setting=analysis.Children[0]                        #Turning on large deflection and other options to accurately capture stress-strain relation
        analysis_setting.NumberOfSteps=2
        analysis_setting.CurrentStepNumber=1
        analysis_setting.AutomaticTimeStepping=AutomaticTimeStepping.On
        analysis_setting.InitialSubsteps=30
        analysis_setting.MinimumSubsteps=30
        analysis_setting.MaximumSubsteps=100
        analysis_setting.LargeDeflection=True
        concentrated_loadVal=4*concentrated_load_value            #setting load large enough to cause plastic deformation

    else:
        analysis_setting=analysis.Children[0]
        analysis_setting.NumberOfSteps=1
        analysis_setting.AutomaticTimeStepping=AutomaticTimeStepping.Off
        analysis_setting.LargeDeflection=False
    
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
    
        #adding concentrated load
        concentrated_load=analysis.AddForce()
        concentrated_load.Location=named_selection.Children[4]
        concentrated_load.DefineBy=LoadDefineBy.Components
        if Analysis_type=="Non-linear":
            concentrated_load.YComponent.Inputs[0].DiscreteValues=[Quantity('0 [sec]'),Quantity('1 [sec]'),Quantity('2 [sec]')]
            concentrated_load.YComponent.Output.DiscreteValues=[Quantity(0,"N"),Quantity(-concentrated_loadVal,"N"),Quantity(0,"N")]
        else:
            concentrated_load.YComponent.Output.SetDiscreteValue(0,Quantity(-concentrated_load_value,"N"))
        concentrated_load.Name="concentrated_load"
    else:
        pass

def analysis_objects():
        #adding required analysis
    if Analysis_type=="Non-linear":
        if len(solution.Children)==1:
            #adding equivalent stress
            equivalent_stress=solution.AddEquivalentStress()
            equivalent_stress.Name="Equivalent von mises stress"
            equivalent_stress.By = SetDriverStyle.ResultSet
            
            #adding a equivalent total strain
            total_strain=solution.AddEquivalentTotalStrain()
            
            #adding a equivalent plastic strain
            plastic_strain=solution.AddEquivalentPlasticStrainRST()
            
    else:
        #solution.MaximumRefinementLoops=3
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
            #convergence=equivalent_stress.AddConvergence()
            #convergence.AllowableChange = 2
            
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
            
            #adding shear stress
            shear_stress=solution.AddShearStress()
            shear_stress.ScopingMethod = GeometryDefineByType.Path
            shear_stress.Location=construction_geometry.Children[3]
            shear_stress.Name="Shear stress at half distance to concentrated load"
            
            #adding unaverage principle stress
            principle_stress_unavg=solution.AddMaximumPrincipalStress()
            principle_stress_unavg.DisplayOption = ResultAveragingType.Unaveraged
            principle_stress_unavg.Name="Maximum principal stress unaveraged"
            
        else:
            pass

def result_analysis():
    result=solution.Children
    if Analysis_type=="Non-linear":
        equivalent_stress_result=result[1].PlotData
        total_strain=result[2].PlotData
        plastic_strain=result[3].PlotData
        
        equivalent_stress_list=[i for i in equivalent_stress_result["Values"]]
        node_list=[i for i in equivalent_stress_result["Node"]]
        def stress_strain_graph_non_linear():
            node_equivalent_stress=solution.AddEquivalentStress()
            node_equivalent_stress.Location=named_selection.Children[5]
            
            equivalent_total_strain=solution.AddEquivalentTotalStrain()
            equivalent_total_strain.Location=named_selection.Children[5]
            
            chart=model.AddChart()
            chart.OutlineSelection=[node_equivalent_stress,equivalent_total_strain]
    else:
        deformation_result=result[1].PlotData    #data frame with index,X Coordi,Y Coordi,Z Coordi,Values
        compressive_stress_result=result[4].PlotData      #data frame with index,Node,Values
        tensile_stress_result=result[5].PlotData
        shear_stress_result=result[6].PlotData
        
        deformation_list=[i*10**3 for i in deformation_result["Values"]]                      #make the result into list and convert each value into mm
        compressive_stress_list=[i*10**(-6) for i in compressive_stress_result["Values"]]     #make the result into list and convert each value from Pa to Mpa
        tensile_stress_list=[i*10**(-6) for i in tensile_stress_result["Values"]]             #make the result into list and convert each value from Pa to Mpa
        shear_stress_list=[i*10**(-6) for i in shear_stress_result["Values"]]               #make the result into list and convert each value from Pa to Mpa
        
        ####export results 
        # with open('C:\Users\Admin\Desktop\simply_supported_concentrated_load.txt','w') as testfile:
        #     wrt=str("Index")+'\t'+str("deformation neutral axis")+'\t'+str("Compressive stress[MPa]")+"\t"+str("Tensile stress[MPa]")+"\t"+str("Shear stress[MPa]")+"\n"
        #     count=0
        #     for i in range(len(deformation_list)):
        #         a=deformation_list[i]
        #         b=compressive_stress_list[i]
        #         c=tensile_stress_list[i]
        #         d=shear_stress_list[i]
        #         if count==0:
        #             wrt+=str(i)+'\t'+str(a)+"\t"+str(b)+'\t'+str(c)+"\t"+str(d)+"\n"
        #         else:
        #             wrt=str(i)+'\t'+str(a)+"\t"+str(b)+'\t'+str(c)+"\t"+str(d)+"\n"
        #         count+=1
        #         testfile.write(wrt)
        
'''prior to running this function create a named selection of a node where the stress-strain diagram is needed to be made'''
def stress_strain_graph():
        ''' This is post processing section for this to work delete all the solution and then run this function separately.another requirement is to select a node to generate the stress-strain graph'''
        result=solution.Children
        analysis_setting=analysis.Children[0]
        analysis_setting.NumberOfSteps=2
        analysis_setting.CurrentStepNumber=1
        analysis_setting.AutomaticTimeStepping=AutomaticTimeStepping.On
        analysis_setting.InitialSubsteps=30
        analysis_setting.MinimumSubsteps=30
        analysis_setting.MaximumSubsteps=100
        analysis_setting.LargeDeflection=False   #since no plastic deformation is expected
        con_load=analysis.Children[3]
        con_load.YComponent.Inputs[0].DiscreteValues=[Quantity('0 [sec]'),Quantity('1 [sec]'),Quantity('2 [sec]')]
        con_load.YComponent.Output.DiscreteValues=[Quantity(0,"N"),Quantity(-concentrated_load_value,"N"),Quantity(0,"N")]
        
        node_equivalent_stress=solution.AddEquivalentStress()
        node_equivalent_stress.Location=named_selection.Children[5]
        
        equivalent_total_strain=solution.AddEquivalentTotalStrain()
        equivalent_total_strain.Location=named_selection.Children[5]
        
        chart=model.AddChart()
        chart.OutlineSelection=[node_equivalent_stress,equivalent_total_strain]

def parameterize():
    if Analysis_type=="Non-linear":
        pass
    else:
        load=analysis.Children[3]
        load.CreateParameter("YComponent")
        mesh.CreateParameter("ElementSize")
        mesh.CreateParameter("Nodes")
        mesh.CreateParameter("Elements")
        defor=solution.Children[1]
        defor.CreateParameter("Minimum")
        equiv=solution.Children[2]
        equiv.CreateParameter("Maximum")
        maxpri=solution.Children[3]
        maxpri.CreateParameter("Maximum")
        tensl_str=solution.Children[5]
        tensl_str.CreateParameter("Maximum")
        shear_str=solution.Children[6]
        shear_str.CreateParameter("Minimum")
        maxpri_unavg=solution.Children[7]
        maxpri_unavg.CreateParameter("Maximum")

Boundary_conditions()
mesh_creation()            #for stress strain diagram function comment this line after creating a named selection for a node
analysis_objects()         #comment this line when doing stress-strain post processing function
solution.Solve(True)       #solve the analysis
result_analysis()          # for post analysis of results and comment this line for stress-strain graph
parameterize()             #comment this line after parameterising once
'''after this line of code the node selection has to be made and click solve to generate the stress-strain diagram for the node'''
#stress_strain_graph()     #uncomment this to invoke the function to generate the stress-strain diagram for the selected node
