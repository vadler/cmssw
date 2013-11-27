#include <string>
#include <iostream>

#include "FWCore/PythonParameterSet/interface/MakeParameterSets.h"

#include "CommonTools/MyTools/interface/RootFunctions.h"

#include "TopQuarkAnalysis/TopMassSemiLeptonic/interface/FitTopTransferFunctionsRunner.h"


int main( int argc, char * argv[] )
{

  int oStatus( 0 );

  const std::string name( argv[ 0 ] );

  // Check configuration file
  if ( argc < 2 ) {
    std::cout << name << " --> Usage:" << std::endl
              << "    " << name << " [CONFIG_FILE.py]" << std::endl;
    oStatus += 0x1;
    return oStatus;
  }
  if ( ! edm::readPSetsFrom( argv[ 1 ] )->existsAs< edm::ParameterSet >( "fitTopTransferFunctions" ) ) {
    std::cout << name << " --> ERROR:" << std::endl
              << "    cms.PSet 'fitTopTransferFunctions' missing in " << argv[ 1 ] << std::endl;
    oStatus += 0x2;
    return oStatus;
  }

  // Run
  my::FitTopTransferFunctionsRunner runner( name, edm::readPSetsFrom( argv[ 1 ] )->getParameter< edm::ParameterSet >( "fitTopTransferFunctions" ) );
  oStatus += runner.run();

  return oStatus;

}