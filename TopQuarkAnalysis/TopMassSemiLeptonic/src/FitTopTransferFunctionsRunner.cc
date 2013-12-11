#include "TopQuarkAnalysis/TopMassSemiLeptonic/interface/FitTopTransferFunctionsRunner.h"

#include <cassert>
#include <iostream>
#include <iomanip>
#include <sstream>

#include <TROOT.h>
#include <TStyle.h>
#include <TObject.h>
#include <TFile.h>
#include <TCanvas.h>
#include <TH1D.h>
#include <TH2D.h>
#include <TFitResult.h>
#include <TKey.h>

#include "DataFormats/Math/interface/deltaR.h"

#include "CommonTools/MyTools/interface/RootTools.h"
#include "TopQuarkAnalysis/TopMassSemiLeptonic/interface/MyTools.h"


using namespace my;


FitTopTransferFunctionsRunner::FitTopTransferFunctionsRunner( const std::string& iName, const edm::ParameterSet& iConfig )
: myName_( iName )
, status_( 0 )
, config_( iConfig )
, verbose_( config_.getParameter< unsigned >( "verbose" ) )
, useSymm_( config_.getParameter< bool >( "useSymm" ) )
, useAlt_( config_.getParameter< bool >( "useAlt" ) )
, useNonT_( config_.getParameter< bool >( "useNonT" ) )
, refGen_( config_.getParameter< bool >( "refGen" ) )
, scale_( config_.getParameter< bool >( "scale" ) )
, overwrite_( config_.getParameter< bool >( "overwrite" ) ? TObject::kOverwrite : 0 )
, objCats_( config_.getParameter< edm::ParameterSet >( "objects" ).getParameterNamesForType< edm::ParameterSet >() )
{

  if ( verbose_ > 1 ) {
    std::cout << std::endl
              << myName_ << " --> INFO:" << std::endl
              << "    called for object categories ";
    for ( unsigned uCat = 0; uCat < objCats_.size() - 1; ++uCat ) {
      std::cout << "'" << objCats_.at( uCat ) << "', ";
    }
    std::cout << "'" << objCats_.back() << "'" << std::endl;
  }

  const edm::ParameterSet& configIO( config_.getParameter< edm::ParameterSet >( "io" ) );
  const bool         configIOFullStats( configIO.getParameter< bool >( "fullStats" ) );
  const std::string& configIOInFile( configIO.getParameter< std::string >( "inputFile" ) );
  const bool         configIORefSel( configIO.getParameter< bool >( "refSel" ) );
  const bool         configIOUsePileUp( configIO.getParameter< bool >( "usePileUp" ) );
  const std::string& configIOPileUp( configIO.getParameter< std::string >( "pileUp" ) );
  const std::string& configIOOutFile( configIO.getParameter< std::string >( "outputFile" ) );
  writeFiles_ = configIO.getParameter< bool >( "writeFiles" );
  plot_       = configIO.getParameter< bool >( "plot" );
  pathPlots_  = configIO.getParameter< std::string >( "pathPlots" );

  // Set up ROOT
  setPlotEnvironment( gStyle );
  if ( configIOFullStats ) {
    gStyle->SetOptStat( 111111 );
    gStyle->SetOptFit( 1111 );
  }
  TH1D::SetDefaultSumw2();
  TH2D::SetDefaultSumw2();

  // Set constants
  std::string evtSel( "analyzeHitFit" );
  if ( configIORefSel ) evtSel.append( "Reference" );
  const std::string baseTitlePtL( useAlt_ ? "E" : "p" );
  const std::string baseTitlePtU( useAlt_ ? "E" : "P" );
  baseTitlePt_     = useNonT_ ? baseTitlePtU : baseTitlePtU + "t";
  titlePtT_ = useNonT_ ? baseTitlePtL : baseTitlePtL + "_{t}";
  titlePt_         = refGen_ ? titlePtT_ + "^{GEN} (GeV)" : titlePtT_ + " (GeV)";
  baseTitleEta_    = useSymm_ ? "|#eta|" : "#eta";
  titleEta_        = refGen_ ? baseTitleEta_ + "^{GEN}" : baseTitleEta_ + "^{RECO}";
  titleTrans_      = "#Delta" + titlePtT_ + " (GeV)";
//   titleTransMean_  = "#mu of " + titleTrans_;
//   titleTransNorm_  = "c of " + titleTrans_;
//   titleTransSigma_ = "#sigma of " + titleTrans_;

  // Open input file
  if ( verbose_ > 1 ) {
    std::cout << myName_ << " --> INFO:" << std::endl
              << "    using input file '" << configIOInFile  << "'" << std::endl;
  }
  fileIn_ = TFile::Open( configIOInFile.c_str(), "READ" );
  if ( ! fileIn_ ) {
    std::cout << myName_ << " --> ERROR:" << std::endl
              << "    input file '" << configIOInFile << "' missing" << std::endl;
    status_ += 0x10;
  }
  dirInSel_ = ( TDirectory* )( fileIn_->Get( evtSel.c_str() ) );
  if ( ! dirInSel_ ) {
    std::cout << myName_ << " --> ERROR:" << std::endl
              << "    selection '" << evtSel << "' does not exist in input file" << std::endl;
    status_ += 0x20;
  }

  // Load pile-up data
  data_.loadPileUpWeights( configIOUsePileUp, configIOPileUp, dirInSel_ );

  // Open output file
  fileOut_ = TFile::Open( configIOOutFile.c_str(), "UPDATE" );
  if ( ! fileOut_ ) {
    fileOut_ = TFile::Open( configIOOutFile.c_str(), "NEW" );
  }
  if ( ! fileOut_ ) {
    std::cout << myName_ << " --> ERROR:" << std::endl
              << "    output file '" << configIOOutFile << "' could not be opened" << std::endl;
    status_ += 0x30;
  }
  dirOutSel_ = ( TDirectory* )( fileOut_->Get( evtSel.c_str() ) );
  if ( ! dirOutSel_ ) {
    fileOut_->cd();
    dirOutSel_ = new TDirectoryFile( evtSel.c_str(), std::string( configIORefSel ? "Reference selection" : "Basic selection" ).c_str() );
  }
  else {
    if ( overwrite_ == TObject::kOverwrite ) {
      if ( verbose_ > 0 ) {
        std::cout << myName_ << " --> WARNING:" << std::endl
                  << "    existing output will be overwritten in '" << configIOInFile  << ":" << evtSel << "'" << std::endl;
      }
    }
    else if ( verbose_ > 1 ) {
      std::cout << myName_ << " --> INFO:" << std::endl
                << "    output will be appended as new cycle in '" << configIOInFile  << ":" << evtSel << "'" << std::endl;
    }
  }
  if ( verbose_ > 2 ) gDirectory->pwd();
}


