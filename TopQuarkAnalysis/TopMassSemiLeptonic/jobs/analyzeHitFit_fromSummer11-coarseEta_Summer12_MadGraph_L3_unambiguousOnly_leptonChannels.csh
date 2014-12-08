#!/bin/tcsh
cd ~/work/cms/Top/CMSSW_5_3_13/src/
cmsenv
cmsRun ~/work/cms/Top/CMSSW_5_3_13/src/TopQuarkAnalysis/TopMassSemiLeptonic/test/analyzeHitFit_fromSummer11-coarseEta_Summer12_MadGraph_L3_unambiguousOnly_elecChannel_cfg.py >&! ~/work/cms/Top/CMSSW_5_3_13/output/analyzeHitFit_fromSummer11-coarseEta_Summer12_MadGraph_L3_unambiguousOnly_elecChannel.log
cmsRun ~/work/cms/Top/CMSSW_5_3_13/src/TopQuarkAnalysis/TopMassSemiLeptonic/test/analyzeHitFit_fromSummer11-coarseEta_Summer12_MadGraph_L3_unambiguousOnly_muonChannel_cfg.py >&! ~/work/cms/Top/CMSSW_5_3_13/output/analyzeHitFit_fromSummer11-coarseEta_Summer12_MadGraph_L3_unambiguousOnly_muonChannel.log
