import os
import FWCore.ParameterSet.Config as cms

### Switches ###

test = True

# Origin of existing resolution functions
#era    = 'Summer11'
era    = 'Summer11-coarseEta'
#era    = 'Summer11-coarsePt'
# Input sample
sample = 'Summer12_MadGraph_L3_unambiguousOnly'
#sample = 'Summer12_MCatNLO_L3_unambiguousOnly'

### Contstants ###

# Fit functions #
sGauss = 'sGauss'
dGauss = 'dGauss'
lCB    = 'lCB'
uCB    = 'uCB'
dCB    = 'dCB'

# Dependency functions #
linear     = 'linear'
resolution = 'resolution'
squared    = 'squared'

# Fit options #
fitOptions = 'IBRS+'

### Configuration ###

fitTopTransferFunctions = cms.PSet(
  verbose   = cms.uint32( 3 )
, maxEvents = cms.int32( -1 )
, useSymm   = cms.bool( True )
, useAlt    = cms.bool( True )
, useNonT   = cms.bool( True )
, refGen    = cms.bool( True )
, scale     = cms.bool( True )
)

fitTopTransferFunctions.io = cms.PSet(
  fullStats    = cms.bool( True )
, sample       = cms.string( sample )
, inputFile    = cms.string( '' ) # defined below
, refSel       = cms.bool( True )
, usePileUp    = cms.bool( False )
, pileUp       = cms.string( 'PileUpWeightTrue' ) # 'PileUpWeightTrue' or 'PileUpWeightObserved'
, outputFile   = cms.string( '' ) # defined below
, overwrite    = cms.bool( False )
, writeFiles   = cms.bool( True )
, writeFilesPt = cms.bool( True )
, pathOut      = cms.string( '' ) # defined below
, plot         = cms.bool( True )
, pathPlots    = cms.string( '' ) # defined below
, formatPlots  = cms.vstring( 'png'
                            #, 'pdf'
                            #, 'ps'
                            #, 'eps'
                            #, 'jpg'
                            #, 'gif'
                            )
)

fitTopTransferFunctions.objects = cms.PSet(
  UdscJet = cms.PSet(
    deltaPtBins        = cms.uint32( 50 )
  , deltaPtMax         = cms.double( 50. )
  , widthFactor        = cms.double( 5.0 )
  , minPt              = cms.double( 0.0 )
  , maxEta             = cms.double( 999999. )
  , maxDR              = cms.double( 0.1 )
  , fitFunction        = cms.string( dGauss )
  , dependencyFunction = cms.string( squared )
  , resolutionFunction = cms.string( squared )
  , fitEtaBins         = cms.bool( False )
  , fitMaxPt           = cms.double( 999999. )
  , fitRange           = cms.double( 5.0 ) # if not 'sGauss', should be widthFactor
  , fitOptions         = cms.string( fitOptions )
  , minEntriesFactor   = cms.uint32( 5 )
  , exclude            = cms.vuint32(  ) # MadGraph
  #, exclude            = cms.vuint32(  ) # MC@NLO
  )
#, BJet = cms.PSet(
  ##BJet = cms.PSet(
    #deltaPtBins        = cms.uint32( 50 )
  #, deltaPtMax         = cms.double( 50. )
  #, widthFactor        = cms.double( 5.0 )
  #, minPt              = cms.double( 0.0 )
  #, maxEta             = cms.double( 999999. )
  #, maxDR              = cms.double( 0.1 )
  #, fitFunction        = cms.string( dGauss )
  #, dependencyFunction = cms.string( squared )
  #, resolutionFunction = cms.string( resolution )
  #, fitEtaBins         = cms.bool( True )
  #, fitMaxPt           = cms.double( 999999. )
  #, fitRange           = cms.double( 5.0 ) # if not 'sGauss', should be widthFactor
  #, fitOptions         = cms.string( fitOptions )
  #, minEntriesFactor   = cms.uint32( 5 )
  #, exclude            = cms.vuint32(  ) # MadGraph
  ##, exclude            = cms.vuint32(  ) # MC@NLO
  #)
#, Mu = cms.PSet(
    #deltaPtBins        = cms.uint32( 50 )
  #, deltaPtMax         = cms.double( 50. )
  #, widthFactor        = cms.double( 5.0 )
  #, minPt              = cms.double( 0.0 )
  #, maxEta             = cms.double( 999999. )
  #, maxDR              = cms.double( 0.1 )
  #, fitFunction        = cms.string( sGauss )
  #, dependencyFunction = cms.string( linear )
  #, resolutionFunction = cms.string( linear )
  #, fitEtaBins         = cms.bool( False )
  #, fitMaxPt           = cms.double( 999999. )
  #, fitRange           = cms.double( 1.0 ) # if not 'sGauss', should be widthFactor
  #, fitOptions         = cms.string( fitOptions )
  #, minEntriesFactor   = cms.uint32( 5 )
  #, exclude            = cms.vuint32(  ) # MadGraph
  ##, exclude            = cms.vuint32(  ) # MC@NLO
  #)
#, Elec = cms.PSet(
    #deltaPtBins        = cms.uint32( 50 )
  #, deltaPtMax         = cms.double( 50. )
  #, widthFactor        = cms.double( 5.0 )
  #, minPt              = cms.double( 0.0 )
  #, maxEta             = cms.double( 999999. )
  #, maxDR              = cms.double( 0.1 )
  #, fitFunction        = cms.string( sGauss )
  #, dependencyFunction = cms.string( linear )
  #, resolutionFunction = cms.string( linear )
  #, fitEtaBins         = cms.bool( False )
  #, fitMaxPt           = cms.double( 999999. )
  #, fitRange           = cms.double( 1.0 ) # if not 'sGauss', should be widthFactor
  #, fitOptions         = cms.string( fitOptions )
  #, minEntriesFactor   = cms.uint32( 5 )
  #, exclude            = cms.vuint32(  ) # MadGraph
  ##, exclude            = cms.vuint32(  ) # MC@NLO
  #)
)

