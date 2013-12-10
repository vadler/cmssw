#ifndef TopQuarkPhysics_TopMassSemiLeptonic_FitTopTransferFunctionsRunner_h
#define TopQuarkPhysics_TopMassSemiLeptonic_FitTopTransferFunctionsRunner_h


#include <vector>
#include <string>

#include <TCanvas.h>

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "TopQuarkAnalysis/TopMassSemiLeptonic/interface/DataContainer.h"
#include "TopQuarkAnalysis/TopMassSemiLeptonic/interface/ObjectDataContainer.h"
#include "TopQuarkAnalysis/TopMassSemiLeptonic/interface/FitTopTransferFunctionsHistos.h"


namespace my {

  class FitTopTransferFunctionsRunner {

      std::string myName_;
      int         status_;
      // Config
      edm::ParameterSet          config_;
      unsigned                   verbose_;
      bool                       useSymm_;
      bool                       useAlt_;
      bool                       useNonT_;
      bool                       refGen_;
      bool                       scale_;
      int                        overwrite_;
      std::vector< std::string > objCats_;
      // Input
      TFile*                                   fileIn_;
      TDirectory*                              dirInSel_;
      std::vector< TDirectory* >               dirsInObjCat_;
      std::vector< TDirectory* >               dirsInObjCatSubFit_;
      my::DataContainer                        data_;
      // Output
      TFile*                                    fileOut_;
      TDirectory*                               dirOutSel_;
      std::vector< TDirectory* >                dirsOutObjCat_;
      std::vector< TDirectory* >                dirsOutObjCatSubFit_;
      std::vector< std::vector< TDirectory* > > dirsOutObjCatSubFitEta_;
      // Strings
      std::string baseTitlePt_;
      std::string titlePtT_;
      std::string titlePt_;
      std::string baseTitleEta_;
      std::string titleEta_;
      std::string titleTrans_;
//       std::string titleTransMean_;
//       std::string titleTransNorm_;
//       std::string titleTransSigma_;
      // Histograms
      std::vector< HistosTrans >                   histosVecRebinTrans_;
      std::vector< std::vector< HistosTransEta > > histosVecRebinVecTransEta_;

    public:

      FitTopTransferFunctionsRunner( const std::string& iName, const edm::ParameterSet& iConfig );
      ~FitTopTransferFunctionsRunner();

      int  run();
      bool fillPerCategory( unsigned uCat );
      void fillPerCategoryEta( const ObjectDataContainer& dataContainer, unsigned uEta, HistosTrans& histosTrans, HistosTransEta& histosTransEta, double minPt, double maxEta, double maxDR );
      bool fitPerCategory( unsigned uCat );

  };

}


#endif