FitTopTransferFunctionsRunner::~FitTopTransferFunctionsRunner()
{
  // Write and close ROOT files
  fileIn_->Close();
  Int_t writeOut( fileOut_->Write( 0, overwrite_ ) );
  fileOut_->Close();
  if ( verbose_ > 2 )
    std::cout << std::endl
              << myName_ << " --> DEBUG:" << std::endl
              << "    return status   " << status_ << std::endl
              << "    " << writeOut << " bytes written to output file" << std::endl;
}


int FitTopTransferFunctionsRunner::run()
{

  // Clear vectors
  dirsInObjCat_.clear();
  dirsInObjCatSubFit_.clear();
  dirsOutObjCat_.clear();
  dirsOutObjCatSubFit_.clear();
  dirsOutObjCatSubFitEta_.clear();

  // Reserve vectors
  dirsInObjCat_.reserve( objCats_.size() );
  dirsInObjCatSubFit_.reserve( objCats_.size() );
  dirsOutObjCat_.reserve( objCats_.size() );
  dirsOutObjCatSubFit_.reserve( objCats_.size() );
  dirsOutObjCatSubFitEta_.reserve( objCats_.size() );

  // Run per objects category
  for ( unsigned uCat = 0; uCat < objCats_.size(); ++uCat ) {
    if ( ! fillPerCategory( uCat ) ) {
      status_ += 0x100;
      return status_ ;
    }
    if ( ! fitPerCategory( uCat ) ) {
      status_ += 0x200;
      return status_ ;
    }
  }

  return status_;

}


