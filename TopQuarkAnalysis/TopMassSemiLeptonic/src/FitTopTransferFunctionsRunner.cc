#include "TopQuarkAnalysis/TopMassSemiLeptonic/interface/FitTopTransferFunctionsRunner.h"

#include <cassert>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <fstream>

#include "boost/lexical_cast.hpp"

#include <TROOT.h>
#include <TStyle.h>
#include <TObject.h>
#include <TFile.h>
#include <TCanvas.h>
#include <TH1D.h>
#include <TH2D.h>
#include <TFitResult.h>
#include <TKey.h>
#include <TMath.h>

#include "DataFormats/Math/interface/deltaR.h"

#include "CommonTools/MyTools/interface/RootTools.h"
#include "TopQuarkAnalysis/TopMassSemiLeptonic/interface/MyTools.h"


using namespace my;


FitTopTransferFunctionsRunner::FitTopTransferFunctionsRunner( const std::string& iName, const edm::ParameterSet& iConfig )
: myName_( iName )
, status_( 0 )
, config_( iConfig )
, verbose_( config_.getParameter< unsigned >( "verbose" ) )
, maxEvents_( config_.getParameter< int >( "maxEvents" ) )
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
  refSel_ = configIO.getParameter< bool >( "refSel" );
  usePileup_ = configIO.getParameter< bool >( "usePileUp" );
  const std::string& configIOPileUp( configIO.getParameter< std::string >( "pileUp" ) );
  const std::string& configIOOutFile( configIO.getParameter< std::string >( "outputFile" ) );
  writeFiles_   = configIO.getParameter< bool >( "writeFiles" );
  writeFilesPt_ = configIO.getParameter< bool >( "writeFilesPt" );
  sample_       = configIO.getParameter< std::string >( "sample" );
  pathOut_      = configIO.getParameter< std::string >( "pathOut" );
  plot_         = configIO.getParameter< bool >( "plot" );
  pathPlots_    = configIO.getParameter< std::string >( "pathPlots" );
  formatPlots_  = configIO.getParameter< std::vector< std::string > >( "formatPlots" );

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
  if ( refSel_ ) evtSel.append( "Reference" );
  const std::string baseTitlePtL( useAlt_ ? "E" : "p" );
  const std::string baseTitlePtU( useAlt_ ? "E" : "P" );
  baseTitlePt_     = useNonT_ ? baseTitlePtU : baseTitlePtU + "t";
  titlePtT_        = useNonT_ ? baseTitlePtL : baseTitlePtL + "_{t}";
  titlePt_         = refGen_  ? titlePtT_ + "^{GEN} (GeV)" : titlePtT_ + " (GeV)";
  baseTitleEta_    = useSymm_ ? "|#eta|" : "#eta";
  titleEta_        = refGen_  ? baseTitleEta_ + "^{GEN}" : baseTitleEta_ + "^{RECO}";
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
  data_.loadPileUpWeights( usePileup_, configIOPileUp, dirInSel_, maxEvents_ );

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
    dirOutSel_ = new TDirectoryFile( evtSel.c_str(), std::string( refSel_ ? "Reference selection" : "Basic selection" ).c_str() );
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
    if ( ! dependencyPerCategory( uCat ) ) {
      status_ += 0x300;
      return status_ ;
    }
    if ( ! transferPerCategory( uCat ) ) {
      status_ += 0x400;
      return status_ ;
    }
    if ( ! compatibilityPerCategory( uCat ) ) {
      status_ += 0x500;
      return status_ ;
    }
    if ( writeFiles_ ) {
      if ( ! writeFilesPerCategory( uCat ) ) {
        status_ += 0x600;
        return status_ ;
      }
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
              << "    filling for object category " << objCat << std::endl;
  }

  // Get object configuration
  const edm::ParameterSet& configObj( config_.getParameter< edm::ParameterSet >( "objects" ).getParameter< edm::ParameterSet >( objCat ) );
  const unsigned configObjDeltaPtBins( configObj.getParameter< unsigned >( "deltaPtBins" ) );
  const double   configObjDeltaPtMax( configObj.getParameter< double >( "deltaPtMax" ) );
  const double   configObjMinPt( configObj.getParameter< double >( "minPt" ) );
  const double   configObjMaxEta( configObj.getParameter< double >( "maxEta" ) );
  const double   configObjMaxDR( configObj.getParameter< double >( "maxDR" ) );
  const double   configObjWidthFactor( configObj.getParameter< double >( "widthFactor" ) );

  // Open ROOT file directories
  TDirectory* dirInObjCat( ( TDirectory* )( dirInSel_->Get( objCat.c_str() ) ) );
  if ( ! dirInObjCat ) {
    if ( verbose_ > 0 ) {
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
  ObjectDataContainer dataContainer( objCat, dirInObjCat, useSymm_, useAlt_, useNonT_, refGen_, data_, maxEvents_ );

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
  objectData_.push_back( dataContainer );
  const unsigned nPtBins( dataContainer.nPtBins() );
  assert( dataContainer.nEtaBins() == dirsOutObjCatSubFitEta_.back().size() );
  const unsigned nEtaBins( dirsOutObjCatSubFitEta_.back().size() );

  const std::string name( objCat + "_" + baseTitlePt_ + "_" + subFit );

  // Filling histograms
  if ( verbose_ > 2 ) {
    std::cout << std::endl
              << myName_ << " --> DEBUG:" << std::endl
              << "    Filling histograms... " << std::endl;
  }

  // Create histograms
  dirsOutObjCatSubFit_.back()->cd();
  if ( verbose_ > 2 ) gDirectory->pwd();
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
    fillPerCategoryBin( uEta, histosTrans, histosTransEta, configObjMinPt, configObjMaxEta, configObjMaxDR );
    histosVecTransEta.push_back( histosTransEta );
  } // loop:uEta < nEtaBins

  // Re-bin histograms
  if ( verbose_ > 2 ) {
    std::cout << std::endl
              << myName_ << " --> DEBUG:" << std::endl
              << "    Re-binning histograms... " << std::endl;
  }

  // Create histograms
  dirsOutObjCatSubFit_.back()->cd();
  if ( verbose_ > 2 ) gDirectory->pwd();
  const std::string nameRebin( name + "_Rebin" );
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
    fillPerCategoryBin( uEta, histosRebinTrans, histosRebinTransEta, configObjMinPt, configObjMaxEta, configObjMaxDR );
    histosRebinVecTransEta.push_back( histosRebinTransEta );
  } // loop:uEta < nEtaBins
  histosVecRebinTrans_.push_back( histosRebinTrans );
  histosVecRebinVecTransEta_.push_back( histosRebinVecTransEta );

  // Add scaled histograms
  if ( scale_ ) {
    if ( verbose_ > 2 ) {
      std::cout << std::endl
                << myName_ << " --> DEBUG:" << std::endl
                << "    Scaling re-binned histograms... " << std::endl;
    }
    // Create histograms
    dirsOutObjCatSubFit_.back()->cd();
    if ( verbose_ > 2 ) gDirectory->pwd();
    std::string nameRebinScale( nameRebin + "Scale" );
    HistosTrans histosRebinScaleTrans( histosRebinTrans, nameRebinScale, baseTitlePt_, true );
    histosVecRebinScaleTrans_.push_back( histosRebinScaleTrans );
    // Loop over eta bins
    std::vector< HistosTransEta > histosRebinScaleVecTransEta;
    for ( unsigned uEta = 0; uEta < nEtaBins; ++uEta ) {
      // Create histograms
      dirsOutObjCatSubFitEta_.back().at( uEta )->cd();
      if ( verbose_ > 2 ) gDirectory->pwd();
      const std::string binEta( gDirectory->GetName() );
      const std::string nameEtaRebinScale( nameRebinScale + "_" + binEta );
      HistosTransEta histosRebinScaleTransEta( histosVecRebinVecTransEta_.back().at( uEta ), nameEtaRebinScale, baseTitlePt_, true );
      // Fill
      histosRebinScaleVecTransEta.push_back( histosRebinScaleTransEta );
    } // loop:uEta < nEtaBins
    histosVecRebinScaleVecTransEta_.push_back( histosRebinScaleVecTransEta );
  }

  return true;

}


