// -*- C++ -*-
//
// Package:    TopMassSemiLeptonic
// Class:      AnalyzeHitFit
//
// $Id: AnalyzeHitFit.cc,v 1.1 2011/08/31 14:45:53 vadler Exp $
//
/**
  \class    AnalyzeHitFit AnalyzeHitFit.cc "TopQuarkAnalysis/TopMassSemiLeptonic/plugins/AnalyzeHitFit.cc"
  \brief    Fill histograms and n-tuples for HitFit resolution function determination



  \author   Volker Adler
*/


#include <vector>
#include <map>
#include <string>

#include "TH1D.h"
#include "TTree.h"

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ParameterSet/interface/FileInPath.h"

#include "AnalysisDataFormats/TopObjects/interface/TtSemiLeptonicEvent.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"

#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"


class AnalyzeHitFit : public edm::EDAnalyzer {

  public:

    /// Constructors and Desctructor

    /// Default constructor
    explicit AnalyzeHitFit( const edm::ParameterSet & iConfig );

    /// Destructor
    virtual ~AnalyzeHitFit() {};

    /// Methods

    /// Begin
    virtual void beginJob();

    /// Event loop
    virtual void analyze( const edm::Event & iEvent, const edm::EventSetup & iSetup );

    /// End
    virtual void endJob();

  private:

    /// Data members
    // Pile-up input files
    edm::FileInPath pileUpFileMC_;
    edm::FileInPath pileUpFileDataTrue_;
    edm::FileInPath pileUpFileDataObserved_;
    // Lumi weights
    edm::LumiReWeighting lumiWeightTrue_;
    edm::LumiReWeighting lumiWeightObserved_;

    /// Configuration parameters
    edm::InputTag ttSemiLeptonicEventMuonsTag_;
    edm::InputTag ttSemiLeptonicEventElecsTag_;
    edm::InputTag ttGenEventTag_;
    edm::InputTag patMuonsTag_;
    edm::InputTag patElecsTag_;
    edm::InputTag patJetsTag_;
    edm::InputTag patMETsTag_;
    std::string jecLevel_;
    bool        allJets_;
    std::string pathPlots_;
    bool        plot_;
    // Eta binning
    std::vector< std::vector< double > > etaBins_;
    std::vector< std::vector< double > > etaSymmBins_;
    // P_t binning
    std::vector< std::vector< double > > ptBins_;
    std::vector< std::vector< std::vector< double > > > ptBinsVector_;
    std::vector< bool > useBinVector_;
    double minBTag_;
    unsigned minBTags_;

    /// Constants
    // Object categories
    std::vector< std::string > objCats_;
    // Kinematic properties
    std::vector< std::string > kinProps_;

    /// Data
    unsigned filledEvents_;
    std::vector< TTree * > catData_; // data per object category
    // pile-up
    Float_t  nPVTrue_;               // mean number of primery vertices' distribution
    Int_t    nPVObserved_;           // observed number of primery vertices
    Double_t pileUpWeightTrue_;      // MC weight for true pile-up
    Double_t pileUpWeightObserved_;  // MC weight for observed pile-up
    // reconstructed
    Double_t pt_;
    Double_t eta_;
    Double_t phi_;
    Double_t energy_;
    Int_t    binEta_;                // eta bin number as determined by 'getEtaBin'
    Int_t    binEtaSymm_;            // symmetrised eta bin number as determined by 'getEtaBin'
    // reconstructed alternative
    Double_t ptAlt_;
    Double_t etaAlt_;
    Double_t phiAlt_;
    Double_t energyAlt_;
    Int_t    binEtaAlt_;             // eta bin number as determined by 'getEtaBin'
    Int_t    binEtaSymmAlt_;         // symmetrised eta bin number as determined by 'getEtaBin'
    // recostructed from generated
    Double_t ptGenJet_;
    Double_t etaGenJet_;
    Double_t phiGenJet_;
    Double_t energyGenJet_;
    Int_t    binEtaGenJet_;          // eta bin number as determined by 'getEtaBin'
    Int_t    binEtaSymmGenJet_;      // symmetrised eta bin number as determined by 'getEtaBin'
    // recostructed alternative from generated
    Double_t ptGenJetAlt_;
    Double_t etaGenJetAlt_;
    Double_t phiGenJetAlt_;
    Double_t energyGenJetAlt_;
    Int_t    binEtaGenJetAlt_;       // eta bin number as determined by 'getEtaBin'
    Int_t    binEtaSymmGenJetAlt_;   // symmetrised eta bin number as determined by 'getEtaBin'
    // generated
    Double_t ptGen_;
    Double_t etaGen_;
    Double_t phiGen_;
    Double_t energyGen_;
    Int_t    binEtaGen_;             // eta bin number as determined by 'getEtaBin'
    Int_t    binEtaSymmGen_;         // symmetrised eta bin number as determined by 'getEtaBin'
    // additional
    Double_t tagCSV_;                // CSV b-tag discriminator value

    /// Private functions

    unsigned getEtaBin( unsigned iCat, double eta, bool symm = false );

    // Fill n-tuples
    void fill( unsigned iCat, const edm::Handle< TtSemiLeptonicEvent > & ttSemiLeptonicEvent, edm::Handle< pat::MuonCollection > & patMuons, edm::Handle< pat::ElectronCollection > & patElecs, edm::Handle< pat::JetCollection > & patJets, edm::Handle< pat::METCollection > & patMETs, edm::Handle< std::vector< PileupSummaryInfo > > & pileUp, edm::Handle< TtGenEvent > & ttGenEvent, bool repeat = false, bool allJets = false );

};


#include <cassert>
#include <iostream>
#include <sstream>

#include "boost/lexical_cast.hpp"
#include "boost/algorithm/string/replace.hpp"
#include <boost/shared_ptr.hpp>

#include <TROOT.h>
#include <TSystem.h>
#include "TStyle.h"
#include "TCanvas.h"

#include "Math/GenVector/VectorUtil.h"

#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "AnalysisDataFormats/TopObjects/interface/TtSemiLepEvtPartons.h"
#include "TopQuarkAnalysis/TopHitFit/interface/EtaDepResolution.h"

#include "CommonTools/MyTools/interface/RootTools.h"


