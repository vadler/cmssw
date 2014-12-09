import os
import FWCore.ParameterSet.Config as cms

### Switches ###

test = True

### Configuration ###

compareTopTransferFunctions = cms.PSet(
  verbose   = cms.uint32( 99 )
)
if not test:
  compareTopTransferFunctions.verbose = 2

compareTopTransferFunctions.io = cms.PSet(
  stats       = cms.int32( -1 ) # < 0: no stats; 0: default stats; > 0: full stats
, plot        = cms.bool( True )
, pathPlots   = cms.string( '' ) # defined below
, formatPlots = cms.vstring( 'png'
                           , 'pdf'
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

##label = 'Generators'
##compareTopTransferFunctions.compare.inputFiles.Default = cms.PSet( # "Default" *must* exist!
  ##fileName = cms.string( 'file:%s/output/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MadGraph_L3_unambiguousOnly_PileUp.root'%( os.getenv( "CMSSW_BASE" ) ) )
##, legendLabel = cms.string( 'MadGraph' )
##, useAlt     = cms.bool( False )
##, useNonT    = cms.bool( True )
##, useNonP    = cms.bool( True )
##, refGen     = cms.bool( True )
##, refSel     = cms.bool( True )
##, cycle    = cms.int32( 1 )
##)
##compareTopTransferFunctions.compare.inputFiles.Compare1 = cms.PSet(
  ##fileName = cms.string( 'file:%s/output/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MCatNLO_L3_unambiguousOnly_PileUp.root'%( os.getenv( "CMSSW_BASE" ) ) )
##, legendLabel = cms.string( 'MC@NLO' )
##, useAlt     = cms.bool( False )
##, useNonT    = cms.bool( True )
##, useNonP    = cms.bool( True )
##, refGen     = cms.bool( True )
##, refSel     = cms.bool( True )
##, cycle    = cms.int32( 1 )
##)

#label = 'MadGraph_functions_elecs'
#compareTopTransferFunctions.compare.inputFiles.Default = cms.PSet( # "Default" *must* exist!
  #fileName = cms.string( 'file:%s/output/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MadGraph_L3_unambiguousOnly_PileUp.root'%( os.getenv( "CMSSW_BASE" ) ) )
#, legendLabel = cms.string( 'single Gaussian' )
#, useAlt     = cms.bool( True )
#, useNonT    = cms.bool( True )
#, useNonP    = cms.bool( True )
#, refGen     = cms.bool( True )
#, refSel     = cms.bool( True )
#, cycle    = cms.int32( 1 )
#)
#compareTopTransferFunctions.compare.inputFiles.Compare1 = cms.PSet(
  #fileName = cms.string( 'file:%s/output/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MadGraph_L3_unambiguousOnly_PileUp.root'%( os.getenv( "CMSSW_BASE" ) ) )
#, legendLabel = cms.string( 'double Gaussian' )
#, useAlt     = cms.bool( True )
#, useNonT    = cms.bool( True )
#, useNonP    = cms.bool( True )
#, refGen     = cms.bool( True )
#, refSel     = cms.bool( True )
#, cycle    = cms.int32( 3 )
#)

#label = 'MadGraph_functions_muons'
#compareTopTransferFunctions.compare.inputFiles.Default = cms.PSet( # "Default" *must* exist!
  #fileName = cms.string( 'file:%s/output/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MadGraph_L3_unambiguousOnly_PileUp.root'%( os.getenv( "CMSSW_BASE" ) ) )
#, legendLabel = cms.string( 'single Gaussian' )
#, useAlt     = cms.bool( False )
#, useNonT    = cms.bool( True )
#, useNonP    = cms.bool( True )
#, refGen     = cms.bool( True )
#, refSel     = cms.bool( True )
#, cycle    = cms.int32( 1 )
#)
#compareTopTransferFunctions.compare.inputFiles.Compare1 = cms.PSet(
  #fileName = cms.string( 'file:%s/output/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MadGraph_L3_unambiguousOnly_PileUp.root'%( os.getenv( "CMSSW_BASE" ) ) )
#, legendLabel = cms.string( 'double Gaussian' )
#, useAlt     = cms.bool( False )
#, useNonT    = cms.bool( True )
#, useNonP    = cms.bool( True )
#, refGen     = cms.bool( True )
#, refSel     = cms.bool( True )
#, cycle    = cms.int32( 3 )
#)

#label = 'MadGraph_functions_jets'
#compareTopTransferFunctions.compare.inputFiles.Default = cms.PSet( # "Default" *must* exist!
  #fileName = cms.string( 'file:%s/output/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MadGraph_L3_unambiguousOnly_PileUp.root'%( os.getenv( "CMSSW_BASE" ) ) )
#, legendLabel = cms.string( 'double Gaussian' )
#, useAlt     = cms.bool( False )
#, useNonT    = cms.bool( True )
#, useNonP    = cms.bool( True )
#, refGen     = cms.bool( True )
#, refSel     = cms.bool( True )
#, cycle    = cms.int32( 1 )
#)
#compareTopTransferFunctions.compare.inputFiles.Compare1 = cms.PSet(
  #fileName = cms.string( 'file:%s/output/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MadGraph_L3_unambiguousOnly_PileUp.root'%( os.getenv( "CMSSW_BASE" ) ) )
#, legendLabel = cms.string( 'single Gaussian' )
#, useAlt     = cms.bool( False )
#, useNonT    = cms.bool( True )
#, useNonP    = cms.bool( True )
#, refGen     = cms.bool( True )
#, refSel     = cms.bool( True )
#, cycle    = cms.int32( 3 )
#)

#label = 'MCatNLO_functions_elecs'
#compareTopTransferFunctions.compare.inputFiles.Default = cms.PSet( # "Default" *must* exist!
  #fileName = cms.string( 'file:%s/output/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MCatNLO_L3_unambiguousOnly_PileUp.root'%( os.getenv( "CMSSW_BASE" ) ) )
#, legendLabel = cms.string( 'single Gaussian' )
#, useAlt     = cms.bool( True )
#, useNonT    = cms.bool( True )
#, useNonP    = cms.bool( True )
#, refGen     = cms.bool( True )
#, refSel     = cms.bool( True )
#, cycle    = cms.int32( 1 )
#)
#compareTopTransferFunctions.compare.inputFiles.Compare1 = cms.PSet(
  #fileName = cms.string( 'file:%s/output/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MCatNLO_L3_unambiguousOnly_PileUp.root'%( os.getenv( "CMSSW_BASE" ) ) )
#, legendLabel = cms.string( 'double Gaussian' )
#, useAlt     = cms.bool( True )
#, useNonT    = cms.bool( True )
#, useNonP    = cms.bool( True )
#, refGen     = cms.bool( True )
#, refSel     = cms.bool( True )
#, cycle    = cms.int32( 3 )
#)

#label = 'MCatNLO_functions_muons'
#compareTopTransferFunctions.compare.inputFiles.Default = cms.PSet( # "Default" *must* exist!
  #fileName = cms.string( 'file:%s/output/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MCatNLO_L3_unambiguousOnly_PileUp.root'%( os.getenv( "CMSSW_BASE" ) ) )
#, legendLabel = cms.string( 'single Gaussian' )
#, useAlt     = cms.bool( False )
#, useNonT    = cms.bool( True )
#, useNonP    = cms.bool( True )
#, refGen     = cms.bool( True )
#, refSel     = cms.bool( True )
#, cycle    = cms.int32( 1 )
#)
#compareTopTransferFunctions.compare.inputFiles.Compare1 = cms.PSet(
  #fileName = cms.string( 'file:%s/output/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MCatNLO_L3_unambiguousOnly_PileUp.root'%( os.getenv( "CMSSW_BASE" ) ) )
#, legendLabel = cms.string( 'double Gaussian' )
#, useAlt     = cms.bool( False )
#, useNonT    = cms.bool( True )
#, useNonP    = cms.bool( True )
#, refGen     = cms.bool( True )
#, refSel     = cms.bool( True )
#, cycle    = cms.int32( 3 )
#)

#label = 'MCatNLO_functions_jets'
#compareTopTransferFunctions.compare.inputFiles.Default = cms.PSet( # "Default" *must* exist!
  #fileName = cms.string( 'file:%s/output/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MCatNLO_L3_unambiguousOnly_PileUp.root'%( os.getenv( "CMSSW_BASE" ) ) )
#, legendLabel = cms.string( 'double Gaussian' )
#, useAlt     = cms.bool( False )
#, useNonT    = cms.bool( True )
#, useNonP    = cms.bool( True )
#, refGen     = cms.bool( True )
#, refSel     = cms.bool( True )
#, cycle    = cms.int32( 1 )
#)
#compareTopTransferFunctions.compare.inputFiles.Compare1 = cms.PSet(
  #fileName = cms.string( 'file:%s/output/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MCatNLO_L3_unambiguousOnly_PileUp.root'%( os.getenv( "CMSSW_BASE" ) ) )
#, legendLabel = cms.string( 'single Gaussian' )
#, useAlt     = cms.bool( False )
#, useNonT    = cms.bool( True )
#, useNonP    = cms.bool( True )
#, refGen     = cms.bool( True )
#, refSel     = cms.bool( True )
#, cycle    = cms.int32( 3 )
#)

#label = 'MadGraph_elecKinematics'
#compareTopTransferFunctions.compare.inputFiles.Default = cms.PSet( # "Default" *must* exist!
  #fileName = cms.string( 'file:%s/output/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MadGraph_newElec_L3_unambiguousOnly_PileUp.root'%( os.getenv( "CMSSW_BASE" ) ) )
#, legendLabel = cms.string( 're-calibrated kinematics' )
#, useAlt     = cms.bool( False )
#, useNonT    = cms.bool( True )
#, useNonP    = cms.bool( True )
#, refGen     = cms.bool( True )
#, refSel     = cms.bool( True )
#, cycle    = cms.int32( 1 )
#)
#compareTopTransferFunctions.compare.inputFiles.Compare1 = cms.PSet(
  #fileName = cms.string( 'file:%s/output/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MadGraph_L3_unambiguousOnly_PileUp.root'%( os.getenv( "CMSSW_BASE" ) ) )
#, legendLabel = cms.string( 'GSF kinematics from PF' )
#, useAlt     = cms.bool( True )
#, useNonT    = cms.bool( True )
#, useNonP    = cms.bool( True )
#, refGen     = cms.bool( True )
#, refSel     = cms.bool( True )
#, cycle    = cms.int32( 1 )
#)
#compareTopTransferFunctions.compare.inputFiles.Compare2 = cms.PSet(
  #fileName = cms.string( 'file:%s/output/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MadGraph_L3_unambiguousOnly_PileUp.root'%( os.getenv( "CMSSW_BASE" ) ) )
#, legendLabel = cms.string( 'PF kinematics' )
#, useAlt     = cms.bool( False )
#, useNonT    = cms.bool( True )
#, useNonP    = cms.bool( True )
#, refGen     = cms.bool( True )
#, refSel     = cms.bool( True )
#, cycle    = cms.int32( 1 )
#)

#label = 'MCatNLO_elecKinematics'
#compareTopTransferFunctions.compare.inputFiles.Default = cms.PSet( # "Default" *must* exist!
  #fileName = cms.string( 'file:%s/output/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MCatNLO_newElec_L3_unambiguousOnly_PileUp.root'%( os.getenv( "CMSSW_BASE" ) ) )
#, legendLabel = cms.string( 're-calibrated kinematics' )
#, useAlt     = cms.bool( False )
#, useNonT    = cms.bool( True )
#, useNonP    = cms.bool( True )
#, refGen     = cms.bool( True )
#, refSel     = cms.bool( True )
#, cycle    = cms.int32( 1 )
#)
#compareTopTransferFunctions.compare.inputFiles.Compare1 = cms.PSet(
  #fileName = cms.string( 'file:%s/output/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MCatNLO_L3_unambiguousOnly_PileUp.root'%( os.getenv( "CMSSW_BASE" ) ) )
#, legendLabel = cms.string( 'GSF kinematics from PF' )
#, useAlt     = cms.bool( True )
#, useNonT    = cms.bool( True )
#, useNonP    = cms.bool( True )
#, refGen     = cms.bool( True )
#, refSel     = cms.bool( True )
#, cycle    = cms.int32( 1 )
#)
#compareTopTransferFunctions.compare.inputFiles.Compare2 = cms.PSet(
  #fileName = cms.string( 'file:%s/output/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MCatNLO_L3_unambiguousOnly_PileUp.root'%( os.getenv( "CMSSW_BASE" ) ) )
#, legendLabel = cms.string( 'PF kinematics' )
#, useAlt     = cms.bool( False )
#, useNonT    = cms.bool( True )
#, useNonP    = cms.bool( True )
#, refGen     = cms.bool( True )
#, refSel     = cms.bool( True )
#, cycle    = cms.int32( 1 )
#)

#label = 'MadGraph_jetBias'
#compareTopTransferFunctions.compare.inputFiles.Default = cms.PSet( # "Default" *must* exist!
  #fileName = cms.string( 'file:%s/output/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MadGraph_UnbiasedE_L3_unambiguousOnly_PileUp.root'%( os.getenv( "CMSSW_BASE" ) ) )
#, legendLabel = cms.string( 'unbiased jet selection (E)' )
#, useAlt     = cms.bool( False )
#, useNonT    = cms.bool( True )
#, useNonP    = cms.bool( True )
#, refGen     = cms.bool( True )
#, refSel     = cms.bool( True )
#, cycle    = cms.int32( 1 )
#)
#compareTopTransferFunctions.compare.inputFiles.Compare1 = cms.PSet(
  #fileName = cms.string( 'file:%s/output/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MadGraph_Unbiased_L3_unambiguousOnly_PileUp.root'%( os.getenv( "CMSSW_BASE" ) ) )
#, legendLabel = cms.string( 'unbiased jet selection' )
#, useAlt     = cms.bool( False )
#, useNonT    = cms.bool( True )
#, useNonP    = cms.bool( True )
#, refGen     = cms.bool( True )
#, refSel     = cms.bool( True )
#, cycle    = cms.int32( 1 )
#)
#compareTopTransferFunctions.compare.inputFiles.Compare2 = cms.PSet(
  #fileName = cms.string( 'file:%s/output/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MadGraph_L3_unambiguousOnly_PileUp.root'%( os.getenv( "CMSSW_BASE" ) ) )
#, legendLabel = cms.string( 'original jet selection' )
#, useAlt     = cms.bool( False )
#, useNonT    = cms.bool( True )
#, useNonP    = cms.bool( True )
#, refGen     = cms.bool( True )
#, refSel     = cms.bool( True )
#, cycle    = cms.int32( 1 )
#)

##label = 'MCatNLO_jetBias'
##compareTopTransferFunctions.compare.inputFiles.Default = cms.PSet( # "Default" *must* exist!
  ##fileName = cms.string( 'file:%s/output/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MCatNLO_UnbiasedE_L3_unambiguousOnly_PileUp.root'%( os.getenv( "CMSSW_BASE" ) ) )
##, legendLabel = cms.string( 'unbiased jet selection (E)' )
##, useAlt     = cms.bool( False )
##, useNonT    = cms.bool( True )
##, useNonP    = cms.bool( True )
##, refGen     = cms.bool( True )
##, refSel     = cms.bool( True )
##, cycle    = cms.int32( 1 )
##)
##compareTopTransferFunctions.compare.inputFiles.Compare1 = cms.PSet(
  ##fileName = cms.string( 'file:%s/output/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MCatNLO_Unbiased_L3_unambiguousOnly_PileUp.root'%( os.getenv( "CMSSW_BASE" ) ) )
##, legendLabel = cms.string( 'unbiased jet selection' )
##, useAlt     = cms.bool( False )
##, useNonT    = cms.bool( True )
##, useNonP    = cms.bool( True )
##, refGen     = cms.bool( True )
##, refSel     = cms.bool( True )
##, cycle    = cms.int32( 1 )
##)
##compareTopTransferFunctions.compare.inputFiles.Compare2 = cms.PSet(
  ##fileName = cms.string( 'file:%s/output/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MCatNLO_L3_unambiguousOnly_PileUp.root'%( os.getenv( "CMSSW_BASE" ) ) )
##, legendLabel = cms.string( 'original jet selection' )
##, useAlt     = cms.bool( False )
##, useNonT    = cms.bool( True )
##, useNonP    = cms.bool( True )
##, refGen     = cms.bool( True )
##, refSel     = cms.bool( True )
##, cycle    = cms.int32( 1 )
##)

#label = 'MadGraph_bTag'
#compareTopTransferFunctions.compare.inputFiles.Default = cms.PSet(
  #fileName = cms.string( 'file:%s/output/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MadGraph_L3_unambiguousOnly_PileUp.root'%( os.getenv( "CMSSW_BASE" ) ) )
#, legendLabel = cms.string( 'original jet selection' )
#, useAlt     = cms.bool( False )
#, useNonT    = cms.bool( True )
#, useNonP    = cms.bool( True )
#, refGen     = cms.bool( True )
#, refSel     = cms.bool( True )
#, cycle    = cms.int32( 1 )
#)
#compareTopTransferFunctions.compare.inputFiles.Compare1 = cms.PSet(
  #fileName = cms.string( 'file:%s/output/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MadGraph_L3_unambiguousOnly_bTag_PileUp.root'%( os.getenv( "CMSSW_BASE" ) ) )
#, legendLabel = cms.string( 'jet selection with CSVT requirement/veto' )
#, useAlt     = cms.bool( False )
#, useNonT    = cms.bool( True )
#, useNonP    = cms.bool( True )
#, refGen     = cms.bool( True )
#, refSel     = cms.bool( True )
#, cycle    = cms.int32( 1 )
#)

##label = 'MCatNLO_bTag'
##compareTopTransferFunctions.compare.inputFiles.Default = cms.PSet(
  ##fileName = cms.string( 'file:%s/output/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MCatNLO_L3_unambiguousOnly_PileUp.root'%( os.getenv( "CMSSW_BASE" ) ) )
##, legendLabel = cms.string( 'original jet selection' )
##, useAlt     = cms.bool( False )
##, useNonT    = cms.bool( True )
##, useNonP    = cms.bool( True )
##, refGen     = cms.bool( True )
##, refSel     = cms.bool( True )
##, cycle    = cms.int32( 1 )
##)
##compareTopTransferFunctions.compare.inputFiles.Compare1 = cms.PSet(
  ##fileName = cms.string( 'file:%s/output/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MCatNLO_L3_unambiguousOnly_bTag_PileUp.root'%( os.getenv( "CMSSW_BASE" ) ) )
##, legendLabel = cms.string( 'jet selection with CSVT requirement/veto' )
##, useAlt     = cms.bool( False )
##, useNonT    = cms.bool( True )
##, useNonP    = cms.bool( True )
##, refGen     = cms.bool( True )
##, refSel     = cms.bool( True )
##, cycle    = cms.int32( 1 )
##)

#label = 'MadGraph_leptonChannels'
#compareTopTransferFunctions.compare.inputFiles.Default = cms.PSet( # "Default" *must* exist!
  #fileName = cms.string( 'file:%s/output/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MadGraph_L3_unambiguousOnly_PileUp.root'%( os.getenv( "CMSSW_BASE" ) ) )
#, legendLabel = cms.string( 'both lepton channels' )
#, useAlt     = cms.bool( False )
#, useNonT    = cms.bool( True )
#, useNonP    = cms.bool( True )
#, refGen     = cms.bool( True )
#, refSel     = cms.bool( True )
#, cycle    = cms.int32( 1 )
#)
#compareTopTransferFunctions.compare.inputFiles.Compare1 = cms.PSet(
  #fileName = cms.string( 'file:%s/output/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MadGraph_L3_unambiguousOnly_elecChannel_PileUp.root'%( os.getenv( "CMSSW_BASE" ) ) )
#, legendLabel = cms.string( 'electron channel only' )
#, useAlt     = cms.bool( False )
#, useNonT    = cms.bool( True )
#, useNonP    = cms.bool( True )
#, refGen     = cms.bool( True )
#, refSel     = cms.bool( True )
#, cycle    = cms.int32( 1 )
#)
#compareTopTransferFunctions.compare.inputFiles.Compare2 = cms.PSet(
  #fileName = cms.string( 'file:%s/output/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MadGraph_L3_unambiguousOnly_muonChannel_PileUp.root'%( os.getenv( "CMSSW_BASE" ) ) )
#, legendLabel = cms.string( 'muon channel only' )
#, useAlt     = cms.bool( False )
#, useNonT    = cms.bool( True )
#, useNonP    = cms.bool( True )
#, refGen     = cms.bool( True )
#, refSel     = cms.bool( True )
#, cycle    = cms.int32( 1 )
#)

### Paths ###

logFile = 'compareTopTransferFunctions_%s.log'%( label )
cfgFile = logFile.replace( '.log', '_cfg.py' )
if test:
  logFile = logFile.replace( 'log', 'test.log' )
  cfgFile = cfgFile.replace( 'py', 'test.py' )
logFile    = '%s/output/%s'%( os.getenv( "CMSSW_BASE" ), logFile )
cfgFile    = '%s/output/%s'%( os.getenv( "CMSSW_BASE" ), cfgFile )
pathPlots = ''
if compareTopTransferFunctions.io.plot.value() is True:
  pathPlots = '%s/output/plots/compareTopTransferFunctions/compareTopTransferFunctions_%s_'%( os.getenv( "CMSSW_BASE" ), label )

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
#print '[NOT IMPLEMENTED]'
# DEBUG BEGIN
print 'Reference: ', compareTopTransferFunctions.compare.inputFiles.Default.fileName.value()
print 'Compare 1: ', compareTopTransferFunctions.compare.inputFiles.Compare1.fileName.value()
if hasattr( compareTopTransferFunctions.compare.inputFiles, 'Compare2' ):
  print 'Compare 2: ', compareTopTransferFunctions.compare.inputFiles.Compare2.fileName.value()
# DEBUG END
if compareTopTransferFunctions.io.plot.value() is True:
  print
  print 'Plots destination:'
  print '------------------'
  print pathPlots + '*.*'
print
print 'Log file destination:'
print '---------------------'
print logFile
print '================================================================================'
print