void FitTopTransferFunctionsRunner::fillPerCategoryBin( unsigned uEta, HistosTrans& histosTrans, HistosTransEta& histosTransEta, double minPt, double maxEta, double maxDR )
{
  TCanvas canvas;
  // Loop over pt bins
  for ( unsigned uPt = 0; uPt < objectData_.back().nPtBins(); ++uPt ) {
    if ( objectData_.back().sizePt( uEta, uPt ) == 0 ) continue;
    // Loop over entries
    for ( unsigned uEntry = 0; uEntry < objectData_.back().sizePt( uEta, uPt ); ++uEntry ) {
      const Double_t ptRef( refGen_ ? objectData_.back().ptGenPt( uEta, uPt ).at( uEntry ) : objectData_.back().ptPt( uEta, uPt ).at( uEntry ) );
      const Double_t etaRef( refGen_ ? objectData_.back().etaGenPt( uEta, uPt ).at( uEntry ) : objectData_.back().etaPt( uEta, uPt ).at( uEntry ) );
      if ( ptRef >= minPt && std::fabs( etaRef ) < maxEta && reco::deltaR( objectData_.back().etaGenPt( uEta, uPt ).at( uEntry ), objectData_.back().phiGenPt( uEta, uPt ).at( uEntry ), objectData_.back().etaPt( uEta, uPt ).at( uEntry ), objectData_.back().phiPt( uEta, uPt ).at( uEntry ) ) <= maxDR ) {
        const Double_t value( refGen_ ? objectData_.back().ptGenPt( uEta, uPt ).at( uEntry ) - objectData_.back().ptPt( uEta, uPt ).at( uEntry ) : objectData_.back().ptPt( uEta, uPt ).at( uEntry ) - objectData_.back().ptGenPt( uEta, uPt ).at( uEntry ) );
        histosTransEta.histVecPtTrans.at( uPt )->Fill( value, objectData_.back().weightPt( uEta, uPt ).at( uEntry ) );
        histosTrans.histVecPtTrans.at( uPt )->Fill( value, objectData_.back().weightPt( uEta, uPt ).at( uEntry ) );
        histosTransEta.histTrans->Fill( value, objectData_.back().weightPt( uEta, uPt ).at( uEntry ) );
        histosTrans.histTrans->Fill( value, objectData_.back().weightPt( uEta, uPt ).at( uEntry ) );
        if ( ! ( scale_ && histosTransEta.histVecPtTrans.at( uPt )->Integral("width") == 0. ) ) {
          const Double_t etaGenSymm( useSymm_ ? std::fabs( objectData_.back().etaGenPt( uEta, uPt ).at( uEntry ) ) : objectData_.back().etaGenPt( uEta, uPt ).at( uEntry ) );
          const Double_t etaSymm( useSymm_ ? std::fabs( objectData_.back().etaPt( uEta, uPt ).at( uEntry ) ) : objectData_.back().etaPt( uEta, uPt ).at( uEntry ) );
          const Double_t etaRef( refGen_ ? etaGenSymm : etaSymm );
          const Double_t weightPt( scale_ ? objectData_.back().weightPt( uEta, uPt ).at( uEntry ) / histosTrans.histVecPtTrans.at( uPt )->Integral("width") : objectData_.back().weightPt( uEta, uPt ).at( uEntry ) );
          const Double_t weightEta( scale_ ? objectData_.back().weightPt( uEta, uPt ).at( uEntry ) / histosTransEta.histTrans->Integral("width") : objectData_.back().weightPt( uEta, uPt ).at( uEntry ) );
          const Double_t weightEtaPt( scale_ ? objectData_.back().weightPt( uEta, uPt ).at( uEntry ) / histosTransEta.histVecPtTrans.at( uPt )->Integral("width") : objectData_.back().weightPt( uEta, uPt ).at( uEntry ) );
          histosTransEta.histTransMapPt->Fill( ptRef, value, weightEtaPt );
          histosTrans.histVecPtTransMapEta.at( uPt )->Fill( etaRef, value, weightEtaPt);
          histosTrans.histTransMapPt->Fill( ptRef, value, weightPt );
          histosTrans.histTransMapEta->Fill( etaRef, value, weightEta );
        }
      }
    } // loop: uEntry < objectData_.back().sizePt( uEta, uPt )
    if ( plot_ ) {
      histosTrans.histVecPtTransMapEta.at( uPt )->Draw();
      for ( unsigned uForm = 0; uForm < formatPlots_.size(); ++uForm ) canvas.Print( std::string( pathPlots_ + histosTrans.histVecPtTransMapEta.at( uPt )->GetName() + "." + formatPlots_.at( uForm ) ).c_str() );
    }
  } // loop:uPt < nPtBins
  if ( plot_ ) {
    histosTransEta.histTransMapPt->Draw();
    for ( unsigned uForm = 0; uForm < formatPlots_.size(); ++uForm ) canvas.Print( std::string( pathPlots_ + histosTransEta.histTransMapPt->GetName() + "." + formatPlots_.at( uForm )  ).c_str() );
    histosTrans.histTransMapPt->Draw();
    for ( unsigned uForm = 0; uForm < formatPlots_.size(); ++uForm ) canvas.Print( std::string( pathPlots_ + histosTrans.histTransMapPt->GetName() + "." + formatPlots_.at( uForm )  ).c_str() );
    histosTrans.histTransMapEta->Draw();
    for ( unsigned uForm = 0; uForm < formatPlots_.size(); ++uForm ) canvas.Print( std::string( pathPlots_ + histosTrans.histTransMapEta->GetName() + "." + formatPlots_.at( uForm )  ).c_str() );
  }
}