// Default constructor
AnalyzeHitFit::AnalyzeHitFit( const edm::ParameterSet & iConfig )
: pileUpFileMC_( iConfig.getParameter< edm::FileInPath >( "pileUpFileMC" ) )
, pileUpFileDataTrue_( iConfig.getParameter< edm::FileInPath >( "pileUpFileDataTrue" ) )
, pileUpFileDataObserved_( iConfig.getParameter< edm::FileInPath >( "pileUpFileDataObserved" ) )
, ttSemiLeptonicEventMuonsTag_( iConfig.getParameter< edm::InputTag >( "ttSemiLeptonicEventMuons" ) )
, ttSemiLeptonicEventElecsTag_( iConfig.getParameter< edm::InputTag >( "ttSemiLeptonicEventElectrons" ) )
, ttGenEventTag_( iConfig.getParameter< edm::InputTag >( "ttGenEvent" ) )
, patMuonsTag_( iConfig.getParameter< edm::InputTag >( "patMuons" ) )
, patElecsTag_( iConfig.getParameter< edm::InputTag >( "patElectrons" ) )
, patJetsTag_( iConfig.getParameter< edm::InputTag >( "patJets" ) )
, patMETsTag_( iConfig.getParameter< edm::InputTag >( "patMETs" ) )
, jecLevel_( iConfig.getParameter< std::string >( "jecLevel" ) )
, allJets_( iConfig.getParameter< bool >( "allJets" ) )
, pathPlots_( iConfig.getParameter< std::string >( "pathPlots" ) )
, plot_( ! pathPlots_.empty() )
, minBTag_( 0. )
, minBTags_( 0 )
, filledEvents_( 0 )
{

  if ( iConfig.existsAs< double >( "minBTag" ) )    minBTag_  = iConfig.getParameter< double >( "minBTag" );
  if ( iConfig.existsAs< unsigned >( "minBTags" ) ) minBTags_ = iConfig.getParameter< unsigned >( "minBTags" );

  lumiWeightTrue_     = edm::LumiReWeighting( pileUpFileMC_.fullPath(), pileUpFileDataTrue_.fullPath()    , "pileup", "pileup" );
  lumiWeightObserved_ = edm::LumiReWeighting( pileUpFileMC_.fullPath(), pileUpFileDataObserved_.fullPath(), "pileup", "pileup" );

  // Constants

  objCats_.clear();
  objCats_.push_back( "Mu" );
  objCats_.push_back( "Elec" );
  objCats_.push_back( "UdscJet" );
  objCats_.push_back( "BJet" );
  if ( allJets_ ) objCats_.push_back( "Jet" );
  objCats_.push_back( "MET" );

  catData_.reserve( objCats_.size() );

  std::vector< std::string > objNames;
  objNames.push_back( "muon" );
  objNames.push_back( "electron" );
  objNames.push_back( "udscJet" );
  objNames.push_back( "bJet" );
  if ( allJets_ ) objNames.push_back( "jet" );
  objNames.push_back( "met" );

  kinProps_.clear();
  kinProps_.push_back( "Pt" );
  kinProps_.push_back( "Eta" );
  kinProps_.push_back( "Phi" );

  std::vector< std::string > fileNameParams;
  std::vector< std::string > etaBinParams;
  std::vector< std::string > ptBinParams;
  for ( unsigned iObj = 0; iObj < objNames.size(); ++iObj ) {
    fileNameParams.push_back( objNames.at( iObj ) + "Resolutions" );
    etaBinParams.push_back( objNames.at( iObj ) + "EtaBins" );
    ptBinParams.push_back( objNames.at( iObj ) + "PtBins" );
  }

  for ( unsigned iCat = 0; iCat < objCats_.size(); ++iCat ) {

    if ( iConfig.getParameter< std::vector< double > >( etaBinParams.at( iCat ) ).size() == 0 ) {
      std::vector< double > etaBins;
      if ( objCats_.at( iCat ) == "MET" ) {
        etaBins.push_back( -999. );
        etaBins.push_back(  999. );
      }
      else {
        hitfit::EtaDepResolution hitFitRes( edm::FileInPath( iConfig.getParameter< std::string >( fileNameParams.at( iCat ) ) ).fullPath() );
        for ( unsigned iEta = 0; iEta < hitFitRes.GetEtaDepResElement().size(); ++iEta ) {
          etaBins.push_back( hitFitRes.GetEtaDepResElement().at( iEta ).EtaMin() );
        }
        etaBins.push_back( hitFitRes.GetEtaDepResElement().back().EtaMax() );
      }
      etaBins_.push_back( etaBins );
    }
    else {
      etaBins_.push_back( iConfig.getParameter< std::vector< double > >( etaBinParams.at( iCat ) ) );
    }

    std::vector< double > etaSymmBins;
    for ( unsigned iEta = 0; iEta < etaBins_.back().size() - 1; ++iEta ) {
      if ( etaBins_.back().at( iEta + 1 ) <= 0. ) continue;
      if ( etaBins_.back().at( iEta ) < 0. )
        etaSymmBins.push_back( 0. );
      else
        etaSymmBins.push_back( etaBins_.back().at( iEta ) );
    }
    if ( etaBins_.back().size() > 0 && etaBins_.back().back() > 0. ) {
      etaSymmBins.push_back( etaBins_.back().back() );
    }
    etaSymmBins_.push_back( etaSymmBins );

    if ( iConfig.existsAs< std::vector< double > >( ptBinParams.at( iCat ) ) ) {
      useBinVector_.push_back( false );
      ptBins_.push_back( iConfig.getParameter< std::vector< double > >( ptBinParams.at( iCat ) ) );
      std::vector< std::vector< double > > emptyBins;
      ptBinsVector_.push_back( emptyBins );
    }
    else if ( iConfig.existsAs< std::vector< edm::ParameterSet > >( ptBinParams.at( iCat ) ) ) {
      useBinVector_.push_back( true );
      std::vector< edm::ParameterSet > ptBinsVPSet( iConfig.getParameter< std::vector< edm::ParameterSet > >( ptBinParams.at( iCat ) ) );
      std::vector< std::vector< double > > ptBins;
      for ( unsigned iPSet = 0; iPSet < ptBinsVPSet.size(); ++iPSet ) {
        ptBins.push_back( ptBinsVPSet.at( iPSet ).getParameter< std::vector< double > >( "bins" ) );
      }
      ptBinsVector_.push_back( ptBins );
      std::vector< double > emptyBins;
      ptBins_.push_back( emptyBins );
    }

  }

  // Logging output
  std::stringstream sstrEta;
  std::stringstream sstrPt;
  for ( unsigned iCat = 0; iCat < objCats_.size(); ++iCat ) {
    if ( etaBins_.at( iCat ).size() < 2 )
      edm::LogError( "AnalyzeHitFit" ) << objCats_.at( iCat ) << ": less than 2 eta bin bounderies found";
    sstrEta << "  " << objCats_.at( iCat ) << ": ";
    for ( unsigned iEta = 0; iEta < etaBins_.at( iCat ).size() - 1; ++iEta ) {
      sstrEta << etaBins_.at( iCat ).at( iEta ) << ", ";
    }
    sstrEta << etaBins_.at( iCat ).back() << std::endl;
    std::string cat( objCats_.at( iCat ) );
    sstrPt << "  " << cat << ": ";
    if ( useBinVector_.at( iCat ) ) {
      assert( ptBinsVector_.at( iCat ).size() - etaBins_.at( iCat ).size() );
      for ( unsigned iEta = 0; iEta < ptBinsVector_.at( iCat ).size(); ++iEta )  {
        if ( ptBinsVector_.at( iCat ).at( iEta ).size() < 2 ) {
          edm::LogError( "AnalyzeHitFit" ) << objCats_.at( iCat ) << ": less than 2 p_t bin bounderies found in eta bin " << iEta;
        }
        for ( unsigned iPt = 0; iPt < ptBinsVector_.at( iCat ).at( iEta ).size() - 1; ++iPt ) {
          sstrPt <<  ptBinsVector_.at( iCat ).at( iEta ).at( iPt ) << ", ";
        }
        sstrPt << ptBinsVector_.at( iCat ).at( iEta ).back() << std::endl;
      }
    }
    else {
      if ( ptBins_.at( iCat ).size() < 2 )
        edm::LogError( "AnalyzeHitFit" ) << objCats_.at( iCat ) << ": less than 2 p_t bin bounderies found";
      for ( unsigned iPt = 0; iPt < ptBins_.at( iCat ).size() - 1; ++iPt ) {
        sstrPt << ptBins_.at( iCat ).at( iPt ) << ", ";
      }
      sstrPt << ptBins_.at( iCat ).back() << std::endl;
    }
  }
  edm::LogInfo( "AnalyzeHitFit" ) << "Eta binning\n" << sstrEta.str();
  edm::LogInfo( "AnalyzeHitFit" ) << "Pt binning\n" << sstrPt.str();

}


