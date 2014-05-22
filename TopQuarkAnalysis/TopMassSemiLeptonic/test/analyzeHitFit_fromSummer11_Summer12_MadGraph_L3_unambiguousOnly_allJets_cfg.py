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


process.findTtSemiLepJetCombGeom = cms.EDProducer("TtSemiLepJetCombGeom",
    minBDiscBJets = cms.double(1.0),
    maxNJets = cms.int32(4),
    bTagAlgorithm = cms.string('trackCountingHighEffBJetTags'),
    leps = cms.InputTag("selectedPatMuons"),
    maxBDiscLightJets = cms.double(3.0),
    useBTagging = cms.bool(False),
    useDeltaR = cms.bool(True),
    jets = cms.InputTag("selectedPatJets")
)


process.findTtSemiLepJetCombMVA = cms.EDProducer("TtSemiLepJetCombMVAComputer",
    jets = cms.InputTag("selectedPatJets"),
    mets = cms.InputTag("patMETs"),
    maxNJets = cms.int32(4),
    leps = cms.InputTag("selectedPatMuons"),
    maxNComb = cms.int32(1)
)


process.findTtSemiLepJetCombMaxSumPtWMass = cms.EDProducer("TtSemiLepJetCombMaxSumPtWMass",
    minBDiscBJets = cms.double(1.0),
    maxNJets = cms.int32(4),
    bTagAlgorithm = cms.string('trackCountingHighEffBJetTags'),
    leps = cms.InputTag("selectedPatMuons"),
    maxBDiscLightJets = cms.double(3.0),
    useBTagging = cms.bool(False),
    jets = cms.InputTag("selectedPatJets"),
    wMass = cms.double(80.4)
)


process.findTtSemiLepJetCombWMassDeltaTopMass = cms.EDProducer("TtSemiLepJetCombWMassDeltaTopMass",
    minBDiscBJets = cms.double(1.0),
    mets = cms.InputTag("patMETs"),
    maxNJets = cms.int32(4),
    bTagAlgorithm = cms.string('trackCountingHighEffBJetTags'),
    leps = cms.InputTag("selectedPatMuons"),
    maxBDiscLightJets = cms.double(3.0),
    useBTagging = cms.bool(False),
    neutrinoSolutionType = cms.int32(-1),
    jets = cms.InputTag("selectedPatJets"),
    wMass = cms.double(80.4)
)


process.findTtSemiLepJetCombWMassMaxSumPt = cms.EDProducer("TtSemiLepJetCombWMassMaxSumPt",
    minBDiscBJets = cms.double(1.0),
    maxNJets = cms.int32(4),
    bTagAlgorithm = cms.string('trackCountingHighEffBJetTags'),
    leps = cms.InputTag("selectedPatMuons"),
    maxBDiscLightJets = cms.double(3.0),
    useBTagging = cms.bool(False),
    jets = cms.InputTag("selectedPatJets"),
    wMass = cms.double(80.4)
)


process.hitFitTtSemiLepEventHypothesis = cms.EDProducer("TtSemiLepHitFitProducerMuon",
    jesB = cms.double(1.0),
    jes = cms.double(1.0),
    bTagAlgo = cms.string('trackCountingHighEffBJetTags'),
    maxNJets = cms.int32(4),
    maxNComb = cms.int32(1),
    leps = cms.InputTag("selectedPatMuons"),
    maxBDiscLightJets = cms.double(3.0),
    useBTagging = cms.bool(False),
    mW = cms.double(80.4),
    mTop = cms.double(0.0),
    jetCorrectionLevel = cms.string('L3Absolute'),
    mets = cms.InputTag("patMETs"),
    jets = cms.InputTag("selectedPatJets"),
    minBDiscBJets = cms.double(1.0)
)


