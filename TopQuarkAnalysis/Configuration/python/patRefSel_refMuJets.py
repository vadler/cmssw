#
# This file contains the Top PAG reference selection for mu + jets analysis.
#

### Muon configuration

# PAT muons
muonsUsePV     = True  # use PV (True) or BS (False)
muonEmbedTrack = True  # embedded track needed for muon ID cuts

### Jet configuration

# Jet algorithm
jetAlgo = 'AK5'

# JEC sets
jecSetBase = jetAlgo


### ------------------------- Reference selection -------------------------- ###


# PF2PAT settings
from TopQuarkAnalysis.Configuration.patRefSel_PF2PAT import *

### Trigger selection

# HLT selection
triggerSelectionData = 'HLT_IsoMu17_eta2p1_TriCentralPFNoPUJet30_30_20_v*'
triggerSelectionMC   = 'HLT_*' # not recommended

### Muon selection

# Minimal selection for PF muons, also basis for signal and veto muons
muonCutPF  =     'pt > 10.'                                                                      # transverse momentum
muonCutPF += ' && abs(eta) < 2.5'                                                                # pseudo-rapisity range

# Minimal selection for all muons, also basis for signal and veto muons
muonCut  =     'isPFMuon'                                                                      # general reconstruction property
muonCut += ' && (isGlobalMuon || isTrackerMuon)'                                               # general reconstruction property
muonCut += ' && pt > 10.'                                                                      # transverse momentum
muonCut += ' && abs(eta) < 2.5'                                                                # pseudo-rapisity range
muonCut += ' && (chargedHadronIso+max(0.,neutralHadronIso+photonIso-0.50*puChargedHadronIso))/pt < 0.2' # relative isolation w/ Delta beta corrections (factor 0.5)

# Signal muon selection on top of 'muonCut'
signalMuonCut  =     'isPFMuon'                                                                       # general reconstruction property
signalMuonCut += ' && isGlobalMuon'                                                                   # general reconstruction property
signalMuonCut += ' && pt > 26.'                                                                       # transverse momentum
signalMuonCut += ' && abs(eta) < 2.1'                                                                 # pseudo-rapisity range
signalMuonCut += ' && globalTrack.normalizedChi2 < 10.'                                               # muon ID: 'isGlobalMuonPromptTight'
signalMuonCut += ' && track.hitPattern.trackerLayersWithMeasurement > 5'                              # muon ID: 'isGlobalMuonPromptTight'
signalMuonCut += ' && globalTrack.hitPattern.numberOfValidMuonHits > 0'                               # muon ID: 'isGlobalMuonPromptTight'
signalMuonCut += ' && abs(dB("PV2D")) < 0.2'                                                          # 2-dim impact parameter with respect to primary vertex
signalMuonCut += ' && innerTrack.hitPattern.numberOfValidPixelHits > 0'                               # tracker reconstruction
signalMuonCut += ' && numberOfMatchedStations > 1'                                                    # muon chamber reconstruction
signalMuonCut += ' && (chargedHadronIso+max(0.,neutralHadronIso+photonIso-0.50*puChargedHadronIso))/pt < 0.12' # relative isolation w/ Delta beta corrections (factor 0.5)

muonVertexMaxDZ = 0.5 # DeltaZ between muon vertex and PV

### Jet selection

# Signal jet selection
jetCut  =     'abs(eta) < 2.5'                                        # pseudo-rapisity range
jetCut += ' && numberOfDaughters > 1'                                 # PF jet ID:
jetCut += ' && neutralHadronEnergyFraction < 0.99'                    # PF jet ID:
jetCut += ' && neutralEmEnergyFraction < 0.99'                        # PF jet ID:
jetCut += ' && (chargedEmEnergyFraction < 0.99 || abs(eta) >= 2.4)'   # PF jet ID:
jetCut += ' && (chargedHadronEnergyFraction > 0. || abs(eta) >= 2.4)' # PF jet ID:
jetCut += ' && (chargedMultiplicity > 0 || abs(eta) >= 2.4)'          # PF jet ID:
# varying jet pt thresholds
veryLooseJetCut = 'pt > 20.' # transverse momentum (all jets)
looseJetCut     = 'pt > 35.' # transverse momentum (3rd jet, optional)
tightJetCut     = 'pt > 45.' # transverse momentum (leading jets)

### Electron selection

# Minimal selection for all electrons, also basis for signal and veto muons
electronCutPF  =     'pt > 20.'                                                                              # transverse energy
electronCutPF += ' && abs(eta) < 2.5'                                                                        # pseudo-rapisity range

# Minimal selection for all electrons, also basis for signal and veto muons
electronCut  =     'pt > 20.'                                                                              # transverse energy
electronCut += ' && abs(eta) < 2.5'                                                                        # pseudo-rapisity range
electronCut += ' && electronID("mvaTrigV0") > 0.'                                                          # MVA electrons ID
#electronCut += ' && (chargedHadronIso+max(0.,neutralHadronIso)+photonIso-0.5*puChargedHadronIso)/et < 0.15' # relative isolation with Delta beta corrections
electronCut += ' && (chargedHadronIso+max(0.,neutralHadronIso+photonIso-1.0*userIsolation("User1Iso")))/et < 0.15' # relative isolation with EA corrections

### ------------------------------------------------------------------------ ###


### Trigger matching

# Trigger object selection
triggerObjectSelectionData = 'type("TriggerMuon") && ( path("HLT_IsoMu17_eta2p1_TriCentralPFNoPUJet30_30_20_v*") )'
triggerObjectSelectionMC   = 'type("TriggerMuon") && ( path("HLT_*") )' # not recommended