// Begin job
void AnalyzeHitFit::beginJob()
{

  boost::shared_ptr< TFile > fileMC_( new TFile( pileUpFileMC_.fullPath().c_str() ) );
  boost::shared_ptr< TH1 >   histoMC_( ( static_cast< TH1 * >( fileMC_->Get( "pileup" )->Clone() ) ) );
  const int nBinsMC( histoMC_->GetNbinsX() );

  edm::Service< TFileService > fileService;

  TH1D * histo_pileUpWeightTrue_ = fileService->make< TH1D >( "PileUpWeightTrue", "True pile-up weights", nBinsMC, 0., double( nBinsMC ) );
  histo_pileUpWeightTrue_->SetXTitle( "true number of interactions" );
  histo_pileUpWeightTrue_->SetYTitle( "weight #left(#frac{data_{true}}{MC}#right)" );
  for ( int iBin = 1; iBin < nBinsMC + 1; ++iBin ) {
    histo_pileUpWeightTrue_->Fill( iBin, lumiWeightTrue_.weight( iBin ) );
  }
  histo_pileUpWeightTrue_->Write();
  TH1D * histo_pileUpWeightObserved_ = fileService->make< TH1D >( "PileUpWeightObserved", "Observed pile-up weights", nBinsMC, 0., double( nBinsMC ) );
  histo_pileUpWeightObserved_->SetXTitle( "true number of interactions" );
  histo_pileUpWeightObserved_->SetYTitle( "weight #left(#frac{data_{observed}}{MC}#right)" );
  for ( int iBin = 1; iBin < nBinsMC + 1; ++iBin ) {
    histo_pileUpWeightObserved_->Fill( iBin, lumiWeightObserved_.weight( iBin ) );
  }
  histo_pileUpWeightObserved_->Write();
  if ( plot_ ) {
    my::setPlotEnvironment( gStyle );
    TCanvas c1( "c1" );
    c1.cd();
    histo_pileUpWeightTrue_->Draw();
    c1.Print( std::string( pathPlots_ + histo_pileUpWeightTrue_->GetName() + ".png" ).c_str() );
    histo_pileUpWeightObserved_->Draw();
    c1.Print( std::string( pathPlots_ + histo_pileUpWeightObserved_->GetName() + ".png" ).c_str() );
  }
  delete histo_pileUpWeightTrue_;
  delete histo_pileUpWeightObserved_;

  for ( unsigned iCat = 0; iCat < objCats_.size(); ++iCat ) {
    const std::string cat( objCats_.at( iCat ) );
    TFileDirectory dir( fileService->mkdir( cat.c_str(), "" ) );

    // Eta binning
    TH1D * histo_EtaBins_ = dir.make< TH1D >( std::string( cat + "_binsEta" ).c_str(), cat.c_str(), etaBins_.at( iCat ).size() - 1, etaBins_.at( iCat ).data() );
    histo_EtaBins_->SetXTitle( "#eta" );
    histo_EtaBins_->SetYTitle( "bin" );
    histo_EtaBins_->GetYaxis()->SetRangeUser( -1., etaBins_.at( iCat ).size() );
    for ( unsigned iEta = 0; iEta < etaBins_.at( iCat ).size() - 1; ++iEta ) {
      histo_EtaBins_->Fill( ( etaBins_.at( iCat ).at( iEta ) + etaBins_.at( iCat ).at( iEta + 1 ) ) / 2., iEta ); // fill bin with mean
    }
    histo_EtaBins_->Write();
    if ( plot_ ) {
      my::setPlotEnvironment( gStyle );
      TCanvas c1( "c1" );
      c1.cd();
      histo_EtaBins_->Draw();
      c1.Print( std::string( pathPlots_ + histo_EtaBins_->GetName() + ".png" ).c_str() );
    }
    delete histo_EtaBins_;

    // Pt binning
    if ( useBinVector_.at( iCat ) ) {
      for ( unsigned iEta = 0; iEta < ptBinsVector_.at( iCat ).size(); ++iEta ) {
        const std::string eta( "Eta" + boost::lexical_cast< std::string >( iEta ) );
        TH1D * histo_PtBins_ = dir.make< TH1D >( std::string( cat + "_binsPt_" + eta ).c_str(), cat.c_str(), ptBinsVector_.at( iCat ).at( iEta ).size() - 1, ptBinsVector_.at( iCat ).at( iEta ).data() );
        histo_PtBins_->SetXTitle( "p_{t} (GeV)" );
        histo_PtBins_->SetYTitle( "bin" );
        histo_PtBins_->GetYaxis()->SetRangeUser( -1.,  ptBinsVector_.at( iCat ).at( iEta ).size() );
        for ( unsigned iPt = 0; iPt < ptBinsVector_.at( iCat ).at( iEta ).size() - 1; ++iPt ) {
          histo_PtBins_->Fill( ( ptBinsVector_.at( iCat ).at( iEta ).at( iPt ) + ptBinsVector_.at( iCat ).at( iEta ).at( iPt + 1 ) ) / 2., iPt ); // fill bin with mean
        }
        histo_PtBins_->Write();
        if ( plot_ ) {
          my::setPlotEnvironment( gStyle );
          TCanvas c1( "c1" );
          c1.cd();
          histo_PtBins_->Draw();
          c1.Print( std::string( pathPlots_ + histo_PtBins_->GetName() + ".png" ).c_str() );
        }
        delete histo_PtBins_;
      }
    }
    else {
      TH1D * histo_PtBins_ = dir.make< TH1D >( std::string( cat + "_binsPt" ).c_str(), cat.c_str(), ptBins_.at( iCat ).size() - 1, ptBins_.at( iCat ).data() );
      histo_PtBins_->SetXTitle( "p_{t} (GeV)" );
      histo_PtBins_->SetYTitle( "bin" );
      histo_PtBins_->GetYaxis()->SetRangeUser( -1., ptBins_.at( iCat ).size() );
      for ( unsigned iPt = 0; iPt < ptBins_.at( iCat ).size() - 1; ++iPt ) {
        histo_PtBins_->Fill( ( ptBins_.at( iCat ).at( iPt ) + ptBins_.at( iCat ).at( iPt + 1 ) ) / 2., iPt ); // fill bin with mean
      }
      histo_PtBins_->Write();
      if ( plot_ ) {
        my::setPlotEnvironment( gStyle );
        TCanvas c1( "c1" );
        c1.cd();
        histo_PtBins_->Draw();
        c1.Print( std::string( pathPlots_ + histo_PtBins_->GetName() + ".png" ).c_str() );
      }
      delete histo_PtBins_;
    }

    // N-tuple
    catData_.push_back( dir.make< TTree >( std::string( cat + "_data" ).c_str(), std::string( cat + " data" ).c_str() ) );
    catData_.back()->Branch( "NPVTrue"             , &nPVTrue_             , "nPVTrue/F" );
    catData_.back()->Branch( "NPVObserved"         , &nPVObserved_         , "nPVObserved/I" );
    catData_.back()->Branch( "PileUpWeightTrue"    , &pileUpWeightTrue_    , "pileUpWeightTrue/D" );
    catData_.back()->Branch( "PileUpWeightObserved", &pileUpWeightObserved_, "pileUpWeightObserved/D" );
    catData_.back()->Branch( "Pt"        , &pt_        , "pt/D" );
    catData_.back()->Branch( "Eta"       , &eta_       , "eta/D" );
    catData_.back()->Branch( "Phi"       , &phi_       , "phi/D" );
    catData_.back()->Branch( "Energy"    , &energy_    , "energy/D" );
    catData_.back()->Branch( "BinEta"    , &binEta_    , "binEta/I" );
    catData_.back()->Branch( "BinEtaSymm", &binEtaSymm_, "binEtaSymm/I" );
    catData_.back()->Branch( "PtAlt"        , &ptAlt_        , "ptAlt/D" );
    catData_.back()->Branch( "EtaAlt"       , &etaAlt_       , "etaAlt/D" );
    catData_.back()->Branch( "PhiAlt"       , &phiAlt_       , "phiAlt/D" );
    catData_.back()->Branch( "EnergyAlt"    , &energyAlt_    , "energyAlt/D" );
    catData_.back()->Branch( "BinEtaAlt"    , &binEtaAlt_    , "binEtaAlt/I" );
    catData_.back()->Branch( "BinEtaSymmAlt", &binEtaSymmAlt_, "binEtaSymmAlt/I" );
    if ( cat == "UdscJet" || cat == "BJet" ) {
      catData_.back()->Branch( "PtGenJet"        , &ptGenJet_        , "ptGenJet/D" );
      catData_.back()->Branch( "EtaGenJet"       , &etaGenJet_       , "etaGenJet/D" );
      catData_.back()->Branch( "PhiGenJet"       , &phiGenJet_       , "phiGenJet/D" );
      catData_.back()->Branch( "EnergyGenJet"    , &energyGenJet_    , "energyGenJet/D" );
      catData_.back()->Branch( "BinEtaGenJet"    , &binEtaGenJet_    , "binEtaGenJet/I" );
      catData_.back()->Branch( "BinEtaSymmGenJet", &binEtaSymmGenJet_, "binEtaSymmGenJet/I" );
      catData_.back()->Branch( "PtGenJetAlt"        , &ptGenJetAlt_        , "ptGenJetAlt/D" );
      catData_.back()->Branch( "EtaGenJetAlt"       , &etaGenJetAlt_       , "etaGenJetAlt/D" );
      catData_.back()->Branch( "PhiGenJetAlt"       , &phiGenJetAlt_       , "phiGenJetAlt/D" );
      catData_.back()->Branch( "EnergyGenJetAlt"    , &energyGenJetAlt_    , "energyGenJetAlt/D" );
      catData_.back()->Branch( "BinEtaGenJetAlt"    , &binEtaGenJetAlt_    , "binEtaGenJetAlt/I" );
      catData_.back()->Branch( "BinEtaSymmGenJetAlt", &binEtaSymmGenJetAlt_, "binEtaSymmGenJetAlt/I" );
    }
    catData_.back()->Branch( "PtGen"        , &ptGen_        , "ptGen/D" );
    catData_.back()->Branch( "EtaGen"       , &etaGen_       , "etaGen/D" );
    catData_.back()->Branch( "PhiGen"       , &phiGen_       , "phiGen/D" );
    catData_.back()->Branch( "EnergyGen"    , &energyGen_    , "energyGen/D" );
    catData_.back()->Branch( "BinEtaGen"    , &binEtaGen_    , "binEtaGen/I" );
    catData_.back()->Branch( "BinEtaSymmGen", &binEtaSymmGen_, "binEtaSymmGen/I" );
    if ( cat == "UdscJet" || cat == "BJet" ) {
      catData_.back()->Branch( "TagCSV", &tagCSV_, "tagCSV/D" );
    }

    for ( unsigned iProp = 0; iProp < kinProps_.size(); ++iProp ) {
      const std::string prop( kinProps_.at( iProp ) );
      TFileDirectory subDir( dir.mkdir( prop.c_str(), "" ) );

      TFileDirectory subDirReco( subDir.mkdir( "Reco", "" ) );
      TFileDirectory subDirRecoInv( subDir.mkdir( "RecoInv", "" ) );
      TFileDirectory subDirAlt( subDir.mkdir( "Alt", "" ) );
      TFileDirectory subDirAltInv( subDir.mkdir( "AltInv", "" ) );
      TFileDirectory subDirGen( subDir.mkdir( "Gen", "" ) );
      TFileDirectory subDirGenInv( subDir.mkdir( "GenInv", "" ) );
      TFileDirectory subDirAltGen( subDir.mkdir( "AltGen", "" ) );
      TFileDirectory subDirAltGenInv( subDir.mkdir( "AltGenInv", "" ) );
      for ( unsigned iEta = 0; iEta < etaBins_.at( iCat ).size() - 1; ++iEta ) {
        const std::string eta( "Eta" + boost::lexical_cast< std::string >( iEta ) );
        const std::string title( cat + ", " + boost::lexical_cast< std::string >( etaBins_.at( iCat ).at( iEta ) ) + " #leq #eta #leq " + boost::lexical_cast< std::string >( etaBins_.at( iCat ).at( iEta + 1 ) ) );
        TFileDirectory subDirRecoEta( subDirReco.mkdir( eta.c_str(), title.c_str() ) );
        subDirRecoEta.mkdir( std::string( "Reco_" + eta ).c_str(), "" );
        TFileDirectory subDirRecoInvEta( subDirRecoInv.mkdir( eta.c_str(), title.c_str() ) );
        subDirRecoInvEta.mkdir( std::string( "RecoInv_" + eta ).c_str(), "" );
        TFileDirectory subDirAltEta( subDirAlt.mkdir( eta.c_str(), title.c_str() ) );
        subDirAltEta.mkdir( std::string( "Alt_" + eta ).c_str(), "" );
        TFileDirectory subDirAltInvEta( subDirAltInv.mkdir( eta.c_str(), title.c_str() ) );
        subDirAltInvEta.mkdir( std::string( "AltInv_" + eta ).c_str(), "" );
        TFileDirectory subDirGenEta( subDirGen.mkdir( eta.c_str(), title.c_str() ) );
        subDirGenEta.mkdir( std::string( "Gen_" + eta ).c_str(), "" );
        TFileDirectory subDirGenInvEta( subDirGenInv.mkdir( eta.c_str(), title.c_str() ) );
        subDirGenInvEta.mkdir( std::string( "GenInv_" + eta ).c_str(), "" );
        TFileDirectory subDirAltGenEta( subDirAltGen.mkdir( eta.c_str(), title.c_str() ) );
        subDirAltGenEta.mkdir( std::string( "AltGen_" + eta ).c_str(), "" );
        TFileDirectory subDirAltGenInvEta( subDirAltGenInv.mkdir( eta.c_str(), title.c_str() ) );
        subDirAltGenInvEta.mkdir( std::string( "AltGenInv_" + eta ).c_str(), "" );
      }

      TFileDirectory subDirRecoSymm( subDir.mkdir( "RecoSymm", "" ) );
      TFileDirectory subDirRecoInvSymm( subDir.mkdir( "RecoInvSymm", "" ) );
      TFileDirectory subDirAltSymm( subDir.mkdir( "AltSymm", "" ) );
      TFileDirectory subDirAltInvSymm( subDir.mkdir( "AltInvSymm", "" ) );
      TFileDirectory subDirGenSymm( subDir.mkdir( "GenSymm", "" ) );
      TFileDirectory subDirGenInvSymm( subDir.mkdir( "GenInvSymm", "" ) );
      TFileDirectory subDirAltGenSymm( subDir.mkdir( "AltGenSymm", "" ) );
      TFileDirectory subDirAltGenInvSymm( subDir.mkdir( "AltGenInvSymm", "" ) );
      for ( unsigned iEtaSymm = 0; iEtaSymm < etaSymmBins_.at( iCat ).size() - 1; ++iEtaSymm ) {
        const std::string etaSymm( "Eta" + boost::lexical_cast< std::string >( iEtaSymm ) );
        const std::string title( cat + ", " + boost::lexical_cast< std::string >( etaSymmBins_.at( iCat ).at( iEtaSymm ) ) + " #leq |#eta| #leq " + boost::lexical_cast< std::string >( etaSymmBins_.at( iCat ).at( iEtaSymm + 1 ) ) );
        TFileDirectory subDirRecoSymmEta( subDirRecoSymm.mkdir( etaSymm.c_str(), title.c_str() ) );
        subDirRecoSymmEta.mkdir( std::string( "RecoSymm_" + etaSymm ).c_str(), "" );
        TFileDirectory subDirRecoInvSymmEta( subDirRecoInvSymm.mkdir( etaSymm.c_str(), title.c_str() ) );
        subDirRecoInvSymmEta.mkdir( std::string( "RecoInvSymm_" + etaSymm ).c_str(), "" );
        TFileDirectory subDirAltSymmEta( subDirAltSymm.mkdir( etaSymm.c_str(), title.c_str() ) );
        subDirAltSymmEta.mkdir( std::string( "AltSymm_" + etaSymm ).c_str(), "" );
        TFileDirectory subDirAltInvSymmEta( subDirAltInvSymm.mkdir( etaSymm.c_str(), title.c_str() ) );
        subDirAltInvSymmEta.mkdir( std::string( "AltInvSymm_" + etaSymm ).c_str(), "" );
        TFileDirectory subDirGenSymmEta( subDirGenSymm.mkdir( etaSymm.c_str(), title.c_str() ) );
        subDirGenSymmEta.mkdir( std::string( "GenSymm_" + etaSymm ).c_str(), "" );
        TFileDirectory subDirGenInvSymmEta( subDirGenInvSymm.mkdir( etaSymm.c_str(), title.c_str() ) );
        subDirGenInvSymmEta.mkdir( std::string( "GenInvSymm_" + etaSymm ).c_str(), "" );
        TFileDirectory subDirAltGenSymmEta( subDirAltGenSymm.mkdir( etaSymm.c_str(), title.c_str() ) );
        subDirAltGenSymmEta.mkdir( std::string( "AltGenSymm_" + etaSymm ).c_str(), "" );
        TFileDirectory subDirAltGenInvSymmEta( subDirAltGenInvSymm.mkdir( etaSymm.c_str(), title.c_str() ) );
        subDirAltGenInvSymmEta.mkdir( std::string( "AltGenInvSymm_" + etaSymm ).c_str(), "" );
      }

    }

  }

}


