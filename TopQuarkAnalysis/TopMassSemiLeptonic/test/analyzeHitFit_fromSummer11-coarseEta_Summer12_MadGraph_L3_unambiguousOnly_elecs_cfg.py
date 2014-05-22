import FWCore.ParameterSet.Config as cms

process = cms.Process("USER")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_10_1_pXz.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_11_1_ZmD.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_12_1_XAb.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_13_2_sfo.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_14_1_spu.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_15_4_dTK.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_16_1_GkI.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_17_1_TN1.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_18_1_3M1.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_19_1_xkY.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_1_1_Zy8.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_20_1_Ror.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_21_1_1r6.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_22_1_OwY.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_23_1_XSG.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_24_1_wWd.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_25_1_3QF.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_26_1_Ciy.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_27_1_XML.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_28_1_kix.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_29_1_JZF.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_2_1_vAZ.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_30_1_kdG.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_31_1_AcA.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_32_1_Riq.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_33_2_GRg.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_34_1_oSm.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_35_1_bD0.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_36_3_EEO.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_37_2_L08.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_38_3_10Z.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_39_1_CoA.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_3_2_gbc.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_40_1_J3k.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_41_1_FMK.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_42_2_ujW.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_43_2_iba.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_44_1_sra.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_45_3_6f6.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_46_1_WNg.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_47_1_QwB.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_48_1_cu8.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_49_1_EDp.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_4_1_Z8A.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_50_4_xN3.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_51_1_DUh.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_52_2_aql.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_53_1_sxH.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_54_1_Gdm.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_55_1_iam.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_56_1_pY8.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_57_1_UIK.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_58_1_Atv.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_59_1_r8g.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_5_1_yXV.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_60_1_qKl.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_61_1_JIy.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_62_1_wda.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_63_3_wxH.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_64_1_HfU.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_65_1_onv.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_66_2_z8B.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_67_2_Ak7.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_68_1_z8t.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_69_1_ktY.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_6_1_Ebx.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_70_1_IZH.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_71_1_e4N.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_7_1_B4l.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_8_1_AI6.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFit_9_2_OLJ.root')
)


process.ttSemiLepEventHitFitElectrons = cms.EDProducer("TtSemiLepEvtBuilder",
    genMatch = cms.PSet(
        sumPt = cms.InputTag("ttSemiLepJetPartonMatchHitFitElectrons","SumPt"),
        sumDR = cms.InputTag("ttSemiLepJetPartonMatchHitFitElectrons","SumDR")
    ),
    hitFit = cms.PSet(
        chi2 = cms.InputTag("hitFitTtSemiLepEventHypothesis","Chi2"),
        sigmt = cms.InputTag("hitFitTtSemiLepEventHypothesis","SigMT"),
        prob = cms.InputTag("hitFitTtSemiLepEventHypothesis","Prob"),
        mt = cms.InputTag("hitFitTtSemiLepEventHypothesis","MT")
    ),
    verbosity = cms.int32(0),
    mvaDisc = cms.PSet(
        meth = cms.InputTag("findTtSemiLepJetCombMVA","Method"),
        disc = cms.InputTag("findTtSemiLepJetCombMVA","Discriminators")
    ),
    kinFit = cms.PSet(
        chi2 = cms.InputTag("kinFitTtSemiLepEventHypothesis","Chi2"),
        prob = cms.InputTag("kinFitTtSemiLepEventHypothesis","Prob")
    ),
    hypotheses = cms.VInputTag("ttSemiLepHypGenMatchHitFitElectrons"),
    genEvent = cms.InputTag("genEvt"),
    decayChannel1 = cms.int32(2),
    decayChannel2 = cms.int32(0)
)


