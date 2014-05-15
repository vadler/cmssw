import FWCore.ParameterSet.Config as cms

process = cms.Process("USER")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_10_1_EUp.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_11_1_OKY.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_12_3_MVW.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_13_1_JKf.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_14_1_n2W.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_15_1_nNZ.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_16_1_YTb.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_17_1_rko.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_18_1_Hh8.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_19_1_wJK.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_1_1_Iem.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_20_1_IJp.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_21_1_JwF.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_22_1_fvp.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_23_1_eok.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_24_1_rw7.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_25_1_ZPf.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_26_1_Sl1.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_27_1_f5z.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_28_1_g35.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_29_1_CQL.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_2_1_LEI.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_30_1_D72.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_31_1_Zpu.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_32_1_tus.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_33_1_lOm.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_34_1_OtV.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_35_2_Nru.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_36_1_swq.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_37_1_cyd.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_38_1_yMA.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_39_1_SgL.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_3_1_SY6.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_40_1_8SH.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_41_1_mgg.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_42_1_wzQ.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_43_1_XuM.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_44_1_Att.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_45_1_npT.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_46_1_wtM.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_47_1_3Tc.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_48_1_9YS.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_49_1_oLD.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_4_1_Wc5.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_50_1_vZS.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_51_1_g4O.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_52_1_0Qm.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_53_1_bsy.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_54_1_tjF.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_55_1_sPd.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_56_1_wGv.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_57_2_0cc.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_58_1_NzO.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_59_1_ugo.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_5_1_IxM.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_60_1_RZr.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_61_1_R5l.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_62_1_z0L.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_63_1_4cm.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_64_1_Jmg.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_65_1_Jbv.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_66_1_NpY.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_67_1_Wbd.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_68_1_rYE.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_69_1_x79.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_6_1_Mdk.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_70_1_7kz.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_71_1_woG.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_7_1_CZ0.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_8_1_Hs9.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MadGraph/skimHitFitUnbiased_9_1_5AX.root')
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


process.ttSemiLepHypGenMatchHitFitElectrons = cms.EDProducer("TtSemiLepHypGenMatch",
    mets = cms.InputTag("patMETs"),
    jetCorrectionLevel = cms.string('L3Absolute'),
    leps = cms.InputTag("selectedPatElectronsUnbiasedHitFit"),
    neutrinoSolutionType = cms.int32(-1),
    nJetsConsidered = cms.InputTag("ttSemiLepJetPartonMatchHitFitElectrons","NumberOfConsideredJets"),
    jets = cms.InputTag("selectedPatJetsUnbiasedHitFit"),
    match = cms.InputTag("ttSemiLepJetPartonMatchHitFitElectrons")
)


process.ttSemiLepHypGenMatchHitFitMuons = cms.EDProducer("TtSemiLepHypGenMatch",
    mets = cms.InputTag("patMETs"),
    jetCorrectionLevel = cms.string('L3Absolute'),
    leps = cms.InputTag("selectedPatMuonsUnbiasedHitFit"),
    neutrinoSolutionType = cms.int32(-1),
    nJetsConsidered = cms.InputTag("ttSemiLepJetPartonMatchHitFitMuons","NumberOfConsideredJets"),
    jets = cms.InputTag("selectedPatJetsUnbiasedHitFit"),
    match = cms.InputTag("ttSemiLepJetPartonMatchHitFitMuons")
)


process.ttSemiLepHypGenMatchMCMatchElectrons = cms.EDProducer("TtSemiLepHypGenMatch",
    mets = cms.InputTag("patMETs"),
    jetCorrectionLevel = cms.string('L3Absolute'),
    leps = cms.InputTag("selectedPatElectronsUnbiasedMCMatch"),
    neutrinoSolutionType = cms.int32(-1),
    nJetsConsidered = cms.InputTag("ttSemiLepJetPartonMatchMCMatchElectrons","NumberOfConsideredJets"),
    jets = cms.InputTag("selectedPatJetsUnbiasedMCMatch"),
    match = cms.InputTag("ttSemiLepJetPartonMatchMCMatchElectrons")
)


