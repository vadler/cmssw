#include "TopQuarkAnalysis/TopMassSemiLeptonic/interface/JetDataContainer.h"

#include <cmath>
#include <cassert>

#include <TH1D.h>
#include <TTree.h>


using namespace my;


JetDataContainer::JetDataContainer( const std::string& objCat, TDirectory* dirInCat, Bool_t useSymm, Bool_t useAlt, Bool_t useNonT, Bool_t useNonP, Bool_t refGen, Bool_t usePileUp, const std::string& pileUp, Int_t maxEvents )
: ObjectDataContainer( objCat, dirInCat, useSymm, useAlt, useNonT, useNonP, refGen, usePileUp, pileUp, maxEvents )
{

  if ( objCat == "UdscJet" || objCat == "BJet" ) {

    // Get data
    ptGenJetData_.reserve( nEtaBins() );
    energyGenJetData_.reserve( nEtaBins() );
    etaGenJetData_.reserve( nEtaBins() );
    phiGenJetData_.reserve( nEtaBins() );
    tagCSVData_.reserve( nEtaBins() );
    for ( unsigned uEta = 0; uEta < nEtaBins(); ++uEta ) {
      ptGenJetData_.push_back( std::vector< double >() );
      energyGenJetData_.push_back( std::vector< double >() );
      etaGenJetData_.push_back( std::vector< double >() );
      phiGenJetData_.push_back( std::vector< double >() );
      tagCSVData_.push_back( std::vector< double >() );
    }
    Double_t ptGenJetData;
    Double_t energyGenJetData;
    Double_t etaGenJetData;
    Double_t phiGenJetData;
    Double_t tagCSVData;
    Int_t    iEta;
    TTree* dataTree( ( TTree* )( dirInCat->Get( std::string( objCat + "_data" ).c_str() ) ) );
    if ( useAlt ) {
      dataTree->SetBranchAddress( "PtGenJetAlt" , &ptGenJetData );
      dataTree->SetBranchAddress( "EnergyGenJetAlt" , &energyGenJetData );
      dataTree->SetBranchAddress( "EtaGenJetAlt", &etaGenJetData );
      dataTree->SetBranchAddress( "PhiGenJetAlt", &phiGenJetData );
    }
    else {
      dataTree->SetBranchAddress( "PtGenJet" , &ptGenJetData );
      dataTree->SetBranchAddress( "EnergyGenJet" , &energyGenJetData );
      dataTree->SetBranchAddress( "EtaGenJet", &etaGenJetData );
      dataTree->SetBranchAddress( "PhiGenJet", &phiGenJetData );
    }
    dataTree->SetBranchAddress( "TagCSV", &tagCSVData );
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
    maxEvents *= 2;
    if ( 0 <= maxEvents && maxEvents < nEntries ) nEntries = maxEvents;
    assert( nEntries % 2 == 0 ); // need two jet entries per event
    for ( int iEntry = 0; iEntry < nEntries; ++iEntry ) {
      dataTree->GetEntry( iEntry );
      assert( iEta < ( Int_t )( nEtaBins() ) ); // has to fit (and be consistent)
      if ( iEta == -1 ) continue; // FIXME: eta out of range in analyzer; should be solved more consistently
      ptGenJetData_[ iEta ].push_back( ptGenJetData );
      energyGenJetData_[ iEta ].push_back( energyGenJetData );
      etaGenJetData_[ iEta ].push_back( etaGenJetData );
      phiGenJetData_[ iEta ].push_back( phiGenJetData );
      tagCSVData_[ iEta ].push_back( tagCSVData );
    }
    dataTree->ResetBranchAddresses();

    // Split data into pt bins per eta bin
    ptGenJetDataPt_.reserve( nEtaBins() );
    etaGenJetDataPt_.reserve( nEtaBins() );
    phiGenJetDataPt_.reserve( nEtaBins() );
    tagCSVDataPt_.reserve( nEtaBins() );
    for ( unsigned uEta = 0; uEta < nEtaBins(); ++uEta ) {
      DataTable ptGenJetEtaBin( nPtBins() );
      DataTable etaGenJetEtaBin( nPtBins() );
      DataTable phiGenJetEtaBin( nPtBins() );
      DataTable tagCSVEtaBin( nPtBins() );
      std::vector< unsigned > sizePt( nPtBins() );
      for ( unsigned uEntry = 0; uEntry < sizeEta( uEta ); ++uEntry ) {
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
        Double_t ptGenJetVal;
        if ( useNonP ) {
          if ( energyGenJetData_[ uEta ][ uEntry ] == -9. )  {
            ptGenJetVal = -9.;
          }
          else {
            ptGenJetVal = useNonT ? energyGenJetData_[ uEta ][ uEntry ] : std::sqrt( std::pow( energyGenJetData_[ uEta ][ uEntry ], 2 ) + ( 1. - std::pow( std::cosh( etaGenJetData_[ uEta ][ uEntry ] ), 2 ) ) * std::pow( ptGenJetData_[ uEta ][ uEntry ], 2 ) );
          }
        }
        else {
          if ( ptGenJetData_[ uEta ][ uEntry ] == -9. )  {
            ptGenJetVal = -9.;
          }
          else {
            ptGenJetVal = useNonT ? ptGenJetData_[ uEta ][ uEntry ] * std::cosh( etaGenJetData_[ uEta ][ uEntry ] ) : ptGenJetData_[ uEta ][ uEntry ];
          }
        }
        for ( unsigned uPt = 0; uPt < nPtBins(); ++uPt ) {
          if ( ptBins()[ uPt ] <= ptRef && ptRef < ptBins()[ uPt + 1 ] ) {
            ptGenJetEtaBin[ uPt ].push_back( ptGenJetVal );
            etaGenJetEtaBin[ uPt ].push_back( etaGenJetData_[ uEta ][ uEntry ] );
            phiGenJetEtaBin[ uPt ].push_back( phiGenJetData_[ uEta ][ uEntry ] );
            tagCSVEtaBin[ uPt ].push_back( tagCSVData_[ uEta ][ uEntry ] );
            break;
          }
        } // loop: uPt < nPtBins()
      } // loop: uEntry < sizeEta_[ uEta ]
      ptGenJetDataPt_.push_back( ptGenJetEtaBin );
      etaGenJetDataPt_.push_back( etaGenJetEtaBin );
      phiGenJetDataPt_.push_back( phiGenJetEtaBin );
      tagCSVDataPt_.push_back( tagCSVEtaBin );
    }

  }

}
