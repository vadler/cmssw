import os
import FWCore.ParameterSet.Config as cms

### Switches ###

test = True

### Configuration ###

compareTopTransferFunctions = cms.PSet(
  verbose   = cms.uint32( 3 )
)

compareTopTransferFunctions.io = cms.PSet(
  fullStats   = cms.bool( True )
, usePileUp   = cms.bool( False )
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
, useAlt     = cms.bool( True )
, useNonT    = cms.bool( True )
, refGen     = cms.bool( True )
, refSel     = cms.bool( True )
)

### Input Files ###

compareTopTransferFunctions.compare.inputFiles.Default = cms.PSet(
  fileName = cms.string( '' )
, cycle    = cms.int32( -1 )
)

### Paths ###

name = ''
if compareTopTransferFunctions.compare.useAlt.value() is True:
  name += 'Alt'
if compareTopTransferFunctions.compare.refGen.value() is True:
  name += 'Gen'
if compareTopTransferFunctions.compare.useSymm.value() is True:
  name += 'Symm'
logFile = 'compareTopTransferFunctions.log'
if compareTopTransferFunctions.io.usePileUp.value() is True:
  logFile    = logFile.replace( '.log', '_PileUp.log' )
if compareTopTransferFunctions.compare.refSel.value() is True:
  logFile = logFile.replace( '.', '_Ref.', 1 )
if compareTopTransferFunctions.compare.useNonT.value() is True:
  if compareTopTransferFunctions.compare.useAlt.value() is True:
    logFile = logFile.replace( '.', '_E_.', 1 )
  else:
    logFile = logFile.replace( '.', '_P_.', 1 )
else:
  if compareTopTransferFunctions.compare.useAlt.value() is True:
    logFile = logFile.replace( '.', '_Et_.', 1 )
  else:
    logFile = logFile.replace( '.', '_Pt_.', 1 )
logFile = logFile.replace( '_.', '_' + name + '.', 1 )
logFile = logFile.replace( '_.', '.', 1 )
cfgFile = logFile.replace( '.log', '_cfg.py' )
if test:
  logFile = logFile.replace( 'log', 'test.log' )
  cfgFile = cfgFile.replace( 'py', 'test.py' )
logFile    = '%s/output/%s'%( os.getenv( "CMSSW_BASE" ), logFile )
cfgFile    = '%s/output/%s'%( os.getenv( "CMSSW_BASE" ), cfgFile )
pathPlots = ''
if compareTopTransferFunctions.io.plot.value() is True:
  pathPlots = '%s/output/plots/compareTopTransferFunctions/compareTopTransferFunctions_from%s_%s_'%( os.getenv( "CMSSW_BASE" ), era, sample )
  if compareTopTransferFunctions.io.refSel.value() is True:
    pathPlots += 'Ref_'

compareTopTransferFunctions.io.pathPlots = pathPlots

### Messaging ###

f = open( cfgFile, 'w' )
print >> f, comnpareTopTransferFunctions.dumpPython()
f.close()
print
print 'Config file:'
print '------------'
print cfgFile
print
print 'Input file:'
print '----------'
print inputFile
print
print 'Output file:'
print '-----------'
if fitTopTransferFunctions.io.plot.value() is True:
  print
  print 'Plots destination:'
  print '------------------'
  print pathPlots + '*' + name + '*.png'
print
print 'Log file destination:'
print '---------------------'
print logFile
print '================================================================================'
print
