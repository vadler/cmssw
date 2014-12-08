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
      // Input
      size_t                                    size_;
      size_t                                    default_;
      std::vector< std::string >                names_;
      std::vector< std::string >                fileNames_;
      std::vector< std::string >                legendLabels_;
      std::vector< bool >                       useAlt_;
      std::vector< bool >                       useNonT_;
      std::vector< bool >                       useNonP_;
      std::vector< bool >                       refGen_;
      std::vector< bool >                       refSel_;
      std::vector< int >                        cycles_;
      std::vector< TFile* >                     filesIn_;
      std::vector< std::string >                objCats_;
      std::vector< std::string >                strPt_;
      std::vector< std::string >                subFits_;
      std::vector< TDirectory* >                pwds_;
      std::vector< std::vector< TDirectory* > > pwdsEta_;
      std::vector< std::vector< std::string > > histos_;
      std::vector< std::vector< std::vector< std::string > > > histosEta_;

    public:

      CompareTopTransferFunctionsRunner( const std::string& iName, const edm::ParameterSet& iConfig );
      ~CompareTopTransferFunctionsRunner();

      int  run();

    private:

  };

}


#endif
