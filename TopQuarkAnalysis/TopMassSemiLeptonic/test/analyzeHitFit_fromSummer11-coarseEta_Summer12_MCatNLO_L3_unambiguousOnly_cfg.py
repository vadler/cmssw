import FWCore.ParameterSet.Config as cms

process = cms.Process("USER")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_100_1_xnt.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_101_1_2hI.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_102_1_45p.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_103_1_1yV.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_104_1_4j7.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_105_1_U2h.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_106_2_TZ4.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_107_1_s5j.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_108_1_1iU.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_109_1_eMV.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_10_1_hSG.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_110_1_TlM.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_111_1_7jO.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_112_1_3ff.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_113_1_LbQ.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_114_1_ATK.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_115_1_ZSH.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_116_1_hUO.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_117_1_FDN.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_118_1_sE1.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_119_1_Cq6.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_11_1_SrS.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_120_1_kLE.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_121_1_Iq4.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_122_1_f3W.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_123_1_Spw.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_124_1_T1u.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_125_1_6vE.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_126_1_3AR.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_127_1_3wt.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_128_1_XHe.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_129_1_zng.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_12_1_8S8.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_130_1_sY4.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_131_1_tef.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_132_1_8UA.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_133_1_AQz.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_134_1_5xw.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_135_1_EWf.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_136_1_pjh.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_137_1_evA.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_13_1_n9G.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_14_1_6HU.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_15_1_9qp.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_16_1_u8N.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_17_1_YAx.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_18_1_KlQ.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_19_1_ePj.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_1_1_Row.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_20_1_dZJ.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_21_1_I4t.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_22_1_RjH.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_23_1_BkR.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_24_1_4qU.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_25_1_tQy.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_26_1_CJq.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_27_1_laA.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_28_1_6BE.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_29_1_EJW.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_2_1_mzK.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_30_1_9vu.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_31_1_Hzw.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_32_1_Gzc.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_33_1_nck.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_34_1_ZpB.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_35_1_ihm.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_36_1_g36.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_37_1_lIs.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_38_1_CyR.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_39_1_tOq.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_3_1_jWe.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_40_1_cvg.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_41_1_Ud8.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_42_1_PO8.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_43_1_U94.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_44_1_Rc5.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_45_1_fJR.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_46_1_Rb7.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_47_1_MxL.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_48_1_b1g.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_49_1_s8I.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_4_1_h3N.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_50_1_PUp.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_51_1_wwM.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_52_1_WG2.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_53_1_MuJ.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_54_1_rDV.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_55_1_Y5Y.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_56_1_8QV.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_57_1_7DW.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_58_1_M7r.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_59_1_gCg.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_5_1_5Ji.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_60_1_v4d.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_61_1_o8d.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_62_1_2cA.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_63_1_Fr2.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_64_1_iu3.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_65_1_sgl.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_66_1_2s5.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_67_1_6jQ.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_68_1_qZi.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_69_1_ZAc.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_6_1_QOe.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_70_1_S3A.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_71_1_DWw.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_72_1_5fX.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_73_1_bmO.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_74_1_yN7.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_75_1_TR0.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_76_1_cdV.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_77_1_OnA.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_78_1_erH.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_79_1_C2o.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_7_1_n9c.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_80_1_aUl.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_81_1_kXY.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_82_1_x0w.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_83_1_ypF.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_84_1_khC.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_85_1_Fr2.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_86_1_BkC.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_87_1_ctX.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_88_1_gae.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_89_1_AGt.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_8_1_P52.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_90_1_Ohi.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_91_1_pjk.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_92_1_6Qy.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_93_1_qyl.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_94_1_aP4.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_95_1_Smu.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_96_1_47X.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_97_1_Tpu.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_98_1_qd0.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_99_1_KxG.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_10_patch1/data/Summer12_MCatNLO/skimHitFit_9_1_6Pl.root')
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
    pathPlots = cms.string('/afs/cern.ch/user/v/vadler/cms/Top/CMSSW_5_3_11/output/plots/analyzeHitFit/analyzeHitFit_fromSummer11-coarseEta_Summer12_MCatNLO_L3_unambiguousOnly_'),
    metPtBins = cms.vdouble(10.0, 20.0, 29.0, 37.0, 44.0,
        51.0, 59.0, 69.0, 80.0, 96.0,
        122.0, 200.0, 300.0),
    ttSemiLeptonicEventElectrons = cms.InputTag("ttSemiLepEventHitFitElectrons"),
    electronEtaBins = cms.vdouble( -2.500, -1.5660, -1.4442, -0.870, 0.000, 0.870, 1.4442, 1.5660, 2.500 ),
    bJetEtaBins = cms.vdouble( -2.500, -1.479, -0.870, 0.000, 0.870, 1.479, 2.500 ),
    jecLevel = cms.string('L3Absolute'),
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
    patMuons = cms.InputTag("selectedPatMuonsHitFit"),
    muonEtaBins = cms.vdouble( -2.4, -2.1, -1.3, -0.9, 0.0, 0.9, 1.3, 2.1, 2.4 ),
    bJetPtBins = cms.vdouble(30.0, 40.0, 50.0, 60.0, 70.0,
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
    pathPlots = cms.string('/afs/cern.ch/user/v/vadler/cms/Top/CMSSW_5_3_11/output/plots/analyzeHitFit/analyzeHitFit_fromSummer11-coarseEta_Summer12_MCatNLO_L3_unambiguousOnly_'),
    metPtBins = cms.vdouble(10.0, 20.0, 29.0, 37.0, 44.0,
        51.0, 59.0, 69.0, 80.0, 96.0,
        122.0, 200.0, 300.0),
    ttSemiLeptonicEventElectrons = cms.InputTag("ttSemiLepEventReferenceElectrons"),
    electronEtaBins = cms.vdouble( -2.500, -1.5660, -1.4442, -0.870, 0.000, 0.870, 1.4442, 1.5660, 2.500 ),
    bJetEtaBins = cms.vdouble( -2.500, -1.479, -0.870, 0.000, 0.870, 1.479, 2.500 ),
    jecLevel = cms.string('L3Absolute'),
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
    patMuons = cms.InputTag("referencePatMuons"),
    muonEtaBins = cms.vdouble( -2.4, -2.1, -1.3, -0.9, 0.0, 0.9, 1.3, 2.1, 2.4 ),
    bJetResolutions = cms.string('TopQuarkAnalysis/TopHitFit/data/resolution/tqafBJetResolution_Summer11.txt'),
    metEtaBins = cms.vdouble(),
    ttSemiLeptonicEventMuons = cms.InputTag("ttSemiLepEventReferenceMuons"),
    udscJetResolutions = cms.string('TopQuarkAnalysis/TopHitFit/data/resolution/tqafUdscJetResolution_Summer11.txt')
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
    fileName = cms.string('/afs/cern.ch/user/v/vadler/cms/Top/CMSSW_5_3_11/output/analyzeHitFit_fromSummer11-coarseEta_Summer12_MCatNLO_L3_unambiguousOnly.root')
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