bool FitTopTransferFunctionsRunner::fitPerCategory( unsigned uCat )
{

  const std::string objCat( objCats_.at( uCat ) );
  if ( verbose_ > 1 ) {
    std::cout << std::endl
              << myName_ << " --> INFO:" << std::endl
              << "    fitting for object category " << objCat << std::endl;
  }

  // Get object configuration
  const edm::ParameterSet& configObj( config_.getParameter< edm::ParameterSet >( "objects" ).getParameter< edm::ParameterSet >( objCat ) );
  const double configObjMinPt( configObj.getParameter< double >( "minPt" ) );
//   const double configObjMaxEta( configObj.getParameter< double >( "maxEta" ) );
  const double configObjMaxDR( configObj.getParameter< double >( "maxDR" ) );
  fitFuncID_  = configObj.getParameter< std::string >( "fitFunction" );
  depFuncID_  = configObj.getParameter< std::string >( "dependencyFunction" );
  resFuncID_  = configObj.getParameter< std::string >( "resolutionFunction" );
  fitEtaBins_ = configObj.getParameter< bool >( "fitEtaBins" );
  fitRange_   = configObj.getParameter< double >( "fitRange" );
  fitOptions_ = configObj.getParameter< std::string >( "fitOptions" );
  if      ( verbose_ < 2 ) fitOptions_.append( "Q" );
  else if ( verbose_ > 3 ) fitOptions_.append( "V" );
  minEntriesFactor_ = configObj.getParameter< unsigned >( "minEntriesFactor" );
  excludeVec_       = configObj.getParameter< std::vector< unsigned > >( "exclude" ); // FIXME: not yet set up for eta bins
  fitMaxPt_         = configObj.getParameter< double >( "fitMaxPt" );

  const unsigned nPtBins( objectData_.back().nPtBins() );
  const unsigned nEtaBins( objectData_.back().nEtaBins() );

  // Initialise Functions // FIXME: optimise!
  // Dummies
  fitFunction_ = new TF1( "fitFunction", "1" );
  dependencyFunction_ = new TF1( "dependencyFunction", "1" );
  resolutionFunction_ = new TF1( "resolutionFunction", "1" );
  TransferFunction transferPt;
  // Initialisation
  if ( fitFuncID_ == "sGauss" ) {
    if ( depFuncID_ == "linear" ) {
      if ( resFuncID_ == "linear" )          transferPt = initialiseFunctions< SingleGaussian, Line, Line >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else if ( depFuncID_ == "squared" )    transferPt = initialiseFunctions< SingleGaussian, Line, Parabola >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else if ( depFuncID_ == "resolution" ) transferPt = initialiseFunctions< SingleGaussian, Line, ResolutionLike >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else {
        std::cout << myName_ << " --> ERROR:" << std::endl
                  << "    resolution function identifier '" << resFuncID_ << "' unknown" << std::endl;
        return false;
      }
    }
    else if ( depFuncID_ == "squared" ) {
      if ( resFuncID_ == "linear" )          transferPt = initialiseFunctions< SingleGaussian, Parabola, Line >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else if ( depFuncID_ == "squared" )    transferPt = initialiseFunctions< SingleGaussian, Parabola, Parabola >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else if ( depFuncID_ == "resolution" ) transferPt = initialiseFunctions< SingleGaussian, Parabola, ResolutionLike >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else {
        std::cout << myName_ << " --> ERROR:" << std::endl
                  << "    resolution function identifier '" << resFuncID_ << "' unknown" << std::endl;
        return false;
      }
    }
    else if ( depFuncID_ == "resolution" ) {
      if ( resFuncID_ == "linear" )          transferPt = initialiseFunctions< SingleGaussian, ResolutionLike, Line >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else if ( depFuncID_ == "squared" )    transferPt = initialiseFunctions< SingleGaussian, ResolutionLike, Parabola >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else if ( depFuncID_ == "resolution" ) transferPt = initialiseFunctions< SingleGaussian, ResolutionLike, ResolutionLike >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else {
        std::cout << myName_ << " --> ERROR:" << std::endl
                  << "    resolution function identifier '" << resFuncID_ << "' unknown" << std::endl;
        return false;
      }
    }
    else {
      std::cout << myName_ << " --> ERROR:" << std::endl
                << "    dependency function identifier '" << depFuncID_ << "' unknown" << std::endl;
      return false;
    }
  }
  else if ( fitFuncID_ == "dGauss" ){
    if ( depFuncID_ == "linear" ) {
      if ( resFuncID_ == "linear" )          transferPt = initialiseFunctions< DoubleGaussian, Line, Line >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else if ( depFuncID_ == "squared" )    transferPt = initialiseFunctions< DoubleGaussian, Line, Parabola >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else if ( depFuncID_ == "resolution" ) transferPt = initialiseFunctions< DoubleGaussian, Line, ResolutionLike >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else {
        std::cout << myName_ << " --> ERROR:" << std::endl
                  << "    resolution function identifier '" << resFuncID_ << "' unknown" << std::endl;
        return false;
      }
    }
    else if ( depFuncID_ == "squared" ) {
      if ( resFuncID_ == "linear" )          transferPt = initialiseFunctions< DoubleGaussian, Parabola, Line >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else if ( depFuncID_ == "squared" )    transferPt = initialiseFunctions< DoubleGaussian, Parabola, Parabola >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else if ( depFuncID_ == "resolution" ) transferPt = initialiseFunctions< DoubleGaussian, Parabola, ResolutionLike >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else {
        std::cout << myName_ << " --> ERROR:" << std::endl
                  << "    resolution function identifier '" << resFuncID_ << "' unknown" << std::endl;
        return false;
      }
    }
    else if ( depFuncID_ == "resolution" ) {
      if ( resFuncID_ == "linear" )          transferPt = initialiseFunctions< DoubleGaussian, ResolutionLike, Line >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else if ( depFuncID_ == "squared" )    transferPt = initialiseFunctions< DoubleGaussian, ResolutionLike, Parabola >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else if ( depFuncID_ == "resolution" ) transferPt = initialiseFunctions< DoubleGaussian, ResolutionLike, ResolutionLike >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else {
        std::cout << myName_ << " --> ERROR:" << std::endl
                  << "    resolution function identifier '" << resFuncID_ << "' unknown" << std::endl;
        return false;
      }
    }
    else {
      std::cout << myName_ << " --> ERROR:" << std::endl
                << "    dependency function identifier '" << depFuncID_ << "' unknown" << std::endl;
      return false;
    }
  }
  else if ( fitFuncID_ == "lCB" ) {
    if ( depFuncID_ == "linear" ) {
      if ( resFuncID_ == "linear" )          transferPt = initialiseFunctions< LowerCrystalBall, Line, Line >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else if ( depFuncID_ == "squared" )    transferPt = initialiseFunctions< LowerCrystalBall, Line, Parabola >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else if ( depFuncID_ == "resolution" ) transferPt = initialiseFunctions< LowerCrystalBall, Line, ResolutionLike >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else {
        std::cout << myName_ << " --> ERROR:" << std::endl
                  << "    resolution function identifier '" << resFuncID_ << "' unknown" << std::endl;
        return false;
      }
    }
    else if ( depFuncID_ == "squared" ) {
      if ( resFuncID_ == "linear" )          transferPt = initialiseFunctions< LowerCrystalBall, Parabola, Line >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else if ( depFuncID_ == "squared" )    transferPt = initialiseFunctions< LowerCrystalBall, Parabola, Parabola >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else if ( depFuncID_ == "resolution" ) transferPt = initialiseFunctions< LowerCrystalBall, Parabola, ResolutionLike >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else {
        std::cout << myName_ << " --> ERROR:" << std::endl
                  << "    resolution function identifier '" << resFuncID_ << "' unknown" << std::endl;
        return false;
      }
    }
    else if ( depFuncID_ == "resolution" ) {
      if ( resFuncID_ == "linear" )          transferPt = initialiseFunctions< LowerCrystalBall, ResolutionLike, Line >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else if ( depFuncID_ == "squared" )    transferPt = initialiseFunctions< LowerCrystalBall, ResolutionLike, Parabola >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else if ( depFuncID_ == "resolution" ) transferPt = initialiseFunctions< LowerCrystalBall, ResolutionLike, ResolutionLike >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else {
        std::cout << myName_ << " --> ERROR:" << std::endl
                  << "    resolution function identifier '" << resFuncID_ << "' unknown" << std::endl;
        return false;
      }
    }
    else {
      std::cout << myName_ << " --> ERROR:" << std::endl
                << "    dependency function identifier '" << depFuncID_ << "' unknown" << std::endl;
      return false;
    }
  }
  else if ( fitFuncID_ == "uCB" ) {
    if ( depFuncID_ == "linear" ) {
      if ( resFuncID_ == "linear" )          transferPt = initialiseFunctions< UpperCrystalBall, Line, Line >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else if ( depFuncID_ == "squared" )    transferPt = initialiseFunctions< UpperCrystalBall, Line, Parabola >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else if ( depFuncID_ == "resolution" ) transferPt = initialiseFunctions< UpperCrystalBall, Line, ResolutionLike >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else {
        std::cout << myName_ << " --> ERROR:" << std::endl
                  << "    resolution function identifier '" << resFuncID_ << "' unknown" << std::endl;
        return false;
      }
    }
    else if ( depFuncID_ == "squared" ) {
      if ( resFuncID_ == "linear" )          transferPt = initialiseFunctions< UpperCrystalBall, Parabola, Line >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else if ( depFuncID_ == "squared" )    transferPt = initialiseFunctions< UpperCrystalBall, Parabola, Parabola >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else if ( depFuncID_ == "resolution" ) transferPt = initialiseFunctions< UpperCrystalBall, Parabola, ResolutionLike >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else {
        std::cout << myName_ << " --> ERROR:" << std::endl
                  << "    resolution function identifier '" << resFuncID_ << "' unknown" << std::endl;
        return false;
      }
    }
    else if ( depFuncID_ == "resolution" ) {
      if ( resFuncID_ == "linear" )          transferPt = initialiseFunctions< UpperCrystalBall, ResolutionLike, Line >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else if ( depFuncID_ == "squared" )    transferPt = initialiseFunctions< UpperCrystalBall, ResolutionLike, Parabola >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else if ( depFuncID_ == "resolution" ) transferPt = initialiseFunctions< UpperCrystalBall, ResolutionLike, ResolutionLike >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else {
        std::cout << myName_ << " --> ERROR:" << std::endl
                  << "    resolution function identifier '" << resFuncID_ << "' unknown" << std::endl;
        return false;
      }
    }
    else {
      std::cout << myName_ << " --> ERROR:" << std::endl
                << "    dependency function identifier '" << depFuncID_ << "' unknown" << std::endl;
      return false;
    }
  }
  else if ( fitFuncID_ == "dCB" ) {
    if ( depFuncID_ == "linear" ) {
      if ( resFuncID_ == "linear" )          transferPt = initialiseFunctions< DoubleCrystalBall, Line, Line >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else if ( depFuncID_ == "squared" )    transferPt = initialiseFunctions< DoubleCrystalBall, Line, Parabola >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else if ( depFuncID_ == "resolution" ) transferPt = initialiseFunctions< DoubleCrystalBall, Line, ResolutionLike >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else {
        std::cout << myName_ << " --> ERROR:" << std::endl
                  << "    resolution function identifier '" << resFuncID_ << "' unknown" << std::endl;
        return false;
      }
    }
    else if ( depFuncID_ == "squared" ) {
      if ( resFuncID_ == "linear" )          transferPt = initialiseFunctions< DoubleCrystalBall, Parabola, Line >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else if ( depFuncID_ == "squared" )    transferPt = initialiseFunctions< DoubleCrystalBall, Parabola, Parabola >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else if ( depFuncID_ == "resolution" ) transferPt = initialiseFunctions< DoubleCrystalBall, Parabola, ResolutionLike >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else {
        std::cout << myName_ << " --> ERROR:" << std::endl
                  << "    resolution function identifier '" << resFuncID_ << "' unknown" << std::endl;
        return false;
      }
    }
    else if ( depFuncID_ == "resolution" ) {
      if ( resFuncID_ == "linear" )          transferPt = initialiseFunctions< DoubleCrystalBall, ResolutionLike, Line >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else if ( depFuncID_ == "squared" )    transferPt = initialiseFunctions< DoubleCrystalBall, ResolutionLike, Parabola >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else if ( depFuncID_ == "resolution" ) transferPt = initialiseFunctions< DoubleCrystalBall, ResolutionLike, ResolutionLike >( fitFunction_, dependencyFunction_, resolutionFunction_ );
      else {
        std::cout << myName_ << " --> ERROR:" << std::endl
                  << "    resolution function identifier '" << resFuncID_ << "' unknown" << std::endl;
        return false;
      }
    }
    else {
      std::cout << myName_ << " --> ERROR:" << std::endl
                << "    dependency function identifier '" << depFuncID_ << "' unknown" << std::endl;
      return false;
    }
  }
  else {
    std::cout << myName_ << " --> ERROR:" << std::endl
              << "    fit function identifier '" << fitFuncID_ << "' unknown" << std::endl;
    return false;
  }

  // Transfer function parameters
  std::stringstream comment( std::ios_base::out );
  const std::string part( refGen_ ? "_parton" : "_reco" );
  comment << baseTitlePt_ << part << " <= " << fitMaxPt_;
  comment << ", " << baseTitlePt_ << part << " >= " << configObjMinPt << ", DeltaR(parton, reco) <= " << configObjMaxDR << ", minEntries / bins: " << minEntriesFactor_;
  transferPt.SetComment( comment.str() );
  TransferFunctionCollection transferVecPt( nPtBins, transferPt );
  TransferFunctionCollection transferVecEta( nEtaBins, transferPt );
  std::vector< TransferFunctionCollection > transferVecEtaPt( nEtaBins, transferVecPt );
  transferVecRebin_.push_back( transferPt );
  transferVecRebinVecPt_.push_back( transferVecPt );
  transferVecRebinScale_.push_back( transferPt );
  transferVecRebinScaleVecPt_.push_back( transferVecPt );
  transferVecRebinVecEta_.push_back( transferVecEta );
  transferVecRebinVecEtaVecPt_.push_back( transferVecEtaPt );
  transferVecRebinScaleVecEta_.push_back( transferVecEta );
  transferVecRebinScaleVecEtaVecPt_.push_back( transferVecEtaPt );

  // Fitting unscaled distribution
  if ( ! scale_ ) {
    if ( verbose_ > 2 ) {
      std::cout << std::endl
                << myName_ << " --> DEBUG:" << std::endl
                << "    Fitting unscaled distributions... " << std::endl;
    }

    fitPerCategoryLoop( objCat, scale_ );
  }

  // Fitting scaled distribution
  if ( scale_ ) {
    if ( verbose_ > 2 ) {
      std::cout << std::endl
                << myName_ << " --> DEBUG:" << std::endl
                << "    Fitting scaled distributions... " << std::endl;
    }

    fitPerCategoryLoop( objCat, scale_ );
  }

  return true;

}


