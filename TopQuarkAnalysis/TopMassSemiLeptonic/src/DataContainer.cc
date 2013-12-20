#include "TopQuarkAnalysis/TopMassSemiLeptonic/interface/DataContainer.h"


#include <TTree.h>


using namespace my;


void DataContainer::loadPileUpWeights( bool usePileUp, const std::string & pileUp, TDirectory* dirInSel, Int_t maxEvents )
{
  Double_t pileUpWeight;
  TTree * pileUpData( ( TTree* )( dirInSel->Get( "Data" ) ) );
  pileUpData->SetBranchAddress( pileUp.c_str(), &pileUpWeight );
  Int_t nEntries( ( Int_t )pileUpData->GetEntries() );
  if ( 0 <= maxEvents && maxEvents < nEntries ) nEntries = maxEvents;
  for ( Int_t iEntry = 0; iEntry < nEntries; ++iEntry ) {
    pileUpData->GetEntry( iEntry );
    if ( usePileUp ) pileUpWeights_.push_back( pileUpWeight );
    else             pileUpWeights_.push_back( 1. );
  }
}
