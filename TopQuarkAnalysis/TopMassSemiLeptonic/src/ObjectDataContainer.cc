#include "TopQuarkAnalysis/TopMassSemiLeptonic/interface/ObjectDataContainer.h"

#include <cmath>
#include <cassert>

#include <TH1D.h>
#include <TTree.h>


using namespace my;


ObjectDataContainer::ObjectDataContainer( const std::string& objCat, TDirectory* dirInCat, Bool_t useSymm, Bool_t useAlt, Bool_t useNonT, Bool_t useNonP, Bool_t refGen, Bool_t usePileUp, const std::string& pileUp, Int_t maxEvents )
{

  // Get eta binning
  TH1D * histEtaBins( ( TH1D* )( dirInCat->Get( std::string( objCat + "_binsEta" ).c_str() ) ) );
  const Bool_t objMetLike( histEtaBins->GetNbinsX() == 1 );
  if ( objMetLike ) {
    etaBins_.push_back( histEtaBins->GetBinLowEdge( 1 ) );
  }
  else {
    for ( Int_t iEta = 0; iEta < histEtaBins->GetNbinsX(); ++iEta ) {
      Double_t edge( histEtaBins->GetBinLowEdge( iEta + 1 ) );
      if ( useSymm  && edge < 0. ) continue;
      if ( useSymm  && edge > 0. && etaBins_.size() == 0 ) {
        etaBins_.push_back( 0. );
        continue;
      }
      etaBins_.push_back( edge );
    }
  }
  etaBins_.push_back( histEtaBins->GetBinLowEdge( histEtaBins->GetNbinsX() ) + histEtaBins->GetBinWidth( histEtaBins->GetNbinsX() ) );

  // Get pt binning
  TH1D * histPtBins( ( TH1D* )( dirInCat->Get( std::string( objCat + "_binsPt" ).c_str() ) ) );
  for ( Int_t iPt = 0; iPt < histPtBins->GetNbinsX(); ++iPt ) {
    ptBins_.push_back( histPtBins->GetBinLowEdge( iPt + 1 ) );
  }
  ptBins_.push_back( histPtBins->GetBinLowEdge( histPtBins->GetNbinsX() ) + histPtBins->GetBinWidth( histPtBins->GetNbinsX() ) );
//   if ( fitMaxPt_ > ptBins_.back() ) fitMaxPt_ = ptBins_.back();

  // Get data
  sizeEta_.reserve( nEtaBins() );
  weightData_.reserve( nEtaBins() );
  ptData_.reserve( nEtaBins() );
  ptGenData_.reserve( nEtaBins() );
  energyData_.reserve( nEtaBins() );
  energyGenData_.reserve( nEtaBins() );
  etaData_.reserve( nEtaBins() );
  etaGenData_.reserve( nEtaBins() );
  phiData_.reserve( nEtaBins() );
  phiGenData_.reserve( nEtaBins() );
  for ( unsigned uEta = 0; uEta < nEtaBins(); ++uEta ) {
    sizeEta_.push_back( 0 );
    weightData_.push_back( std::vector< double >() );
    ptData_.push_back( std::vector< double >() );
    ptGenData_.push_back( std::vector< double >() );
    energyData_.push_back( std::vector< double >() );
    energyGenData_.push_back( std::vector< double >() );
    etaData_.push_back( std::vector< double >() );
    etaGenData_.push_back( std::vector< double >() );
    phiData_.push_back( std::vector< double >() );
    phiGenData_.push_back( std::vector< double >() );
  }
  Double_t pileUpWeight;
  Double_t ptData;
  Double_t ptGenData;
  Double_t energyData;
  Double_t energyGenData;
  Double_t etaData;
  Double_t etaGenData;
  Double_t phiData;
  Double_t phiGenData;
  Int_t    iEta;
  TTree* dataTree( ( TTree* )( dirInCat->Get( std::string( objCat + "_data" ).c_str() ) ) );
  dataTree->SetBranchAddress( pileUp.c_str(), &pileUpWeight );
  if ( useAlt ) {
    dataTree->SetBranchAddress( "PtAlt" , &ptData );
    dataTree->SetBranchAddress( "EnergyAlt" , &energyData );
    dataTree->SetBranchAddress( "EtaAlt", &etaData );
    dataTree->SetBranchAddress( "PhiAlt", &phiData );
  }
  else {
    dataTree->SetBranchAddress( "Pt" , &ptData );
    dataTree->SetBranchAddress( "Energy" , &energyData );
    dataTree->SetBranchAddress( "Eta", &etaData );
    dataTree->SetBranchAddress( "Phi", &phiData );
  }
  dataTree->SetBranchAddress( "PtGen" , &ptGenData );
  dataTree->SetBranchAddress( "EnergyGen" , &energyGenData );
  dataTree->SetBranchAddress( "EtaGen", &etaGenData );
  dataTree->SetBranchAddress( "PhiGen", &phiGenData );
  if ( useSymm ) {
    if      ( refGen ) dataTree->SetBranchAddress( "BinEtaSymmGen", &iEta );
    else if ( useAlt ) dataTree->SetBranchAddress( "BinEtaSymmAlt", &iEta );
    else               dataTree->SetBranchAddress( "BinEtaSymm"   , &iEta );
  }
  else {
    if      ( refGen ) dataTree->SetBranchAddress( "BinEtaGen", &iEta );
    else if ( useAlt ) dataTree->SetBranchAddress( "BinEtaAlt", &iEta );
    else               dataTree->SetBranchAddress( "BinEta"   , &iEta );
  }
  Int_t nEntries( ( Int_t )dataTree->GetEntries() );
  if ( objCat == "UdscJet" || objCat == "BJet" ) {
    maxEvents *= 2;
    if ( 0 <= maxEvents && maxEvents < nEntries ) nEntries = maxEvents;
    assert( nEntries % 2 == 0 ); // need two jet entries per event
  }
  else {
    if ( 0 <= maxEvents && maxEvents < nEntries ) nEntries = maxEvents;
  }
  for ( int iEntry = 0; iEntry < nEntries; ++iEntry ) {
    dataTree->GetEntry( iEntry );
    assert( iEta < ( Int_t )( nEtaBins() ) ); // has to fit (and be consistent)
    if ( iEta == -1 ) continue; // FIXME: eta out of range in analyzer; should be solved more consistently
    sizeEta_[ iEta ] += 1;
    if ( usePileUp ) weightData_[ iEta ].push_back( pileUpWeight );
    else             weightData_[ iEta ].push_back( 1. );
    ptData_[ iEta ].push_back( ptData );
    ptGenData_[ iEta ].push_back( ptGenData );
    energyData_[ iEta ].push_back( energyData );
    energyGenData_[ iEta ].push_back( energyGenData );
    etaData_[ iEta ].push_back( etaData );
    etaGenData_[ iEta ].push_back( etaGenData );
    phiData_[ iEta ].push_back( phiData );
    phiGenData_[ iEta ].push_back( phiGenData );
  }
  dataTree->ResetBranchAddresses();

  // Split data into pt bins per eta bin
  sizePt_.reserve( nEtaBins() );
  weightDataPt_.reserve( nEtaBins() );
  ptDataPt_.reserve( nEtaBins() );
  ptGenDataPt_.reserve( nEtaBins() );
  etaDataPt_.reserve( nEtaBins() );
  etaGenDataPt_.reserve( nEtaBins() );
  phiDataPt_.reserve( nEtaBins() );
  phiGenDataPt_.reserve( nEtaBins() );
  for ( unsigned uEta = 0; uEta < nEtaBins(); ++uEta ) {
    DataTable weightEtaBin( nPtBins() );
    DataTable ptEtaBin( nPtBins() );
    DataTable ptGenEtaBin( nPtBins() );
    DataTable etaEtaBin( nPtBins() );
    DataTable etaGenEtaBin( nPtBins() );
    DataTable phiEtaBin( nPtBins() );
    DataTable phiGenEtaBin( nPtBins() );
    std::vector< unsigned > sizePt( nPtBins() );
    for ( unsigned uEntry = 0; uEntry < sizeEta_[ uEta ]; ++uEntry ) {
      Double_t ptVal;
      Double_t ptGenVal;
      if ( useNonP ) {
        if ( energyData_[ uEta ][ uEntry ] == -9. || energyGenData_[ uEta ][ uEntry ] == -9. ) continue; // no match
        ptVal = useNonT ? energyData_[ uEta ][ uEntry ] : std::sqrt( std::pow( energyData_[ uEta ][ uEntry ], 2 ) + ( 1. - std::pow( std::cosh( etaData_[ uEta ][ uEntry ] ), 2 ) ) * std::pow( ptData_[ uEta ][ uEntry ], 2 ) );
        ptGenVal = useNonT ? energyGenData_[ uEta ][ uEntry ] : std::sqrt( std::pow( energyGenData_[ uEta ][ uEntry ], 2 ) + ( 1. - std::pow( std::cosh( etaGenData_[ uEta ][ uEntry ] ), 2 ) ) * std::pow( ptGenData_[ uEta ][ uEntry ], 2 ) );
      }
      else {
        if ( ptData_[ uEta ][ uEntry ] == -9. || ptGenData_[ uEta ][ uEntry ] == -9. ) continue; // no match
        ptVal = useNonT ? ptData_[ uEta ][ uEntry ] * std::cosh( etaData_[ uEta ][ uEntry ] ) : ptData_[ uEta ][ uEntry ];
        ptGenVal = useNonT ? ptGenData_[ uEta ][ uEntry ] * std::cosh( etaGenData_[ uEta ][ uEntry ] ) : ptGenData_[ uEta ][ uEntry ];
      }
      Double_t ptRef( refGen ? ptGenVal : ptVal );
      for ( unsigned uPt = 0; uPt < nPtBins(); ++uPt ) {
        if ( ptBins_[ uPt ] <= ptRef && ptRef < ptBins_[ uPt + 1 ] ) {
          sizePt[ uPt ] += 1;
          weightEtaBin[ uPt ].push_back( weightData_[ uEta ][ uEntry ] );
          ptEtaBin[ uPt ].push_back( ptVal );
          ptGenEtaBin[ uPt ].push_back( ptGenVal );
          etaEtaBin[ uPt ].push_back( etaData_[ uEta ][ uEntry ] );
          etaGenEtaBin[ uPt ].push_back( etaGenData_[ uEta ][ uEntry ] );
          phiEtaBin[ uPt ].push_back( phiData_[ uEta ][ uEntry ] );
          phiGenEtaBin[ uPt ].push_back( phiGenData_[ uEta ][ uEntry ] );
          break;
        }
      } // loop: uPt < nPtBins()
    } // loop: uEntry < sizeEta_[ uEta ]
    weightDataPt_.push_back( weightEtaBin );
    ptDataPt_.push_back( ptEtaBin );
    ptGenDataPt_.push_back( ptGenEtaBin );
    etaDataPt_.push_back( etaEtaBin );
    etaGenDataPt_.push_back( etaGenEtaBin );
    phiDataPt_.push_back( phiEtaBin );
    phiGenDataPt_.push_back( phiGenEtaBin );
    sizePt_.push_back( sizePt );
  }

}