bool FitTopTransferFunctionsRunner::fillPerCategory( unsigned uCat )
{

  const std::string objCat( objCats_.at( uCat ) );
  if ( verbose_ > 1 ) {
    std::cout << std::endl
              << myName_ << " --> INFO:" << std::endl
              << "    filling for object categorie " << objCat << std::endl;
  }

  // Get object configuration
  const edm::ParameterSet& configObj( config_.getParameter< edm::ParameterSet >( "objects" ).getParameter< edm::ParameterSet >( objCat ) );
  const unsigned configObjDeltaPtBins( configObj.getParameter< unsigned >( "deltaPtBins" ) );
  const double configObjDeltaPtMax( configObj.getParameter< double >( "deltaPtMax" ) );
  const double configObjMinPt( configObj.getParameter< double >( "minPt" ) );
  const double configObjMaxEta( configObj.getParameter< double >( "maxEta" ) );
  const double configObjMaxDR( configObj.getParameter< double >( "maxDR" ) );
  const double configObjWidthFactor( configObj.getParameter< double >( "widthFactor" ) );

  // Open ROOT file directories
  TDirectory* dirInObjCat( ( TDirectory* )( dirInSel_->Get( objCat.c_str() ) ) );
  if ( ! dirInObjCat ) {
    if ( verbose_ > 1 ) {
      std::cout << myName_ << " --> WARNING:" << std::endl
                << "    object category '" << objCat << "' does not exist in input file" << std::endl;
    }
    return false;
  }
  dirsInObjCat_.push_back( dirInObjCat );
  TDirectory* dirOutObjCat( ( TDirectory* )( dirOutSel_->Get( objCat.c_str() ) ) );
  if ( ! dirOutObjCat ) {
    dirOutSel_->cd();
    if ( verbose_ > 2 ) gDirectory->pwd();
    dirOutObjCat = new TDirectoryFile( objCat.c_str(), std::string( objCat + " objects" ).c_str() );
  }
  dirsOutObjCat_.push_back( dirOutObjCat );

  // Read and sort data
  if ( verbose_ > 2 ) {
    std::cout << std::endl
              << myName_ << " --> DEBUG:" << std::endl
              << "    Reading data... " << std::endl;
  }
  ObjectDataContainer dataContainer( objCat, dirInObjCat, useSymm_, useAlt_, useNonT_, refGen_, data_ );
  // Caching
  const unsigned nPtBins( dataContainer.nPtBins() );

  // Find requested subdirectories
  TDirectory* dirInPt( ( TDirectory* )( dirInObjCat->Get( "Pt" ) ) );
  if ( ! dirInPt ) {
    std::cout << myName_ << " --> ERROR:" << std::endl
              << "    kinematic property 'Pt' does not exist in input file" << std::endl;
    return false;
  }
  TDirectory* dirOutPt( ( TDirectory* )( dirOutObjCat->Get( "Pt" ) ) );
  if ( ! dirOutPt ) {
    dirOutObjCat->cd();
    if ( verbose_ > 2 ) gDirectory->pwd();
    dirOutPt = new TDirectoryFile( "Pt", "Momentum variable" );
  }
  const std::string subFit( addDirectoryPointersSubFits( dirInPt, dirsInObjCatSubFit_, dirOutPt, dirsOutObjCatSubFit_, dirsOutObjCatSubFitEta_, useSymm_, useAlt_, refGen_ ) );
  if ( subFit.empty() ) {
    std::cout << myName_ << " --> ERROR:" << std::endl
              << "    requested fit does not exist in input file" << std::endl;
    return false;
  }
  // Caching
  assert( dataContainer.nEtaBins() == dirsOutObjCatSubFitEta_.back().size() );
  const unsigned nEtaBins( dirsOutObjCatSubFitEta_.back().size() );

  // Filling histograms
  if ( verbose_ > 2 ) {
    std::cout << std::endl
              << myName_ << " --> DEBUG:" << std::endl
              << "    Filling histograms... " << std::endl;
  }

  // Create histograms
  dirsOutObjCatSubFit_.back()->cd();
  if ( verbose_ > 2 ) gDirectory->pwd();
  std::string name( objCat + "_" + baseTitlePt_ + "_" + subFit );
  HistosTrans histosTrans( objCat, name, configObjDeltaPtBins, configObjDeltaPtMax, nPtBins, dataContainer.ptBins(), nEtaBins, dataContainer.etaBins(), titleTrans_, baseTitlePt_, titlePtT_, titlePt_, titleEta_ );

  // Loop over eta bins
  std::vector< HistosTransEta > histosVecTransEta;
  for ( unsigned uEta = 0; uEta < nEtaBins; ++uEta ) {
    // Create histograms
    dirsOutObjCatSubFitEta_.back().at( uEta )->cd();
    if ( verbose_ > 2 ) gDirectory->pwd();
    const std::string binEta( gDirectory->GetName() );
    const std::string nameEta( name + "_" + binEta );
    HistosTransEta histosTransEta( objCat, nameEta, configObjDeltaPtBins, configObjDeltaPtMax, nPtBins, dataContainer.ptBins(), titleTrans_, baseTitlePt_, titlePtT_, titlePt_, titleEta_ );
    // Fill
    fillPerCategoryBin( dataContainer, uEta, histosTrans, histosTransEta, configObjMinPt, configObjMaxEta, configObjMaxDR );
    if ( scale_ ) histosTransEta.scale();
    histosVecTransEta.push_back( histosTransEta );
  } // loop:uEta < nEtaBins
  if ( scale_ ) histosTrans.scale();

  // Re-bin histograms
  if ( verbose_ > 2 ) {
    std::cout << std::endl
              << myName_ << " --> DEBUG:" << std::endl
              << "    Re-binning histograms... " << std::endl;
  }

  // Create histograms
  dirsOutObjCatSubFit_.back()->cd();
  if ( verbose_ > 2 ) gDirectory->pwd();
  std::string nameRebin( name + "Rebin" );
  HistosTrans histosRebinTrans( objCat, nameRebin, configObjDeltaPtBins, configObjDeltaPtMax, nPtBins, dataContainer.ptBins(), nEtaBins, dataContainer.etaBins(), titleTrans_, baseTitlePt_, titlePtT_, titlePt_, titleEta_, histosTrans, configObjWidthFactor );

  // Loop over eta bins
  std::vector< HistosTransEta > histosRebinVecTransEta;
  for ( unsigned uEta = 0; uEta < nEtaBins; ++uEta ) {
    // Create histograms
    dirsOutObjCatSubFitEta_.back().at( uEta )->cd();
    if ( verbose_ > 2 ) gDirectory->pwd();
    const std::string binEta( gDirectory->GetName() );
    const std::string nameEtaRebin( nameRebin + "_" + binEta );
    HistosTransEta histosRebinTransEta( objCat, nameEtaRebin, configObjDeltaPtBins, configObjDeltaPtMax, nPtBins, dataContainer.ptBins(), titleTrans_, baseTitlePt_, titlePtT_, titlePt_, titleEta_, histosVecTransEta.at( uEta), configObjWidthFactor );
    // Fill
    fillPerCategoryBin( dataContainer, uEta, histosRebinTrans, histosRebinTransEta, configObjMinPt, configObjMaxEta, configObjMaxDR );
    if ( scale_ ) histosRebinTransEta.scale();
    histosRebinVecTransEta.push_back( histosRebinTransEta );
  } // loop:uEta < nEtaBins
  if ( scale_ ) histosRebinTrans.scale();
  histosVecRebinTrans_.push_back( histosRebinTrans );
  histosVecRebinVecTransEta_.push_back( histosRebinVecTransEta );

  return true;

}


