#ifndef TopQuarkPhysics_TopMassSemiLeptonic_FitTopTransferFunctionsRunner_h
#define TopQuarkPhysics_TopMassSemiLeptonic_FitTopTransferFunctionsRunner_h


#include <vector>
#include <string>

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "TopQuarkAnalysis/TopMassSemiLeptonic/interface/FitTopTransferFunctionsDataContainer.h"


namespace my {

  class FitTopTransferFunctionsRunner {

      std::string name_;
      int         status_;
      // Config
      edm::ParameterSet          config_;
      bool                       verbose_;
      bool                       overwrite_;
      std::vector< std::string > objCats_;
      std::string fitFunction_;
      std::string dependencyFunction_;
      // Input
      TFile*                                   fileIn_;
      TDirectory*                              dirInSel_;
      my::FitTopTransferFunctionsDataContainer data_;
      // Output
      TFile*      fileOut_;
      TDirectory* dirOutSel_;

    public:

      FitTopTransferFunctionsRunner( const std::string& iName, const edm::ParameterSet& iConfig );
      ~FitTopTransferFunctionsRunner();

      int  run();
      void runPerCategory( const std::string& objCat );

  };

}


#endif
