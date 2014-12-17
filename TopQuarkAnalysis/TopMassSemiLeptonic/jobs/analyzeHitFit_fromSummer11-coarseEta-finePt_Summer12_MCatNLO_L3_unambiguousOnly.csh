#!/bin/tcsh
cd ~/work/cms/Top/CMSSW_5_3_13/src/
cmsenv
cmsRun ~/work/cms/Top/CMSSW_5_3_13/src/TopQuarkAnalysis/TopMassSemiLeptonic/test/analyzeHitFit_fromSummer11-coarseEta-finePt_Summer12_MCatNLO_L3_unambiguousOnly_cfg.py >&! ~/work/cms/Top/CMSSW_5_3_13/output/analyzeHitFit_fromSummer11-coarseEta-finePt_Summer12_MCatNLO_L3_unambiguousOnly.log
