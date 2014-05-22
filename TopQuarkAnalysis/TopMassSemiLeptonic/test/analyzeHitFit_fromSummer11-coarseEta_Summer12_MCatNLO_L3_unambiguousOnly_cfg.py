import FWCore.ParameterSet.Config as cms

process = cms.Process("USER")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_100_1_C6V.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_101_1_duR.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_102_1_Puj.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_103_1_BGl.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_104_1_tXV.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_105_1_5If.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_106_1_16X.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_107_1_hel.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_108_1_iIs.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_109_1_P5k.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_10_1_NTu.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_110_1_5mS.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_111_1_XXo.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_112_1_UiB.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_113_1_63L.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_114_1_jU9.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_115_1_IxW.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_116_1_SHZ.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_117_1_R8W.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_118_1_iiT.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_119_1_CxN.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_11_1_awx.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_120_1_Mn3.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_121_1_qER.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_122_1_NBB.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_123_1_wAw.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_124_1_xVd.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_125_1_eiE.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_126_1_3y3.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_127_1_NOy.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_128_1_6Om.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_129_1_P9D.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_12_1_Nm2.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_130_1_7Jj.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_131_1_ig6.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_132_1_PlJ.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_133_1_n5d.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_134_1_jDu.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_135_1_VTb.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_136_1_YUa.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_137_1_UEU.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_138_1_vCI.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_139_1_f6h.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_13_1_tkY.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_140_1_ulJ.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_141_1_RpM.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_142_1_XeU.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_143_1_NqH.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_144_1_bia.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_145_1_Z3R.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_146_1_HFR.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_147_1_JCa.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_148_1_zM5.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_149_1_NMs.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_14_1_Dh1.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_150_1_Su7.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_151_1_8NA.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_152_1_E2u.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_153_1_Jhv.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_154_1_DVO.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_155_1_KpH.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_156_1_867.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_157_1_0vy.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_158_1_wFb.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_159_1_A27.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_15_2_uW8.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_160_1_Bq9.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_161_1_FUt.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_162_1_kjr.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_163_1_Exw.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_164_1_lOE.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_165_1_CYH.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_166_1_jej.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_167_1_gF3.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_168_1_bz0.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_169_2_OdN.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_16_1_nYF.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_170_1_yVZ.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_171_2_UqF.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_172_1_UFj.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_173_1_Rqa.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_174_1_Nan.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_175_1_qWH.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_176_1_J8r.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_177_1_zdH.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_178_1_8Ee.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_179_1_JmD.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_17_1_AE2.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_180_1_9xY.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_181_1_lVK.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_182_1_rxP.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_183_1_VJT.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_184_1_KdH.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_185_1_uMO.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_186_1_mze.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_187_1_yOT.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_188_1_Ny3.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_189_1_wAA.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_18_1_rIL.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_190_1_S3y.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_191_1_UJZ.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_192_1_ViW.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_193_1_Ibn.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_194_1_shs.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_195_1_dRI.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_196_1_jRG.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_197_1_86N.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_198_1_PLC.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_199_1_HZy.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_19_1_tTi.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_1_1_3Pu.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_200_1_rDb.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_201_1_hOG.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_202_1_5WN.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_203_1_XaB.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_204_1_QwM.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_205_1_hwX.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_206_1_gNx.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_207_1_HCl.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_208_1_TEk.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_209_1_C6c.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_20_1_9fT.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_210_1_kuq.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_211_1_lr3.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_212_1_LEs.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_213_1_l5j.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_214_1_FRI.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_215_1_ZDn.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_216_1_dE4.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_217_1_a8H.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_218_1_rLt.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_219_1_7yX.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_21_1_8D1.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_220_1_1py.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_221_1_7Gv.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_222_1_BYn.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_223_1_KLI.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_224_1_wMl.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_225_1_CeS.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_226_1_6z7.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_227_1_3fQ.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_228_1_9Rk.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_229_1_eHV.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_22_1_wn8.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_230_1_y4M.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_231_1_LTN.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_232_1_nCV.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_233_1_yag.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_234_1_rfC.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_235_1_T2o.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_236_1_OwW.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_237_1_Jte.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_238_1_6Q6.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_239_1_0EA.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_23_1_MO5.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_240_2_7O9.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_241_1_qTA.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_242_1_JtF.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_243_1_4cb.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_244_1_oRS.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_245_1_2jT.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_246_1_kBo.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_247_1_XRQ.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_248_1_Ji0.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_249_1_Ut5.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_24_1_C7F.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_250_1_Zga.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_251_1_ZOB.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_252_1_iaW.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_253_1_tKD.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_254_1_80P.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_255_1_4oC.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_256_1_kXN.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_257_1_eKm.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_258_2_Kmk.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_259_1_Unr.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_25_1_SbH.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_260_1_S8O.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_261_1_ypL.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_262_1_apa.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_263_1_eNG.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_264_1_RAy.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_265_1_Mxx.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_266_1_C0q.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_267_1_hZm.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_268_1_InM.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_269_1_uO4.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_26_1_Dry.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_270_1_aGh.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_271_1_Grs.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_272_1_Dky.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_273_1_85j.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_274_1_dt8.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_275_1_AGy.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_276_1_irC.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_277_1_fuB.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_278_2_G97.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_279_2_5Ce.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_27_1_9Nd.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_280_1_XXo.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_281_1_E0w.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_282_1_Aol.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_283_1_ZuR.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_284_1_8NR.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_285_1_jqh.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_286_1_ejJ.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_287_1_0do.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_288_1_vOg.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_289_1_5tU.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_28_1_t2B.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_290_1_eXv.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_291_1_jZW.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_292_2_OFy.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_293_1_EQs.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_294_1_0RL.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_295_1_Tm0.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_296_1_XxQ.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_297_1_xzV.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_298_1_YLL.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_299_1_GBf.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_29_1_5Jr.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_2_1_PGq.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_300_1_dBL.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_301_1_VQz.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_302_1_Dm6.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_303_1_REt.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_304_2_wfX.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_305_1_Evs.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_306_1_YIj.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_307_1_Hyp.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_308_1_orw.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_309_1_z5Q.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_30_1_iIS.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_310_1_GrW.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_311_1_thH.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_312_2_kML.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_313_1_u6c.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_314_1_vnD.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_315_1_Cwe.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_316_1_9s9.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_317_2_1Pm.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_318_1_85w.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_319_1_uZx.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_31_1_7sa.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_320_1_OJz.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_321_1_LKa.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_322_1_2KG.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_323_1_eOY.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_324_1_djL.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_325_1_kRN.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_326_1_YMT.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_327_1_6Iv.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_328_1_Aue.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_329_1_zEM.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_32_1_R6t.root')
)
process.source.fileNames.extend(['/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_330_1_71G.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_331_1_vsW.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_332_1_mCj.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_333_1_V6i.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_33_1_vv4.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_34_1_WTs.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_35_1_UfY.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_36_1_jAX.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_37_1_69N.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_38_1_BuQ.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_39_1_Dvz.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_3_1_3F3.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_40_1_2hA.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_41_1_qSl.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_42_1_iSM.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_43_1_mtJ.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_44_1_d3G.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_45_1_56h.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_46_1_9qd.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_47_1_Aic.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_48_1_yHB.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_49_1_Lbd.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_4_1_DlP.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_50_1_WJI.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_51_1_mR5.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_52_1_lt9.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_53_1_Z1z.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_54_1_aoR.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_55_1_zww.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_56_1_x6v.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_57_1_sGj.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_58_1_XmQ.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_59_1_M4Q.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_5_1_wNr.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_60_1_P9d.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_61_1_Uln.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_62_1_2m8.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_63_1_tP9.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_64_1_dHw.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_65_1_buG.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_66_1_275.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_67_1_Miq.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_68_1_qtr.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_69_1_B7r.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_6_1_brL.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_70_1_MRH.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_71_1_3tk.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_72_1_e5p.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_73_1_LtF.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_74_1_Ges.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_75_1_ITG.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_76_1_9pT.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_77_1_q4u.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_78_1_ewL.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_79_1_UNg.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_7_1_sch.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_80_1_vY3.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_81_1_h1i.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_82_1_6Rf.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_83_1_35g.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_84_1_cCV.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_85_1_Ba3.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_86_1_Z06.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_87_1_rca.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_88_1_ZmV.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_89_1_WJe.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_8_1_1yQ.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_90_1_rhs.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_91_1_dLQ.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_92_1_1BI.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_93_1_XXE.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_94_1_cdQ.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_95_1_RkX.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_96_2_1Tc.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_97_1_JlD.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_98_1_My1.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_99_1_Kox.root',
        '/store/user/vadler/cms/Top/CMSSW_5_3_13/data/Summer12_MCatNLO/skimHitFit_9_1_iJN.root'])


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
    pathPlots = cms.string('/afs/cern.ch/user/v/vadler/cms/Top/CMSSW_5_3_11/output/plots/analyzeHitFit/analyzeHitFit_fromSummer11-coarseEta_Summer12_MCatNLO_L3_unambiguousOnly_'),
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
    fileName = cms.string('/afs/cern.ch/user/v/vadler/work/cms/Top/CMSSW_5_3_13/output/analyzeHitFit_fromSummer11-coarseEta_Summer12_MCatNLO_L3_unambiguousOnly.root')
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