process.ttSemiLepHypGenMatchMCMatchMuons = cms.EDProducer("TtSemiLepHypGenMatch",
    mets = cms.InputTag("patMETs"),
    jetCorrectionLevel = cms.string('L3Absolute'),
    leps = cms.InputTag("selectedPatMuonsUnbiasedMCMatch"),
    neutrinoSolutionType = cms.int32(-1),
    nJetsConsidered = cms.InputTag("ttSemiLepJetPartonMatchMCMatchMuons","NumberOfConsideredJets"),
    jets = cms.InputTag("selectedPatJetsUnbiasedMCMatch"),
    match = cms.InputTag("ttSemiLepJetPartonMatchMCMatchMuons")
)


process.ttSemiLepHypGenMatchReferenceElectrons = cms.EDProducer("TtSemiLepHypGenMatch",
    mets = cms.InputTag("patMETs"),
    jetCorrectionLevel = cms.string('L3Absolute'),
    leps = cms.InputTag("referencePatElectronsUnbiased"),
    neutrinoSolutionType = cms.int32(-1),
    nJetsConsidered = cms.InputTag("ttSemiLepJetPartonMatchReferenceElectrons","NumberOfConsideredJets"),
    jets = cms.InputTag("referencePatJetsUnbiased"),
    match = cms.InputTag("ttSemiLepJetPartonMatchReferenceElectrons")
)


process.ttSemiLepHypGenMatchReferenceMuons = cms.EDProducer("TtSemiLepHypGenMatch",
    mets = cms.InputTag("patMETs"),
    jetCorrectionLevel = cms.string('L3Absolute'),
    leps = cms.InputTag("referencePatMuonsUnbiased"),
    neutrinoSolutionType = cms.int32(-1),
    nJetsConsidered = cms.InputTag("ttSemiLepJetPartonMatchReferenceMuons","NumberOfConsideredJets"),
    jets = cms.InputTag("referencePatJetsUnbiased"),
    match = cms.InputTag("ttSemiLepJetPartonMatchReferenceMuons")
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
    jets = cms.InputTag("selectedPatJetsUnbiasedHitFit")
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
    jets = cms.InputTag("selectedPatJetsUnbiasedHitFit")
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
    jets = cms.InputTag("selectedPatJetsUnbiasedMCMatch")
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
    jets = cms.InputTag("selectedPatJetsUnbiasedMCMatch")
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
    jets = cms.InputTag("referencePatJetsUnbiased")
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
    jets = cms.InputTag("referencePatJetsUnbiased")
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
    leptonSelector = cms.string('selectedPatElectronsUnbiasedHitFit'),
    jetSelector = cms.string('selectedPatJetsUnbiasedHitFit'),
    processName = cms.string('SKIM'),
    ttSemiLepHypLeptons = cms.InputTag("selectedPatElectronsUnbiasedMCMatch"),
    ttSemiLepEvt = cms.InputTag("ttSemiLepEventMCMatchElectrons"),
    ttSemiLepHypJets = cms.InputTag("selectedPatJetsUnbiasedMCMatch")
)


process.ttSemiLepHypSelectionFilterElectronsReference = cms.EDFilter("TtSemiLepHypSelectionFilter",
    jetCut = cms.string('pt > 30. && numberOfDaughters > 1 && chargedEmEnergyFraction < 0.99 && neutralHadronEnergyFraction < 0.99 && neutralEmEnergyFraction < 0.99 && (chargedHadronEnergyFraction > 0. || abs(eta) >= 2.4) && (chargedMultiplicity > 0 || abs(eta) >= 2.4) && abs(eta) < 3.0 && abs(eta) < 2.5'),
    ttSemiLepHyp = cms.string('kGenMatch'),
    leptonSelector = cms.string('referencePatElectronsUnbiased'),
    jetSelector = cms.string('referencePatJetsUnbiased'),
    processName = cms.string('SKIM'),
    ttSemiLepHypLeptons = cms.InputTag("selectedPatElectronsUnbiasedMCMatch"),
    ttSemiLepEvt = cms.InputTag("ttSemiLepEventMCMatchElectrons"),
    ttSemiLepHypJets = cms.InputTag("selectedPatJetsUnbiasedMCMatch"),
    leptonCut = cms.string('et > 35. && abs(eta) < 2.5 && !(1.4442 < abs(superCluster.eta) && abs(superCluster.eta) < 1.5660) && abs(dB) < 0.02 && (electronID("eidHyperTight1MC") == 9. || electronID("eidHyperTight1MC") == 11. || electronID("eidHyperTight1MC") == 13. || electronID("eidHyperTight1MC") == 15.) && (chargedHadronIso+neutralHadronIso+photonIso)/pt < 0.1 && passConversionVeto && gsfTrack.trackerExpectedHitsInner.numberOfLostHits == 0')
)


