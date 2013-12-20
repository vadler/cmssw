#ifndef TopQuarkPhysics_TopMassSemiLeptonic_DataContainer_h
#define TopQuarkPhysics_TopMassSemiLeptonic_DataContainer_h


#include <vector>
#include <string>

#include <TROOT.h>
#include <TDirectory.h>


namespace my {

  struct DataContainer {

      DataContainer() {};
      ~DataContainer() {};

      void loadPileUpWeights( bool usePileUp, const std::string & pileUp, TDirectory* dirInSel, Int_t maxEvents = -1 );

      std::vector< Double_t > pileUpWeights() const { return pileUpWeights_; };

    private:

      std::vector< Double_t > pileUpWeights_;

  };

}


#endif
