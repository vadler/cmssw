#include <string>
#include <iostream>

#include <TROOT.h>
#include <TSystem.h>
#include <TFile.h>
#include <TH1D.h>

#include "FWCore/FWLite/interface/AutoLibraryLoader.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/PythonParameterSet/interface/MakeParameterSets.h"


int main(  int argc, char * argv[] )
{

  // Load libraries
  gSystem->Load( "libFWCoreFWLite" );
  AutoLibraryLoader::enable();

  // Check configuration file
  if ( argc < 2 ) {
    std::cout << argv[ 0 ] << " --> Usage:" << std::endl
              << "    " << argv[ 0 ] << " [CONFIG_FILE.py]" << std::endl;
    return 0;
  }
  if ( ! edm::readPSetsFrom( argv[ 1 ] )->existsAs< edm::ParameterSet >( "process" ) ) {
    std::cout << argv[ 0 ] << " --> ERROR:" << std::endl
              << "   cms.PSet 'process' missing in " << argv[ 1 ] << std::endl;
    return 1;
  }

  // Get the configurations
  const edm::ParameterSet & process_( edm::readPSetsFrom( argv[ 1 ] )->getParameter< edm::ParameterSet >( "process" ) );
  const std::string         file_( process_.getParameter< std::string >( "file" ) );
  const std::string         pileUpHisto_( process_.getParameter< std::string >( "pileUpHisto" ) );

  // Open file
  TFile* file( TFile::Open( file_.c_str(), "UPDATE" ) );
  TH1D* histPileUp( ( TH1D* )( file->Get( pileUpHisto_.c_str() ) ) );
  if ( ! histPileUp ) {
    std::cout << argv[ 0 ] << " --> ERROR:" << std::endl
              << "   histogram '" << pileUpHisto_ << "' missing in file '" << file_ << "'" << std::endl;
    return 10;
  }

  // Create scaled histogram clone
  TH1D* histPileUpScaled = new TH1D( *( ( TH1D* )( histPileUp->Clone( "pileupScaled" ) ) ) );
  histPileUpScaled->SetTitle( "Pile-up (normalised)" );
  histPileUpScaled->Scale( 1. / histPileUp->Integral( "width" ) );

  // Close output file
  histPileUpScaled->Write();
  file->Close();

  return 0;

}