### Paths ###

name = ''
if fitTopTransferFunctions.useAlt.value() is True:
  name += 'Alt'
if fitTopTransferFunctions.refGen.value() is True:
  name += 'Gen'
if fitTopTransferFunctions.useSymm.value() is True:
  name += 'Symm'
inputFile = 'analyzeHitFit_from%s_%s.root'%( era, sample )
outputFile = inputFile.replace( 'analyzeHitFit', 'fitTopTransferFunctions' )
logFile = outputFile.replace( 'root', 'log' )
if fitTopTransferFunctions.io.usePileUp.value() is True:
  outputFile = outputFile.replace( '.root', '_PileUp.root' )
  logFile    = logFile.replace( '.log', '_PileUp.log' )
if fitTopTransferFunctions.io.refSel.value() is True:
  logFile = logFile.replace( '.', '_Ref.', 1 )
if fitTopTransferFunctions.useNonT.value() is True:
  if fitTopTransferFunctions.useAlt.value() is True:
    logFile = logFile.replace( '.', '_E_.', 1 )
  else:
    logFile = logFile.replace( '.', '_P_.', 1 )
else:
  if fitTopTransferFunctions.useAlt.value() is True:
    logFile = logFile.replace( '.', '_Et_.', 1 )
  else:
    logFile = logFile.replace( '.', '_Pt_.', 1 )
logFile = logFile.replace( '_.', '_' + name + '.', 1 )
logFile = logFile.replace( '_.', '.', 1 )
cfgFile    = logFile.replace( '.log', '_cfg.py' )
if test:
  outputFile = outputFile.replace( 'root', 'test.root' )
  logFile = logFile.replace( 'log', 'test.log' )
  cfgFile = cfgFile.replace( 'py', 'test.py' )
inputFile  = 'file:%s/output/%s'%( os.getenv( "CMSSW_BASE" ), inputFile )
outputFile = 'file:%s/output/%s'%( os.getenv( "CMSSW_BASE" ), outputFile )
logFile    = '%s/output/%s'%( os.getenv( "CMSSW_BASE" ), logFile )
cfgFile    = '%s/output/%s'%( os.getenv( "CMSSW_BASE" ), cfgFile )
pathPlots = ''
if fitTopTransferFunctions.io.plot.value() is True:
  pathPlots = '%s/output/plots/fitTopTransferFunctions/fitTopTransferFunctions_from%s_%s_'%( os.getenv( "CMSSW_BASE" ), era, sample )
  if fitTopTransferFunctions.io.refSel.value() is True:
    pathPlots += 'Ref_'
pathOut = ''
if fitTopTransferFunctions.io.writeFiles.value() is True:
  pathOut = '%s/src/TopQuarkAnalysis/TopMassSemiLeptonic/data/transfer_from%s'%( os.getenv( "CMSSW_BASE" ), era ) # path to write the transfer functions

fitTopTransferFunctions.io.inputFile  = inputFile
fitTopTransferFunctions.io.outputFile = outputFile
fitTopTransferFunctions.io.pathPlots  = pathPlots
fitTopTransferFunctions.io.pathOut    = pathOut


### Messaging ###

f = open( cfgFile, 'w' )
print >> f, fitTopTransferFunctions.dumpPython()
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
print outputFile
if fitTopTransferFunctions.io.writeFiles.value() is True:
  pathOut = fitTopTransferFunctions.io.pathOut.value() + '/gentTransferFunction_' + sample + '_*' + name + '*.txt'
  if fitTopTransferFunctions.io.refSel.value() is True:
    pathOut = pathOut.replace( sample, sample + '_Ref', 1)
  print
  print 'Output destination:'
  print '------------------'
  print pathOut
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