void FitTopTransferFunctionsRunner::fillPerCategoryBin( const ObjectDataContainer& dataContainer, unsigned uEta, HistosTrans& histosTrans, HistosTransEta& histosTransEta, double minPt, double maxEta, double maxDR )
{
  // Loop over pt bins
  for ( unsigned uPt = 0; uPt < dataContainer.nPtBins(); ++uPt ) {
    if ( dataContainer.sizePt( uEta, uPt ) == 0 ) continue;
    // Loop over entries
    for ( unsigned uEntry = 0; uEntry < dataContainer.sizePt( uEta, uPt ); ++uEntry ) {
      const Double_t ptRef( refGen_ ? dataContainer.ptGenPt( uEta, uPt ).at( uEntry ) : dataContainer.ptPt( uEta, uPt ).at( uEntry ) );
      const Double_t etaRef( refGen_ ? dataContainer.etaGenPt( uEta, uPt ).at( uEntry ) : dataContainer.etaPt( uEta, uPt ).at( uEntry ) );
      if ( ptRef >= minPt && std::fabs( etaRef ) < maxEta && reco::deltaR( dataContainer.etaGenPt( uEta, uPt ).at( uEntry ), dataContainer.phiGenPt( uEta, uPt ).at( uEntry ), dataContainer.etaPt( uEta, uPt ).at( uEntry ), dataContainer.phiPt( uEta, uPt ).at( uEntry ) ) <= maxDR ) {
        const Double_t value( refGen_ ? dataContainer.ptGenPt( uEta, uPt ).at( uEntry ) - dataContainer.ptPt( uEta, uPt ).at( uEntry ) : dataContainer.ptPt( uEta, uPt ).at( uEntry ) - dataContainer.ptGenPt( uEta, uPt ).at( uEntry ) );
        histosTransEta.histVecPtTrans.at( uPt )->Fill( value, dataContainer.weightPt( uEta, uPt ).at( uEntry ) );
        histosTrans.histVecPtTrans.at( uPt )->Fill( value, dataContainer.weightPt( uEta, uPt ).at( uEntry ) );
        histosTransEta.histTrans->Fill( value, dataContainer.weightPt( uEta, uPt ).at( uEntry ) );
        histosTrans.histTrans->Fill( value, dataContainer.weightPt( uEta, uPt ).at( uEntry ) );
        if ( ! ( scale_ && histosTransEta.histVecPtTrans.at( uPt )->Integral("width") == 0. ) ) {
          const Double_t etaGenSymm( useSymm_ ? std::fabs( dataContainer.etaGenPt( uEta, uPt ).at( uEntry ) ) : dataContainer.etaGenPt( uEta, uPt ).at( uEntry ) );
          const Double_t etaSymm( useSymm_ ? std::fabs( dataContainer.etaPt( uEta, uPt ).at( uEntry ) ) : dataContainer.etaPt( uEta, uPt ).at( uEntry ) );
          const Double_t etaRef( refGen_ ? etaGenSymm : etaSymm );
          const Double_t weightPt( scale_ ? dataContainer.weightPt( uEta, uPt ).at( uEntry ) / histosTrans.histVecPtTrans.at( uPt )->Integral("width") : dataContainer.weightPt( uEta, uPt ).at( uEntry ) );
          const Double_t weightEta( scale_ ? dataContainer.weightPt( uEta, uPt ).at( uEntry ) / histosTransEta.histTrans->Integral("width") : dataContainer.weightPt( uEta, uPt ).at( uEntry ) );
          const Double_t weightEtaPt( scale_ ? dataContainer.weightPt( uEta, uPt ).at( uEntry ) / histosTransEta.histVecPtTrans.at( uPt )->Integral("width") : dataContainer.weightPt( uEta, uPt ).at( uEntry ) );
          histosTransEta.histTransMapPt->Fill( ptRef, value, weightEtaPt );
          histosTrans.histVecPtTransMapEta.at( uPt )->Fill( etaRef, value, weightEtaPt);
          histosTrans.histTransMapPt->Fill( ptRef, value, weightPt );
          histosTrans.histTransMapEta->Fill( etaRef, value, weightEta );
        }
      }
    } // loop: uEntry < dataContainer.sizePt( uEta, uPt )
  } // loop:uPt < nPtBins
}


