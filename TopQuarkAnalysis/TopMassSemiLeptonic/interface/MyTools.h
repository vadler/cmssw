#ifndef TopQuarkPhysics_TopMassSemiLeptonic_MyTools_h
#define TopQuarkPhysics_TopMassSemiLeptonic_MyTools_h


#include <string>
#include <vector>

#include <TH1D.h>
#include <TH2D.h>
#include <TF1.h>
#include <TF2.h>
#include <TDirectory.h>


namespace my {

  void setParametersFitFrac( TF1 * fit, TH1D * histo, bool useBkgFunction = false );
  void setParametersFitDelta( TF1 * fit, TH1D * histo );
  void setParametersBkg( TF1 * fit, TF1 * bkg );

  std::string addDirectoryPointersSubFits( TDirectory* dirIn, std::vector< TDirectory* >& dirsInSubFit, TDirectory* dirOut, std::vector< TDirectory* >& dirsOutSubFit, std::vector< std::vector< TDirectory* > >& dirsOutSubFitEta, Bool_t useSymm, Bool_t useAlt, Bool_t refGen );

}


#endif
