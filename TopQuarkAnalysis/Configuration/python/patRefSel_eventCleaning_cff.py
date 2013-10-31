import FWCore.ParameterSet.Config as cms

# from RecoMET.METFilters.metFilters_cff import *

from RecoMET.METFilters.metFilters_cff import HBHENoiseFilter
#from CommonTools.RecoAlgos.HBHENoiseFilter_cfi import *
# s. https://hypernews.cern.ch/HyperNews/CMS/get/JetMET/1196.html
HBHENoiseFilter.minIsolatedNoiseSumE        = 999999.
HBHENoiseFilter.minNumIsolatedNoiseChannels = 999999
HBHENoiseFilter.minIsolatedNoiseSumEt       = 999999.

from RecoMET.METFilters.metFilters_cff import CSCTightHaloFilter
#from RecoMET.METAnalyzers.CSCHaloFilter_cfi import *

from RecoMET.METFilters.metFilters_cff import hcalLaserEventFilter
#from RecoMET.METFilters.hcalLaserEventFilter_cfi import *
hcalLaserEventFilter.vetoByRunEventNumber = cms.untracked.bool( False )
hcalLaserEventFilter.vetoByHBHEOccupancy = cms.untracked.bool( True )

from RecoMET.METFilters.metFilters_cff import EcalDeadCellTriggerPrimitiveFilter
#from RecoMET.METFilters.EcalDeadCellTriggerPrimitiveFilter_cfi import *
EcalDeadCellTriggerPrimitiveFilter.tpDigiCollection = cms.InputTag( 'ecalTPSkimNA' )

from RecoMET.METFilters.metFilters_cff import eeBadScFilter
#from RecoMET.METFilters.eeBadScFilter_cfi import *

#from RecoMET.METFilters.metFilters_cff import ecalLaserCorrFilter # new
##from RecoMET.METFilters.ecalLaserCorrFilter_cfi import * # new

from RecoMET.METFilters.metFilters_cff import trackingFailureFilter
#from RecoMET.METFilters.trackingFailureFilter_cfi import *

#from RecoMET.METFilters.metFilters_cff import trkPOGFilters # new
##from RecoMET.METFilters.trackingPOGFilters_cff import * # new

from TopQuarkAnalysis.Configuration.patRefSel_eventCleaning_cfi import *

eventCleaningData = cms.Sequence(
  scrapingFilter
)

eventCleaningMC = cms.Sequence(
)

# eventCleaning = cms.Sequence(
#   metFilters
# )

eventCleaning = cms.Sequence(
  HBHENoiseFilter
+ CSCTightHaloFilter
+ hcalLaserEventFilter
+ EcalDeadCellTriggerPrimitiveFilter
+ eeBadScFilter
#+ ecalLaserCorrFilter # new
+ trackingFailureFilter
#+ trkPOGFilters # new
)