void FitTopTransferFunctionsRunner::fitPerCategoryLoop( const std::string& objCat, bool scale )
{
  if ( scale ) fitPerCategoryBin( objCat, dirsOutObjCatSubFit_.back(), transferVecRebinScale_.back(), transferVecRebinScaleVecPt_.back(), histosVecRebinScaleTrans_.back(), histosVecRebinScaleDependency_, scale );
  else         fitPerCategoryBin( objCat, dirsOutObjCatSubFit_.back(), transferVecRebin_.back(), transferVecRebinVecPt_.back(), histosVecRebinTrans_.back(), histosVecRebinDependency_, scale );

  // Loop over eta bins
  if ( fitEtaBins_ ) {
    std::vector< HistosDependency > histosVecDependencyEta;
    for ( unsigned uEta = 0; uEta < dirsOutObjCatSubFitEta_.back().size(); ++uEta ) {
      if ( scale ) fitPerCategoryBin( objCat, dirsOutObjCatSubFitEta_.back().at( uEta ), transferVecRebinScaleVecEta_.back().at( uEta ), transferVecRebinScaleVecEtaVecPt_.back().at( uEta ), histosVecRebinScaleVecTransEta_.back().at( uEta ), histosVecDependencyEta, scale );
      else         fitPerCategoryBin( objCat, dirsOutObjCatSubFitEta_.back().at( uEta ), transferVecRebinVecEta_.back().at( uEta ), transferVecRebinVecEtaVecPt_.back().at( uEta ), histosVecRebinVecTransEta_.back().at( uEta ), histosVecDependencyEta, scale );
    } // loop: uEta < nEtaBins
    if ( scale ) histosVecRebinScaleVecDependencyEta_.push_back( histosVecDependencyEta );
    else         histosVecRebinVecDependencyEta_.push_back( histosVecDependencyEta );
  }
}


void FitTopTransferFunctionsRunner::fitPerCategoryBin( const std::string& objCat, TDirectory* dirOut, TransferFunction& transfer, TransferFunctionCollection& transferColl, HistosTransEta& histosTransEta, std::vector< HistosDependency >& histosVecDependency, bool scale )
{
  // Create histograms
  dirOut->cd();
  if ( verbose_ > 2 ) gDirectory->pwd();
  HistosDependency histosDependency( objCat, histosTransEta.name, objectData_.back().nPtBins(), objectData_.back().ptBins(), transfer.NParFit(), baseTitlePt_, titlePt_ );

  // Fit
  fitPerCategoryFit( transfer, histosTransEta.histTrans, 0, -1, scale );
  for ( unsigned uPt = 0; uPt < histosTransEta.histVecPtTrans.size(); ++uPt ) {
    fitPerCategoryFit( transferColl.at( uPt ), histosTransEta.histVecPtTrans.at( uPt ), &histosDependency, uPt, scale );
  }
  histosVecDependency.push_back( histosDependency );

  // Plot
  if ( plot_ ) {
    TCanvas canvas;
    histosDependency.histPtProb->Draw();
    const std::string entryHisto( "from " + titlePtT_ + " bins" );
    histosDependency.legPtProb->AddEntry( histosDependency.histPtProb, entryHisto.c_str(), "F" );
    histosDependency.legPtProb->Draw();
    for ( unsigned uForm = 0; uForm < formatPlots_.size(); ++uForm ) canvas.Print( std::string( pathPlots_ + histosDependency.histPtProb->GetName() + "." + formatPlots_.at( uForm ) ).c_str() );
  }
}


