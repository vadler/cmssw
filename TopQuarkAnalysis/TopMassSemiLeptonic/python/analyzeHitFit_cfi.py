import FWCore.ParameterSet.Config as cms

from TopQuarkAnalysis.TopMassSemiLeptonic.bins_cff import *

# Steering

analyzeHitFit = cms.EDAnalyzer(
  "AnalyzeHitFit"

  ### Input ###

  # Pile-up distributions
, pileUpFileMC           = cms.FileInPath( 'CommonTools/MyTools/data/pileUpFileMC_Summer12_S10.root' )
, pileUpFileDataTrue     = cms.FileInPath( 'CommonTools/MyTools/data/pileUpFileData_2012truePixel.root' )
, pileUpFileDataObserved = cms.FileInPath( 'CommonTools/MyTools/data/pileUpFileData_2012observedPixel.root' )

  # TQAF semi-leptonic event
, ttSemiLeptonicEventMuons     = cms.InputTag( 'ttSemiLepEventHitFitMuons' )
, ttSemiLeptonicEventElectrons = cms.InputTag( 'ttSemiLepEventHitFitElectrons' )

  # TQAF MC event
, ttGenEvent = cms.InputTag( 'genEvt' )

  # PAT objects
, patMuons     = cms.InputTag( 'selectedPatMuons' )
, patElectrons = cms.InputTag( 'selectedPatElectrons' )
, patJets      = cms.InputTag( 'selectedPatJets' )
, patMETs      = cms.InputTag( 'patMETs' )              # 'patMETs' (TypeI) or 'patMETsUncorr' (none)

  # JEC level to be considered
, jecLevel = cms.string( 'L3Absolute' )

  # Add branch for all jets
, allJets = cms.bool( False )

  # HitFit resolution file paths (only used, if eta binning empty per objects category)
, muonResolutions     = cms.string( 'TopQuarkAnalysis/TopHitFit/data/resolution/tqafMuonResolution.txt' )
, electronResolutions = cms.string( 'TopQuarkAnalysis/TopHitFit/data/resolution/tqafElectronResolution.txt' )
, udscJetResolutions  = cms.string( 'TopQuarkAnalysis/TopHitFit/data/resolution/tqafUdscJetResolution.txt' )
, bJetResolutions     = cms.string( 'TopQuarkAnalysis/TopHitFit/data/resolution/tqafBJetResolution.txt' )
, metResolutions      = cms.string( 'TopQuarkAnalysis/TopHitFit/data/resolution/tqafKtResolution.txt' )
, jetResolutions      = cms.string( 'TopQuarkAnalysis/TopHitFit/data/resolution/tqafUdscJetResolution.txt' )

  ### Output ###

, pathPlots = cms.string( '' ) # empty string prevents from plotting

  # Eta binning (overrides input from resolution files, if not empty)
, muonEtaBins     = muonEtaBins
, electronEtaBins = electronEtaBins
, udscJetEtaBins  = udscJetEtaBins
, bJetEtaBins     = bJetEtaBins
, jetEtaBins      = jetEtaBins
, metEtaBins      = metEtaBins

  # P_t binning (overrides input from resolution files, if not empty)
, muonPtBins     = muonPtBins
, electronPtBins = electronPtBins
, udscJetPtBins  = udscJetPtBins
, bJetPtBins     = bJetPtBins
, jetPtBins      = jetPtBins
, metPtBins      = metPtBins

)