bool FitTopTransferFunctionsRunner::fitPerCategory( unsigned uCat )
{

  const std::string objCat( objCats_.at( uCat ) );
  if ( verbose_ > 1 ) {
    std::cout << std::endl
              << myName_ << " --> INFO:" << std::endl
              << "    fitting for object categorie " << objCat << std::endl;
  }

  // Get object configuration
  const edm::ParameterSet& configObj( config_.getParameter< edm::ParameterSet >( "objects" ).getParameter< edm::ParameterSet >( objCat ) );
  const double configObjMinPt( configObj.getParameter< double >( "minPt" ) );
//   const double configObjMaxEta( configObj.getParameter< double >( "maxEta" ) );
  const double configObjMaxDR( configObj.getParameter< double >( "maxDR" ) );
  const std::string configObjFitFunction( configObj.getParameter< std::string >( "fitFunction" ) );
  const std::string configObjDependencyFunction( configObj.getParameter< std::string >( "dependencyFunction" ) );
  const bool configObjFitEtaBins( configObj.getParameter< bool >( "fitEtaBins" ) );
  const double configObjFitMaxPt( configObj.getParameter< double >( "fitMaxPt" ) );
  const double configObjFitRange( configObj.getParameter< double >( "fitRange" ) );
  const std::string configObjFitOptions( configObj.getParameter< std::string >( "fitOptions" ) );

  HistosTrans&                   histosRebinTrans( histosVecRebinTrans_.at( uCat) );
  std::vector< HistosTransEta >& histosRebinVecTransEta( histosVecRebinVecTransEta_.at( uCat) );
  TDirectory*                    dirOutObjCatSubFit( dirsOutObjCatSubFit_.at( uCat ) );
  std::vector< TDirectory* >&    dirOutObjCatSubFitEta( dirsOutObjCatSubFitEta_.at( uCat ) );
  const unsigned nEtaBins( dirOutObjCatSubFitEta.size() );

  // Initialise Functions
  // Dummies
  TF1* fitFunction( new TF1( "fitFunction", "1" ) );
  TF1* dependencyFunction( new TF1( "dependencyFunction", "1" ) );
  TransferFunction transferPt;
  // Initialisation
  if ( configObjFitFunction == "sGauss" ) {
    if ( configObjDependencyFunction == "linear" )          transferPt = initialiseFunctions< SingleGaussian, Line >( fitFunction, dependencyFunction );
    else if ( configObjDependencyFunction == "squared" )    transferPt = initialiseFunctions< SingleGaussian, Parabola >( fitFunction, dependencyFunction );
    else if ( configObjDependencyFunction == "resolution" ) transferPt = initialiseFunctions< SingleGaussian, ResolutionLike >( fitFunction, dependencyFunction );
    else {
      std::cout << myName_ << " --> ERROR:" << std::endl
                << "    dependency function identifier '" << configObjDependencyFunction << "' unknown" << std::endl;
      return false;
    }
  }
  else if ( configObjFitFunction == "dGauss" ){
    if ( configObjDependencyFunction == "linear" )          transferPt = initialiseFunctions< DoubleGaussian, Line >( fitFunction, dependencyFunction );
    else if ( configObjDependencyFunction == "squared" )    transferPt = initialiseFunctions< DoubleGaussian, Parabola >( fitFunction, dependencyFunction );
    else if ( configObjDependencyFunction == "resolution" ) transferPt = initialiseFunctions< DoubleGaussian, ResolutionLike >( fitFunction, dependencyFunction );
    else {
      std::cout << myName_ << " --> ERROR:" << std::endl
                << "    dependency function identifier '" << configObjDependencyFunction << "' unknown" << std::endl;
      return false;
    }
  }
  else if ( configObjFitFunction == "lCB" ) {
    if ( configObjDependencyFunction == "linear" )          transferPt = initialiseFunctions< LowerCrystalBall, Line >( fitFunction, dependencyFunction );
    else if ( configObjDependencyFunction == "squared" )    transferPt = initialiseFunctions< LowerCrystalBall, Parabola >( fitFunction, dependencyFunction );
    else if ( configObjDependencyFunction == "resolution" ) transferPt = initialiseFunctions< LowerCrystalBall, ResolutionLike >( fitFunction, dependencyFunction );
    else {
      std::cout << myName_ << " --> ERROR:" << std::endl
                << "    dependency function identifier '" << configObjDependencyFunction << "' unknown" << std::endl;
      return false;
    }
  }
  else if ( configObjFitFunction == "uCB" ) {
    if ( configObjDependencyFunction == "linear" )          transferPt = initialiseFunctions< UpperCrystalBall, Line >( fitFunction, dependencyFunction );
    else if ( configObjDependencyFunction == "squared" )    transferPt = initialiseFunctions< UpperCrystalBall, Parabola >( fitFunction, dependencyFunction );
    else if ( configObjDependencyFunction == "resolution" ) transferPt = initialiseFunctions< UpperCrystalBall, ResolutionLike >( fitFunction, dependencyFunction );
    else {
      std::cout << myName_ << " --> ERROR:" << std::endl
                << "    dependency function identifier '" << configObjDependencyFunction << "' unknown" << std::endl;
      return false;
    }
  }
  else if ( configObjFitFunction == "dCB" ) {
    if ( configObjDependencyFunction == "linear" )          transferPt = initialiseFunctions< DoubleCrystalBall, Line >( fitFunction, dependencyFunction );
    else if ( configObjDependencyFunction == "squared" )    transferPt = initialiseFunctions< DoubleCrystalBall, Parabola >( fitFunction, dependencyFunction );
    else if ( configObjDependencyFunction == "resolution" ) transferPt = initialiseFunctions< DoubleCrystalBall, ResolutionLike >( fitFunction, dependencyFunction );
    else {
      std::cout << myName_ << " --> ERROR:" << std::endl
                << "    dependency function identifier '" << configObjDependencyFunction << "' unknown" << std::endl;
      return false;
    }
  }
  else {
    std::cout << myName_ << " --> ERROR:" << std::endl
              << "    fit function identifier '" << configObjFitFunction << "' unknown" << std::endl;
    return false;
  }

  // Fitting distribution
  if ( verbose_ > 2 ) {
    std::cout << std::endl
              << myName_ << " --> DEBUG:" << std::endl
              << "    Fitting distributions... " << std::endl;
  }

  // Transfer function parameters
  std::stringstream comment( std::ios_base::out );
  const std::string part( refGen_ ? "_parton" : "_reco" );
  comment << baseTitlePt_ << part << " <= " << configObjFitMaxPt;
  comment << ", " << baseTitlePt_ << part << " >= " << configObjMinPt << ", " << "DeltaR(parton, reco) <= " << configObjMaxDR;
  transferPt.SetComment( comment.str() );
  TransferFunctionCollection transferVecEtaPt( nEtaBins, transferPt );

  // Create histograms
  dirOutObjCatSubFit->cd();
  if ( verbose_ > 2 ) gDirectory->pwd();

  // Fit
  fitPerCategoryBin( dirOutObjCatSubFit, transferPt, histosRebinTrans.histTrans, fitFunction, configObjFitFunction, configObjFitOptions, configObjFitRange );
  // Loop over pt
  for ( unsigned uPt = 0; uPt < histosRebinTrans.histVecPtTrans.size(); ++uPt ) {
    fitPerCategoryBin( dirOutObjCatSubFit, transferPt, histosRebinTrans.histVecPtTrans.at( uPt ), fitFunction, configObjFitFunction, configObjFitOptions, configObjFitRange );
  }

  // Loop over eta bins
  if ( configObjFitEtaBins ) {
    for ( unsigned uEta = 0; uEta < nEtaBins; ++uEta ) {
      // Create histograms
      dirOutObjCatSubFitEta.at( uEta )->cd();
      if ( verbose_ > 2 ) gDirectory->pwd();
      // Fit
      fitPerCategoryBin( dirOutObjCatSubFitEta.at( uEta ), transferPt, histosRebinTrans.histTrans, fitFunction, configObjFitFunction, configObjFitOptions, configObjFitRange );
      // Loop over pt
      for ( unsigned uPt = 0; uPt < histosRebinVecTransEta.at( uEta ).histVecPtTrans.size(); ++uPt ) {
        fitPerCategoryBin( dirOutObjCatSubFitEta.at( uEta ), transferPt, histosRebinVecTransEta.at( uEta ).histVecPtTrans.at( uPt ), fitFunction, configObjFitFunction, configObjFitOptions, configObjFitRange );
      }
    } // loop: uEta < nEtaBins
  }

  return true;

}