void FitTopTransferFunctionsRunner::fitPerCategoryFit( TransferFunction& transfer, TH1D* histoTrans, HistosDependency* histosDependency, int uPt, bool scale )
{
  const Int_t nParFit( fitFunction_->GetNpar() );
  const std::string nameTrans( histoTrans->GetName() );
  const std::string nameTransFit( nameTrans + "_fit" );
  TF1* fitTrans( new TF1( nameTransFit.c_str(), fitFunction_, std::max( histoTrans->GetXaxis()->GetXmin(), histoTrans->GetMean() - histoTrans->GetRMS() * fitRange_ ), std::min( histoTrans->GetXaxis()->GetXmax(), histoTrans->GetMean() + histoTrans->GetRMS() * fitRange_ ), nParFit ) );
  initialiseFitParameters( fitTrans, &*histoTrans, fitFuncID_, scale );
  TFitResultPtr fitTransResultPtr( histoTrans->Fit( fitTrans, fitOptions_.c_str() ) );
  if ( fitTransResultPtr >= 0 ) {
    if ( histoTrans->GetEntries() >= minEntriesFactor_ * histoTrans->GetNbinsX()  && fitTransResultPtr->Status() == 0 && fitTransResultPtr->Prob() > 0. && fitTransResultPtr->Ndf() != 0. && std::find( excludeVec_.begin(), excludeVec_.end(), uPt ) == excludeVec_.end() ) {
      if ( checkParametersDoubleGaussian( fitTrans, fitFuncID_ ) ) {
        mixParametersDoubleGaussian( transfer, fitTrans );
        if ( verbose_ > 0 ) {
          std::cout << myName_ << " --> WARNING:" << std::endl
                    << "    mixed fit parameters in directory "; gDirectory->pwd();
          std::cout << "    '" << nameTrans << "'" << std::endl;
        }
      }
      else {
        for ( Int_t uPar = 0; uPar < nParFit; ++uPar ) {
          transfer.SetParameter( uPar, fitTrans->GetParameter( uPar ) );
          transfer.SetError( uPar, fitTrans->GetParError( uPar ) );
        }
      }
      if ( histosDependency != 0 && uPt >= 0 ) { // 2-D
        histosDependency->histPtProb->SetBinContent( uPt + 1, log10( fitTransResultPtr->Prob() ) );
        for ( Int_t uPar = 0; uPar < nParFit; ++uPar ) {
          histosDependency->histVecPtPar.at( uPar )->SetBinContent( uPt + 1, transfer.Parameter( uPar ) );
          histosDependency->histVecPtPar.at( uPar )->SetBinError( uPt + 1, transfer.Error( uPar ) );
        }
      }
    }
    else {
      if ( verbose_ > 0 ) {
        std::cout << myName_ << " --> WARNING:" << std::endl
                  << "    failing fit in directory "; gDirectory->pwd();
        std::cout << "    '" << nameTrans << "'" << std::endl;
        if ( fitTransResultPtr->Status() != 0 ) std::cout << "         status: " << fitTransResultPtr->Status() << std::endl;
        if ( fitTransResultPtr->Prob() <= 0. )  std::cout << "         prob  : " << fitTransResultPtr->Prob()   << std::endl;
        if ( fitTransResultPtr->Ndf() == 0. )   std::cout << "         ndf   : " << fitTransResultPtr->Ndf()    << std::endl;
      }
    }
  }
  else {
    if ( verbose_ > 0 ) {
      std::cout << myName_ << " --> WARNING:" << std::endl
                << "    missing fit in directory "; gDirectory->pwd();
      std::cout << "    '" << nameTrans << std::endl;
    }
  }
//   if ( plot_ ) {
//     TCanvas canvas;
//     histoTrans->Draw();
//     for ( unsigned uForm = 0; uForm < formatPlots_.size(); ++uForm ) canvas.Print( std::string( pathPlots_ + histoTrans->GetName() + "." + formatPlots_.at( uForm ) ).c_str() );
//   }
}


bool FitTopTransferFunctionsRunner::dependencyPerCategory( unsigned uCat )
{

  const std::string objCat( objCats_.at( uCat ) );
  if ( verbose_ > 1 ) {
    std::cout << std::endl
              << myName_ << " --> INFO:" << std::endl
              << "    Dependency fitting for object category " << objCat << std::endl;
  }

  // Fitting unscaled distribution
  if ( ! scale_ ) {
    if ( verbose_ > 2 ) {
      std::cout << std::endl
                << myName_ << " --> DEBUG:" << std::endl
                << "    Fitting unscaled dependencies... " << std::endl;
    }

    dependencyPerCategoryLoop( objCat, scale_ );
  }

  // Fitting scaled distribution
  if ( scale_ ) {
    if ( verbose_ > 2 ) {
      std::cout << std::endl
                << myName_ << " --> DEBUG:" << std::endl
                << "    Fitting scaled dependencies... " << std::endl;
    }

    dependencyPerCategoryLoop( objCat, scale_ );
  }

  return true;

}


void FitTopTransferFunctionsRunner::dependencyPerCategoryLoop( const std::string& objCat, bool scale )
{
  if ( scale ) dependencyPerCategoryBin( objCat, dirsOutObjCatSubFit_.back(), transferVecRebinScale_.back(), histosVecRebinScaleDependency_.back(), scale );
  else         dependencyPerCategoryBin( objCat, dirsOutObjCatSubFit_.back(), transferVecRebin_.back(), histosVecRebinDependency_.back(), scale );

  // Loop over eta bins
  if ( fitEtaBins_ ) {
    for ( unsigned uEta = 0; uEta < dirsOutObjCatSubFitEta_.back().size(); ++uEta ) {
      if ( scale ) dependencyPerCategoryBin( objCat, dirsOutObjCatSubFitEta_.back().at( uEta ), transferVecRebinScaleVecEta_.back().at( uEta ), histosVecRebinScaleVecDependencyEta_.back().at( uEta ), scale );
      else         dependencyPerCategoryBin( objCat, dirsOutObjCatSubFitEta_.back().at( uEta ), transferVecRebinVecEta_.back().at( uEta ), histosVecRebinVecDependencyEta_.back().at( uEta ), scale );
    } // loop: uEta < nEtaBins
  }
}


void FitTopTransferFunctionsRunner::dependencyPerCategoryBin( const std::string& objCat, TDirectory* dirOut, TransferFunction& transfer, HistosDependency& histosDependency, bool scale )
{
  const Int_t nParFit( fitFunction_->GetNpar() );
  const Int_t nParDep( dependencyFunction_->GetNpar() );
  for ( Int_t uPar = 0; uPar < nParFit; ++uPar ) {
    const std::string parFit( boost::lexical_cast< std::string >( uPar ) );
    const std::string nameDep( histosDependency.histVecPtPar.at( uPar )->GetName() );
    const std::string nameDepFit( nameDep + "_fit" );
    TF1* fitDep( new TF1( nameDepFit.c_str(), dependencyFunction_, objectData_.back().ptBins().front(), fitMaxPt_, nParDep ) );
    initialiseDependencyParameters( fitDep, histosDependency.histVecPtPar.at( uPar ), depFuncID_ );
    TFitResultPtr fitDepResultPtr( histosDependency.histVecPtPar.at( uPar )->Fit( fitDep, fitOptions_.c_str() ) );
    if ( fitDepResultPtr >= 0 ) {
      if ( fitDepResultPtr->Status() == 0 && fitDepResultPtr->Ndf() != 0. ) {
        for ( Int_t uDep = 0; uDep < nParDep; ++uDep ) {
          transfer.SetParameter( uPar, uDep, fitDep->GetParameter( uDep ) );
          transfer.SetError( uPar, uDep, fitDep->GetParError( uDep ) );
        }
      }
      else {
        if ( verbose_ > 0 ) {
          std::cout << myName_ << " --> WARNING:" << std::endl
                    << "    failing fit in directory '"; dirOut->pwd();
          if ( fitDepResultPtr->Status() != 0 ) std::cout << "    '" << nameDep << "' status " << fitDepResultPtr->Status() << std::endl;
          if ( fitDepResultPtr->Ndf() == 0. )   std::cout << "    '" << nameDep << "' ndf    " << fitDepResultPtr->Ndf()    << std::endl;
        }
      }
    }
    else {
      if ( verbose_ > 0 ) {
        std::cout << myName_ << " --> WARNING:" << std::endl
                  << "    missing dependency in directory '"; dirOut->pwd();
        std::cout << "    '" << nameDep << std::endl;
      }
    }
    if ( plot_ ) {
      TCanvas canvas;
      histosDependency.histVecPtPar.at( uPar )->Draw();
      const std::string entryHisto( "from " + titlePtT_ + " bins" );
      histosDependency.legVecPtPar.at( uPar )->AddEntry( histosDependency.histVecPtPar.at( uPar ), entryHisto.c_str(), "LEP" );
      const std::string entryFit( "fitted " + titlePtT_ + " dependency" );
      histosDependency.legVecPtPar.at( uPar )->AddEntry( fitDep, entryFit.c_str(), "L" );
      histosDependency.legVecPtPar.at( uPar )->Draw();
      for ( unsigned uForm = 0; uForm < formatPlots_.size(); ++uForm ) canvas.Print( std::string( pathPlots_ + histosDependency.histVecPtPar.at( uPar )->GetName() + "." + formatPlots_.at( uForm ) ).c_str() );
    }
  }

}