process.ttSemiLepHypSelectionFilterMuons = cms.EDFilter("TtSemiLepHypSelectionFilter",
    ttSemiLepHyp = cms.string('kGenMatch'),
    leptonSelector = cms.string('selectedPatMuonsUnbiasedHitFit'),
    jetSelector = cms.string('selectedPatJetsUnbiasedHitFit'),
    processName = cms.string('SKIM'),
    ttSemiLepHypLeptons = cms.InputTag("selectedPatMuonsUnbiasedMCMatch"),
    ttSemiLepEvt = cms.InputTag("ttSemiLepEventMCMatchMuons"),
    ttSemiLepHypJets = cms.InputTag("selectedPatJetsUnbiasedMCMatch")
)


process.ttSemiLepHypSelectionFilterMuonsReference = cms.EDFilter("TtSemiLepHypSelectionFilter",
    jetCut = cms.string('pt > 30. && numberOfDaughters > 1 && chargedEmEnergyFraction < 0.99 && neutralHadronEnergyFraction < 0.99 && neutralEmEnergyFraction < 0.99 && (chargedHadronEnergyFraction > 0. || abs(eta) >= 2.4) && (chargedMultiplicity > 0 || abs(eta) >= 2.4) && abs(eta) < 3.0 && abs(eta) < 2.5'),
    ttSemiLepHyp = cms.string('kGenMatch'),
    leptonSelector = cms.string('referencePatMuonsUnbiased'),
    jetSelector = cms.string('referencePatJetsUnbiased'),
    processName = cms.string('SKIM'),
    ttSemiLepHypLeptons = cms.InputTag("selectedPatMuonsUnbiasedMCMatch"),
    ttSemiLepEvt = cms.InputTag("ttSemiLepEventMCMatchMuons"),
    ttSemiLepHypJets = cms.InputTag("selectedPatJetsUnbiasedMCMatch"),
    leptonCut = cms.string('isTrackerMuon && pt > 26. && abs(eta) < 2.1 && globalTrack.normalizedChi2 < 10. && globalTrack.hitPattern.numberOfValidMuonHits > 0 && abs(dB) < 0.02 && innerTrack.hitPattern.trackerLayersWithMeasurement > 8 && innerTrack.hitPattern.pixelLayersWithMeasurement >= 1 && numberOfMatches > 1 && (chargedHadronIso+neutralHadronIso+photonIso)/pt < 0.125')
)


