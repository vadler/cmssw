#include "TopQuarkAnalysis/TopMassSemiLeptonic/interface/MyTools.h"

#include <TROOT.h>


void my::setParametersFitFrac( TF1 * fit, TH1D * histo, bool useBkgFunction )
{
  // Starting points
//   double m( histo->GetMean() );
//   double c( histo->GetBinContent( histo->FindBin( histo->GetMean() ) ) );
//   double m( histo->GetBinCenter( histo->GetMaximumBin() ) );
//   double c( histo->GetBinContent( histo->GetMaximumBin() ) );
  double m( 1. );
  double c( histo->GetBinContent( histo->FindBin( 1. ) ) );
// //   double c( histo->GetBinContent( histo->GetMaximumBin() ) * std::sqrt( TMath::TwoPi() ) * histo->GetRMS() );
  double s( histo->GetRMS() );
  // Gaussian part
  fit->SetParameter( 0, m );
  fit->SetParLimits( 0, 0., 2. );
  fit->SetParName( 0, "Gaussian #Mu" );
  fit->SetParameter( 1, c );
  fit->SetParLimits( 1, 0., 2. * c );
  fit->SetParName( 1, "Gaussian c" );
  fit->SetParameter( 2, s );
  fit->SetParLimits( 2, 0., 2. );
  fit->SetParName( 2, "Gaussian #sigma" );
  // Additional part
  if ( useBkgFunction ) {
//     fit->SetParameter( 3, log( (m-2.*s)*(m-2.*s) / std::sqrt( s*s + (m-2.*s)*(m-2.*s) ) ) );
    fit->SetParameter( 3, 0. );
    fit->SetParName( 3, "bkg #mu" );
    fit->SetParameter( 4, c ); // just a rough guess, which should serve both cases (highest peak in "signal" or background)
    fit->SetParLimits( 4, 0., 99. );
    fit->SetParName( 4, "bkg c" );
//     fit->SetParameter( 5, std::sqrt( log( s*s / (m-2.*s)*(m-2.*s) + 1. ) ) );
    fit->SetParameter( 5, 1. );
    fit->SetParLimits( 5, 0., 99. );
    fit->SetParName( 5, "bkg #sigma" );
  }
}


void my::setParametersFitDelta( TF1 * fit, TH1D * histo )
{
  // Starting points
  Double_t c( histo->Integral() );                             // Constant
  Double_t m( histo->GetMean() );                              // Mean
//   Double_t p( histo->GetBinCenter( histo->GetMaximumBin() ) ); // Peak
  Double_t s( histo->GetRMS() );                               // RMS
  // Gaussian part
  // Constant
  fit->SetParameter( 0, c );
//   fit->SetParLimits( 0, 0., 2. * c );
  fit->SetParName( 0, "Constant" );
  // Mean
  fit->SetParameter( 1, m );
  fit->SetParLimits( 1, -2. * s, 2. * s );
  fit->SetParName( 1, "Gaussian #Mu" );
  // Sigma
  fit->SetParameter( 2, s );
  fit->SetParLimits( 2, 0., 2. * s );
  fit->SetParName( 2, "Gaussian #sigma" );
}


void my::setParametersBkg( TF1 * fit, TF1 * bkg )
{
  Int_t n( fit->GetNumberFreeParameters() );
  for ( Int_t i = 3; i < n; ++i ) {
    bkg->SetParameter( i, fit->GetParameter( i ) );
  }
}


#include <cmath>


