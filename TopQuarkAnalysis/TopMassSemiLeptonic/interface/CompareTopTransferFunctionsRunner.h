#ifndef TopQuarkPhysics_TopMassSemiLeptonic_CompareTopTransferFunctionsRunner_h
#define TopQuarkPhysics_TopMassSemiLeptonic_CompareTopTransferFunctionsRunner_h


#include <vector>
#include <string>

#include <TFile.h>
#include <TDirectory.h>

#include "FWCore/ParameterSet/interface/ParameterSet.h"


namespace my {

  class CompareTopTransferFunctionsRunner {

      std::string myName_;
      int         status_;
      // Config
      edm::ParameterSet config_;
      unsigned          verbose_;
      bool              useSymm_;
      bool              useAlt_;
      bool              useNonT_;
      bool              refGen_;
      bool              refSel_;
      // Input
      unsigned                    size_;
      std::vector< std::string >  names_;
      std::vector< std::string >  fileNames_;
      std::vector< int >          cycles_;
      std::vector< TFile* >       filesIn_;
      std::vector< TDirectory* >  pwds_;

    public:

      CompareTopTransferFunctionsRunner( const std::string& iName, const edm::ParameterSet& iConfig );
      ~CompareTopTransferFunctionsRunner();

      int  run();

    private:

  };

}


#endif
