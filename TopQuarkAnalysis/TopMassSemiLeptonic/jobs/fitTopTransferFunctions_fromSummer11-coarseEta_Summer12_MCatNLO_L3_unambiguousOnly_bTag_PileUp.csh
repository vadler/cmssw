#!/bin/tcsh
cd ~/work/cms/Top/CMSSW_5_3_13/src/
cmsenv
fitTopTransferFunctions TopQuarkAnalysis/TopMassSemiLeptonic/bin/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MCatNLO_L3_unambiguousOnly_bTag_PileUp_Ref_E_GenSymm_cfg.py >&! ~/work/cms/Top/CMSSW_5_3_13/output/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MCatNLO_L3_unambiguousOnly_bTag_PileUp_Ref_E_GenSymm.log