// Event loop
void AnalyzeHitFit::analyze( const edm::Event & iEvent, const edm::EventSetup & iSetup )
{

  // MC
  if ( iEvent.isRealData() ) return;

  // PAT objects
  edm::Handle< pat::MuonCollection > patMuons;
  iEvent.getByLabel( patMuonsTag_, patMuons );
  edm::Handle< pat::ElectronCollection > patElecs;
  iEvent.getByLabel( patElecsTag_, patElecs );
  edm::Handle< pat::JetCollection > patJets;
  iEvent.getByLabel( patJetsTag_, patJets );
  edm::Handle< pat::METCollection > patMETs;
  iEvent.getByLabel( patMETsTag_, patMETs );

  // b-tag requirement
  unsigned btags( 0 );
  for ( size_t iJet = 0; iJet < patJets->size(); ++iJet ) {
    if ( patJets->at( iJet ).bDiscriminator( "combinedSecondaryVertexBJetTags" ) > minBTag_ ) ++btags;
  }
  if ( btags < minBTags_ ) {
    edm::LogInfo( "AnalyzeHitFit" ) << "...fail b-tag requirement";
    return;
  }

  // TQAF MC event
  edm::Handle< TtGenEvent > ttGenEvent;
  iEvent.getByLabel( ttGenEventTag_, ttGenEvent );

  // Semi-leptonic signal event
  if ( ! (ttGenEvent->isTtBar() && ( ttGenEvent->isSemiLeptonic( WDecay::kMuon ) || ttGenEvent->isSemiLeptonic( WDecay::kElec ) ) ) ) {
    edm::LogInfo( "AnalyzeHitFit" ) << "...no signal event";
    return;
  } // Semi-leptonic signal event

  // TQAF semi-leptonic events
  edm::Handle< TtSemiLeptonicEvent > ttSemiLeptonicEventMuons;
  iEvent.getByLabel( ttSemiLeptonicEventMuonsTag_, ttSemiLeptonicEventMuons );
  edm::Handle< TtSemiLeptonicEvent > ttSemiLeptonicEventElecs;
  iEvent.getByLabel( ttSemiLeptonicEventElecsTag_, ttSemiLeptonicEventElecs );

    // Valid full TTbar MC matching
  if ( ! ( ( ttSemiLeptonicEventMuons.isValid() && ttSemiLeptonicEventMuons->isHypoValid( TtEvent::kGenMatch ) ) || ( ttSemiLeptonicEventElecs.isValid() && ttSemiLeptonicEventElecs->isHypoValid( TtEvent::kGenMatch ) ) ) ) {
    edm::LogInfo( "AnalyzeHitFit" ) << "...no valid MC match";
    return;
  } // Valid full TTbar MC matching

  // Pile-up
  edm::Handle< std::vector< PileupSummaryInfo > > pileUp;
  iEvent.getByLabel( "addPileupInfo", pileUp );

  for ( unsigned iCat = 0; iCat < objCats_.size(); ++iCat ) {
    const std::string cat( objCats_.at( iCat ) );
    // Initialise variables
    nPVTrue_              = -1.;
    nPVObserved_          = -1;
    pileUpWeightTrue_     =  0.;
    pileUpWeightObserved_ =  0.;
    binEta_              = -1;
    binEtaAlt_           = -1;
    binEtaGenJet_        = -1;
    binEtaGenJetAlt_     = -1;
    binEtaGen_           = -1;
    binEtaSymm_          = -1;
    binEtaSymmAlt_       = -1;
    binEtaSymmGen_       = -1;
    binEtaSymmGenJet_    = -1;
    binEtaSymmGenJetAlt_ = -1;
    pt_           = -9.;
    ptAlt_        = -9.;
    ptGenJet_     = -9.;
    ptGenJetAlt_  = -9.;
    ptGen_        = -9.;
    eta_          = -9.;
    etaAlt_       = -9.;
    etaGenJet_    = -9.;
    etaGenJetAlt_ = -9.;
    etaGen_       = -9.;
    phi_          = -9.;
    phiAlt_       = -9.;
    phiGenJet_    = -9.;
    phiGenJetAlt_ = -9.;
    phiGen_       = -9.;
    energy_          = -9.;
    energyAlt_       = -9.;
    energyGenJet_    = -9.;
    energyGenJetAlt_ = -9.;
    energyGen_       = -9.;
    tagCSV_       = -9.;
    // Fill variables
    if ( objCats_.at( iCat ) == "Mu" ) {
      if ( ttGenEvent->isSemiLeptonic( WDecay::kMuon ) ) {
        if ( ttSemiLeptonicEventMuons.isValid() && ttSemiLeptonicEventMuons->isHypoValid( TtEvent::kGenMatch )  ) {
          fill( iCat, ttSemiLeptonicEventMuons, patMuons, patElecs, patJets, patMETs, pileUp, ttGenEvent );
        }
        else edm::LogInfo( "AnalyzeHitFit" ) << "...no valid MC match in muon channel";
      }
    }
    else if ( objCats_.at( iCat ) == "Elec" ) {
      if ( ttGenEvent->isSemiLeptonic( WDecay::kElec ) ) {
        if ( ttSemiLeptonicEventElecs.isValid() && ttSemiLeptonicEventElecs->isHypoValid( TtEvent::kGenMatch ) ) {
          fill( iCat, ttSemiLeptonicEventElecs, patMuons, patElecs, patJets, patMETs, pileUp, ttGenEvent );
        }
        else edm::LogInfo( "AnalyzeHitFit" ) << "...no valid MC match in electron channel";
      }
    }
    else {
      if ( ttGenEvent->isSemiLeptonic( WDecay::kMuon ) && ttSemiLeptonicEventMuons.isValid() && ttSemiLeptonicEventMuons->isHypoValid( TtEvent::kGenMatch )  ) {
        fill( iCat, ttSemiLeptonicEventMuons, patMuons, patElecs, patJets, patMETs, pileUp, ttGenEvent );
      }
      else if ( ttGenEvent->isSemiLeptonic( WDecay::kElec ) && ttSemiLeptonicEventElecs.isValid() && ttSemiLeptonicEventElecs->isHypoValid( TtEvent::kGenMatch ) ) {
        fill( iCat, ttSemiLeptonicEventElecs, patMuons, patElecs, patJets, patMETs, pileUp, ttGenEvent );
      }
      else edm::LogInfo( "AnalyzeHitFit" ) << "...no valid MC match in both channel";
    }
    // Fill tree
    catData_.at( iCat )->Fill();

    // Do it again for jets
    if ( cat == "UdscJet" || cat == "BJet" || cat == "Jet" ) {
      // Do it again
      nPVTrue_              = -1.;
      nPVObserved_          = -1;
      pileUpWeightTrue_     =  0.;
      pileUpWeightObserved_ =  0.;
      binEta_              = -1;
      binEtaAlt_           = -1;
      binEtaGenJet_        = -1;
      binEtaGenJetAlt_     = -1;
      binEtaGen_           = -1;
      binEtaSymm_          = -1;
      binEtaSymmAlt_       = -1;
      binEtaSymmGen_       = -1;
      binEtaSymmGenJet_    = -1;
      binEtaSymmGenJetAlt_ = -1;
      pt_           = -9.;
      ptAlt_        = -9.;
      ptGenJet_     = -9.;
      ptGenJetAlt_  = -9.;
      ptGen_        = -9.;
      eta_          = -9.;
      etaAlt_       = -9.;
      etaGenJet_    = -9.;
      etaGenJetAlt_ = -9.;
      etaGen_       = -9.;
      phi_          = -9.;
      phiAlt_       = -9.;
      phiGenJet_    = -9.;
      phiGenJetAlt_ = -9.;
      phiGen_       = -9.;
      energy_          = -9.;
      energyAlt_       = -9.;
      energyGenJet_    = -9.;
      energyGenJetAlt_ = -9.;
      energyGen_       = -9.;
      tagCSV_       = -9.;
      if ( ttSemiLeptonicEventMuons.isValid() && ttSemiLeptonicEventMuons->isHypoValid( TtEvent::kGenMatch )  ) {
        fill( iCat, ttSemiLeptonicEventMuons, patMuons, patElecs, patJets, patMETs, pileUp, ttGenEvent, true );
      }
      else if ( ttSemiLeptonicEventElecs.isValid() && ttSemiLeptonicEventElecs->isHypoValid( TtEvent::kGenMatch ) ) {
        fill( iCat, ttSemiLeptonicEventElecs, patMuons, patElecs, patJets, patMETs, pileUp, ttGenEvent, true );
      }
      else edm::LogInfo( "AnalyzeHitFit" ) << "...no valid MC match in both channel";
      catData_.at( iCat )->Fill();
    }

    // Do it again for all jets
    if ( cat == "Jet" ) {
      // Do it again
      nPVTrue_              = -1.;
      nPVObserved_          = -1;
      pileUpWeightTrue_     =  0.;
      pileUpWeightObserved_ =  0.;
      binEta_              = -1;
      binEtaAlt_           = -1;
      binEtaGenJet_        = -1;
      binEtaGenJetAlt_     = -1;
      binEtaGen_           = -1;
      binEtaSymm_          = -1;
      binEtaSymmAlt_       = -1;
      binEtaSymmGen_       = -1;
      binEtaSymmGenJet_    = -1;
      binEtaSymmGenJetAlt_ = -1;
      pt_           = -9.;
      ptAlt_        = -9.;
      ptGenJet_     = -9.;
      ptGenJetAlt_  = -9.;
      ptGen_        = -9.;
      eta_          = -9.;
      etaAlt_       = -9.;
      etaGenJet_    = -9.;
      etaGenJetAlt_ = -9.;
      etaGen_       = -9.;
      phi_          = -9.;
      phiAlt_       = -9.;
      phiGenJet_    = -9.;
      phiGenJetAlt_ = -9.;
      phiGen_       = -9.;
      energy_          = -9.;
      energyAlt_       = -9.;
      energyGenJet_    = -9.;
      energyGenJetAlt_ = -9.;
      energyGen_       = -9.;
      tagCSV_       = -9.;
      if ( ttSemiLeptonicEventMuons.isValid() && ttSemiLeptonicEventMuons->isHypoValid( TtEvent::kGenMatch )  ) {
        fill( iCat, ttSemiLeptonicEventMuons, patMuons, patElecs, patJets, patMETs, pileUp, ttGenEvent, false, true );
      }
      else if ( ttSemiLeptonicEventElecs.isValid() && ttSemiLeptonicEventElecs->isHypoValid( TtEvent::kGenMatch ) ) {
        fill( iCat, ttSemiLeptonicEventElecs, patMuons, patElecs, patJets, patMETs, pileUp, ttGenEvent, false, true );
      }
      else edm::LogInfo( "AnalyzeHitFit" ) << "...no valid MC match in both channel";
      catData_.at( iCat )->Fill();
      // ...and again
      nPVTrue_              = -1.;
      nPVObserved_          = -1;
      pileUpWeightTrue_     =  0.;
      pileUpWeightObserved_ =  0.;
      binEta_              = -1;
      binEtaAlt_           = -1;
      binEtaGenJet_        = -1;
      binEtaGenJetAlt_     = -1;
      binEtaGen_           = -1;
      binEtaSymm_          = -1;
      binEtaSymmAlt_       = -1;
      binEtaSymmGen_       = -1;
      binEtaSymmGenJet_    = -1;
      binEtaSymmGenJetAlt_ = -1;
      pt_           = -9.;
      ptAlt_        = -9.;
      ptGenJet_     = -9.;
      ptGenJetAlt_  = -9.;
      ptGen_        = -9.;
      eta_          = -9.;
      etaAlt_       = -9.;
      etaGenJet_    = -9.;
      etaGenJetAlt_ = -9.;
      etaGen_       = -9.;
      phi_          = -9.;
      phiAlt_       = -9.;
      phiGenJet_    = -9.;
      phiGenJetAlt_ = -9.;
      phiGen_       = -9.;
      energy_          = -9.;
      energyAlt_       = -9.;
      energyGenJet_    = -9.;
      energyGenJetAlt_ = -9.;
      energyGen_       = -9.;
      tagCSV_       = -9.;
      if ( ttSemiLeptonicEventMuons.isValid() && ttSemiLeptonicEventMuons->isHypoValid( TtEvent::kGenMatch )  ) {
        fill( iCat, ttSemiLeptonicEventMuons, patMuons, patElecs, patJets, patMETs, pileUp, ttGenEvent, true, true );
      }
      else if ( ttSemiLeptonicEventElecs.isValid() && ttSemiLeptonicEventElecs->isHypoValid( TtEvent::kGenMatch ) ) {
        fill( iCat, ttSemiLeptonicEventElecs, patMuons, patElecs, patJets, patMETs, pileUp, ttGenEvent, true, true );
      }
      else edm::LogInfo( "AnalyzeHitFit" ) << "...no valid MC match in both channel";
      catData_.at( iCat )->Fill();
    }
  }
  ++filledEvents_;

}