process.analyzeHitFit = cms.EDAnalyzer("AnalyzeHitFit",
    patJets = cms.InputTag("selectedPatJetsUnbiasedHitFit"),
    pileUpFileMCObserved = cms.FileInPath('CommonTools/MyTools/data/pileUpFileMC_Fall11inTime.root'),
    patElectrons = cms.InputTag("selectedPatElectronsUnbiasedHitFit"),
    patMETs = cms.InputTag("patMETs"),
    pathPlots = cms.string('/afs/cern.ch/user/v/vadler/cms/Top/CMSSW_5_3_11/output/plots/analyzeHitFit/analyzeHitFit_fromSummer11-coarseEta_Summer12_MadGraph_L3_unambiguousOnly_'),
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
    udscJetPtBins = cms.vdouble(30.0, 40.0, 50.0, 60.0, 70.0,
        80.0, 90.0, 100.0, 120.0, 150.0,
        200.0, 300.0, 500.0),
    udscJetEtaBins = cms.vdouble( -2.500, -1.479, -0.870, 0.000, 0.870, 1.479, 2.500 ),
    muonPtBins = cms.vdouble(20.0, 27.0, 33.0, 40.0, 47.0,
        54.0, 62.0, 73.0, 86.0, 109.0,
        200.0, 400.0),
    pileUpFileMCTrue = cms.FileInPath('CommonTools/MyTools/data/pileUpFileMC_Fall11.root'),
    electronPtBins = cms.vdouble(20.0, 27.0, 33.0, 40.0, 47.0,
        54.0, 62.0, 73.0, 86.0, 109.0,
        200.0, 400.0),
    electronResolutions = cms.string('TopQuarkAnalysis/TopHitFit/data/resolution/tqafElectronResolution_Summer11.txt'),
    ttGenEvent = cms.InputTag("genEvt"),
    metResolutions = cms.string('TopQuarkAnalysis/TopHitFit/data/resolution/tqafKtResolution_Summer11.txt'),
    muonResolutions = cms.string('TopQuarkAnalysis/TopHitFit/data/resolution/tqafMuonResolution_Summer11.txt'),
    pileUpFileDataTrue = cms.FileInPath('CommonTools/MyTools/data/pileUpFileData_2011truePixel.root'),
    patMuons = cms.InputTag("selectedPatMuonsUnbiasedHitFit"),
    muonEtaBins = cms.vdouble( -2.4, -2.1, -1.3, -0.9, 0.0, 0.9, 1.3, 2.1, 2.4 ),
    bJetPtBins = cms.vdouble(30.0, 40.0, 50.0, 60.0, 70.0,
        80.0, 90.0, 100.0, 120.0, 150.0,
        200.0, 300.0, 500.0),
    metEtaBins = cms.vdouble(),
    ttSemiLeptonicEventMuons = cms.InputTag("ttSemiLepEventHitFitMuons"),
    udscJetResolutions = cms.string('TopQuarkAnalysis/TopHitFit/data/resolution/tqafUdscJetResolution_Summer11.txt')
)


process.analyzeHitFitReference = cms.EDAnalyzer("AnalyzeHitFit",
    patJets = cms.InputTag("referencePatJetsUnbiased"),
    pileUpFileMCObserved = cms.FileInPath('CommonTools/MyTools/data/pileUpFileMC_Fall11inTime.root'),
    patElectrons = cms.InputTag("referencePatElectronsUnbiased"),
    patMETs = cms.InputTag("patMETs"),
    pathPlots = cms.string('/afs/cern.ch/user/v/vadler/cms/Top/CMSSW_5_3_11/output/plots/analyzeHitFit/analyzeHitFit_fromSummer11-coarseEta_Summer12_MadGraph_L3_unambiguousOnly_'),
    metPtBins = cms.vdouble(10.0, 20.0, 29.0, 37.0, 44.0,
        51.0, 59.0, 69.0, 80.0, 96.0,
        122.0, 200.0, 300.0),
    ttSemiLeptonicEventElectrons = cms.InputTag("ttSemiLepEventReferenceElectrons"),
    electronEtaBins = cms.vdouble( -2.500, -1.5660, -1.4442, -0.870, 0.000, 0.870, 1.4442, 1.5660, 2.500 ),
    bJetEtaBins = cms.vdouble( -2.500, -1.479, -0.870, 0.000, 0.870, 1.479, 2.500 ),
    jecLevel = cms.string('L3Absolute'),
    allJets = cms.bool(False),
    pileUpFileDataObserved = cms.FileInPath('CommonTools/MyTools/data/pileUpFileData_2011observedPixel.root'),
    bJetPtBins = cms.vdouble(30.0, 40.0, 50.0, 60.0, 70.0,
        80.0, 90.0, 100.0, 120.0, 150.0,
        200.0, 300.0, 500.0),
    udscJetPtBins = cms.vdouble(30.0, 40.0, 50.0, 60.0, 70.0,
        80.0, 90.0, 100.0, 120.0, 150.0,
        200.0, 300.0, 500.0),
    electronPtBins = cms.vdouble(20.0, 27.0, 33.0, 40.0, 47.0,
        54.0, 62.0, 73.0, 86.0, 109.0,
        200.0, 400.0),
    muonPtBins = cms.vdouble(20.0, 27.0, 33.0, 40.0, 47.0,
        54.0, 62.0, 73.0, 86.0, 109.0,
        200.0, 400.0),
    pileUpFileMCTrue = cms.FileInPath('CommonTools/MyTools/data/pileUpFileMC_Fall11.root'),
    udscJetEtaBins = cms.vdouble( -2.500, -1.479, -0.870, 0.000, 0.870, 1.479, 2.500 ),
    electronResolutions = cms.string('TopQuarkAnalysis/TopHitFit/data/resolution/tqafElectronResolution_Summer11.txt'),
    ttGenEvent = cms.InputTag("genEvt"),
    metResolutions = cms.string('TopQuarkAnalysis/TopHitFit/data/resolution/tqafKtResolution_Summer11.txt'),
    muonResolutions = cms.string('TopQuarkAnalysis/TopHitFit/data/resolution/tqafMuonResolution_Summer11.txt'),
    pileUpFileDataTrue = cms.FileInPath('CommonTools/MyTools/data/pileUpFileData_2011truePixel.root'),
    patMuons = cms.InputTag("referencePatMuonsUnbiased"),
    muonEtaBins = cms.vdouble( -2.4, -2.1, -1.3, -0.9, 0.0, 0.9, 1.3, 2.1, 2.4 ),
    bJetResolutions = cms.string('TopQuarkAnalysis/TopHitFit/data/resolution/tqafBJetResolution_Summer11.txt'),
    metEtaBins = cms.vdouble(),
    ttSemiLeptonicEventMuons = cms.InputTag("ttSemiLepEventReferenceMuons"),
    udscJetResolutions = cms.string('TopQuarkAnalysis/TopHitFit/data/resolution/tqafUdscJetResolution_Summer11.txt')
)