process.ttSemiLepEventMCMatchElectrons = cms.EDProducer("TtSemiLepEvtBuilder",
    genMatch = cms.PSet(
        sumPt = cms.InputTag("ttSemiLepJetPartonMatchMCMatchElectrons","SumPt"),
        sumDR = cms.InputTag("ttSemiLepJetPartonMatchMCMatchElectrons","SumDR")
    ),
    hitFit = cms.PSet(
        chi2 = cms.InputTag("hitFitTtSemiLepEventHypothesis","Chi2"),
        sigmt = cms.InputTag("hitFitTtSemiLepEventHypothesis","SigMT"),
        prob = cms.InputTag("hitFitTtSemiLepEventHypothesis","Prob"),
        mt = cms.InputTag("hitFitTtSemiLepEventHypothesis","MT")
    ),
    verbosity = cms.int32(0),
    mvaDisc = cms.PSet(
        meth = cms.InputTag("findTtSemiLepJetCombMVA","Method"),
        disc = cms.InputTag("findTtSemiLepJetCombMVA","Discriminators")
    ),
    kinFit = cms.PSet(
        chi2 = cms.InputTag("kinFitTtSemiLepEventHypothesis","Chi2"),
        prob = cms.InputTag("kinFitTtSemiLepEventHypothesis","Prob")
    ),
    hypotheses = cms.VInputTag("ttSemiLepHypGenMatchMCMatchElectrons"),
    genEvent = cms.InputTag("genEvt"),
    decayChannel1 = cms.int32(2),
    decayChannel2 = cms.int32(0)
)


process.ttSemiLepEventReferenceElectrons = cms.EDProducer("TtSemiLepEvtBuilder",
    genMatch = cms.PSet(
        sumPt = cms.InputTag("ttSemiLepJetPartonMatchReferenceElectrons","SumPt"),
        sumDR = cms.InputTag("ttSemiLepJetPartonMatchReferenceElectrons","SumDR")
    ),
    hitFit = cms.PSet(
        chi2 = cms.InputTag("hitFitTtSemiLepEventHypothesis","Chi2"),
        sigmt = cms.InputTag("hitFitTtSemiLepEventHypothesis","SigMT"),
        prob = cms.InputTag("hitFitTtSemiLepEventHypothesis","Prob"),
        mt = cms.InputTag("hitFitTtSemiLepEventHypothesis","MT")
    ),
    verbosity = cms.int32(0),
    mvaDisc = cms.PSet(
        meth = cms.InputTag("findTtSemiLepJetCombMVA","Method"),
        disc = cms.InputTag("findTtSemiLepJetCombMVA","Discriminators")
    ),
    kinFit = cms.PSet(
        chi2 = cms.InputTag("kinFitTtSemiLepEventHypothesis","Chi2"),
        prob = cms.InputTag("kinFitTtSemiLepEventHypothesis","Prob")
    ),
    hypotheses = cms.VInputTag("ttSemiLepHypGenMatchReferenceElectrons"),
    genEvent = cms.InputTag("genEvt"),
    decayChannel1 = cms.int32(2),
    decayChannel2 = cms.int32(0)
)


process.ttSemiLepHypGenMatchHitFitElectrons = cms.EDProducer("TtSemiLepHypGenMatch",
    mets = cms.InputTag("patMETs"),
    jetCorrectionLevel = cms.string('L3Absolute'),
    leps = cms.InputTag("selectedPatElectronsHitFit"),
    neutrinoSolutionType = cms.int32(-1),
    nJetsConsidered = cms.InputTag("ttSemiLepJetPartonMatchHitFitElectrons","NumberOfConsideredJets"),
    jets = cms.InputTag("selectedPatJetsHitFit"),
    match = cms.InputTag("ttSemiLepJetPartonMatchHitFitElectrons")
)


process.ttSemiLepHypGenMatchMCMatchElectrons = cms.EDProducer("TtSemiLepHypGenMatch",
    mets = cms.InputTag("patMETs"),
    jetCorrectionLevel = cms.string('L3Absolute'),
    leps = cms.InputTag("selectedPatElectronsMCMatch"),
    neutrinoSolutionType = cms.int32(-1),
    nJetsConsidered = cms.InputTag("ttSemiLepJetPartonMatchMCMatchElectrons","NumberOfConsideredJets"),
    jets = cms.InputTag("selectedPatJetsMCMatch"),
    match = cms.InputTag("ttSemiLepJetPartonMatchMCMatchElectrons")
)


process.ttSemiLepHypGenMatchReferenceElectrons = cms.EDProducer("TtSemiLepHypGenMatch",
    mets = cms.InputTag("patMETs"),
    jetCorrectionLevel = cms.string('L3Absolute'),
    leps = cms.InputTag("referencePatElectrons"),
    neutrinoSolutionType = cms.int32(-1),
    nJetsConsidered = cms.InputTag("ttSemiLepJetPartonMatchReferenceElectrons","NumberOfConsideredJets"),
    jets = cms.InputTag("referencePatJets"),
    match = cms.InputTag("ttSemiLepJetPartonMatchReferenceElectrons")
)


