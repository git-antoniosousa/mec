#criar o sketch e a extrusão
L = 10

W = 1

## Abaqus/CAE imports (normally common to all scripts)

from abaqus import *
from abaqusConstants import *
from part import *
from material import *
from section import *
from optimization import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *

## Specify how to record selection of geometry in the replay and recovery files

session.journalOptions.setValues(replayGeometry=COORDINATE, recoverGeometry=COORDINATE)

## Abaqus/CAE imports for startup scripts

from driverUtils import executeOnCaeStartup
executeOnCaeStartup()

## Create an empty model database

Mdb()

# ---------------------------------------------------------- #


## Create a model (or rename an existing one, namely if an

## empty model database was created using Mdb())

modelName = 'UNT'

mdb.models.changeKey(fromName='Model-1', toName=modelName)

plateModel = mdb.models[modelName]

# ---------------------------------------------------------- #


import part

## Create a sketch for the base feature

plateSketch = plateModel.ConstrainedSketch(name='sketchFrontView',sheetSize=20 * L)

## Criar laminado

plateSketch.Line(point1=(-5 * L, 1.76 * W),point2=(5 * L, 1.76 * W))

plateSketch.HorizontalConstraint(addUndoState=False, entity=plateSketch.geometry[2])

plateSketch.Line(point1=(5 * L, 1.76 * W), point2=(11 * L, -1.76 * W))

plateSketch.Line(point1=(11 * L, -1.76 * W),point2=(1 * L, -1.76 * W))

plateSketch.HorizontalConstraint(addUndoState=False, entity=plateSketch.geometry[4])

plateSketch.Line(point1=(1 * L, -1.76 * W),point2=(-5 * L, 1.76 * W))

## Create a three-dimensional, deformable part

platePart = plateModel.Part(name='platePart', dimensionality=THREE_D,type=DEFORMABLE_BODY)

## Create the part's base feature by extruding the sketch

## through a distance equal to the laminate thickness

t_ply = 0.11

t_lam = 32 * t_ply

platePart.BaseSolidExtrude(sketch=plateSketch, depth=30)

##NOTA ATÉ AQUI FUNCIONA




#dá um erro: AttributeError: 'Model' object has no attribute 'platepart'

platePart.DatumPlaneByPrincipalPlane(offset=tply, principalPlane=XZPLANE)

platePart.PartitionCellByDatumPlane(cells=plateModel.parts['platePart'].cells.getSequenceFromMask((' [#1 ]',),), datumPlane=plateModel.parts['platePart'].datums[2])

plateModel.ConstrainedSketch(name='edit', objectToCopy=plateModel.platePart.features['Solid extrude-1'].sketch)

plateModel.platePart.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=plateModel.sketches['edit'],upToFeature=plateModel.platePart.features['Solid extrude-1'])

plateModel.sketches['edit'].HorizontalDimension(textPoint=(45.694091796875, 12.5842628479004), value=100.0, vertex1=plateModel.sketches['edit'].vertices[0],vertex2=plateModel.sketches['edit'].vertices[1])

plateModel.sketches['edit'].DistanceDimension(entity1=plateModel.sketches['edit'].geometry[2], entity2 =plateModel.sketches['edit'].geometry[4], textPoint(-11.8780250549316, 1.47088623046875), value = 3.52)

del plateModel.sketches['edit']

plateModel.platePart.regenerate()

i=2
for tply in range (15)
    i=i+2
    plateModel.platePart.DatumPlaneByPrincipalPlane(offset=tply, principalPlane=XZPLANE)
    plateModel.platePart.PartitionCellByDatumPlane(cells=plateModel.platePart.cells.getSequenceFromMask((' [#1 ]',),), datumPlane=plateModel.platePart.datums[i]))
    tply=tply+0.11