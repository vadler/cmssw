#include "TopQuarkAnalysis/TopMassSemiLeptonic/interface/CompareTopTransferFunctionsRunner.h"

#include <iostream>

#include <TROOT.h>
#include <TStyle.h>
#include <TH1D.h>
#include <TH2D.h>

#include "CommonTools/MyTools/interface/RootTools.h"


using namespace my;


CompareTopTransferFunctionsRunner::CompareTopTransferFunctionsRunner( const std::string& iName, const edm::ParameterSet& iConfig )
: myName_( iName )
, status_( 0 )
, config_( iConfig )
, verbose_( config_.getParameter< unsigned >( "verbose" ) )
{

  const edm::ParameterSet& configIO( config_.getParameter< edm::ParameterSet >( "io" ) );
  const bool configIOFullStats( configIO.getParameter< bool >( "fullStats" ) );
  const edm::ParameterSet& configCompare( config_.getParameter< edm::ParameterSet >( "compare" ) );
  useSymm_ = configCompare.getParameter< bool >( "useSymm" );
  useAlt_  = configCompare.getParameter< bool >( "useAlt" );
  useNonT_ = configCompare.getParameter< bool >( "useNonT" );
  refGen_  = configCompare.getParameter< bool >( "refGen" );
  refSel_  = configCompare.getParameter< bool >( "refSel" );
  const edm::ParameterSet& configInput( configCompare.getParameter< edm::ParameterSet >( "inputFiles" ) );
  names_ = configInput.getParameterNamesForType< edm::ParameterSet >();
  size_  = names_.size();
  fileNames_.clear();
  cycles_.clear();
  for ( unsigned uName = 0; uName < size_; ++uName ) {
    const edm::ParameterSet& config( configInput.getParameter< edm::ParameterSet >( names_.at( uName ) ) );
    fileNames_.push_back( config.getParameter< std::string >( "fileName" ) );
    cycles_.push_back( config.getParameter< int >( "cycle" ) );
  }

  if ( verbose_ > 1 ) {
    std::cout << std::endl
              << myName_ << " --> INFO:" << std::endl
              << "    called for" << size_ << " input files " << std::endl;
    for ( unsigned uName = 0; uName < size_; ++uName ) {
      std::cout << "  '" << fileNames_.at( uName ) << "', cycle " << cycles_.at( uName ) << std::endl;
    }
  }

  // Set up ROOT
  setPlotEnvironment( gStyle );
  if ( configIOFullStats ) {
    gStyle->SetOptStat( 111111 );
    gStyle->SetOptFit( 1111 );
    gStyle->SetStatW( 0.1 );
  }
  TH1D::SetDefaultSumw2();
  TH2D::SetDefaultSumw2();

  // Set constants
  std::string evtSel( "analyzeHitFit" );
  if ( refSel_ ) evtSel.append( "Reference" );

  // Open input files
  filesIn_.clear();
  pwds_.clear();
  for ( unsigned uName = 0; uName < size_; ++uName ) {
    const std::string fileName( fileNames_.at( uName ) );
    if ( verbose_ > 1 ) {
      std::cout << myName_ << " --> INFO:" << std::endl
                << "    opening input file '" << fileName  << "'" << std::endl;
    }
    TFile* file( TFile::Open( fileName.c_str(), "READ" ) );
    if ( ! file ) {
      std::cout << myName_ << " --> ERROR:" << std::endl
                << "    input file '" << fileName << "' missing" << std::endl;
      status_ += 0x10;
      return;
    }
    filesIn_.push_back( file );
    TDirectory* pwd( ( TDirectory* )( file->Get( evtSel.c_str() ) ) );
    if ( ! pwd ) {
      std::cout << myName_ << " --> ERROR:" << std::endl
                << "    selection '" << evtSel << "' does not exist in input file " << fileName << std::endl;
      status_ += 0x20;
      return;
    }
    pwds_.push_back( pwd );
  }

}


CompareTopTransferFunctionsRunner::~CompareTopTransferFunctionsRunner()
{

  for ( unsigned uName = 0; uName < size_; ++uName ) {
    filesIn_.at( uName )->Close();
  }

}


int CompareTopTransferFunctionsRunner::run()
{

  if ( status != 0 ) return status_;
  return status_;

}