void FitTopTransferFunctionsRunner::fitPerCategoryBin( TDirectory const * dirOut, TransferFunction transferPt, TH1D* histoTrans, TF1* fitFunction, const std::string& fitFuncID, const std::string& fitOptions, const double fitRange )
{
  TCanvas     canvas;
  const Int_t nParFit( fitFunction->GetNpar() );
  const std::string nameTransRebin( histoTrans->GetName() );
  const std::string nameTransRebinFit( nameTransRebin + "_fit" );
  TF1* fitTransRebin( new TF1( nameTransRebinFit.c_str(), fitFunction, std::max( histoTrans->GetXaxis()->GetXmin(), histoTrans->GetMean() - histoTrans->GetRMS() * fitRange ), std::min( histoTrans->GetXaxis()->GetXmax(), histoTrans->GetMean() + histoTrans->GetRMS() * fitRange ), nParFit) );
  initialiseFitParameters( fitTransRebin, &*histoTrans, fitFuncID, scale_ );
  TFitResultPtr fitTransRebinResultPtr( histoTrans->Fit( fitTransRebin, fitOptions.c_str() ) );
  if ( fitTransRebinResultPtr >= 0 ) {
    if ( fitTransRebinResultPtr->Status() == 0 && fitTransRebinResultPtr->Prob() > 0. && fitTransRebinResultPtr->Ndf() != 0. ) {
      if ( checkParametersDoubleGaussian( fitTransRebin, fitFuncID ) ) {
        mixParametersDoubleGaussian( transferPt, fitTransRebin );
      }
      else {
        for ( Int_t uPar = 0; uPar < nParFit; ++uPar ) {
          transferPt.SetParameter( uPar, fitTransRebin->GetParameter( uPar ) );
          transferPt.SetError( uPar, fitTransRebin->GetParError( uPar ) );
        }
      }
    }
    else {
      if ( verbose_ > 1 ) {
        std::cout << myName_ << " --> WARNING:" << std::endl
                  << "    failing fit in directory '"; dirOut->pwd();
        if ( fitTransRebinResultPtr->Status() != 0 ) std::cout << "    '" << nameTransRebin << "' status " << fitTransRebinResultPtr->Status() << std::endl;
        if ( fitTransRebinResultPtr->Prob() <= 0. )  std::cout << "    '" << nameTransRebin << "' prob   " << fitTransRebinResultPtr->Prob()   << std::endl;
        if ( fitTransRebinResultPtr->Ndf() == 0. )   std::cout << "    '" << nameTransRebin << "' ndf    " << fitTransRebinResultPtr->Ndf()    << std::endl;
      }
    }
  }
  else {
    if ( verbose_ > 1 ) {
      std::cout << myName_ << " --> WARNING:" << std::endl
                << "    missing fit in directory '"; dirOut->pwd();
      std::cout << "    '" << nameTransRebin << std::endl;
    }
  }
  histoTrans->Draw();
  if ( plot_ ) {
    canvas.Print( std::string( pathPlots_ + histoTrans->GetName() + ".png" ).c_str() );
  }
}