process.ttSemiLepJetPartonMatchHitFitElectrons = cms.EDProducer("TtSemiLepJetPartonMatch",
    maxDist = cms.double(0.3),
    useMaxDist = cms.bool(False),
    maxNJets = cms.int32(6),
    algorithm = cms.string('unambiguousOnly'),
    maxNComb = cms.int32(1),
    verbosity = cms.int32(0),
    partonsToIgnore = cms.vstring(),
    useDeltaR = cms.bool(True),
    jets = cms.InputTag("selectedPatJetsHitFit")
)


process.ttSemiLepJetPartonMatchMCMatchElectrons = cms.EDProducer("TtSemiLepJetPartonMatch",
    maxDist = cms.double(0.3),
    useMaxDist = cms.bool(False),
    maxNJets = cms.int32(6),
    algorithm = cms.string('unambiguousOnly'),
    maxNComb = cms.int32(1),
    verbosity = cms.int32(0),
    partonsToIgnore = cms.vstring(),
    useDeltaR = cms.bool(True),
    jets = cms.InputTag("selectedPatJetsMCMatch")
)


process.ttSemiLepJetPartonMatchReferenceElectrons = cms.EDProducer("TtSemiLepJetPartonMatch",
    maxDist = cms.double(0.3),
    useMaxDist = cms.bool(False),
    maxNJets = cms.int32(6),
    algorithm = cms.string('unambiguousOnly'),
    maxNComb = cms.int32(1),
    verbosity = cms.int32(0),
    partonsToIgnore = cms.vstring(),
    useDeltaR = cms.bool(True),
    jets = cms.InputTag("referencePatJets")
)


process.hltHighLevel = cms.EDFilter("HLTHighLevel",
    eventSetupPathsKey = cms.string(''),
    TriggerResultsTag = cms.InputTag("TriggerResults","","SKIM"),
    HLTPaths = cms.vstring('pf2PatPathElectrons'),
    throw = cms.bool(True),
    andOr = cms.bool(True)
)


process.hltHighLevelReference = cms.EDFilter("HLTHighLevel",
    eventSetupPathsKey = cms.string(''),
    andOr = cms.bool(True),
    HLTPaths = cms.vstring('referencePathElectrons'),
    throw = cms.bool(True),
    TriggerResultsTag = cms.InputTag("TriggerResults","","SKIM")
)


process.ttSemiLepHypSelectionFilterElectrons = cms.EDFilter("TtSemiLepHypSelectionFilter",
    ttSemiLepHyp = cms.string('kGenMatch'),
    leptonSelector = cms.string('selectedPatElectronsHitFit'),
    jetSelector = cms.string('selectedPatJetsHitFit'),
    processName = cms.string('SKIM'),
    ttSemiLepHypLeptons = cms.InputTag("selectedPatElectronsMCMatch"),
    ttSemiLepEvt = cms.InputTag("ttSemiLepEventMCMatchElectrons"),
    ttSemiLepHypJets = cms.InputTag("selectedPatJetsMCMatch")
)


process.ttSemiLepHypSelectionFilterElectronsReference = cms.EDFilter("TtSemiLepHypSelectionFilter",
    jetCut = cms.string('pt > 30. && numberOfDaughters > 1 && chargedEmEnergyFraction < 0.99 && neutralHadronEnergyFraction < 0.99 && neutralEmEnergyFraction < 0.99 && (chargedHadronEnergyFraction > 0. || abs(eta) >= 2.4) && (chargedMultiplicity > 0 || abs(eta) >= 2.4) && abs(eta) < 3.0 && abs(eta) < 2.5'),
    ttSemiLepHyp = cms.string('kGenMatch'),
    leptonSelector = cms.string('referencePatElectrons'),
    jetSelector = cms.string('referencePatJets'),
    processName = cms.string('SKIM'),
    ttSemiLepHypLeptons = cms.InputTag("selectedPatElectronsMCMatch"),
    ttSemiLepEvt = cms.InputTag("ttSemiLepEventMCMatchElectrons"),
    ttSemiLepHypJets = cms.InputTag("selectedPatJetsMCMatch"),
    leptonCut = cms.string('et > 35. && abs(eta) < 2.5 && !(1.4442 < abs(superCluster.eta) && abs(superCluster.eta) < 1.5660) && abs(dB) < 0.02 && (electronID("eidHyperTight1MC") == 9. || electronID("eidHyperTight1MC") == 11. || electronID("eidHyperTight1MC") == 13. || electronID("eidHyperTight1MC") == 15.) && (chargedHadronIso+neutralHadronIso+photonIso)/pt < 0.1 && passConversionVeto && gsfTrack.trackerExpectedHitsInner.numberOfLostHits == 0')
)