void my::initialiseFitParameters( TF1* fit, TH1D const* histo, const std::string& fitFuncId, bool scale )
{
  //. This function assumes fit functions of the forms
  // - [0]*exp(-0.5*((x-[1])/[2])**2)/([2]*sqrt(2*pi)) (single Gaissian) or
  // - [0]*(exp(-0.5*((x-[1])/[2])**2)+[3]*exp(-0.5*((x-[4])/[5])**2))/(([2]+[3]*[5])*sqrt(2*pi)) (double Gaussian)

  // Starting points
  const Double_t c( scale ? 1. : histo->Integral("width") );         // Constant
  const Double_t m( histo->GetMean() );                              // Mean
  const Double_t p( histo->GetBinCenter( histo->GetMaximumBin() ) ); // Peak
  const Double_t s( histo->GetRMS() );                               // RMS
  Double_t fitMin, fitMax;
  fit->GetRange( fitMin, fitMax );                                   // function's fit limits

  // Single Gaussian case
  if ( fitFuncId == "sGauss" ) {
    fit->SetParameter( 0, c );
    fit->SetParName( 0, "c" );
    fit->SetParameter( 1, p );
    fit->SetParName( 1, "#mu" );
    fit->SetParameter( 2, sqrt( s - m ) );
    fit->SetParName( 2, "#sigma" );
  }

  // Double Gaussian case
  if ( fitFuncId == "dGauss" ) {
    fit->SetParName( 0, "Signal c" );
    fit->SetParName( 1, "Signal #mu" );
    fit->SetParName( 2, "Signal #sigma" );
    fit->SetParName( 3, "Bkg c" );
    fit->SetParName( 4, "Bkg #mu" );
    fit->SetParName( 5, "Bkg #sigma" );
    fit->SetParameter( 0, c );
    fit->SetParameter( 1, p );
    fit->SetParLimits( 1, fitMin, fitMax );
    fit->SetParameter( 2, sqrt( s - m ) );
    fit->SetParLimits( 2, 0., 2. * s );
    fit->SetParameter( 3, 0.25 );
    fit->SetParLimits( 3, 0., 100. );
    fit->SetParameter( 4, 2 * m - p );
    fit->SetParLimits( 4, fitMin, fitMax );
    fit->SetParameter( 5, ( fitMax - fitMin ) / 4. );
    fit->SetParLimits( 5, 0., fitMax - fitMin );
  }

  // Crystal Ball cases
  if ( fitFuncId == "lCB" ) {
    // par = 1: mean
    // par = 2: sigma > 0.
    // par = 3: alpha > 0.
    // par = 4: exponent > 0.
    fit->SetParameter( 0, c );
    fit->SetParLimits( 0, 0., 100. );
    fit->SetParName( 0, "c" );
    fit->SetParameter( 1, p );
    fit->SetParName( 1, "#mu" );
    fit->SetParameter( 2, sqrt( s - m ) );
    fit->SetParLimits( 2, 0., 100. );
    fit->SetParName( 2, "#sigma" );
    fit->SetParameter( 3, 1. );
    fit->SetParLimits( 3, 0., 100. );
    fit->SetParName( 3, "#alpha_{l}" );
    fit->SetParameter( 4, 1. );
    fit->SetParName( 4, "n_{l}" );
//     fit->SetParLimits( 4, 1., 100. );
  }
  else if ( fitFuncId == "uCB" ) {
    // par = 1: mean
    // par = 2: sigma > 0.
    // par = 3: alpha > 0.
    // par = 4: exponent > 0.
    fit->SetParameter( 0, c );
    fit->SetParLimits( 0, 0., 100. );
    fit->SetParName( 0, "c" );
    fit->SetParameter( 1, p );
    fit->SetParName( 1, "#mu" );
    fit->SetParameter( 2, sqrt( s - m ) );
    fit->SetParLimits( 2, 0., 100. );
    fit->SetParName( 2, "#sigma" );
    fit->SetParameter( 3, 1. );
    fit->SetParLimits( 3, 0., 100. );
    fit->SetParName( 3, "#alpha_{u}" );
    fit->SetParameter( 4, 1. );
    fit->SetParName( 4, "n_{u}" );
//     fit->SetParLimits( 4, 1., 100. );
  }
  else if ( fitFuncId == "dCB" ) {
    // par = 1: mean
    // par = 2: sigma > 0.
    // par = 3: alpha low > 0.
    // par = 4: exponent low > 0.
    // par = 5: alpha up > 0.
    // par = 6: exponent up > 0.
    fit->SetParameter( 0, c );
    fit->SetParLimits( 0, 0., 100. );
    fit->SetParName( 0, "c" );
    fit->SetParameter( 1, p );
    fit->SetParName( 1, "#mu" );
    fit->SetParameter( 2, sqrt( s - m ) );
    fit->SetParLimits( 2, 0., 100. );
    fit->SetParName( 2, "#sigma" );
    fit->SetParameter( 3, 1. );
    fit->SetParLimits( 3, 0., 100. );
    fit->SetParName( 3, "#alpha_{l}" );
    fit->SetParameter( 4, 1. );
    fit->SetParName( 4, "n_{l}" );
//     fit->SetParLimits( 4, 1., 100. );
    fit->SetParameter( 5, 1. );
    fit->SetParLimits( 5, 0., 100. );
    fit->SetParName( 5, "#alpha_{u}" );
    fit->SetParameter( 6, 1. );
    fit->SetParName( 6, "n_{u}" );
//     fit->SetParLimits( 6, 1., 100. );
  }

}

