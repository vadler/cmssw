#ifndef TopQuarkPhysics_TopMassSemiLeptonic_FitTopTransferFunctionsRunner_h
#define TopQuarkPhysics_TopMassSemiLeptonic_FitTopTransferFunctionsRunner_h


#include <vector>
#include <string>

#include <TF1.h>

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "CommonTools/MyTools/interface/RootFunctions.h"
#include "TopQuarkAnalysis/TopMassSemiLeptonic/interface/DataContainer.h"
#include "TopQuarkAnalysis/TopMassSemiLeptonic/interface/ObjectDataContainer.h"
#include "TopQuarkAnalysis/TopMassSemiLeptonic/interface/FitTopTransferFunctionsHistos.h"
#include "TopQuarkAnalysis/TopMassSemiLeptonic/interface/TransferFunction.h"


namespace my {

  class FitTopTransferFunctionsRunner {

      std::string myName_;
      int         status_;
      // Config
      edm::ParameterSet          config_;
      unsigned                   verbose_;
      int                        maxEvents_; // FIXME: still needs to be propageted
      bool                       useSymm_;
      bool                       useAlt_;
      bool                       useNonT_;
      bool                       refGen_;
      bool                       writeFiles_;
      bool                       fit0D_;
      bool                       fit1D_;
      bool                       fit2D_;
      bool                       refSel_;
      bool                       usePileup_;
      int                        overwrite_;
      std::string                sample_;
      std::string                pathOut_;
      bool                       plot_;
      std::string                pathPlots_;
      std::vector< std::string > formatPlots_;
      std::vector< std::string > objCats_;
      std::string                fitFuncID_;
      std::string                depFuncID_;
      std::string                resFuncID_;
      std::string                fitOptions_;
      double                     fitRange_;
      unsigned                   minEntriesFactor_;
      std::vector< unsigned >    excludeVec_;
      bool                       fitEtaBins_;
      double                     fitMaxPt_;
      // Input
      TFile*                                   fileIn_;
      TDirectory*                              dirInSel_;
      std::vector< TDirectory* >               dirsInObjCat_;
      std::vector< TDirectory* >               dirsInObjCatSubFit_;
      my::DataContainer                        data_;
      std::vector< my::ObjectDataContainer >   objectData_;
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
      // Functions
      TF1* fitFunction_;
      TF1* dependencyFunction_;
      TF1* resolutionFunction_;
      // Histograms
      std::vector< HistosTrans >                   histosVecRebinTrans_;
      std::vector< std::vector< HistosTransEta > > histosVecRebinVecTransEta_;
      std::vector< HistosTrans >                   histosVecRebinScaleTrans_;
      std::vector< std::vector< HistosTransEta > > histosVecRebinScaleVecTransEta_;
      std::vector< HistosDependency >                histosVecRebinDependency_;
      std::vector< std::vector< HistosDependency > > histosVecRebinVecDependencyEta_;
      std::vector< HistosDependency >                histosVecRebinScaleDependency_;
      std::vector< std::vector< HistosDependency > > histosVecRebinScaleVecDependencyEta_;
      // Transfer functions
      std::vector< TransferFunction >                          transferVecRebin_;
      std::vector< TransferFunctionCollection >                transferVecRebinVecPt_;            // for 1-D only
      std::vector< TransferFunctionCollection >                transferVecRebinVecEta_;
      std::vector< std::vector< TransferFunctionCollection > > transferVecRebinVecEtaVecPt_;      // for 1-D only
      std::vector< TransferFunction >                          transferVecRebinScale_;
      std::vector< TransferFunctionCollection >                transferVecRebinScaleVecPt_;       // for 1-D only
      std::vector< TransferFunctionCollection >                transferVecRebinScaleVecEta_;
      std::vector< std::vector< TransferFunctionCollection > > transferVecRebinScaleVecEtaVecPt_; // for 1-D only
      // Compatibility // FIXME: Still need to be propagated to output
      std::vector< std::vector< Double_t > >                pChi2VecRebinVecTrans_;
      std::vector< Double_t >                               avPChi2VecRebinTrans_;
      std::vector< std::vector< std::vector< Double_t > > > pChi2VecRebinVecTransEta_;
      std::vector< std::vector< Double_t > >                avPChi2VecRebinTransEta_;
      std::vector< std::vector< Double_t > >                pKSVecRebinVecTrans_;
      std::vector< Double_t >                               avKSVecRebinTrans_;
      std::vector< std::vector< std::vector< Double_t > > > pKSVecRebinVecTransEta_;
      std::vector< std::vector< Double_t > >                avPKSVecRebinTransEta_;
      //
      std::vector< std::vector< Double_t > >                pChi2VecRebinScaleVecTrans_;
      std::vector< Double_t >                               avPChi2VecRebinScaleTrans_;
      std::vector< std::vector< std::vector< Double_t > > > pChi2VecRebinScaleVecTransEta_;
      std::vector< std::vector< Double_t > >                avPChi2VecRebinScaleTransEta_;
      std::vector< std::vector< Double_t > >                pKSVecRebinScaleVecTrans_;
      std::vector< Double_t >                               avKSVecRebinScaleTrans_;
      std::vector< std::vector< std::vector< Double_t > > > pKSVecRebinScaleVecTransEta_;
      std::vector< std::vector< Double_t > >                avPKSVecRebinScaleTransEta_;

