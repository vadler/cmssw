import os
import FWCore.ParameterSet.Config as cms

### Switches ###

test = True

### Configuration ###

compareTopTransferFunctions = cms.PSet(
  verbose   = cms.uint32( 99 )
)

compareTopTransferFunctions.io = cms.PSet(
  fullStats   = cms.bool( False )
, plot        = cms.bool( True )
, pathPlots   = cms.string( '' ) # defined below
, formatPlots = cms.vstring( 'png'
                           #, 'pdf'
                           #, 'ps'
                           #, 'eps'
                           #, 'jpg'
                           #, 'gif'
                           )
)

compareTopTransferFunctions.compare = cms.PSet(
  inputFiles = cms.PSet() # defined below
, useSymm    = cms.bool( True )
)

### Input Files ###

compareTopTransferFunctions.compare.inputFiles.Default = cms.PSet( # "Default" *must* exist!
  fileName = cms.string( 'file:%s/output/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MadGraph_L3_unambiguousOnly_PileUp.root'%( os.getenv( "CMSSW_BASE" ) ) )
, legendLabel = cms.string( 'MadGraph' )
, useAlt     = cms.bool( False )
, useNonT    = cms.bool( True )
, useNonP    = cms.bool( True )
, refGen     = cms.bool( True )
, refSel     = cms.bool( True )
, cycle    = cms.int32( 1 )
)

compareTopTransferFunctions.compare.inputFiles.Compare = cms.PSet(
  fileName = cms.string( 'file:%s/output/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MCatNLO_L3_unambiguousOnly_PileUp.root'%( os.getenv( "CMSSW_BASE" ) ) )
, legendLabel = cms.string( 'MCatNLO' )
, useAlt     = cms.bool( False )
, useNonT    = cms.bool( True )
, useNonP    = cms.bool( True )
, refGen     = cms.bool( True )
, refSel     = cms.bool( True )
, cycle    = cms.int32( 1 )
)

### Paths ###

logFile = 'compareTopTransferFunctions.log'
cfgFile = logFile.replace( '.log', '_cfg.py' )
if test:
  logFile = logFile.replace( 'log', 'test.log' )
  cfgFile = cfgFile.replace( 'py', 'test.py' )
logFile    = '%s/output/%s'%( os.getenv( "CMSSW_BASE" ), logFile )
cfgFile    = '%s/output/%s'%( os.getenv( "CMSSW_BASE" ), cfgFile )
pathPlots = ''
if compareTopTransferFunctions.io.plot.value() is True:
  pathPlots = '%s/output/plots/compareTopTransferFunctions/compareTopTransferFunctions_'%( os.getenv( "CMSSW_BASE" ) )

compareTopTransferFunctions.io.pathPlots = pathPlots

### Messaging ###

f = open( cfgFile, 'w' )
print >> f, compareTopTransferFunctions.dumpPython()
f.close()
print
print 'Config file:'
print '------------'
print cfgFile
print
print 'Input files:'
print '-----------'
#print inputFile
print '[NOT IMPLEMENTED]'
if compareTopTransferFunctions.io.plot.value() is True:
  print
  print 'Plots destination:'
  print '------------------'
  print pathPlots + '*.png'
print
print 'Log file destination:'
print '---------------------'
print logFile
print '================================================================================'
print