void my::initialiseDependencyParameters( TF1* dep, TH1D const* histo, const std::string& depFuncId )
{
  if ( depFuncId == "resolution" ) {
    dep->SetParameter( 0, 0. );
    dep->SetParName( 0, "Noise N" );
    dep->SetParameter( 1, 0. );
    dep->SetParName( 1, "Resolution R" );
    dep->SetParameter( 2, 0. );
    dep->SetParName( 2, "Constant C" );
    return;
  }
  // Constant
  dep->SetParName( 0, "Constant a" );
  // Slope
  dep->SetParName( 1, "Slope b" );
  // Curvature
  if ( depFuncId == "squared" ) {
    dep->SetParameter( 2, 0. );
    dep->SetParName( 2, "Curvature c" );
  }
  // Starting points
  Int_t minBin( 0 );
  Int_t maxBin( histo->GetNbinsX() + 1 );
  for ( Int_t bin = 1; bin <= histo->GetNbinsX(); ++bin ) {
    if ( histo->GetBinContent( bin ) != 0. ) {
      minBin = bin;
      break;
    }
  }
  for ( Int_t bin = histo->GetNbinsX(); bin > minBin; --bin ) {
    if ( histo->GetBinContent( bin ) != 0. ) {
      maxBin = bin;
      break;
    }
  }
  if ( ( minBin == 0 || maxBin == histo->GetNbinsX() + 1 ) || minBin == maxBin ) {
    // Constant
    dep->SetParameter( 0, 0. );
    dep->SetParLimits( 0, 0., 100. );
    // Slope
    dep->SetParameter( 1, 0. );
    return;
  }
  Double_t x1( histo->GetBinCenter( minBin ) );
  Double_t y1( histo->GetBinContent( minBin ) );
  Double_t x2( histo->GetBinCenter( maxBin ) );
  Double_t y2( histo->GetBinContent( maxBin ) );
  // Constant
  dep->SetParameter( 0, ( x2 * y1 - x1 * y2 ) / ( x2 - x1 ) );
  // Slope
  dep->SetParameter( 1, ( y2 - y1 ) / ( x2 - x1 ) );
}

// FIXME
void my::initialiseTransferParameters( TF2* fit, TH2D const* histo, const std::string& fitFuncId, const std::string& depFuncId, const std::string& resFuncId )
{
  for ( Int_t uPar = 0; uPar < fit->GetNpar(); ++uPar ) {
    fit->SetParameter( uPar, 0. );
  }
}

bool my::checkParametersDoubleGaussian( TF1 const* fit, const std::string& fitFuncId )
{
  //. This function assumes fit functions of the form
  // - [0]*(exp(-0.5*((x-[1])/[2])**2) + [3]*exp(-0.5*((x-[4])/[5])**2))/(([2]+[3]*[5])*sqrt(2*pi)) (double Gaussian)
  if ( fitFuncId != "dGauss" ) return false;
//   if ( fit->GetParameter( 2 ) < fit->GetParameter( 5 ) ) return false;
  if ( fit->GetParameter( 2 ) < fit->GetParameter( 5 ) || std::fabs( fit->GetParameter( 3 ) ) < 1. ) return false;
  std::cout << std::endl
            << " --> WARNING:" << std::endl
            << "    function " << fit->GetName() << " mixed parameters." << std::endl;
  return true; // incorrect assignment assumed!
}

