#!/bin/sh

# --calcMode
# - true:     expected number of interactions --> PileupSummaryInfo::getTrueNumInteractions()
# - observed: --> PileupSummaryInfo::getPU_NumInteractions() (in-time only)
#
# pileup_latest.txt -> pileup_JSON_DCSONLY_190389-208686_All_2012_pixelcorr.txt
#
# --minBiasXsec (ub)
# - default: 73500
# - 2011:    68000
# - 2012:    69400
#
# --maxPileupBin
# - default: 25
# - 2011:    50 (S6)
# - 2012:    60 (S7,10)
#
# --numPileupBins
# - default: 1000
# - --calcMode true:     can/should be large/default
# - --calcMode observed: as --maxPileupBin (int)

pileupCalc.py -i /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions12/8TeV/Reprocessing/Cert_190456-208686_8TeV_22Jan2013ReReco_Collisions12_JSON.txt --calcMode=true --inputLumiJSON=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions12/8TeV/PileUp/pileup_latest.txt --minBiasXsec=69400 --maxPileupBin=60 --numPileupBins=60 --verbose -o $CMSSW_BASE/src/CommonTools/MyTools/data/pileUpFileData_2012truePixel.root  $CMSSW_BASE/src/CommonTools/MyTools/data/pileUpFileData_2012truePixel.root
