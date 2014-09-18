import FWCore.ParameterSet.Config as cms

pfIdentifiedElectrons = cms.EDFilter(
  "ElectronIDPFCandidateSelector"
, recoGsfElectrons = cms.InputTag( "gsfElectrons" )
, electronIdMap    = cms.InputTag( "mvaTrigV0" )
, electronIdCut    = cms.double( 0. )
, src              = cms.InputTag( "pfElectronsFromVertex" )
)