void my::mixParametersDoubleGaussian( TransferFunction& transfer, TF1 const* fit )
{
  //. This function assumes fit functions of the form
  // - [0]*(exp(-0.5*((x-[1])/[2])**2) + [3]*exp(-0.5*((x-[4])/[5])**2))/(([2]+[3]*[5])*sqrt(2*pi)) (double Gaussian)
  transfer.SetParameter( 0, fit->GetParameter( 0 ) );
  transfer.SetError( 0, fit->GetParError( 0 ) );
  transfer.SetParameter( 1, fit->GetParameter( 4 ) );
  transfer.SetError( 1, fit->GetParError( 4 ) );
  transfer.SetParameter( 2, fit->GetParameter( 5 ) );
  transfer.SetError( 2, fit->GetParError( 5 ) );
  transfer.SetParameter( 3, 1. / fit->GetParameter( 3 ) );
  transfer.SetError( 3, fit->GetParError( 3 ) / (fit->GetParameter( 3 ) * fit->GetParameter( 3 ) ) );
  transfer.SetParameter( 4, fit->GetParameter( 1 ) );
  transfer.SetError( 4, fit->GetParError( 1 ) );
  transfer.SetParameter( 5, fit->GetParameter( 2 ) );
  transfer.SetError( 5, fit->GetParError( 2 ) );
}


#include <TKey.h>
#include <TDirectoryFile.h>

std::string my::addDirectoryPointersSubFits( TDirectory* dirIn, std::vector< TDirectory* >& dirsInSubFit, TDirectory* dirOut, std::vector< TDirectory* >& dirsOutSubFit, std::vector< std::vector< TDirectory* > >& dirsOutSubFitEta, Bool_t useSymm, Bool_t useAlt, Bool_t refGen )
{
  TList* listProp( dirIn->GetListOfKeys() );
  TIter nextInListProp( listProp );
  while ( TKey* keyFit = ( TKey* )nextInListProp() ) {
    if ( std::string( keyFit->GetClassName() ) != "TDirectoryFile" ) continue;
    const std::string subFit( keyFit->GetName() );
    if ( subFit.find( "Inv" ) != std::string::npos ) continue; // nothing to do for inverse
    // These are real switches: depending on configuration, only one setting combination can be run at a time
    if ( useAlt  == ( subFit.find( "Alt" )  == std::string::npos ) ) continue;
    if ( useSymm == ( subFit.find( "Symm" ) == std::string::npos ) ) continue;
    if ( refGen  == ( subFit.find( "Gen" )  == std::string::npos ) ) continue;
    TDirectory* dirInSubFit( ( TDirectory* )( dirIn->Get( subFit.c_str() ) ) );
    if ( ! dirInSubFit ) {
      std::cout << "my::addDirectoryPointersSubFits --> ERROR:" << std::endl
                << "    fit '" << subFit << "' does not exist in input file" << std::endl;
      continue;
    }
    dirsInSubFit.push_back( dirInSubFit );
    TDirectory* dirOutSubFit( ( TDirectory* )( dirOut->Get( subFit.c_str() ) ) );
    if ( ! dirOutSubFit ) {
      dirOut->cd();
      dirOutSubFit = new TDirectoryFile( subFit.c_str(), "Particular fit" );
    }
    dirsOutSubFit.push_back( dirOutSubFit );
    // Eta bins
    std::vector< TDirectory* > dirsOutEta;
    TList* listFit( dirInSubFit->GetListOfKeys() );
    TIter nextInListFit( listFit );
    while ( TKey* keyEta = ( TKey* )nextInListFit() ) {
      if ( std::string( keyEta->GetClassName() ) != "TDirectoryFile" ) continue;
      const std::string binEta( keyEta->GetName() );
      TDirectory* dirOutEta( ( TDirectory* )( dirOutSubFit->Get( binEta.c_str() ) ) );
      if ( ! dirOutEta ) {
        dirOutSubFit->cd();
        dirOutEta = new TDirectoryFile( binEta.c_str(), "Eta bin" );
      }
      dirsOutEta.push_back( dirOutEta );
    }
    dirsOutSubFitEta.push_back( dirsOutEta );
    return subFit;
  }
  return std::string();
}