process.analyzeHitFit = cms.EDAnalyzer("AnalyzeHitFit",
    patJets = cms.InputTag("selectedPatJetsHitFit"),
    pileUpFileMCObserved = cms.FileInPath('CommonTools/MyTools/data/pileUpFileMC_Fall11inTime.root'),
    patElectrons = cms.InputTag("selectedPatElectronsHitFit"),
    patMETs = cms.InputTag("patMETs"),
    pathPlots = cms.string('/afs/cern.ch/user/v/vadler/work/cms/Top/CMSSW_5_3_13/output/plots/analyzeHitFit/analyzeHitFit_fromSummer11-coarseEta_Summer12_MadGraph_L3_unambiguousOnly_elecs_'),
    metPtBins = cms.vdouble(10.0, 20.0, 29.0, 37.0, 44.0,
        51.0, 59.0, 69.0, 80.0, 96.0,
        122.0, 200.0, 300.0),
    ttSemiLeptonicEventElectrons = cms.InputTag("ttSemiLepEventHitFitElectrons"),
    electronEtaBins = cms.vdouble( -2.500, -1.5660, -1.4442, -0.870, 0.000, 0.870, 1.4442, 1.5660, 2.500 ),
    bJetEtaBins = cms.vdouble( -2.500, -1.479, -0.870, 0.000, 0.870, 1.479, 2.500 ),
    jecLevel = cms.string('L3Absolute'),
    allJets = cms.bool(False),
    pileUpFileDataObserved = cms.FileInPath('CommonTools/MyTools/data/pileUpFileData_2011observedPixel.root'),
    bJetResolutions = cms.string('TopQuarkAnalysis/TopHitFit/data/resolution/tqafBJetResolution_Summer11.txt'),
    udscJetPtBins = cms.vdouble(0.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0,
        80.0, 90.0, 100.0, 120.0, 150.0,
        200.0, 300.0, 500.0),
    udscJetEtaBins = cms.vdouble( -2.500, -1.479, -0.870, 0.000, 0.870, 1.479, 2.500 ),
    muonPtBins = cms.vdouble(0.0, 20.0, 27.0, 33.0, 40.0, 47.0,
        54.0, 62.0, 73.0, 86.0, 109.0,
        200.0, 400.0),
    pileUpFileMCTrue = cms.FileInPath('CommonTools/MyTools/data/pileUpFileMC_Fall11.root'),
    electronPtBins = cms.vdouble(0.0, 20.0, 27.0, 33.0, 40.0, 47.0,
        54.0, 62.0, 73.0, 86.0, 109.0,
        200.0, 400.0),
    electronResolutions = cms.string('TopQuarkAnalysis/TopHitFit/data/resolution/tqafElectronResolution_Summer11.txt'),
    ttGenEvent = cms.InputTag("genEvt"),
    metResolutions = cms.string('TopQuarkAnalysis/TopHitFit/data/resolution/tqafKtResolution_Summer11.txt'),
    muonResolutions = cms.string('TopQuarkAnalysis/TopHitFit/data/resolution/tqafMuonResolution_Summer11.txt'),
    pileUpFileDataTrue = cms.FileInPath('CommonTools/MyTools/data/pileUpFileData_2011truePixel.root'),
    patMuons = cms.InputTag("selectedPatMuonsHitFit"),
    muonEtaBins = cms.vdouble( -2.4, -2.1, -1.3, -0.9, 0.0, 0.9, 1.3, 2.1, 2.4 ),
    bJetPtBins = cms.vdouble(0.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0,
        80.0, 90.0, 100.0, 120.0, 150.0,
        200.0, 300.0, 500.0),
    metEtaBins = cms.vdouble(),
    ttSemiLeptonicEventMuons = cms.InputTag("ttSemiLepEventHitFitMuons"),
    udscJetResolutions = cms.string('TopQuarkAnalysis/TopHitFit/data/resolution/tqafUdscJetResolution_Summer11.txt')
)