bool FitTopTransferFunctionsRunner::transferPerCategory( unsigned uCat )
{

  const std::string objCat( objCats_.at( uCat ) );
  if ( verbose_ > 1 ) {
    std::cout << std::endl
              << myName_ << " --> INFO:" << std::endl
              << "    Transfer function determination for object category " << objCat << std::endl;
  }

  // Fitting unscaled distribution
  if ( ! scale_ ) {
    if ( verbose_ > 2 ) {
      std::cout << std::endl
                << myName_ << " --> DEBUG:" << std::endl
                << "    Unscaled transfer functions... " << std::endl;
    }

    transferPerCategoryLoop( objCat, scale_ );
  }

  // Fitting scaled distribution
  if ( scale_ ) {
    if ( verbose_ > 2 ) {
      std::cout << std::endl
                << myName_ << " --> DEBUG:" << std::endl
                << "    Scaled transfer functions... " << std::endl;
    }

    transferPerCategoryLoop( objCat, scale_ );
  }

  return true;

}


void FitTopTransferFunctionsRunner::transferPerCategoryLoop( const std::string& objCat, bool scale )
{
  if ( scale ) transferPerCategoryBin( objCat, dirsOutObjCatSubFit_.back(), transferVecRebinScale_.back(), histosVecRebinScaleTrans_.back(), scale );
  else         transferPerCategoryBin( objCat, dirsOutObjCatSubFit_.back(), transferVecRebin_.back(), histosVecRebinTrans_.back(), scale );

  // Loop over eta bins
  if ( fitEtaBins_ ) {
    for ( unsigned uEta = 0; uEta < dirsOutObjCatSubFitEta_.back().size(); ++uEta ) {
      if ( scale ) transferPerCategoryBin( objCat, dirsOutObjCatSubFitEta_.back().at( uEta ), transferVecRebinScaleVecEta_.back().at( uEta ), histosVecRebinScaleVecTransEta_.back().at( uEta ), scale );
      else         transferPerCategoryBin( objCat, dirsOutObjCatSubFitEta_.back().at( uEta ), transferVecRebinVecEta_.back().at( uEta ), histosVecRebinVecTransEta_.back().at( uEta ), scale );
    } // loop: uEta < nEtaBins
  }
}


void FitTopTransferFunctionsRunner::transferPerCategoryBin( const std::string& objCat, TDirectory* dirOut, TransferFunction& transfer, HistosTransEta& histosTransEta, bool scale )
{

  // Get object configuration
  const edm::ParameterSet& configObj( config_.getParameter< edm::ParameterSet >( "objects" ).getParameter< edm::ParameterSet >( objCat ) );
  const double configObjDeltaPtMax( configObj.getParameter< double >( "deltaPtMax" ) );
  const double configObjWidthFactor( configObj.getParameter< double >( "widthFactor" ) );

  dirOut->cd();
  if ( verbose_ > 2 ) gDirectory->pwd();
  const std::string name( histosTransEta.histTrans->GetName() );
  const std::string nameTransferFunction( name + "_TransferFunction" );
  TF2* transferFunction( new TF2( ( ( TF2& )( *( transfer.Function( 0 ).Clone( nameTransferFunction.c_str() ) ) ) ) ) ); // hard-coded norm index 0
  transferFunction->SetRange( -2. * configObjWidthFactor * configObjDeltaPtMax, 0., 2. * configObjWidthFactor * configObjDeltaPtMax, 2. * objectData_.back().ptBins().back() );
  transferFunction->SetNpx();
  transferFunction->SetNpy();
  transferFunction->GetXaxis()->SetTitle( titleTrans_.c_str() );
  transferFunction->GetYaxis()->SetTitle( titlePt_.c_str() );
  if ( overwrite_ ) transferFunction->Write( 0, TObject::kOverwrite );
  else              transferFunction->Write();

  for ( unsigned uPt = 0; uPt < histosTransEta.histVecPtTrans.size(); ++uPt ) {
    const std::string binPt( boost::lexical_cast< std::string >( uPt ) );
    const std::string namePt( name + "_" + baseTitlePt_ + binPt );
    const std::string namePtTransferFunction( namePt + "_TransferFunction" );
    TF1* transferFunctionPt( new TF1( ( ( TF1& )( *( transfer.Function( ( objectData_.back().ptBins().at( uPt ) + objectData_.back().ptBins().at( uPt + 1 ) ) / 2., 0 ).Clone( namePtTransferFunction.c_str() ) ) ) ) ) );
    transferFunctionPt->SetRange( histosTransEta.histVecPtTrans.at( uPt )->GetXaxis()->GetXmin(), histosTransEta.histVecPtTrans.at( uPt )->GetXaxis()->GetXmax() );
    transferFunctionPt->SetLineColor( kRed );
    transferFunctionPt->SetLineStyle( 2 );
    histosTransEta.histVecPtTrans.at( uPt )->GetListOfFunctions()->Add( transferFunctionPt );
  }

  if ( plot_ ) {
    TCanvas canvas;
    transferFunction->Draw( "Surf3Z" );
    for ( unsigned uForm = 0; uForm < formatPlots_.size(); ++uForm ) canvas.Print( std::string( pathPlots_ + transferFunction->GetName() + "." + formatPlots_.at( uForm ) ).c_str() );
    histosTransEta.histTrans->Draw();
    std::string header( histosTransEta.legTrans->GetHeader() );
    header += ", scaled";
    histosTransEta.legTrans->SetHeader( header.c_str() );
    histosTransEta.legTrans->AddEntry( histosTransEta.histTrans, "MC", "LEP" );
    histosTransEta.legTrans->AddEntry( histosTransEta.histTrans->GetListOfFunctions()->First(), "fitted 1-D transfer function", "L" );
    histosTransEta.legTrans->Draw();
    for ( unsigned uForm = 0; uForm < formatPlots_.size(); ++uForm ) canvas.Print( std::string( pathPlots_ + histosTransEta.histTrans->GetName() + "." + formatPlots_.at( uForm ) ).c_str() );

    const std::string entryTransfer( "projected 2-D transfer function at " + titlePtT_ + " bin centre" );
    for ( unsigned uPt = 0; uPt < histosTransEta.histVecPtTrans.size(); ++uPt ) {
      histosTransEta.histVecPtTrans.at( uPt )->Draw();
      std::string header( histosTransEta.legVecPtTrans.at( uPt )->GetHeader() );
      header += ", scaled";
      histosTransEta.legVecPtTrans.at( uPt )->SetHeader( header.c_str() );
      histosTransEta.legVecPtTrans.at( uPt )->AddEntry( histosTransEta.histVecPtTrans.at( uPt ), "MC", "LEP" );
      histosTransEta.legVecPtTrans.at( uPt )->AddEntry( histosTransEta.histVecPtTrans.at( uPt )->GetListOfFunctions()->First(), "fitted 1-D transfer function", "L" );
      histosTransEta.legVecPtTrans.at( uPt )->AddEntry( histosTransEta.histVecPtTrans.at( uPt )->GetListOfFunctions()->Last(), entryTransfer.c_str(), "L" );
      histosTransEta.legVecPtTrans.at( uPt )->Draw();
      for ( unsigned uForm = 0; uForm < formatPlots_.size(); ++uForm ) canvas.Print( std::string( pathPlots_ + histosTransEta.histVecPtTrans.at( uPt )->GetName() + "." + formatPlots_.at( uForm ) ).c_str() );
    }
  }

}