    public:

      FitTopTransferFunctionsRunner( const std::string& iName, const edm::ParameterSet& iConfig );
      ~FitTopTransferFunctionsRunner();

      int  run();
      bool fillPerCategory( unsigned uCat );
      bool fitPerCategory( unsigned uCat );
      bool dependencyPerCategory( unsigned uCat );
      bool transferPerCategory( unsigned uCat );
      bool compatibilityPerCategory( unsigned uCat );
      bool writeFilesPerCategory( unsigned uCat );

      template< typename FitFuncType, typename DepFuncType, typename ResFuncType = my::ResolutionLike >
      TransferFunction initialiseFunctions( TF1* fitFunction, TF1* dependencyFunction, TF1* resolutionFunction )
      {
        // ROOT functions
        FitFuncType* fitFunc( new FitFuncType() );
        *fitFunction = TF1( "fitFunction", fitFunc, 0., 1., FitFuncType::NPar() );
        DepFuncType* depFunc( new DepFuncType() );
        *dependencyFunction = TF1( "dependencyFunction", depFunc, 0., 1., DepFuncType::NPar() );
        ResFuncType* resFunc( new ResFuncType() );
        *resolutionFunction = TF1( "resolutionFunction", resFunc, 0., 1., ResFuncType::NPar() );

        // Transfer function
        const std::string part( refGen_ ? "_parton" : "_reco" );
        TransferFunction transfer( fitFunction, FitFuncType::SigmaPars(), dependencyFunction, resolutionFunction, std::string( titlePtT_ + part ) );
        transfer.SetFitFunctionString( FitFuncType::String() );
        transfer.SetDependencyFunctionString( DepFuncType::String() );
        transfer.SetResolutionFunctionString( ResFuncType::String() );

        return transfer;
      }

    private:

      /// These functions are private, since their use underlies certain restrictions, like e.g.:
      /// - run only once;
      /// - run only during first loop over categories due to the usage of std::vector::back().
      void fillPerCategoryBin( unsigned uEta, HistosTrans& histosTrans, HistosTransEta& histosTransEta, double minPt, double maxEta, double maxDR, bool scale = false );
      void plotFillPerCategoryBin( HistosTrans& histosTrans );
      void fitPerCategoryLoop( const std::string& objCat, bool scale = false );
      void fitPerCategoryBin( const std::string& objCat, TDirectory* dirOut, TransferFunction& transfer, TransferFunctionCollection& transferColl, HistosTransEta& histosTransEta, std::vector< HistosDependency >& histosVecDependency, bool scale = false );
      void fitPerCategoryFit( TransferFunction& transfer, TH1D* histoTrans, HistosDependency* histosDependency, int uPt, bool scale = false );
      void dependencyPerCategoryLoop( const std::string& objCat, bool scale = false );
      void dependencyPerCategoryBin( const std::string& objCat, TDirectory* dirOut, TransferFunction& transfer, HistosDependency& histosVecDependency, bool scale = false );
      void transferPerCategoryLoop( const std::string& objCat, bool scale = false );
      void transferPerCategoryBin( const std::string& objCat, TDirectory* dirOut, TransferFunction& transfer, HistosTransEta& histosTransEta, bool scale = false );
      void compatibilityPerCategoryLoop( const std::string& objCat, bool scale = false );
      void compatibilityPerCategoryBin( const std::string& objCat, TDirectory* dirOut, TransferFunction& transfer, HistosTransEta& histosTransEta, int uEta, bool scale = false );
      void writeFilesPerCategoryLoop( const std::string& objCat, bool scale = false );
      void writeFilesPerCategoryBin( const std::string& objCat, TransferFunction& transfer, const std::string& name, int uPt, int uEta, bool scale = false );

  };

}


#endif
