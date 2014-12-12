import FWCore.ParameterSet.Config as cms
fitTopTransferFunctions = cms.PSet(
    verbose = cms.uint32(3),
    useSymm = cms.bool(True),
    refGen = cms.bool(True),
    useAlt = cms.bool(True),
    maxEvents = cms.int32(-1),
    useNonT = cms.bool(True),
    useNonP = cms.bool(True),
    io = cms.PSet(
        overwrite = cms.bool(True),
        plot = cms.bool(True),
        outputFile = cms.string('file:/afs/cern.ch/work/v/vadler/cms/Top/CMSSW_5_3_13/output/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MCatNLO_UnbiasedE_L3_unambiguousOnly_PileUp_1D.root'),
        pathOut = cms.string('/afs/cern.ch/work/v/vadler/cms/Top/CMSSW_5_3_13/src/TopQuarkAnalysis/TopMassSemiLeptonic/data/transfer_fromSummer11-coarseEta'),
        refSel = cms.bool(True),
        writeFiles = cms.bool(True),
        usePileUp = cms.bool(True),
        sample = cms.string('Summer12_MCatNLO_UnbiasedE_L3_unambiguousOnly'),
        pathPlots = cms.string('/afs/cern.ch/work/v/vadler/cms/Top/CMSSW_5_3_13/output/plots/fitTopTransferFunctions/fitTopTransferFunctions_fromSummer11-coarseEta_Summer12_MCatNLO_UnbiasedE_L3_unambiguousOnly_PileUp_Ref_sGauss1D_'),
        formatPlots = cms.vstring('png', 'pdf'),
        pileUp = cms.string('PileUpWeightTrue'),
        fit0D = cms.bool(False),
        fit1D = cms.bool(True),
        fit2D = cms.bool(False),
        histAddEdges = cms.bool(True),
        fitEtaBins = cms.bool(True),
        fullStats = cms.bool(True),
        inputFile = cms.string('file:/afs/cern.ch/work/v/vadler/cms/Top/CMSSW_5_3_13/output/analyzeHitFit_fromSummer11-coarseEta_Summer12_MCatNLO_UnbiasedE_L3_unambiguousOnly.root')
    ),
    objects = cms.PSet(
        Elec = cms.PSet(
            fitRange = cms.double(1.0),
            minPt = cms.double(0.0),
            widthFactor = cms.double(5.0),
            maxEta = cms.double(999999.0),
            fitMaxPt = cms.double(999999.0),
            minEntriesFactor = cms.uint32(5),
            fitEtaBins = cms.bool(True),
            resolutionFunction = cms.string('linear'),
            fitOptions = cms.string('IBRS+'),
            deltaPtMax = cms.double(50.0),
            deltaPtBins = cms.uint32(50),
            exclude = cms.vuint32(0),
            maxDR = cms.double(0.1),
            fitFunction = cms.string('sGauss'),
            dependencyFunction = cms.string('linear')
        )
    )
)