bool FitTopTransferFunctionsRunner::compatibilityPerCategory( unsigned uCat )
{

  const std::string objCat( objCats_.at( uCat ) );
  if ( verbose_ > 1 ) {
    std::cout << std::endl
              << myName_ << " --> INFO:" << std::endl
              << "    Transfer function compatibility for object category " << objCat << std::endl;
  }

  // Fitting unscaled distribution
  if ( ! scale_ ) {
    if ( verbose_ > 2 ) {
      std::cout << std::endl
                << myName_ << " --> DEBUG:" << std::endl
                << "    Unscaled transfer function compatibilities... " << std::endl;
    }

    compatibilityPerCategoryLoop( objCat, scale_ );
  }

  // Fitting scaled distribution
  if ( scale_ ) {
    if ( verbose_ > 2 ) {
      std::cout << std::endl
                << myName_ << " --> DEBUG:" << std::endl
                << "    Scaled transfer function compatibilities... " << std::endl;
    }

    compatibilityPerCategoryLoop( objCat, scale_ );
  }

  return true;

}


void FitTopTransferFunctionsRunner::compatibilityPerCategoryLoop( const std::string& objCat, bool scale )
{
  if ( scale ) compatibilityPerCategoryBin( objCat, dirsOutObjCatSubFit_.back(), transferVecRebinScale_.back(), histosVecRebinTrans_.back(), -1, scale );
  else         compatibilityPerCategoryBin( objCat, dirsOutObjCatSubFit_.back(), transferVecRebin_.back(), histosVecRebinTrans_.back(), -1, scale );

  // Loop over eta bins
  if ( fitEtaBins_ ) {
    avPChi2VecRebinTransEta_.push_back( std::vector< Double_t >() );
    avPKSVecRebinTransEta_.push_back( std::vector< Double_t >() );
    avPChi2VecRebinScaleTransEta_.push_back( std::vector< Double_t >() );
    avPKSVecRebinScaleTransEta_.push_back( std::vector< Double_t >() );
    for ( unsigned uEta = 0; uEta < dirsOutObjCatSubFitEta_.back().size(); ++uEta ) {
      if ( scale ) {
        compatibilityPerCategoryBin( objCat, dirsOutObjCatSubFitEta_.back().at( uEta ), transferVecRebinScaleVecEta_.back().at( uEta ), histosVecRebinVecTransEta_.back().at( uEta ), uEta, scale );
      }
      else {
        compatibilityPerCategoryBin( objCat, dirsOutObjCatSubFitEta_.back().at( uEta ), transferVecRebinVecEta_.back().at( uEta ), histosVecRebinVecTransEta_.back().at( uEta ), uEta, scale );
      }
    } // loop: uEta < nEtaBins
  }
}


void FitTopTransferFunctionsRunner::compatibilityPerCategoryBin( const std::string& objCat, TDirectory* dirOut, TransferFunction& transfer, HistosTransEta& histosTransEta, int uEta, bool scale )
{

  dirOut->cd();
  if ( verbose_ > 2 ) gDirectory->pwd();

  const std::string name( histosTransEta.histTrans->GetName() );
  Double_t sumEntries( 0. );
  Double_t sumPChi2( 0. );
  Double_t sumPKS( 0. );
  std::vector< Double_t > pChi2Vec;
  std::vector< Double_t > pKSVec;
  for ( unsigned uPt = 0; uPt < histosTransEta.histVecPtTrans.size(); ++uPt ) {
    // Get transfer function
    const std::string binPt( boost::lexical_cast< std::string >( uPt ) );
    const std::string namePt( name + "_" + baseTitlePt_ + binPt );
    const std::string namePtTransferFunction( namePt + "_TransferFunction" );
    const std::string formula( transfer.Formula( ( objectData_.back().ptBins().at( uPt ) + objectData_.back().ptBins().at( uPt + 1 ) ) / 2. ) );
    Double_t norm( scale ? histosTransEta.histVecPtTrans.at( uPt )->Integral("width") : 1. );
    const std::string normStr( boost::lexical_cast< std::string >( norm ) );
    const std::string functionStr( normStr + "*(" + formula + ")" );
    TF1* transferFunctionPt( new TF1( namePtTransferFunction.c_str(), functionStr.c_str(), histosTransEta.histVecPtTrans.at( uPt )->GetXaxis()->GetXmin(), histosTransEta.histVecPtTrans.at( uPt )->GetXaxis()->GetXmax() ) );
    transferFunctionPt->SetTitle( functionStr.c_str() );
    transferFunctionPt->SetLineColor( kBlack );
    histosTransEta.histVecPtTrans.at( uPt )->GetListOfFunctions()->Add( transferFunctionPt );
    // Build histogram to compare and perform tests
    TH1D h1;
    histosTransEta.histVecPtTrans.at( uPt )->Copy( h1 );
    const std::string namePtHisto( namePt + "_Histo" );
    h1.SetName( namePtHisto.c_str() );
    for ( Int_t bin = 1; bin <= histosTransEta.histVecPtTrans.at( uPt )->GetNbinsX(); ++bin ) {
      h1.SetBinContent( bin, transferFunctionPt->Integral( histosTransEta.histVecPtTrans.at( uPt )->GetBinLowEdge( bin ), histosTransEta.histVecPtTrans.at( uPt )->GetBinLowEdge( bin ) + histosTransEta.histVecPtTrans.at( uPt )->GetBinWidth( bin ) ) / histosTransEta.histVecPtTrans.at( uPt )->GetBinWidth( bin ) );
      h1.SetBinError( bin, TMath::Sqrt( h1.GetBinContent( bin ) / norm ) );
    }
    std::string optionsChi2( "UW" );
    std::string optionsKS( "" );
    if ( verbose_ > 2 ) {
      optionsChi2.append( "P" );
      optionsKS.append( "D" );
    }
    const Double_t entries( histosTransEta.histVecPtTrans.at( uPt )->GetEntries() );
    pChi2Vec.push_back( histosTransEta.histVecPtTrans.at( uPt )->Chi2Test( &h1, optionsChi2.c_str() ) );
    pKSVec.push_back( histosTransEta.histVecPtTrans.at( uPt )->KolmogorovTest( &h1, optionsKS.c_str() ) );
    sumPChi2   += pChi2Vec.back() * entries;
    sumPKS     += pKSVec.back()   * entries;
    sumEntries += entries;
  }
  Double_t avPChi2( sumPChi2 / sumEntries );
  Double_t avPKS( sumPKS / sumEntries );
  if ( uEta >= 0 ) {
    if ( scale ) {
      avPChi2VecRebinScaleTransEta_.back().push_back( avPChi2 );
      avPKSVecRebinScaleTransEta_.back().push_back( avPKS );
    }
    else {
      avPChi2VecRebinTransEta_.back().push_back( avPChi2 );
      avPKSVecRebinTransEta_.back().push_back( avPKS );
    }
  }
  else {
    if ( scale ) {
      avPChi2VecRebinScaleTrans_.push_back( avPChi2 );
      avKSVecRebinScaleTrans_.push_back( avPKS );
    }
    else {
      avPChi2VecRebinTrans_.push_back( avPChi2 );
      avKSVecRebinTrans_.push_back( avPKS );
    }
  }
  if ( verbose_ > 1 ) {
    std::cout << std::endl
              << myName_ << " --> INFO:" << std::endl
              << "    Weighted average Chi2 prob.: " << avPChi2 << std::endl
              << "    Weighted average KS   prob.: " << avPKS   << std::endl;
  }

  if ( plot_ ) {
    TCanvas canvas;
    histosTransEta.histTrans->Draw();
    std::string header( histosTransEta.legTrans->GetHeader() );
    header += ", unscaled";
    histosTransEta.legTrans->SetHeader( header.c_str() );
    histosTransEta.legTrans->AddEntry( histosTransEta.histTrans, "MC", "LEP" );
    histosTransEta.legTrans->Draw();
    for ( unsigned uForm = 0; uForm < formatPlots_.size(); ++uForm ) canvas.Print( std::string( pathPlots_ + histosTransEta.histTrans->GetName() + "." + formatPlots_.at( uForm ) ).c_str() );

    const std::string entryTransfer( "projected 2-D transfer function at " + titlePtT_ + " bin centre" );
    for ( unsigned uPt = 0; uPt < histosTransEta.histVecPtTrans.size(); ++uPt ) {
      histosTransEta.histVecPtTrans.at( uPt )->Draw();
      std::string header( histosTransEta.legVecPtTrans.at( uPt )->GetHeader() );
      header += ", unscaled";
      histosTransEta.legVecPtTrans.at( uPt )->SetHeader( header.c_str() );
      histosTransEta.legVecPtTrans.at( uPt )->AddEntry( histosTransEta.histVecPtTrans.at( uPt ), "MC", "LEP" );
      histosTransEta.legVecPtTrans.at( uPt )->AddEntry( histosTransEta.histVecPtTrans.at( uPt )->GetListOfFunctions()->Last(), entryTransfer.c_str(), "L" );
      const std::string entryChi2( "#Chi^{2} prob.: " + boost::lexical_cast< std::string >( pChi2Vec.at( uPt ) ) );
      histosTransEta.legVecPtTrans.at( uPt )->AddEntry( (TObject*)0, entryChi2.c_str(), "" );
      const std::string entryKS( "KS prob.: " + boost::lexical_cast< std::string >( pKSVec.at( uPt ) ) );
      histosTransEta.legVecPtTrans.at( uPt )->AddEntry( (TObject*)0, entryKS.c_str(), "" );
      histosTransEta.legVecPtTrans.at( uPt )->Draw();
      for ( unsigned uForm = 0; uForm < formatPlots_.size(); ++uForm ) canvas.Print( std::string( pathPlots_ + histosTransEta.histVecPtTrans.at( uPt )->GetName() + "." + formatPlots_.at( uForm ) ).c_str() );
    }
  }

}


