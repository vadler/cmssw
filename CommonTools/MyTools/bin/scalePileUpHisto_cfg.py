import os

import FWCore.ParameterSet.Config as cms

from CommonTools.MyTools.existingPileUp_cff import *

process = cms.PSet(
  # pile-up histogram
  pileUpHisto = cms.string( 'pileup' )
  # output file
, file = cms.string( 'file:%s/src/CommonTools/MyTools/data/pileUpFileMC_Summer12_S10.root'%( os.getenv( "CMSSW_BASE" ) ) )
#, file = cms.string( 'file:%s/src/CommonTools/MyTools/data/pileUpFileData_2012truePixel.root'%( os.getenv( "CMSSW_BASE" ) ) )
#, file = cms.string( 'file:%s/src/CommonTools/MyTools/data/pileUpFileData_2012observedPixel.root'%( os.getenv( "CMSSW_BASE" ) ) )
)