process.makeHypothesis_genMatchMCMatchMuons = cms.Sequence(process.ttSemiLepJetPartonMatchMCMatchMuons+process.ttSemiLepHypGenMatchMCMatchMuons)


process.makeHypothesis_genMatchReferenceElectrons = cms.Sequence(process.ttSemiLepJetPartonMatchReferenceElectrons+process.ttSemiLepHypGenMatchReferenceElectrons)


process.makeTtSemiLepHypothesesReferenceElectrons = cms.Sequence(process.makeHypothesis_genMatchReferenceElectrons)


process.makeHypothesis_genMatchMCMatchElectrons = cms.Sequence(process.ttSemiLepJetPartonMatchMCMatchElectrons+process.ttSemiLepHypGenMatchMCMatchElectrons)


process.makeTtSemiLepHypothesesMCMatchMuons = cms.Sequence(process.makeHypothesis_genMatchMCMatchMuons)


process.makeHypothesis_genMatchHitFitElectrons = cms.Sequence(process.ttSemiLepJetPartonMatchHitFitElectrons+process.ttSemiLepHypGenMatchHitFitElectrons)


process.makeTtSemiLepEventReferenceElectrons = cms.Sequence(process.makeTtSemiLepHypothesesReferenceElectrons+process.ttSemiLepEventReferenceElectrons)


process.makeHypothesis_genMatchHitFitMuons = cms.Sequence(process.ttSemiLepJetPartonMatchHitFitMuons+process.ttSemiLepHypGenMatchHitFitMuons)


process.makeTtSemiLepEventMCMatchMuons = cms.Sequence(process.makeTtSemiLepHypothesesMCMatchMuons+process.ttSemiLepEventMCMatchMuons)


process.makeTtSemiLepHypothesesMCMatchElectrons = cms.Sequence(process.makeHypothesis_genMatchMCMatchElectrons)


process.makeHypothesis_genMatchReferenceMuons = cms.Sequence(process.ttSemiLepJetPartonMatchReferenceMuons+process.ttSemiLepHypGenMatchReferenceMuons)


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
    fileName = cms.string('/afs/cern.ch/user/v/vadler/work/cms/Top/CMSSW_5_3_13/output/analyzeHitFit_fromSummer11-coarseEta_Summer12_MadGraph_Unbiased_L3_unambiguousOnly.root')
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


