import FWCore.ParameterSet.Config as cms

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
, muonEtaBins     = cms.vdouble()
, electronEtaBins = cms.vdouble()
, udscJetEtaBins  = cms.vdouble()
, bJetEtaBins     = cms.vdouble()
, metEtaBins      = cms.vdouble()
#, muonEtaBins     = cms.vdouble( -2.4, -2.3, -2.2, -2.1, -2.0, -1.9, -1.8, -1.7, -1.6, -1.5, -1.4, -1.3, -1.2, -1.1, -1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4 )
#, electronEtaBins = cms.vdouble( -2.500, -2.322, -2.172, -2.043, -1.930, -1.830, -1.740, -1.653, -1.479, -1.392, -1.305, -1.218, -1.131, -1.044, -0.957, -0.870, -0.783, -0.696, -0.609, -0.522, -0.435, -0.348, -0.261, -0.174, 0.000, 0.174, 0.261, 0.348, 0.435, 0.522, 0.609, 0.696, 0.783, 0.870, 0.957, 1.044, 1.131, 1.218, 1.305, 1.392, 1.479, 1.653, 1.740, 1.830, 1.930, 2.043, 2.172, 2.322, 2.500 )
#, udscJetEtaBins  = cms.vdouble( -2.500, -2.322, -2.172, -2.043, -1.930, -1.830, -1.740, -1.653, -1.566, -1.479, -1.392, -1.305, -1.218, -1.131, -1.044, -0.957, -0.870, -0.783, -0.696, -0.609, -0.522, -0.435, -0.348, -0.261, -0.174, -0.087, 0.000, 0.087, 0.174, 0.261, 0.348, 0.435, 0.522, 0.609, 0.696, 0.783, 0.870, 0.957, 1.044, 1.131, 1.218, 1.305, 1.392, 1.479, 1.566, 1.653, 1.740, 1.830, 1.930, 2.043, 2.172, 2.322, 2.500 )
#, bJetEtaBins     = cms.vdouble( -2.500, -2.322, -2.172, -2.043, -1.930, -1.830, -1.740, -1.653, -1.566, -1.479, -1.392, -1.305, -1.218, -1.131, -1.044, -0.957, -0.870, -0.783, -0.696, -0.609, -0.522, -0.435, -0.348, -0.261, -0.174, -0.087, 0.000, 0.087, 0.174, 0.261, 0.348, 0.435, 0.522, 0.609, 0.696, 0.783, 0.870, 0.957, 1.044, 1.131, 1.218, 1.305, 1.392, 1.479, 1.566, 1.653, 1.740, 1.830, 1.930, 2.043, 2.172, 2.322, 2.500 )
#, metEtaBins      = cms.vdouble()
#, jetEtaBins      = cms.vdouble( -2.500, -2.322, -2.172, -2.043, -1.930, -1.830, -1.740, -1.653, -1.566, -1.479, -1.392, -1.305, -1.218, -1.131, -1.044, -0.957, -0.870, -0.783, -0.696, -0.609, -0.522, -0.435, -0.348, -0.261, -0.174, -0.087, 0.000, 0.087, 0.174, 0.261, 0.348, 0.435, 0.522, 0.609, 0.696, 0.783, 0.870, 0.957, 1.044, 1.131, 1.218, 1.305, 1.392, 1.479, 1.566, 1.653, 1.740, 1.830, 1.930, 2.043, 2.172, 2.322, 2.500 )
#, muonEtaBins     = cms.vdouble( -2.4, -2.1, -1.3, -0.9, 0.0, 0.9, 1.3, 2.1, 2.4 )
##, electronEtaBins = cms.vdouble( -2.500, -1.479, -0.870, 0.000, 0.870, 1.479, 2.500 )
#, electronEtaBins = cms.vdouble( -2.500, -1.5660, -1.4442, -0.870, 0.000, 0.870, 1.4442, 1.5660, 2.500 )
#, udscJetEtaBins  = cms.vdouble( -2.500, -1.479, -0.870, 0.000, 0.870, 1.479, 2.500 )
#, bJetEtaBins     = cms.vdouble( -2.500, -1.479, -0.870, 0.000, 0.870, 1.479, 2.500 )
#, metEtaBins      = cms.vdouble()
#, jetEtaBins      = cms.vdouble( -2.500, -1.479, -0.870, 0.000, 0.870, 1.479, 2.500 )

  # P_t binning (overrides input from resolution files, if not empty)
, muonPtBins     = cms.vdouble( 20., 27., 33., 40., 47., 54., 62.,  73.,  86., 109., 200., 400. )
, electronPtBins = cms.vdouble( 20., 27., 33., 40., 47., 54., 62.,  73.,  86., 109., 200., 400. )
, udscJetPtBins  = cms.vdouble( 30., 40., 50., 60., 70., 80., 90., 100., 120., 150., 200., 300., 500. )
, bJetPtBins     = cms.vdouble( 30., 40., 50., 60., 70., 80., 90., 100., 120., 150., 200., 300., 500. )
, metPtBins      = cms.vdouble( 10., 20., 29., 37., 44., 51., 59.,  69.,  80.,  96., 122., 200., 300. )
, jetPtBins      = cms.vdouble( 30., 40., 50., 60., 70., 80., 90., 100., 120., 150., 200., 300., 500. )

)