process.kinFitTtSemiLepEventHypothesis = cms.EDProducer("TtSemiLepKinFitProducerMuon",
    minBDiscBJets = cms.double(1.0),
    mets = cms.InputTag("patMETs"),
    bTagAlgo = cms.string('trackCountingHighEffBJetTags'),
    maxNJets = cms.int32(4),
    maxNComb = cms.int32(1),
    jetEnergyResolutionScaleFactors = cms.vdouble(1.0),
    maxBDiscLightJets = cms.double(3.0),
    useBTagging = cms.bool(False),
    jetEnergyResolutionEtaBinning = cms.vdouble(0.0, -1.0),
    maxF = cms.double(0.0001),
    maxNrIter = cms.uint32(500),
    useOnlyMatch = cms.bool(False),
    lepParametrisation = cms.uint32(1),
    match = cms.InputTag("findTtSemiLepJetCombMVA"),
    leps = cms.InputTag("selectedPatMuons"),
    mW = cms.double(80.4),
    jets = cms.InputTag("selectedPatJets"),
    jetParametrisation = cms.uint32(1),
    maxDeltaS = cms.double(5e-05),
    mTop = cms.double(173.0),
    metParametrisation = cms.uint32(1),
    constraints = cms.vuint32(1, 2)
)


process.ttSemiLepEvent = cms.EDProducer("TtSemiLepEvtBuilder",
    genMatch = cms.PSet(
        sumPt = cms.InputTag("ttSemiLepJetPartonMatch","SumPt"),
        sumDR = cms.InputTag("ttSemiLepJetPartonMatch","SumDR")
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
    decayChannel1 = cms.int32(2),
    hypotheses = cms.VInputTag("ttSemiLepHypGenMatch"),
    genEvent = cms.InputTag("genEvt"),
    kinFit = cms.PSet(
        chi2 = cms.InputTag("kinFitTtSemiLepEventHypothesis","Chi2"),
        prob = cms.InputTag("kinFitTtSemiLepEventHypothesis","Prob")
    ),
    decayChannel2 = cms.int32(0)
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


process.ttSemiLepEventHitFitMuons = cms.EDProducer("TtSemiLepEvtBuilder",
    genMatch = cms.PSet(
        sumPt = cms.InputTag("ttSemiLepJetPartonMatchHitFitMuons","SumPt"),
        sumDR = cms.InputTag("ttSemiLepJetPartonMatchHitFitMuons","SumDR")
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
    hypotheses = cms.VInputTag("ttSemiLepHypGenMatchHitFitMuons"),
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


process.ttSemiLepEventMCMatchMuons = cms.EDProducer("TtSemiLepEvtBuilder",
    genMatch = cms.PSet(
        sumPt = cms.InputTag("ttSemiLepJetPartonMatchMCMatchMuons","SumPt"),
        sumDR = cms.InputTag("ttSemiLepJetPartonMatchMCMatchMuons","SumDR")
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
    hypotheses = cms.VInputTag("ttSemiLepHypGenMatchMCMatchMuons"),
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


process.ttSemiLepEventReferenceMuons = cms.EDProducer("TtSemiLepEvtBuilder",
    genMatch = cms.PSet(
        sumPt = cms.InputTag("ttSemiLepJetPartonMatchReferenceMuons","SumPt"),
        sumDR = cms.InputTag("ttSemiLepJetPartonMatchReferenceMuons","SumDR")
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
    hypotheses = cms.VInputTag("ttSemiLepHypGenMatchReferenceMuons"),
    genEvent = cms.InputTag("genEvt"),
    decayChannel1 = cms.int32(2),
    decayChannel2 = cms.int32(0)
)


process.ttSemiLepHypGenMatch = cms.EDProducer("TtSemiLepHypGenMatch",
    mets = cms.InputTag("patMETs"),
    jetCorrectionLevel = cms.string('L3Absolute'),
    leps = cms.InputTag("selectedPatMuons"),
    neutrinoSolutionType = cms.int32(-1),
    nJetsConsidered = cms.InputTag("ttSemiLepJetPartonMatch","NumberOfConsideredJets"),
    jets = cms.InputTag("selectedPatJets"),
    match = cms.InputTag("ttSemiLepJetPartonMatch")
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


process.ttSemiLepHypGenMatchHitFitMuons = cms.EDProducer("TtSemiLepHypGenMatch",
    mets = cms.InputTag("patMETs"),
    jetCorrectionLevel = cms.string('L3Absolute'),
    leps = cms.InputTag("selectedPatMuonsHitFit"),
    neutrinoSolutionType = cms.int32(-1),
    nJetsConsidered = cms.InputTag("ttSemiLepJetPartonMatchHitFitMuons","NumberOfConsideredJets"),
    jets = cms.InputTag("selectedPatJetsHitFit"),
    match = cms.InputTag("ttSemiLepJetPartonMatchHitFitMuons")
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


process.ttSemiLepHypGenMatchMCMatchMuons = cms.EDProducer("TtSemiLepHypGenMatch",
    mets = cms.InputTag("patMETs"),
    jetCorrectionLevel = cms.string('L3Absolute'),
    leps = cms.InputTag("selectedPatMuonsMCMatch"),
    neutrinoSolutionType = cms.int32(-1),
    nJetsConsidered = cms.InputTag("ttSemiLepJetPartonMatchMCMatchMuons","NumberOfConsideredJets"),
    jets = cms.InputTag("selectedPatJetsMCMatch"),
    match = cms.InputTag("ttSemiLepJetPartonMatchMCMatchMuons")
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


process.ttSemiLepHypGenMatchReferenceMuons = cms.EDProducer("TtSemiLepHypGenMatch",
    mets = cms.InputTag("patMETs"),
    jetCorrectionLevel = cms.string('L3Absolute'),
    leps = cms.InputTag("referencePatMuons"),
    neutrinoSolutionType = cms.int32(-1),
    nJetsConsidered = cms.InputTag("ttSemiLepJetPartonMatchReferenceMuons","NumberOfConsideredJets"),
    jets = cms.InputTag("referencePatJets"),
    match = cms.InputTag("ttSemiLepJetPartonMatchReferenceMuons")
)


process.ttSemiLepHypGeom = cms.EDProducer("TtSemiLepHypGeom",
    mets = cms.InputTag("patMETs"),
    jetCorrectionLevel = cms.string('L3Absolute'),
    leps = cms.InputTag("selectedPatMuons"),
    neutrinoSolutionType = cms.int32(-1),
    nJetsConsidered = cms.InputTag("findTtSemiLepJetCombGeom","NumberOfConsideredJets"),
    jets = cms.InputTag("selectedPatJets"),
    match = cms.InputTag("findTtSemiLepJetCombGeom")
)


process.ttSemiLepHypHitFit = cms.EDProducer("TtSemiLepHypHitFit",
    status = cms.InputTag("hitFitTtSemiLepEventHypothesis","Status"),
    mets = cms.InputTag("patMETs"),
    partonsLepB = cms.InputTag("hitFitTtSemiLepEventHypothesis","PartonsLepB"),
    neutrinos = cms.InputTag("hitFitTtSemiLepEventHypothesis","Neutrinos"),
    leps = cms.InputTag("selectedPatMuons"),
    partonsHadB = cms.InputTag("hitFitTtSemiLepEventHypothesis","PartonsHadB"),
    leptons = cms.InputTag("hitFitTtSemiLepEventHypothesis","Leptons"),
    nJetsConsidered = cms.InputTag("hitFitTtSemiLepEventHypothesis","NumberOfConsideredJets"),
    jets = cms.InputTag("selectedPatJetsAK5PF"),
    partonsHadQ = cms.InputTag("hitFitTtSemiLepEventHypothesis","PartonsHadQ"),
    partonsHadP = cms.InputTag("hitFitTtSemiLepEventHypothesis","PartonsHadP"),
    match = cms.InputTag("hitFitTtSemiLepEventHypothesis")
)


process.ttSemiLepHypKinFit = cms.EDProducer("TtSemiLepHypKinFit",
    status = cms.InputTag("kinFitTtSemiLepEventHypothesis","Status"),
    mets = cms.InputTag("patMETs"),
    partonsLepB = cms.InputTag("kinFitTtSemiLepEventHypothesis","PartonsLepB"),
    neutrinos = cms.InputTag("kinFitTtSemiLepEventHypothesis","Neutrinos"),
    leps = cms.InputTag("selectedPatMuons"),
    partonsHadB = cms.InputTag("kinFitTtSemiLepEventHypothesis","PartonsHadB"),
    leptons = cms.InputTag("kinFitTtSemiLepEventHypothesis","Leptons"),
    nJetsConsidered = cms.InputTag("kinFitTtSemiLepEventHypothesis","NumberOfConsideredJets"),
    jets = cms.InputTag("selectedPatJets"),
    partonsHadQ = cms.InputTag("kinFitTtSemiLepEventHypothesis","PartonsHadQ"),
    partonsHadP = cms.InputTag("kinFitTtSemiLepEventHypothesis","PartonsHadP"),
    match = cms.InputTag("kinFitTtSemiLepEventHypothesis")
)


process.ttSemiLepHypMVADisc = cms.EDProducer("TtSemiLepHypMVADisc",
    mets = cms.InputTag("patMETs"),
    jetCorrectionLevel = cms.string('L3Absolute'),
    leps = cms.InputTag("selectedPatMuons"),
    neutrinoSolutionType = cms.int32(-1),
    nJetsConsidered = cms.InputTag("findTtSemiLepJetCombMVA","NumberOfConsideredJets"),
    jets = cms.InputTag("selectedPatJets"),
    match = cms.InputTag("findTtSemiLepJetCombMVA")
)


process.ttSemiLepHypMaxSumPtWMass = cms.EDProducer("TtSemiLepHypMaxSumPtWMass",
    mets = cms.InputTag("patMETs"),
    jetCorrectionLevel = cms.string('L3Absolute'),
    leps = cms.InputTag("selectedPatMuons"),
    neutrinoSolutionType = cms.int32(-1),
    nJetsConsidered = cms.InputTag("findTtSemiLepJetCombMaxSumPtWMass","NumberOfConsideredJets"),
    jets = cms.InputTag("selectedPatJets"),
    match = cms.InputTag("findTtSemiLepJetCombMaxSumPtWMass")
)


process.ttSemiLepHypWMassDeltaTopMass = cms.EDProducer("TtSemiLepHypWMassDeltaTopMass",
    mets = cms.InputTag("patMETs"),
    jetCorrectionLevel = cms.string('L3Absolute'),
    leps = cms.InputTag("selectedPatMuons"),
    neutrinoSolutionType = cms.int32(-1),
    nJetsConsidered = cms.InputTag("findTtSemiLepJetCombWMassDeltaTopMass","NumberOfConsideredJets"),
    jets = cms.InputTag("selectedPatJets"),
    match = cms.InputTag("findTtSemiLepJetCombWMassDeltaTopMass")
)


process.ttSemiLepHypWMassMaxSumPt = cms.EDProducer("TtSemiLepHypWMassMaxSumPt",
    mets = cms.InputTag("patMETs"),
    jetCorrectionLevel = cms.string('L3Absolute'),
    leps = cms.InputTag("selectedPatMuons"),
    neutrinoSolutionType = cms.int32(-1),
    nJetsConsidered = cms.InputTag("findTtSemiLepJetCombWMassMaxSumPt","NumberOfConsideredJets"),
    jets = cms.InputTag("selectedPatJets"),
    match = cms.InputTag("findTtSemiLepJetCombWMassMaxSumPt")
)


process.ttSemiLepJetPartonMatch = cms.EDProducer("TtSemiLepJetPartonMatch",
    maxDist = cms.double(0.3),
    useMaxDist = cms.bool(False),
    maxNJets = cms.int32(6),
    algorithm = cms.string('unambiguousOnly'),
    maxNComb = cms.int32(1),
    verbosity = cms.int32(0),
    partonsToIgnore = cms.vstring(),
    useDeltaR = cms.bool(True),
    jets = cms.InputTag("selectedPatJets")
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


process.ttSemiLepJetPartonMatchHitFitMuons = cms.EDProducer("TtSemiLepJetPartonMatch",
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


process.ttSemiLepJetPartonMatchMCMatchMuons = cms.EDProducer("TtSemiLepJetPartonMatch",
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


process.ttSemiLepJetPartonMatchReferenceMuons = cms.EDProducer("TtSemiLepJetPartonMatch",
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
    HLTPaths = cms.vstring('pf2PatPathMuons',
        'pf2PatPathElectrons'),
    throw = cms.bool(True),
    andOr = cms.bool(True)
)


process.hltHighLevelReference = cms.EDFilter("HLTHighLevel",
    eventSetupPathsKey = cms.string(''),
    andOr = cms.bool(True),
    HLTPaths = cms.vstring('referencePathMuons',
        'referencePathElectrons'),
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


process.ttSemiLepHypSelectionFilterMuons = cms.EDFilter("TtSemiLepHypSelectionFilter",
    ttSemiLepHyp = cms.string('kGenMatch'),
    leptonSelector = cms.string('selectedPatMuonsHitFit'),
    jetSelector = cms.string('selectedPatJetsHitFit'),
    processName = cms.string('SKIM'),
    ttSemiLepHypLeptons = cms.InputTag("selectedPatMuonsMCMatch"),
    ttSemiLepEvt = cms.InputTag("ttSemiLepEventMCMatchMuons"),
    ttSemiLepHypJets = cms.InputTag("selectedPatJetsMCMatch")
)


process.ttSemiLepHypSelectionFilterMuonsReference = cms.EDFilter("TtSemiLepHypSelectionFilter",
    jetCut = cms.string('pt > 30. && numberOfDaughters > 1 && chargedEmEnergyFraction < 0.99 && neutralHadronEnergyFraction < 0.99 && neutralEmEnergyFraction < 0.99 && (chargedHadronEnergyFraction > 0. || abs(eta) >= 2.4) && (chargedMultiplicity > 0 || abs(eta) >= 2.4) && abs(eta) < 3.0 && abs(eta) < 2.5'),
    ttSemiLepHyp = cms.string('kGenMatch'),
    leptonSelector = cms.string('referencePatMuons'),
    jetSelector = cms.string('referencePatJets'),
    processName = cms.string('SKIM'),
    ttSemiLepHypLeptons = cms.InputTag("selectedPatMuonsMCMatch"),
    ttSemiLepEvt = cms.InputTag("ttSemiLepEventMCMatchMuons"),
    ttSemiLepHypJets = cms.InputTag("selectedPatJetsMCMatch"),
    leptonCut = cms.string('isTrackerMuon && pt > 26. && abs(eta) < 2.1 && globalTrack.normalizedChi2 < 10. && globalTrack.hitPattern.numberOfValidMuonHits > 0 && abs(dB) < 0.02 && innerTrack.hitPattern.trackerLayersWithMeasurement > 8 && innerTrack.hitPattern.pixelLayersWithMeasurement >= 1 && numberOfMatches > 1 && (chargedHadronIso+neutralHadronIso+photonIso)/pt < 0.125')
)


process.analyzeHitFit = cms.EDAnalyzer("AnalyzeHitFit",
    patJets = cms.InputTag("selectedPatJetsHitFit"),
    pileUpFileMCObserved = cms.FileInPath('CommonTools/MyTools/data/pileUpFileMC_Fall11inTime.root'),
    patElectrons = cms.InputTag("selectedPatElectronsHitFit"),
    patMETs = cms.InputTag("patMETs"),
    pathPlots = cms.string('/afs/cern.ch/user/v/vadler/cms/Top/CMSSW_5_3_11/output/plots/analyzeHitFit/analyzeHitFit_fromSummer11_Summer12_MadGraph_L3_unambiguousOnly_allJets_'),
    metPtBins = cms.vdouble(10.0, 20.0, 29.0, 37.0, 44.0,
        51.0, 59.0, 69.0, 80.0, 96.0,
        122.0, 200.0, 300.0),
    ttSemiLeptonicEventElectrons = cms.InputTag("ttSemiLepEventHitFitElectrons"),
    electronEtaBins = cms.vdouble(),
    bJetEtaBins = cms.vdouble(),
    jecLevel = cms.string('L3Absolute'),
    allJets = cms.bool( True ),
    pileUpFileDataObserved = cms.FileInPath('CommonTools/MyTools/data/pileUpFileData_2011observedPixel.root'),
    bJetResolutions = cms.string('TopQuarkAnalysis/TopHitFit/data/resolution/tqafBJetResolution_Summer11.txt'),
    udscJetPtBins = cms.vdouble(0.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0,
        80.0, 90.0, 100.0, 120.0, 150.0,
        200.0, 300.0, 500.0),
    jetPtBins = cms.vdouble(0.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0,
        80.0, 90.0, 100.0, 120.0, 150.0,
        200.0, 300.0, 500.0),
    udscJetEtaBins = cms.vdouble(),
    jetEtaBins = cms.vdouble(),
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
    muonEtaBins = cms.vdouble(),
    bJetPtBins = cms.vdouble(0.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0,
        80.0, 90.0, 100.0, 120.0, 150.0,
        200.0, 300.0, 500.0),
    metEtaBins = cms.vdouble(),
    ttSemiLeptonicEventMuons = cms.InputTag("ttSemiLepEventHitFitMuons"),
    udscJetResolutions = cms.string('TopQuarkAnalysis/TopHitFit/data/resolution/tqafUdscJetResolution_Summer11.txt') ,
    jetResolutions = cms.string('TopQuarkAnalysis/TopHitFit/data/resolution/tqafUdscJetResolution_Summer11.txt')
)


process.analyzeHitFitReference = cms.EDAnalyzer("AnalyzeHitFit",
    patJets = cms.InputTag("referencePatJets"),
    pileUpFileMCObserved = cms.FileInPath('CommonTools/MyTools/data/pileUpFileMC_Fall11inTime.root'),
    patElectrons = cms.InputTag("referencePatElectrons"),
    patMETs = cms.InputTag("patMETs"),
    pathPlots = cms.string('/afs/cern.ch/user/v/vadler/cms/Top/CMSSW_5_3_11/output/plots/analyzeHitFit/analyzeHitFit_fromSummer11_Summer12_MadGraph_L3_unambiguousOnly_allJets_'),
    metPtBins = cms.vdouble(10.0, 20.0, 29.0, 37.0, 44.0,
        51.0, 59.0, 69.0, 80.0, 96.0,
        122.0, 200.0, 300.0),
    ttSemiLeptonicEventElectrons = cms.InputTag("ttSemiLepEventReferenceElectrons"),
    electronEtaBins = cms.vdouble(),
    bJetEtaBins = cms.vdouble(),
    jecLevel = cms.string('L3Absolute'),
    allJets = cms.bool( True ),
    pileUpFileDataObserved = cms.FileInPath('CommonTools/MyTools/data/pileUpFileData_2011observedPixel.root'),
    bJetPtBins = cms.vdouble(0.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0,
        80.0, 90.0, 100.0, 120.0, 150.0,
        200.0, 300.0, 500.0),
    udscJetPtBins = cms.vdouble(0.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0,
        80.0, 90.0, 100.0, 120.0, 150.0,
        200.0, 300.0, 500.0),
    jetPtBins = cms.vdouble(0.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0,
        80.0, 90.0, 100.0, 120.0, 150.0,
        200.0, 300.0, 500.0),
    electronPtBins = cms.vdouble(0.0, 20.0, 27.0, 33.0, 40.0, 47.0,
        54.0, 62.0, 73.0, 86.0, 109.0,
        200.0, 400.0),
    muonPtBins = cms.vdouble(0.0, 20.0, 27.0, 33.0, 40.0, 47.0,
        54.0, 62.0, 73.0, 86.0, 109.0,
        200.0, 400.0),
    pileUpFileMCTrue = cms.FileInPath('CommonTools/MyTools/data/pileUpFileMC_Fall11.root'),
    udscJetEtaBins = cms.vdouble(),
    jetEtaBins = cms.vdouble(),
    electronResolutions = cms.string('TopQuarkAnalysis/TopHitFit/data/resolution/tqafElectronResolution_Summer11.txt'),
    ttGenEvent = cms.InputTag("genEvt"),
    metResolutions = cms.string('TopQuarkAnalysis/TopHitFit/data/resolution/tqafKtResolution_Summer11.txt'),
    muonResolutions = cms.string('TopQuarkAnalysis/TopHitFit/data/resolution/tqafMuonResolution_Summer11.txt'),
    pileUpFileDataTrue = cms.FileInPath('CommonTools/MyTools/data/pileUpFileData_2011truePixel.root'),
    patMuons = cms.InputTag("referencePatMuons"),
    muonEtaBins = cms.vdouble(),
    bJetResolutions = cms.string('TopQuarkAnalysis/TopHitFit/data/resolution/tqafBJetResolution_Summer11.txt'),
    metEtaBins = cms.vdouble(),
    ttSemiLeptonicEventMuons = cms.InputTag("ttSemiLepEventReferenceMuons"),
    udscJetResolutions = cms.string('TopQuarkAnalysis/TopHitFit/data/resolution/tqafUdscJetResolution_Summer11.txt') ,
    jetResolutions = cms.string('TopQuarkAnalysis/TopHitFit/data/resolution/tqafUdscJetResolution_Summer11.txt')
)


process.makeHypothesis_genMatchMCMatchMuons = cms.Sequence(process.ttSemiLepJetPartonMatchMCMatchMuons+process.ttSemiLepHypGenMatchMCMatchMuons)


process.makeHypothesis_geom = cms.Sequence(process.findTtSemiLepJetCombGeom+process.ttSemiLepHypGeom)


process.makeHypothesis_genMatchReferenceElectrons = cms.Sequence(process.ttSemiLepJetPartonMatchReferenceElectrons+process.ttSemiLepHypGenMatchReferenceElectrons)


process.makeTtSemiLepHypothesesReferenceElectrons = cms.Sequence(process.makeHypothesis_genMatchReferenceElectrons)


process.makeHypothesis_genMatch = cms.Sequence(process.ttSemiLepJetPartonMatch+process.ttSemiLepHypGenMatch)


process.makeHypothesis_hitFit = cms.Sequence(process.hitFitTtSemiLepEventHypothesis+process.ttSemiLepHypHitFit)


process.makeHypothesis_genMatchMCMatchElectrons = cms.Sequence(process.ttSemiLepJetPartonMatchMCMatchElectrons+process.ttSemiLepHypGenMatchMCMatchElectrons)


process.makeTtSemiLepHypothesesMCMatchMuons = cms.Sequence(process.makeHypothesis_genMatchMCMatchMuons)


process.makeTtSemiLepHypotheses = cms.Sequence(process.makeHypothesis_genMatch)


process.makeHypothesis_maxSumPtWMass = cms.Sequence(process.findTtSemiLepJetCombMaxSumPtWMass+process.ttSemiLepHypMaxSumPtWMass)


process.makeHypothesis_genMatchHitFitElectrons = cms.Sequence(process.ttSemiLepJetPartonMatchHitFitElectrons+process.ttSemiLepHypGenMatchHitFitElectrons)


process.makeTtSemiLepEventReferenceElectrons = cms.Sequence(process.makeTtSemiLepHypothesesReferenceElectrons+process.ttSemiLepEventReferenceElectrons)


process.makeHypothesis_wMassMaxSumPt = cms.Sequence(process.findTtSemiLepJetCombWMassMaxSumPt+process.ttSemiLepHypWMassMaxSumPt)


process.makeHypothesis_genMatchHitFitMuons = cms.Sequence(process.ttSemiLepJetPartonMatchHitFitMuons+process.ttSemiLepHypGenMatchHitFitMuons)


process.makeHypothesis_kinFit = cms.Sequence(process.kinFitTtSemiLepEventHypothesis+process.ttSemiLepHypKinFit)


process.makeHypothesis_mvaDisc = cms.Sequence(process.findTtSemiLepJetCombMVA+process.ttSemiLepHypMVADisc)


process.makeTtSemiLepEvent = cms.Sequence(process.makeTtSemiLepHypotheses+process.ttSemiLepEvent)


process.makeTtSemiLepEventMCMatchMuons = cms.Sequence(process.makeTtSemiLepHypothesesMCMatchMuons+process.ttSemiLepEventMCMatchMuons)


process.makeTtSemiLepHypothesesMCMatchElectrons = cms.Sequence(process.makeHypothesis_genMatchMCMatchElectrons)


process.makeHypothesis_genMatchReferenceMuons = cms.Sequence(process.ttSemiLepJetPartonMatchReferenceMuons+process.ttSemiLepHypGenMatchReferenceMuons)


process.makeHypothesis_wMassDeltaTopMass = cms.Sequence(process.findTtSemiLepJetCombWMassDeltaTopMass+process.ttSemiLepHypWMassDeltaTopMass)


process.makeTtSemiLepHypothesesHitFitElectrons = cms.Sequence(process.makeHypothesis_genMatchHitFitElectrons)


process.makeTtSemiLepHypothesesReferenceMuons = cms.Sequence(process.makeHypothesis_genMatchReferenceMuons)


process.makeTtSemiLepEventMCMatchElectrons = cms.Sequence(process.makeTtSemiLepHypothesesMCMatchElectrons+process.ttSemiLepEventMCMatchElectrons)


process.makeTtSemiLepHypothesesHitFitMuons = cms.Sequence(process.makeHypothesis_genMatchHitFitMuons)


process.makeTtSemiLepEventHitFitElectrons = cms.Sequence(process.makeTtSemiLepHypothesesHitFitElectrons+process.ttSemiLepEventHitFitElectrons)


process.makeTtSemiLepEventReferenceMuons = cms.Sequence(process.makeTtSemiLepHypothesesReferenceMuons+process.ttSemiLepEventReferenceMuons)


process.matcherSequenceBase = cms.Sequence(process.makeTtSemiLepEventMCMatchMuons+process.makeTtSemiLepEventMCMatchElectrons)


process.matcherSequenceReference = cms.Sequence(process.makeTtSemiLepEventReferenceMuons+process.makeTtSemiLepEventReferenceElectrons)


process.makeTtSemiLepEventHitFitMuons = cms.Sequence(process.makeTtSemiLepHypothesesHitFitMuons+process.ttSemiLepEventHitFitMuons)


process.matcherSequence = cms.Sequence(process.makeTtSemiLepEventHitFitMuons+process.makeTtSemiLepEventHitFitElectrons)


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
    fileName = cms.string('/afs/cern.ch/user/v/vadler/work/cms/Top/CMSSW_5_3_13/output/analyzeHitFit_fromSummer11_Summer12_MadGraph_L3_unambiguousOnly_allJets.root')
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


