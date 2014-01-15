#ifndef TopQuarkPhysics_TopMassSemiLeptonic_MyTools_h
#define TopQuarkPhysics_TopMassSemiLeptonic_MyTools_h


#include <string>
#include <vector>

#include <TH1D.h>
#include <TH2D.h>
#include <TF1.h>
#include <TF2.h>
#include <TDirectory.h>

#include "TopQuarkAnalysis/TopMassSemiLeptonic/interface/TransferFunction.h"


namespace my {

  void setParametersFitFrac( TF1 * fit, TH1D * histo, bool useBkgFunction = false );
  void setParametersFitDelta( TF1 * fit, TH1D * histo );
  void setParametersBkg( TF1 * fit, TF1 * bkg );

  void initialiseFitParameters( TF1* fit, TH1D const* histo, const std::string& fitFuncId, bool scale );
  void initialiseDependencyParameters( TF1* dep, TH1D const* histo, const std::string& depFuncId );
  void initialiseTransferParameters( TF2* fit, TH2D const* histo, const std::string& fitFuncId, const std::string& depFuncId, const std::string& resFuncId );
  bool checkParametersDoubleGaussian( TF1 const* fit, const std::string& fitFuncId );
  void mixParametersDoubleGaussian( TransferFunction& transfer, TF1 const* fit );

  std::string addDirectoryPointersSubFits( TDirectory* dirIn, std::vector< TDirectory* >& dirsInSubFit, TDirectory* dirOut, std::vector< TDirectory* >& dirsOutSubFit, std::vector< std::vector< TDirectory* > >& dirsOutSubFitEta, Bool_t useSymm, Bool_t useAlt, Bool_t refGen );

}


#endif
