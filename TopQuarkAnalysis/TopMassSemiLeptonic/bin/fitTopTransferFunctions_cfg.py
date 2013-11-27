import os
import FWCore.ParameterSet.Config as cms

fitTopTransferFunctions = cms.PSet(
  verbose            = cms.uint32( verbose )
, overwrite          = cms.bool( overwrite )
, fitFunction        = cms.string( fitFunction )
, dependencyFunction = cms.string( dependencyFunction )
)

fitTopTransferFunctions.objects = cms.PSet(
  fitTopTransferFunctions.UdscJet = cms.PSet(
  )
, fitTopTransferFunctions.BJet = cms.PSet(
  )
, fitTopTransferFunctions.Mu = cms.PSet(
  )
, fitTopTransferFunctions.Elec = cms.PSet(
  )
)

fitTopTransferFunctions.io = cms.PSet(
  fullStats  = cms.bool( fullStats )
, inputFile  = cms.string( inputFile )
, refSel     = cms.bool( refSel )
, usePileUp  = cms.bool( usePileUp )
, outputFile = cms.string( outputFile )
)