process.analyzeHitFitReference = cms.EDAnalyzer("AnalyzeHitFit",
    patJets = cms.InputTag("referencePatJets"),
    pileUpFileMCObserved = cms.FileInPath('CommonTools/MyTools/data/pileUpFileMC_Fall11inTime.root'),
    patElectrons = cms.InputTag("referencePatElectrons"),
    patMETs = cms.InputTag("patMETs"),
    pathPlots = cms.string('/afs/cern.ch/user/v/vadler/work/cms/Top/CMSSW_5_3_13/output/plots/analyzeHitFit/analyzeHitFit_fromSummer11-coarseEta_Summer12_MadGraph_L3_unambiguousOnly_elecs_'),
    metPtBins = cms.vdouble(10.0, 20.0, 29.0, 37.0, 44.0,
        51.0, 59.0, 69.0, 80.0, 96.0,
        122.0, 200.0, 300.0),
    ttSemiLeptonicEventElectrons = cms.InputTag("ttSemiLepEventReferenceElectrons"),
    electronEtaBins = cms.vdouble( -2.500, -1.5660, -1.4442, -0.870, 0.000, 0.870, 1.4442, 1.5660, 2.500 ),
    bJetEtaBins = cms.vdouble( -2.500, -1.479, -0.870, 0.000, 0.870, 1.479, 2.500 ),
    jecLevel = cms.string('L3Absolute'),
    allJets = cms.bool(False),
    pileUpFileDataObserved = cms.FileInPath('CommonTools/MyTools/data/pileUpFileData_2011observedPixel.root'),
    bJetPtBins = cms.vdouble(0.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0,
        80.0, 90.0, 100.0, 120.0, 150.0,
        200.0, 300.0, 500.0),
    udscJetPtBins = cms.vdouble(0.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0,
        80.0, 90.0, 100.0, 120.0, 150.0,
        200.0, 300.0, 500.0),
    electronPtBins = cms.vdouble(0.0, 20.0, 27.0, 33.0, 40.0, 47.0,
        54.0, 62.0, 73.0, 86.0, 109.0,
        200.0, 400.0),
    muonPtBins = cms.vdouble(0.0, 20.0, 27.0, 33.0, 40.0, 47.0,
        54.0, 62.0, 73.0, 86.0, 109.0,
        200.0, 400.0),
    pileUpFileMCTrue = cms.FileInPath('CommonTools/MyTools/data/pileUpFileMC_Fall11.root'),
    udscJetEtaBins = cms.vdouble( -2.500, -1.479, -0.870, 0.000, 0.870, 1.479, 2.500 ),
    electronResolutions = cms.string('TopQuarkAnalysis/TopHitFit/data/resolution/tqafElectronResolution_Summer11.txt'),
    ttGenEvent = cms.InputTag("genEvt"),
    metResolutions = cms.string('TopQuarkAnalysis/TopHitFit/data/resolution/tqafKtResolution_Summer11.txt'),
    muonResolutions = cms.string('TopQuarkAnalysis/TopHitFit/data/resolution/tqafMuonResolution_Summer11.txt'),
    pileUpFileDataTrue = cms.FileInPath('CommonTools/MyTools/data/pileUpFileData_2011truePixel.root'),
    patMuons = cms.InputTag("referencePatMuons"),
    muonEtaBins = cms.vdouble( -2.4, -2.1, -1.3, -0.9, 0.0, 0.9, 1.3, 2.1, 2.4 ),
    bJetResolutions = cms.string('TopQuarkAnalysis/TopHitFit/data/resolution/tqafBJetResolution_Summer11.txt'),
    metEtaBins = cms.vdouble(),
    ttSemiLeptonicEventMuons = cms.InputTag("ttSemiLepEventReferenceMuons"),
    udscJetResolutions = cms.string('TopQuarkAnalysis/TopHitFit/data/resolution/tqafUdscJetResolution_Summer11.txt')
)


process.makeHypothesis_genMatchReferenceElectrons = cms.Sequence(process.ttSemiLepJetPartonMatchReferenceElectrons+process.ttSemiLepHypGenMatchReferenceElectrons)


process.makeTtSemiLepHypothesesReferenceElectrons = cms.Sequence(process.makeHypothesis_genMatchReferenceElectrons)


process.makeHypothesis_genMatchMCMatchElectrons = cms.Sequence(process.ttSemiLepJetPartonMatchMCMatchElectrons+process.ttSemiLepHypGenMatchMCMatchElectrons)


process.makeHypothesis_genMatchHitFitElectrons = cms.Sequence(process.ttSemiLepJetPartonMatchHitFitElectrons+process.ttSemiLepHypGenMatchHitFitElectrons)


