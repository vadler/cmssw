#include "TopQuarkAnalysis/TopMassSemiLeptonic/interface/FitTopTransferFunctionsDataContainer.h"


#include <TTree.h>


using namespace my;


void FitTopTransferFunctionsDataContainer::loadPileUpWeights( bool usePileUp, const std::string & pileUp, TDirectory* dirInSel )
{
  Double_t pileUpWeight;
  TTree * pileUpData( ( TTree* )( dirInSel->Get( "Data" ) ) );
  pileUpData->SetBranchAddress( pileUp.c_str(), &pileUpWeight );
  Int_t nEntries( ( Int_t )pileUpData->GetEntries() );
  for ( Int_t iEntry = 0; iEntry < nEntries; ++iEntry ) {
    pileUpData->GetEntry( iEntry );
    if ( usePileUp ) pileUpWeights.push_back( pileUpWeight );
    else             pileUpWeights.push_back( 1. );
  }
}