bool FitTopTransferFunctionsRunner::writeFilesPerCategory( unsigned uCat )
{

  if ( pathOut_.empty() ) {
    if ( verbose_ > 0 ) {
      std::cout << std::endl
                << myName_ << " --> EARNING:" << std::endl
                << "    No path for transfer function output specified" << std::endl;
    }
    return false;
  }

  const std::string objCat( objCats_.at( uCat ) );
  if ( verbose_ > 1 ) {
    std::cout << std::endl
              << myName_ << " --> INFO:" << std::endl
              << "    Writing files for object category " << objCat << std::endl
              << "        to " << pathOut_ << std::endl;
  }

  // Writing unscaled transfer functions
  if ( ! scale_ ) {
    if ( verbose_ > 2 ) {
      std::cout << std::endl
                << myName_ << " --> DEBUG:" << std::endl
                << "    Unscaled transfer functions... " << std::endl;
    }

    writeFilesPerCategoryLoop( objCat, scale_ );
  }

  // Writing scaled transfer functions
  if ( scale_ ) {
    if ( verbose_ > 2 ) {
      std::cout << std::endl
                << myName_ << " --> DEBUG:" << std::endl
                << "    Scaled transfer functions... " << std::endl;
    }

    writeFilesPerCategoryLoop( objCat, scale_ );
  }

  return true;

}


void FitTopTransferFunctionsRunner::writeFilesPerCategoryLoop( const std::string& objCat, bool scale )
{
  const int nPtBins( objectData_.back().nPtBins() );
  const int nEtaBins( objectData_.back().nEtaBins() );

  if ( scale ) writeFilesPerCategoryBin( objCat, transferVecRebinScale_.back(), histosVecRebinTrans_.back().histTrans->GetName(), -1, -1, scale );
  else         writeFilesPerCategoryBin( objCat, transferVecRebin_.back(), histosVecRebinTrans_.back().histTrans->GetName(), -1, -1, scale );
  // Loop over pt bins
  if ( writeFilesPt_ ) {
    for ( int uPt = 0; uPt < nPtBins; ++uPt ) {
      const std::string binPt( boost::lexical_cast< std::string >( uPt ) );
      std::string namePt( histosVecRebinTrans_.back().histTrans->GetName() );
      namePt.append( "_Pt" + binPt );
      if ( scale ) writeFilesPerCategoryBin( objCat, transferVecRebinScaleVecPt_.back().at( uPt ), namePt, uPt, -1, scale );
      else         writeFilesPerCategoryBin( objCat, transferVecRebinVecPt_.back().at( uPt ), namePt, uPt, -1, scale );
    }
  }

  // Loop over eta bins
  if ( fitEtaBins_ ) {
    for ( int uEta = 0; uEta < nEtaBins; ++uEta ) {
      if ( scale ) writeFilesPerCategoryBin( objCat, transferVecRebinScaleVecEta_.back().at( uEta ), histosVecRebinVecTransEta_.back().at( uEta ).histTrans->GetName(), -1, uEta, scale );
      else         writeFilesPerCategoryBin( objCat, transferVecRebinVecEta_.back().at( uEta ), histosVecRebinVecTransEta_.back().at( uEta ).histTrans->GetName(), -1, uEta, scale );
      // Loop over pt bins
      if ( writeFilesPt_ ) {
        for ( int uPt = 0; uPt < nPtBins; ++uPt ) {
          const std::string binPt( boost::lexical_cast< std::string >( uPt ) );
          std::string namePt( histosVecRebinVecTransEta_.back().at( uEta ).histTrans->GetName() );
          namePt.append( "_Pt" + binPt );
          if ( scale ) writeFilesPerCategoryBin( objCat, transferVecRebinScaleVecEtaVecPt_.back().at( uEta ).at( uPt ), namePt, uPt, uEta, scale );
          else         writeFilesPerCategoryBin( objCat, transferVecRebinVecEtaVecPt_.back().at( uEta ).at( uPt ), namePt, uPt, uEta, scale );
        }
      }
    } // loop: uEta < nEtaBins
  }
}


void FitTopTransferFunctionsRunner::writeFilesPerCategoryBin( const std::string& objCat, TransferFunction& transfer, const std::string& name, int uPt, int uEta, bool scale )
{

  std::string nameOut( pathOut_ + "/gentTransferFunction" + sample_ );
  if ( scale )      nameOut.append( "_Scaled" );
  if ( usePileup_ ) nameOut.append( "_PileUp" );
  if ( refSel_ )    nameOut.append( "_Ref" );
  nameOut.append( "_" + name + ".txt" );

  ofstream fileOut;
  fileOut.open( nameOut.c_str(), std::ios_base::out );
  if ( uEta >= 0 )             fileOut << "for " << objectData_.back().etaBins().at( uEta )   << " <= " << baseTitleEta_ << " < " << objectData_.back().etaBins().at( uEta + 1 )         << std::endl;
  if ( uPt >= 0 )              fileOut << "for " << objectData_.back().ptBins().at( uPt ) << " GeV <= " << baseTitlePt_  << " < " << objectData_.back().ptBins().at( uPt + 1 ) << " GeV" << std::endl;
  if ( uPt >= 0 || uEta >= 0 ) fileOut << "--------------------------------------------------------------------------------" << std::endl;
  if ( uPt >= 0 ) fileOut << transfer.Print( true );
  else            fileOut << transfer.Print();
  fileOut << std::endl;
  fileOut.close();
  if ( verbose_ > 1 ) {
    std::cout << std::endl
              << myName_ << " --> INFO:" << std::endl
              << "    Wrote file:" << std::endl
              << "        " << nameOut << std::endl;
  }

}