// End job
void AnalyzeHitFit::endJob()
{

  edm::LogPrint( "AnalyzeHitFit" ) << "\n\n**************\nFilled events: " << filledEvents_ << "\n**************\n";

  if ( plot_ ) {

    my::setPlotEnvironment( gStyle );

    TCanvas c1( "c1" );
    c1.cd();

    for ( unsigned iCat = 0; iCat < objCats_.size(); ++iCat ) {
      const std::string cat( objCats_.at( iCat ) );

      catData_.at( iCat )->Draw( "NPVTrue", "NPVTrue>-1." );
      c1.Print( std::string( pathPlots_ + cat + "_NPVTrue.png" ).c_str() );
      catData_.at( iCat )->Draw( "NPVObserved", "NPVObserved>-1" );
      c1.Print( std::string( pathPlots_ + cat + "_NPVObserved.png" ).c_str() );
      catData_.at( iCat )->Draw( "PileUpWeightTrue", "PileUpWeightTrue>0." );
      c1.Print( std::string( pathPlots_ + cat + "_PileUpWeightTrue.png" ).c_str() );
      catData_.at( iCat )->Draw( "PileUpWeightObserved", "PileUpWeightObserved>0." );
      c1.Print( std::string( pathPlots_ + cat + "_PileUpWeightObserved.png" ).c_str() );

      catData_.at( iCat )->Draw( "Pt", "Pt>-9." );
      c1.Print( std::string( pathPlots_ + cat + "_Pt.png" ).c_str() );
      catData_.at( iCat )->Draw( "Pt:NPVTrue", "Pt>-9.", "ColZ" );
      c1.Print( std::string( pathPlots_ + cat + "_Pt-NPVTrue.png" ).c_str() );
      catData_.at( iCat )->Draw( "Pt:Eta", "Pt>-9.&&Eta>-9.", "ColZ" );
      c1.Print( std::string( pathPlots_ + cat + "_Pt-Eta.png" ).c_str() );
      catData_.at( iCat )->Draw( "Eta", "Eta>-9." );
      c1.Print( std::string( pathPlots_ + cat + "_Eta.png" ).c_str() );
      catData_.at( iCat )->Draw( "Eta:NPVTrue", "Eta>-9.", "ColZ" );
      c1.Print( std::string( pathPlots_ + cat + "_Eta-NPVTrue.png" ).c_str() );
      catData_.at( iCat )->Draw( "Phi", "Phi>-9." );
      c1.Print( std::string( pathPlots_ + cat + "_Phi.png" ).c_str() );
      catData_.at( iCat )->Draw( "Phi:NPVTrue", "Phi>-9.", "ColZ" );
      c1.Print( std::string( pathPlots_ + cat + "_Phi-NPVTrue.png" ).c_str() );
      catData_.at( iCat )->Draw( "Energy", "Energy>-9." );
      c1.Print( std::string( pathPlots_ + cat + "_Energy.png" ).c_str() );
      catData_.at( iCat )->Draw( "Energy:Eta", "Energy>-9.&&Eta>-9.", "ColZ" );
      c1.Print( std::string( pathPlots_ + cat + "_Energy-Eta.png" ).c_str() );
      catData_.at( iCat )->Draw( "Energy:NPVTrue", "Energy>-9.", "ColZ" );
      c1.Print( std::string( pathPlots_ + cat + "_Energy-NPVTrue.png" ).c_str() );
      catData_.at( iCat )->Draw( "BinEta", "BinEta>-1" );
      c1.Print( std::string( pathPlots_ + cat + "_BinEta.png" ).c_str() );
      catData_.at( iCat )->Draw( "BinEta:NPVTrue", "BinEta>-1", "ColZ" );
      c1.Print( std::string( pathPlots_ + cat + "_BinEta-NPVTrue.png" ).c_str() );
      catData_.at( iCat )->Draw( "BinEtaSymm", "BinEtaSymm>-1" );
      c1.Print( std::string( pathPlots_ + cat + "_BinEtaSymm.png" ).c_str() );
      catData_.at( iCat )->Draw( "BinEtaSymm:NPVTrue", "BinEtaSymm>-1", "ColZ" );
      c1.Print( std::string( pathPlots_ + cat + "_BinEtaSymm-NPVTrue.png" ).c_str() );
      catData_.at( iCat )->Draw( "PtAlt", "PtAlt>-9." );
      c1.Print( std::string( pathPlots_ + cat + "_PtAlt.png" ).c_str() );
      catData_.at( iCat )->Draw( "PtAlt:EtaAlt", "PtAlt>-9.&&EtaAlt>-9.", "ColZ" );
      c1.Print( std::string( pathPlots_ + cat + "_PtAlt-EtaAlt.png" ).c_str() );
      catData_.at( iCat )->Draw( "PtAlt:NPVTrue", "PtAlt>-9.", "ColZ" );
      c1.Print( std::string( pathPlots_ + cat + "_PtAlt-NPVTrue.png" ).c_str() );
      catData_.at( iCat )->Draw( "EtaAlt", "EtaAlt>-9." );
      c1.Print( std::string( pathPlots_ + cat + "_EtaAlt.png" ).c_str() );
      catData_.at( iCat )->Draw( "EtaAlt:NPVTrue", "EtaAlt>-9.", "ColZ" );
      c1.Print( std::string( pathPlots_ + cat + "_EtaAlt-NPVTrue.png" ).c_str() );
      catData_.at( iCat )->Draw( "PhiAlt", "PhiAlt>-9." );
      c1.Print( std::string( pathPlots_ + cat + "_PhiAlt.png" ).c_str() );
      catData_.at( iCat )->Draw( "PhiAlt:NPVTrue", "PhiAlt>-9.", "ColZ" );
      c1.Print( std::string( pathPlots_ + cat + "_PhiAlt-NPVTrue.png" ).c_str() );
      catData_.at( iCat )->Draw( "EnergyAlt", "EnergyAlt>-9." );
      c1.Print( std::string( pathPlots_ + cat + "_EnergyAlt.png" ).c_str() );
      catData_.at( iCat )->Draw( "EnergyAlt:EtaAlt", "EnergyAlt>-9.&&EtaAlt>-9.", "ColZ" );
      c1.Print( std::string( pathPlots_ + cat + "_EnergyAlt-EtaAlt.png" ).c_str() );
      catData_.at( iCat )->Draw( "EnergyAlt:NPVTrue", "EnergyAlt>-9.", "ColZ" );
      c1.Print( std::string( pathPlots_ + cat + "_EnergyAlt-NPVTrue.png" ).c_str() );
      catData_.at( iCat )->Draw( "BinEtaAlt", "BinEtaAlt>-1" );
      c1.Print( std::string( pathPlots_ + cat + "_BinEtaAlt.png" ).c_str() );
      catData_.at( iCat )->Draw( "BinEtaAlt:NPVTrue", "BinEtaAlt>-1", "ColZ" );
      c1.Print( std::string( pathPlots_ + cat + "_BinEtaAlt-NPVTrue.png" ).c_str() );
      catData_.at( iCat )->Draw( "BinEtaSymmAlt", "BinEtaSymmAlt>-1" );
      c1.Print( std::string( pathPlots_ + cat + "_BinEtaSymmAlt.png" ).c_str() );
      catData_.at( iCat )->Draw( "BinEtaSymmAlt:NPVTrue", "BinEtaSymmAlt>-1", "ColZ" );
      c1.Print( std::string( pathPlots_ + cat + "_BinEtaSymmAlt-NPVTrue.png" ).c_str() );
      if ( cat == "UdscJet" || cat == "BJet" ) {
        catData_.at( iCat )->Draw( "PtGenJet", "PtGenJet>-9." );
        c1.Print( std::string( pathPlots_ + cat + "_PtGenJet.png" ).c_str() );
        catData_.at( iCat )->Draw( "PtGenJet:EtaGenJet", "PtGenJet>-9.&&EtaGenJet>-9.", "ColZ" );
        c1.Print( std::string( pathPlots_ + cat + "_PtGenJet-EtaGenJet.png" ).c_str() );
        catData_.at( iCat )->Draw( "PtGenJet:NPVTrue", "PtGenJet>-9.", "ColZ" );
        c1.Print( std::string( pathPlots_ + cat + "_PtGenJet-NPVTrue.png" ).c_str() );
        catData_.at( iCat )->Draw( "EtaGenJet", "EtaGenJet>-9." );
        c1.Print( std::string( pathPlots_ + cat + "_EtaGenJet.png" ).c_str() );
        catData_.at( iCat )->Draw( "EtaGenJet:NPVTrue", "EtaGenJet>-9.", "ColZ" );
        c1.Print( std::string( pathPlots_ + cat + "_EtaGenJet-NPVTrue.png" ).c_str() );
        catData_.at( iCat )->Draw( "PhiGenJet", "PhiGenJet>-9." );
        c1.Print( std::string( pathPlots_ + cat + "_PhiGenJet.png" ).c_str() );
        catData_.at( iCat )->Draw( "PhiGenJet:NPVTrue", "PhiGenJet>-9.", "ColZ" );
        c1.Print( std::string( pathPlots_ + cat + "_PhiGenJet-NPVTrue.png" ).c_str() );
        catData_.at( iCat )->Draw( "EnergyGenJet", "EnergyGenJet>-9." );
        c1.Print( std::string( pathPlots_ + cat + "_EnergyGenJet.png" ).c_str() );
        catData_.at( iCat )->Draw( "EnergyGenJet:EtaGenJet", "EnergyGenJet>-9.&&EtaGenJet>-9.", "ColZ" );
        c1.Print( std::string( pathPlots_ + cat + "_EnergyGenJet-EtaGenJet.png" ).c_str() );
        catData_.at( iCat )->Draw( "EnergyGenJet:NPVTrue", "EnergyGenJet>-9.", "ColZ" );
        c1.Print( std::string( pathPlots_ + cat + "_EnergyGenJet-NPVTrue.png" ).c_str() );
        catData_.at( iCat )->Draw( "BinEtaGenJet", "BinEtaGenJet>-1" );
        c1.Print( std::string( pathPlots_ + cat + "_BinEtaGenJet.png" ).c_str() );
        catData_.at( iCat )->Draw( "BinEtaGenJet:NPVTrue", "BinEtaGenJet>-1", "ColZ" );
        c1.Print( std::string( pathPlots_ + cat + "_BinEtaGenJet-NPVTrue.png" ).c_str() );
        catData_.at( iCat )->Draw( "BinEtaSymmGenJet", "BinEtaSymmGenJet>-1" );
        c1.Print( std::string( pathPlots_ + cat + "_BinEtaSymmGenJet.png" ).c_str() );
        catData_.at( iCat )->Draw( "BinEtaSymmGenJet:NPVTrue", "BinEtaSymmGenJet>-1", "ColZ" );
        c1.Print( std::string( pathPlots_ + cat + "_BinEtaSymmGenJet-NPVTrue.png" ).c_str() );
        catData_.at( iCat )->Draw( "PtGenJetAlt", "PtGenJetAlt>-9." );
        c1.Print( std::string( pathPlots_ + cat + "_PtGenJetAlt.png" ).c_str() );
        catData_.at( iCat )->Draw( "PtGenJetAlt:EtaGenJet", "PtGenJetAlt>-9.&&EtaGenJet>-9.", "ColZ" );
        c1.Print( std::string( pathPlots_ + cat + "_PtGenJetAlt-EtaGenJet.png" ).c_str() );
        catData_.at( iCat )->Draw( "PtGenJetAlt:NPVTrue", "PtGenJetAlt>-9.", "ColZ" );
        c1.Print( std::string( pathPlots_ + cat + "_PtGenJetAlt-NPVTrue.png" ).c_str() );
        catData_.at( iCat )->Draw( "EtaGenJetAlt", "EtaGenJetAlt>-9." );
        c1.Print( std::string( pathPlots_ + cat + "_EtaGenJetAlt.png" ).c_str() );
        catData_.at( iCat )->Draw( "EtaGenJetAlt:NPVTrue", "EtaGenJetAlt>-9.", "ColZ" );
        c1.Print( std::string( pathPlots_ + cat + "_EtaGenJetAlt-NPVTrue.png" ).c_str() );
        catData_.at( iCat )->Draw( "PhiGenJetAlt", "PhiGenJetAlt>-9." );
        c1.Print( std::string( pathPlots_ + cat + "_PhiGenJetAlt.png" ).c_str() );
        catData_.at( iCat )->Draw( "PhiGenJetAlt:NPVTrue", "PhiGenJetAlt>-9.", "ColZ" );
        c1.Print( std::string( pathPlots_ + cat + "_PhiGenJetAlt-NPVTrue.png" ).c_str() );
        catData_.at( iCat )->Draw( "EnergyGenJetAlt", "EnergyGenJetAlt>-9." );
        c1.Print( std::string( pathPlots_ + cat + "_EnergyGenJetAlt.png" ).c_str() );
        catData_.at( iCat )->Draw( "EnergyGenJetAlt:EtaGenJetAlt", "EnergyGenJetAlt>-9.&&EtaGenJetAlt>-9.", "ColZ" );
        c1.Print( std::string( pathPlots_ + cat + "_EnergyGenJetAlt-EtaGenJetAlt.png" ).c_str() );
        catData_.at( iCat )->Draw( "EnergyGenJetAlt:NPVTrue", "EnergyGenJetAlt>-9.", "ColZ" );
        c1.Print( std::string( pathPlots_ + cat + "_EnergyGenJetAlt-NPVTrue.png" ).c_str() );
        catData_.at( iCat )->Draw( "BinEtaGenJetAlt", "BinEtaGenJetAlt>-1" );
        c1.Print( std::string( pathPlots_ + cat + "_BinEtaGenJetAlt.png" ).c_str() );
        catData_.at( iCat )->Draw( "BinEtaGenJetAlt:NPVTrue", "BinEtaGenJetAlt>-1", "ColZ" );
        c1.Print( std::string( pathPlots_ + cat + "_BinEtaGenJetAlt-NPVTrue.png" ).c_str() );
        catData_.at( iCat )->Draw( "BinEtaSymmGenJetAlt", "BinEtaSymmGenJetAlt>-1" );
        c1.Print( std::string( pathPlots_ + cat + "_BinEtaSymmGenJetAlt.png" ).c_str() );
        catData_.at( iCat )->Draw( "BinEtaSymmGenJetAlt:NPVTrue", "BinEtaSymmGenJetAlt>-1", "ColZ" );
        c1.Print( std::string( pathPlots_ + cat + "_BinEtaSymmGenJetAlt-NPVTrue.png" ).c_str() );
      }
      catData_.at( iCat )->Draw( "PtGen", "PtGen>-9." );
      c1.Print( std::string( pathPlots_ + cat + "_PtGen.png" ).c_str() );
      catData_.at( iCat )->Draw( "PtGen:EtaGen", "PtGen>-9.&&NPVTrue>-9.", "ColZ" );
      c1.Print( std::string( pathPlots_ + cat + "_PtGen-EtaGen.png" ).c_str() );
      catData_.at( iCat )->Draw( "PtGen:NPVTrue", "PtGen>-9.", "ColZ" );
      c1.Print( std::string( pathPlots_ + cat + "_PtGen-NPVTrue.png" ).c_str() );
      catData_.at( iCat )->Draw( "EtaGen", "EtaGen>-9." );
      c1.Print( std::string( pathPlots_ + cat + "_EtaGen.png" ).c_str() );
      catData_.at( iCat )->Draw( "EtaGen:NPVTrue", "EtaGen>-9.", "ColZ" );
      c1.Print( std::string( pathPlots_ + cat + "_EtaGen-NPVTrue.png" ).c_str() );
      catData_.at( iCat )->Draw( "PhiGen", "PhiGen>-9." );
      c1.Print( std::string( pathPlots_ + cat + "_PhiGen.png" ).c_str() );
      catData_.at( iCat )->Draw( "PhiGen:NPVTrue", "PhiGen>-9.", "ColZ" );
      c1.Print( std::string( pathPlots_ + cat + "_PhiGen-NPVTrue.png" ).c_str() );
      catData_.at( iCat )->Draw( "EnergyGen", "EnergyGen>-9." );
      c1.Print( std::string( pathPlots_ + cat + "_EnergyGen.png" ).c_str() );
      catData_.at( iCat )->Draw( "EnergyGen:EtaGen", "EnergyGen>-9.&&NPVTrue>-9.", "ColZ" );
      c1.Print( std::string( pathPlots_ + cat + "_EnergyGen-EtaGen.png" ).c_str() );
      catData_.at( iCat )->Draw( "EnergyGen:NPVTrue", "EnergyGen>-9.", "ColZ" );
      c1.Print( std::string( pathPlots_ + cat + "_EnergyGen-NPVTrue.png" ).c_str() );
      catData_.at( iCat )->Draw( "BinEtaGen", "BinEtaGen>-1" );
      c1.Print( std::string( pathPlots_ + cat + "_BinEtaGen.png" ).c_str() );
      catData_.at( iCat )->Draw( "BinEtaGen:NPVTrue", "BinEtaGen>-1", "ColZ" );
      c1.Print( std::string( pathPlots_ + cat + "_BinEtaGen-NPVTrue.png" ).c_str() );
      catData_.at( iCat )->Draw( "BinEtaSymmGen", "BinEtaSymmGen>-1" );
      c1.Print( std::string( pathPlots_ + cat + "_BinEtaSymmGen.png" ).c_str() );
      catData_.at( iCat )->Draw( "BinEtaSymmGen:NPVTrue", "BinEtaSymmGen>-1", "ColZ" );
      c1.Print( std::string( pathPlots_ + cat + "_BinEtaSymmGen-NPVTrue.png" ).c_str() );

    }

  }

}


