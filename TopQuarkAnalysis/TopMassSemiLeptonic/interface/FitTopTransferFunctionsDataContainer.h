#ifndef TopQuarkPhysics_TopMassSemiLeptonic_FitTopTransferFunctionsDataContainer_h
#define TopQuarkPhysics_TopMassSemiLeptonic_FitTopTransferFunctionsDataContainer_h


#include <vector>
#include <string>

#include <TROOT.h>
#include <TDirectory.h>


namespace my {

  struct FitTopTransferFunctionsDataContainer {

    FitTopTransferFunctionsDataContainer() {};
    ~FitTopTransferFunctionsDataContainer() {};

    std::vector< Double_t > pileUpWeights;

    void loadPileUpWeights( bool usePileUp, const std::string & pileUp, TDirectory* dirInSel );

  };

}


#endif