process.makeTtSemiLepEventReferenceElectrons = cms.Sequence(process.makeTtSemiLepHypothesesReferenceElectrons+process.ttSemiLepEventReferenceElectrons)


process.makeTtSemiLepHypothesesMCMatchElectrons = cms.Sequence(process.makeHypothesis_genMatchMCMatchElectrons)


process.makeTtSemiLepHypothesesHitFitElectrons = cms.Sequence(process.makeHypothesis_genMatchHitFitElectrons)


process.makeTtSemiLepEventMCMatchElectrons = cms.Sequence(process.makeTtSemiLepHypothesesMCMatchElectrons+process.ttSemiLepEventMCMatchElectrons)


process.makeTtSemiLepEventHitFitElectrons = cms.Sequence(process.makeTtSemiLepHypothesesHitFitElectrons+process.ttSemiLepEventHitFitElectrons)


process.matcherSequenceBase = cms.Sequence(process.makeTtSemiLepEventMCMatchElectrons)


process.matcherSequenceReference = cms.Sequence(process.makeTtSemiLepEventReferenceElectrons)


process.matcherSequence = cms.Sequence(process.makeTtSemiLepEventHitFitElectrons)


process.standardPath = cms.Path(process.hltHighLevel+process.matcherSequenceBase+process.matcherSequence+process.analyzeHitFit)


process.referencePath = cms.Path(process.hltHighLevelReference+process.matcherSequenceBase+process.matcherSequenceReference+process.analyzeHitFitReference)


process.MessageLogger = cms.Service("MessageLogger",
    suppressInfo = cms.untracked.vstring(),
    debugs = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    suppressDebug = cms.untracked.vstring(),
    cout = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    cerr_stats = cms.untracked.PSet(
        threshold = cms.untracked.string('WARNING'),
        output = cms.untracked.string('cerr'),
        optionalPSet = cms.untracked.bool(True)
    ),
    warnings = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    default = cms.untracked.PSet(

    ),
    statistics = cms.untracked.vstring('cerr_stats'),
    cerr = cms.untracked.PSet(
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        noTimeStamps = cms.untracked.bool(False),
        FwkReport = cms.untracked.PSet(
            reportEvery = cms.untracked.int32(100000),
            optionalPSet = cms.untracked.bool(True),
            limit = cms.untracked.int32(10000000)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            optionalPSet = cms.untracked.bool(True),
            limit = cms.untracked.int32(0)
        ),
        threshold = cms.untracked.string('INFO'),
        FwkJob = cms.untracked.PSet(
            optionalPSet = cms.untracked.bool(True),
            limit = cms.untracked.int32(0)
        ),
        FwkSummary = cms.untracked.PSet(
            reportEvery = cms.untracked.int32(1),
            optionalPSet = cms.untracked.bool(True),
            limit = cms.untracked.int32(10000000)
        ),
        optionalPSet = cms.untracked.bool(True)
    ),
    FrameworkJobReport = cms.untracked.PSet(
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        optionalPSet = cms.untracked.bool(True),
        FwkJob = cms.untracked.PSet(
            optionalPSet = cms.untracked.bool(True),
            limit = cms.untracked.int32(10000000)
        )
    ),
    suppressWarning = cms.untracked.vstring(),
    errors = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    destinations = cms.untracked.vstring('warnings',
        'errors',
        'infos',
        'debugs',
        'cout',
        'cerr'),
    debugModules = cms.untracked.vstring(),
    infos = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        Root_NoDictionary = cms.untracked.PSet(
            optionalPSet = cms.untracked.bool(True),
            limit = cms.untracked.int32(0)
        ),
        placeholder = cms.untracked.bool(True)
    ),
    categories = cms.untracked.vstring('FwkJob',
        'FwkReport',
        'FwkSummary',
        'Root_NoDictionary'),
    fwkJobReports = cms.untracked.vstring('FrameworkJobReport')
)


process.TFileService = cms.Service("TFileService",
    fileName = cms.string('/afs/cern.ch/user/v/vadler/work/cms/Top/CMSSW_5_3_13/output/analyzeHitFit_fromSummer11-coarseEta_Summer12_MadGraph_L3_unambiguousOnly_elecs.root')
)


process.TtSemiLepJetCombMVAFileSource = cms.ESSource("TtSemiLepJetCombMVAFileSource",
    ttSemiLepJetCombMVA = cms.FileInPath('TopQuarkAnalysis/TopJetCombination/data/TtSemiLepJetComb.mva')
)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)


