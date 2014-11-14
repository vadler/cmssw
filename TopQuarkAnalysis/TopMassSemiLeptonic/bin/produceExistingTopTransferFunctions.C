#include <string>
#include <vector>
#include <iostream>
#include <cmath>

#include "boost/lexical_cast.hpp"

#include <TROOT.h>
#include <TSystem.h>
#include <TFile.h>
#include <TF1.h>

#include "FWCore/FWLite/interface/AutoLibraryLoader.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/PythonParameterSet/interface/MakeParameterSets.h"

#include "CommonTools/MyTools/interface/RootFunctions.h"


int main( int argc, char * argv[] )
{

  int returnStatus_( 0 );

  // Check configuration file
  if ( argc < 2 ) {
    std::cout << argv[ 0 ] << " --> Usage:" << std::endl
              << "    " << argv[ 0 ] << " [CONFIG_FILE.py]" << std::endl;
    returnStatus_ += 0x1;
    return returnStatus_;
  }
  if ( ! edm::readPSetsFrom( argv[ 1 ] )->existsAs< edm::ParameterSet >( "process" ) ) {
    std::cout << argv[ 0 ] << " --> ERROR:" << std::endl
              << "   cms.PSet 'process' missing in " << argv[ 1 ] << std::endl;
    returnStatus_ += 0x2;
    return returnStatus_;
  }

  // Get the configurations
  const edm::ParameterSet & process_( edm::readPSetsFrom( argv[ 1 ] )->getParameter< edm::ParameterSet >( "process" ) );
  const std::vector< std::string > objCats_( process_.getParameterNamesForType< edm::ParameterSet >() );

  // Open output file
  TFile* fileOut_( TFile::Open( "existingTopTransferFunctions.root", "UPDATE" ) );
  if ( ! fileOut_ ) fileOut_ = TFile::Open( "existingTopTransferFunctions.root", "NEW" );

  for ( unsigned uCat = 0; uCat < objCats_.size(); ++uCat ) {
    const std::string objCat( objCats_.at( uCat ) );
    TDirectory* dirCat_( ( TDirectory* )( fileOut_->Get( objCat.c_str() ) ) );
    if ( ! dirCat_ ) {
      fileOut_->cd();
      dirCat_ = new TDirectoryFile( objCat.c_str(), "" );
    }

    const edm::ParameterSet& object_( process_.getParameter< edm::ParameterSet >( objCat ) );
    const std::vector< std::string > etaBins_( object_.getParameterNamesForType< edm::ParameterSet >() );
    for ( unsigned uEta = 0; uEta < etaBins_.size(); ++uEta ) {
      const std::string etaBin( etaBins_.at( uEta ) );
      TDirectory* dirEta_( ( TDirectory* )( dirCat_->Get( etaBin.c_str() ) ) );
      if ( ! dirEta_ ) {
        dirCat_->cd();
        dirEta_ = new TDirectoryFile( etaBin.c_str(), "" );
      }

      const edm::ParameterSet& eta_( object_.getParameter< edm::ParameterSet >( etaBin ) );
      const std::vector< std::string > ptBins_( eta_.getParameterNamesForType< edm::ParameterSet >() );
      for ( unsigned uPt = 0; uPt < ptBins_.size(); ++uPt ) {
        const std::string ptBin( ptBins_.at( uPt ) );

        const edm::ParameterSet& pt_( eta_.getParameter< edm::ParameterSet >( ptBin ) );
        const std::vector< double > params( pt_.getParameter< std::vector< double > >( "params" ) );
        TF1* function( new TF1( ptBin.c_str(), "[0]*(exp(-0.5*((x-[1])/[2])**2)+[3]*exp(-0.5*((x-[4])/[5])**2))/(([2]+[3]*[5])*sqrt(2*pi))", -100., 100. ) );
        function->SetParameter( 0, 1. );
        for ( unsigned uPar = 1; uPar <= params.size(); ++uPar ) {
          function->SetParameter( uPar, params.at( uPar - 1 ) );
        }
        dirEta_->cd();
        function->Write();
      }
    }

  }

  // Write and close output file
  fileOut_->Write();
  fileOut_->Close();

}