unsigned AnalyzeHitFit::getEtaBin( unsigned iCat, double eta, bool symm )
{

  std::vector< double > etaBins( symm ? etaSymmBins_.at( iCat ) : etaBins_.at( iCat ) );
  if ( symm ) eta = fabs( eta );
  for ( unsigned iEta = 0; iEta < etaBins.size() - 1; ++iEta ) {
    if ( etaBins.at( iEta ) <= eta && eta < etaBins.at( iEta + 1 ) ) return iEta;
  }

  return etaBins.size();

}


void AnalyzeHitFit::fill( unsigned iCat, const edm::Handle< TtSemiLeptonicEvent > & ttSemiLeptonicEvent, edm::Handle< pat::MuonCollection > & patMuons, edm::Handle< pat::ElectronCollection > & patElecs, edm::Handle< pat::JetCollection > & patJets, edm::Handle< pat::METCollection > & patMETs, edm::Handle< std::vector< PileupSummaryInfo > > & pileUp, edm::Handle< TtGenEvent > & ttGenEvent, bool repeat, bool allJets )
{

  // Vertices
  for ( std::vector< PileupSummaryInfo >::const_iterator iPileUp = pileUp->begin(); iPileUp != pileUp->end(); ++iPileUp ) {
    if ( iPileUp->getBunchCrossing() == 0 ) {
      nPVTrue_     = iPileUp->getTrueNumInteractions();
      nPVObserved_ = iPileUp->getPU_NumInteractions();
      // Pile-up weight
      pileUpWeightTrue_     = lumiWeightTrue_.weight( nPVTrue_ );
      pileUpWeightObserved_ = lumiWeightObserved_.weight( nPVObserved_ ); // FIXME: Is this the correct approach?
      break;
    }
  }

  const std::string cat( objCats_.at( iCat ) );
  const std::vector< int > jetLepCombi( ttSemiLeptonicEvent->jetLeptonCombination( TtEvent::kGenMatch ) );
  if ( cat == "Mu" ) {
    if ( repeat ) {
      edm::LogWarning( "AnalyzeHitFit" ) << "Category repeated: " << cat;
      return;
    }
    const int muonIndex( ttSemiLeptonicEvent->jetLeptonCombination( TtEvent::kGenMatch ).at( TtSemiLepEvtPartons::Lepton ) );
    pt_      = ttSemiLeptonicEvent->singleLepton( TtEvent::kGenMatch )->pt();
    ptAlt_   = patMuons->at( muonIndex ).bestTrack()->pt();
    ptGen_   = ttGenEvent->singleLepton()->pt();
    eta_     = ttSemiLeptonicEvent->singleLepton( TtEvent::kGenMatch )->eta();
    etaAlt_  = patMuons->at( muonIndex ).bestTrack()->eta();
    etaGen_  = ttGenEvent->singleLepton()->eta();
    phi_     = ttSemiLeptonicEvent->singleLepton( TtEvent::kGenMatch )->phi();
    phiAlt_  = patMuons->at( muonIndex ).bestTrack()->phi();
    phiGen_  = ttGenEvent->singleLepton()->phi();
    energy_     = ttSemiLeptonicEvent->singleLepton( TtEvent::kGenMatch )->energy();
    energyAlt_  = patMuons->at( muonIndex ).bestTrack()->p();
    energyGen_  = ttGenEvent->singleLepton()->energy();
  }
  else if ( cat == "Elec" ) {
    if ( repeat ) {
      edm::LogWarning( "AnalyzeHitFit" ) << "Category repeated: " << cat;
      return;
    }
    const int elecIndex( ttSemiLeptonicEvent->jetLeptonCombination( TtEvent::kGenMatch ).at( TtSemiLepEvtPartons::Lepton ) );
    pt_      = ttSemiLeptonicEvent->singleLepton( TtEvent::kGenMatch )->pt();
    ptAlt_   = patElecs->at( elecIndex ).ecalDrivenMomentum().pt();
    ptGen_   = ttGenEvent->singleLepton()->pt();
    eta_     = ttSemiLeptonicEvent->singleLepton( TtEvent::kGenMatch )->eta();
    etaAlt_  = patElecs->at( elecIndex ).ecalDrivenMomentum().eta();
    etaGen_  = ttGenEvent->singleLepton()->eta();
    phi_     = ttSemiLeptonicEvent->singleLepton( TtEvent::kGenMatch )->phi();
    phiAlt_  = patElecs->at( elecIndex ).ecalDrivenMomentum().phi();
    phiGen_  = ttGenEvent->singleLepton()->phi();
    energy_     = ttSemiLeptonicEvent->singleLepton( TtEvent::kGenMatch )->energy();
    energyAlt_  = patElecs->at( elecIndex ).ecalDrivenMomentum().energy();
//     energyAlt_  = patElecs->at( elecIndex ).correctedEcalEnergy(); // ???
    energyGen_  = ttGenEvent->singleLepton()->energy();
  }
  else if ( cat == "UdscJet" || ( cat == "Jet" && ! allJets ) ) {
    if ( repeat ) {
      const pat::Jet jet( patJets->at( ( unsigned )jetLepCombi.at( TtSemiLepEvtPartons::LightQ ) ).correctedJet( jecLevel_, "uds" ) );
      pt_     = jet.pt();
      ptAlt_  = pt_;
      ptGen_  = ttGenEvent->hadronicDecayQuark()->pt();
      eta_    = jet.eta();
      etaAlt_ = eta_;
      etaGen_ = ttGenEvent->hadronicDecayQuark()->eta();
      phi_    = jet.phi();
      phiAlt_ = phi_;
      phiGen_ = ttGenEvent->hadronicDecayQuark()->phi();
      energy_    = jet.energy();
      energyAlt_ = energy_;
      energyGen_ = ttGenEvent->hadronicDecayQuark()->energy();
      if ( jet.genJet() != 0 ) {
        ptGenJet_  = jet.genJet()->pt();
        etaGenJet_ = jet.genJet()->eta();
        phiGenJet_ = jet.genJet()->phi();
        energyGenJet_ = jet.genJet()->energy();
        ptGenJetAlt_  = ptGenJet_;
        etaGenJetAlt_ = etaGenJet_;
        phiGenJetAlt_ = phiGenJet_;
        energyGenJetAlt_ = energyGenJet_;
      }
      tagCSV_ = jet.bDiscriminator( "combinedSecondaryVertexBJetTags" );
    }
    else {
      const pat::Jet jetBar( patJets->at( ( unsigned )jetLepCombi.at( TtSemiLepEvtPartons::LightQBar ) ).correctedJet( jecLevel_, "uds" ) );
      pt_     = jetBar.pt();
      ptAlt_  = pt_;
      ptGen_  = ttGenEvent->hadronicDecayQuarkBar()->pt();
      eta_    = jetBar.eta();
      etaAlt_ = eta_;
      etaGen_ = ttGenEvent->hadronicDecayQuarkBar()->eta();
      phi_    = jetBar.phi();
      phiAlt_ = phi_;
      phiGen_ = ttGenEvent->hadronicDecayQuarkBar()->phi();
      energy_    = jetBar.energy();
      energyAlt_ = energy_;
      energyGen_ = ttGenEvent->hadronicDecayQuarkBar()->energy();
      if ( jetBar.genJet() != 0 ) {
        ptGenJet_  = jetBar.genJet()->pt();
        etaGenJet_ = jetBar.genJet()->eta();
        phiGenJet_ = jetBar.genJet()->phi();
        energyGenJet_ = jetBar.genJet()->energy();
        ptGenJetAlt_  = ptGenJet_;
        etaGenJetAlt_ = etaGenJet_;
        phiGenJetAlt_ = phiGenJet_;
        energyGenJetAlt_ = energyGenJet_;
      }
      tagCSV_ = jetBar.bDiscriminator( "combinedSecondaryVertexBJetTags" );
    }
  }
  else if ( cat == "BJet" || ( cat == "Jet" && allJets ) ) {
    if ( repeat ) {
      const pat::Jet bJetLep( patJets->at( ( unsigned )jetLepCombi.at( TtSemiLepEvtPartons::LepB ) ).correctedJet( jecLevel_, "bottom" ) );
      pt_     = bJetLep.pt();
      ptAlt_  = pt_;
      ptGen_  = ttGenEvent->leptonicDecayB()->pt();
      eta_    = bJetLep.eta();
      etaAlt_ = eta_;
      etaGen_ = ttGenEvent->leptonicDecayB()->eta();
      phi_    = bJetLep.phi();
      phiAlt_ = phi_;
      phiGen_ = ttGenEvent->leptonicDecayB()->phi();
      energy_    = bJetLep.energy();
      energyAlt_ = energy_;
      energyGen_ = ttGenEvent->leptonicDecayB()->energy();
      if ( bJetLep.genJet() != 0 ) {
        ptGenJet_  = bJetLep.genJet()->pt();
        etaGenJet_ = bJetLep.genJet()->eta();
        phiGenJet_ = bJetLep.genJet()->phi();
        energyGenJet_ = bJetLep.genJet()->energy();
        ptGenJetAlt_  = ptGenJet_;
        etaGenJetAlt_ = etaGenJet_;
        phiGenJetAlt_ = phiGenJet_;
        energyGenJetAlt_ = energyGenJet_;
      }
      tagCSV_ = bJetLep.bDiscriminator( "combinedSecondaryVertexBJetTags" );
    }
    else {
      const pat::Jet bJetHad( patJets->at( ( unsigned )jetLepCombi.at( TtSemiLepEvtPartons::HadB ) ).correctedJet( jecLevel_, "bottom" ) );
      pt_     = bJetHad.pt();
      ptAlt_  = pt_;
      ptGen_  = ttGenEvent->hadronicDecayB()->pt();
      eta_    = bJetHad.eta();
      etaAlt_ = eta_;
      etaGen_ = ttGenEvent->hadronicDecayB()->eta();
      phi_    = bJetHad.phi();
      phiAlt_ = phi_;
      phiGen_ = ttGenEvent->hadronicDecayB()->phi();
      energy_    = bJetHad.energy();
      energyAlt_ = energy_;
      energyGen_ = ttGenEvent->hadronicDecayB()->energy();
      if ( bJetHad.genJet() != 0 ) {
        ptGenJet_  = bJetHad.genJet()->pt();
        etaGenJet_ = bJetHad.genJet()->eta();
        phiGenJet_ = bJetHad.genJet()->phi();
        energyGenJet_ = bJetHad.genJet()->energy();
        ptGenJetAlt_  = ptGenJet_;
        etaGenJetAlt_ = etaGenJet_;
        phiGenJetAlt_ = phiGenJet_;
        energyGenJetAlt_ = energyGenJet_;
      }
      tagCSV_ = bJetHad.bDiscriminator( "combinedSecondaryVertexBJetTags" );
    }
  }
  else if ( cat == "MET" ) {
    if ( repeat ) {
      edm::LogWarning( "AnalyzeHitFit" ) << "Category repeated: " << cat;
      return;
    }
//     pt_     = ttSemiLeptonicEvent->singleNeutrino( TtEvent::kGenMatch )->pt();
    pt_     = patMETs->at( 0 ).pt();
    ptAlt_  = pt_;
    ptGen_  = ttGenEvent->singleNeutrino()->pt();
//     eta_    = ttSemiLeptonicEvent->singleNeutrino( TtEvent::kGenMatch )->eta();
    eta_    = patMETs->at( 0 ).eta();
    etaAlt_ = eta_;
    etaGen_ = ttGenEvent->singleNeutrino()->eta();
//     phi_    = ttSemiLeptonicEvent->singleNeutrino( TtEvent::kGenMatch )->phi();
    phi_    = patMETs->at( 0 ).phi();
    phiAlt_ = phi_;
    phiGen_ = ttGenEvent->singleNeutrino()->phi();
//     energy_    = ttSemiLeptonicEvent->singleNeutrino( TtEvent::kGenMatch )->energy();
    energy_    = patMETs->at( 0 ).energy();
    energyAlt_ = energy_;
    energyGen_ = ttGenEvent->singleNeutrino()->energy();
  }
  else {
    edm::LogWarning( "AnalyzeHitFit" ) << "Category missmatch: " << cat;
    return;
  }

  unsigned iEta;
  if ( eta_ != -9. ) {
    iEta = getEtaBin( iCat, eta_ );
    if ( iEta < etaBins_.at( iCat ).size() ) binEta_ = iEta;
  }
  if ( etaAlt_ != -9. ) {
    iEta = getEtaBin( iCat, etaAlt_ );
    if ( iEta < etaBins_.at( iCat ).size() ) binEtaAlt_ = iEta;
  }
  if ( etaGenJet_ != -9. ) {
    iEta = getEtaBin( iCat, etaGenJet_ );
    if ( iEta < etaBins_.at( iCat ).size() ) binEtaGenJet_ = iEta;
  }
  if ( etaGenJetAlt_ != -9. ) {
    iEta = getEtaBin( iCat, etaGenJetAlt_ );
    if ( iEta < etaBins_.at( iCat ).size() ) binEtaGenJetAlt_ = iEta;
  }
  if ( etaGen_ != -9. ) {
    iEta = getEtaBin( iCat, etaGen_ );
    if ( iEta < etaBins_.at( iCat ).size() ) binEtaGen_ = iEta;
  }
  if ( eta_ != -9. ) {
    iEta = getEtaBin( iCat, eta_, true );
    if ( iEta < etaSymmBins_.at( iCat ).size() ) binEtaSymm_ = iEta;
  }
  if ( etaAlt_ != -9. ) {
    iEta = getEtaBin( iCat, etaAlt_, true );
    if ( iEta < etaSymmBins_.at( iCat ).size() ) binEtaSymmAlt_ = iEta;
  }
  if ( etaGenJet_ != -9. ) {
    iEta = getEtaBin( iCat, etaGenJet_, true );
    if ( iEta < etaSymmBins_.at( iCat ).size() ) binEtaSymmGenJet_ = iEta;
  }
  if ( etaGenJetAlt_ != -9. ) {
    iEta = getEtaBin( iCat, etaGenJetAlt_, true );
    if ( iEta < etaSymmBins_.at( iCat ).size() ) binEtaSymmGenJetAlt_ = iEta;
  }
  if ( etaGen_ != -9. ) {
    iEta = getEtaBin( iCat, etaGen_, true );
    if ( iEta < etaSymmBins_.at( iCat ).size() ) binEtaSymmGen_ = iEta;
  }

}


#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE( AnalyzeHitFit );
