//
// $Id: TransferFunction.cc,v 1.21 2013/02/27 02:18:02 vadler Exp $
//


#include "TopQuarkAnalysis/TopMassSemiLeptonic/interface/TransferFunction.h"

#include <sstream>
#include "boost/lexical_cast.hpp"


using namespace my;


// Constructors and Destructor

// Constructor from TransferFunction (copy c'tor)
TransferFunction::TransferFunction( const TransferFunction& transfer )
: fitFunction_( transfer.GetFitFunction() )
, fitFunctionString_( transfer.FitFunctionString() )
, dependencyFunction_( transfer.GetDependencyFunction() )
, dependencyFunctionString_( transfer.DependencyFunctionString() )
, resolutionFunction_( transfer.GetResolutionFunction() )
, resolutionFunctionString_( transfer.ResolutionFunctionString() )
, dependency_( transfer.Dependency() )
, comment_( transfer.Comment() )
{
  sigmaPars_ = transfer.SigmaPars();
  ClearParameters();
  pars1D_    = transfer.pars1D_;
  errs1D_    = transfer.errs1D_;
  pars2D_    = transfer.pars2D_;
  errs2D_    = transfer.errs2D_;
}

// Constructor from strings
TransferFunction::TransferFunction( const std::string& fitFunction, const std::set< int >& sigmaPars, const std::string& dependencyFunction, const std::string& resolutionFunction, const std::string& dependency )
: fitFunction_( "fitFunction", fitFunction.c_str() )
, fitFunctionString_( fitFunction )
, dependencyFunction_( "dependencyFunction", dependencyFunction.c_str() )
, dependencyFunctionString_( dependencyFunction )
, resolutionFunction_( "resolutionFunction", resolutionFunction.c_str() )
, resolutionFunctionString_( resolutionFunction )
, dependency_( dependency )
, comment_()
{
  sigmaPars_ = sigmaPars;
  ClearParameters();
}

// Constructor from TF1s
TransferFunction::TransferFunction( TF1* fitFunction, const std::set< int >& sigmaPars, TF1* dependencyFunction, TF1* resolutionFunction, const std::string& dependency )
: fitFunction_( *fitFunction )
, fitFunctionString_( "" )
, dependencyFunction_( *dependencyFunction )
, dependencyFunctionString_( "" )
, resolutionFunction_( *resolutionFunction )
, resolutionFunctionString_( "" )
, dependency_( dependency )
, comment_()
{
  sigmaPars_ = sigmaPars;
  ClearParameters();
  fitFunction_.SetName( "fitFunction" );
  dependencyFunction_.SetName( "dependencyFunction" );
  resolutionFunction_.SetName( "resolutionFunction" );
}


// Methods

// Setters

void TransferFunction::SetFitFunction( const std::string& fitFunctionString, const std::set< int >& sigmaPars )
{
  fitFunction_       = TF1( "fitFunction", fitFunctionString.c_str() );
  fitFunctionString_ = fitFunctionString;
  sigmaPars_         = sigmaPars;
  ClearParameters();
}

void TransferFunction::SetFitFunction( TF1* fitFunction, const std::set< int >& sigmaPars )
{
  fitFunction_ = TF1( *fitFunction );
  fitFunction_.SetName( "fitFunction" );
  fitFunctionString_ = fitFunction->GetTitle();
  sigmaPars_         = sigmaPars;
  ClearParameters();
}

void TransferFunction::SetFitFunctionString( const std::string& fitFunctionString )
{
  if ( FitFunction().empty() ) fitFunctionString_ = fitFunctionString;
}

void TransferFunction::SetDependencyFunction( const std::string& dependencyFunctionString )
{
  dependencyFunction_       = TF1( "dependencyFunction", dependencyFunctionString.c_str() );
  dependencyFunctionString_ = dependencyFunctionString;
  ClearParameters();
}

void TransferFunction::SetDependencyFunction( TF1* dependencyFunction )
{
  dependencyFunction_ = TF1( *dependencyFunction );
  dependencyFunction_.SetName( "dependencyFunction" );
  dependencyFunctionString_ = dependencyFunction->GetTitle();
  ClearParameters();
}

void TransferFunction::SetDependencyFunctionString( const std::string& dependencyFunctionString )
{
  if ( DependencyFunction().empty() ) dependencyFunctionString_ = dependencyFunctionString;
}

void TransferFunction::SetResolutionFunction( const std::string& resolutionFunctionString )
{
  resolutionFunction_       = TF1( "resolutionFunction", resolutionFunctionString.c_str() );
  resolutionFunctionString_ = resolutionFunctionString;
  ClearParameters();
}

void TransferFunction::SetResolutionFunction( TF1* resolutionFunction )
{
  resolutionFunction_ = TF1( *resolutionFunction );
  resolutionFunction_.SetName( "resolutionFunction" );
  resolutionFunctionString_ = resolutionFunction->GetTitle();
  ClearParameters();
}

void TransferFunction::SetResolutionFunctionString( const std::string& resolutionFunctionString )
{
  if ( ResolutionFunction().empty() ) resolutionFunctionString_ = resolutionFunctionString;
}

bool TransferFunction::SetParameter( unsigned i, double par )
{
  if ( i < NParFit() ) {
    pars1D_.at( i ) = par;
    return true;
  }
  return false;
}

bool TransferFunction::SetError( unsigned i, double err )
{
  if ( i < NParFit() ) {
    errs1D_.at( i ) = err;
    return true;
  }
  return false;
}

bool TransferFunction::SetParameter( unsigned i, unsigned j, double par )
{
  if ( i < NParFit() && j < NParDependency() ) {
    pars2D_.at( i ).at( j ) = par;
    return true;
  }
  return false;
}

bool TransferFunction::SetError( unsigned i, unsigned j, double err )
{
  if ( i < NParFit() && j < NParDependency() ) {
    errs2D_.at( i ).at( j ) = err;
    return true;
  }
  return false;
}

bool TransferFunction::SetParameters( std::vector< double > pars )
{
  if ( pars.size() == NParFit() ) {
    pars1D_ = pars;
    return true;
  }
  return false;
}

bool TransferFunction::SetErrors( std::vector< double > errs )
{
  if ( errs.size() == NParFit() ) {
    errs1D_ = errs;
    return true;
  }
  return false;
}

bool TransferFunction::SetParameters( unsigned j, std::vector< double > pars )
{
  if ( j < NParDependency() && pars.size() == NParFit() ) {
    for ( unsigned i = 0; i < pars.size(); ++i ) {
      pars2D_.at( i ).at( j ) = pars.at( i );
    }
    return true;
  }
  return false;
}

bool TransferFunction::SetErrors( unsigned j, std::vector< double > errs )
{
  if ( j < NParDependency() && errs.size() == NParFit() ) {
    for ( unsigned i = 0; i < errs.size(); ++i ) {
      errs2D_.at( i ).at( j ) = errs.at( i );
    }
    return true;
  }
  return false;
}

void TransferFunction::ClearParameters()
{
  pars1D_.clear();
  pars2D_.clear();
  pars1D_.resize( NParFit() );
  pars2D_.resize( NParFit(), std::vector< double >( NParDependency() ) );
  for ( std::set< int >::const_iterator k = sigmaPars_.begin(); k != sigmaPars_.end(); ++k ) {
    pars2D_.at( *k ).resize( NParResolution() );
  }
  for ( unsigned i = 0; i < NParFit(); ++i ) {
    pars1D_.at( i ) = transferFunctionInitConst;
    for ( unsigned j = 0; j < pars2D_.at( i ).size(); ++j ) {
      pars2D_.at( i ).at( j ) = transferFunctionInitConst;
    }
  }
  ClearErrors();
}

void TransferFunction::ClearErrors()
{
  errs1D_.clear();
  errs2D_.clear();
  errs1D_.resize( NParFit() );
  errs2D_.resize( NParFit(), std::vector< double >( NParDependency() ) );
  for ( std::set< int >::const_iterator k = sigmaPars_.begin(); k != sigmaPars_.end(); ++k ) {
    errs2D_.at( *k ).resize( NParResolution() );
  }
  for ( unsigned i = 0; i < NParFit(); ++i ) {
    errs1D_.at( i ) = transferFunctionInitConst;
    for ( unsigned j = 0; j < errs2D_.at( i ).size(); ++j ) {
      errs2D_.at( i ).at( j ) = transferFunctionInitConst;
    }
  }
}

// Getters

// FIXME: Adapt to resolution function
double TransferFunction::Parameter( unsigned i, unsigned j ) const
{
  if ( i < NParFit() && j < NParDependency() ) return pars2D_.at( i ).at( j );
  return transferFunctionInitConst;
}

// FIXME: Adapt to resolution function
double TransferFunction::Error( unsigned i, unsigned j ) const
{
  if ( i < NParFit() && j < NParDependency() ) return errs2D_.at( i ).at( j );
  return transferFunctionInitConst;
}

// FIXME: Adapt to resolution function
std::vector< double > TransferFunction::Parameters( unsigned j ) const
{
  if ( j < NParDependency() ) {
    std::vector< double > pars;
    for ( unsigned i = 0; i < NParFit(); ++i ) {
      pars.push_back( pars2D_.at( i ).at( j ) );
    }
    return pars;
  }
  return std::vector< double >();
}

// FIXME: Adapt to resolution function
std::vector< double > TransferFunction::Errors( unsigned j ) const
{
  if ( j < NParDependency() ) {
    std::vector< double > errs;
    for ( unsigned i = 0; i < NParFit(); ++i ) {
      errs.push_back( errs2D_.at( i ).at( j ) );
    }
    return errs;
  }
  return std::vector< double >();
}

// Evaluate

// FIXME: Adapt to resolution function
TransferFunction TransferFunction::FunctionErrorsUp() const
{
  TransferFunction transferFunction( *this );
  for ( unsigned i = 0; i < transferFunction.NParFit(); ++i ) {
    transferFunction.SetParameter( i, transferFunction.Parameter( i ) + transferFunction.Error( i ) );
    for ( unsigned j = 0; j < transferFunction.NParDependency(); ++j ) {
      transferFunction.SetParameter( i, j, transferFunction.Parameter( i, j ) + transferFunction.Error( i, j ) );
    }
  }
  transferFunction.ClearErrors();
  return transferFunction;
}

// FIXME: Adapt to resolution function
TransferFunction TransferFunction::FunctionErrorsDown() const
{
  TransferFunction transferFunction( *this );
  for ( unsigned i = 0; i < transferFunction.NParFit(); ++i ) {
    transferFunction.SetParameter( i, transferFunction.Parameter( i ) - transferFunction.Error( i ) );
    for ( unsigned j = 0; j < transferFunction.NParDependency(); ++j ) {
      transferFunction.SetParameter( i, j, transferFunction.Parameter( i, j ) - transferFunction.Error( i, j ) );
    }
  }
  transferFunction.ClearErrors();
  return transferFunction;
}

// FIXME: Adapt to resolution function
TF2 TransferFunction::Function( int norm ) const
{
  TString fitStr;
  if ( FitFunction().empty() && ! FitFunctionString().empty() ) {
    fitStr = TString( FitFunctionString() );
  }
  else {
    fitStr = TString( FitFunction() );
  }
  if ( fitStr.Length() == 0 ) return TF2();
  std::vector< double > pars;
  for ( unsigned i = 0; i < NParFit(); ++i ) {
    if ( ( int )i == norm ) continue;
    TString depStr;
    if ( DependencyFunction().empty() && ! DependencyFunctionString().empty() ) {
      depStr = TString( DependencyFunctionString() );
    }
    else {
      depStr = TString( DependencyFunction() );
    }
    if ( depStr.Length() == 0 ) continue;
    for ( unsigned j = 0; j < NParDependency(); ++j ) {
      TString parStr( "[" + boost::lexical_cast< std::string >( j ) + "]" );
      TString parStrNew( "{" + boost::lexical_cast< std::string >( pars.size() ) + "}" ); // FIXME: Just stupid manipulation.
      depStr.ReplaceAll( parStr, parStrNew );
      depStr.ReplaceAll( "x", "y" );
      depStr.ReplaceAll( "eyp", "exp" ); // Fixing unwanted replacements
      pars.push_back( pars2D_.at( i ).at( j ) );
    }
    depStr.Prepend( "(" );
    depStr.Append( ")" );
    TString parStr( "[" + boost::lexical_cast< std::string >( i ) + "]" );
    fitStr.ReplaceAll( parStr, depStr );
  }
  for ( unsigned i = 0; i < NParFit(); ++i ) {
    TString parStr( "[" + boost::lexical_cast< std::string >( i ) + "]" );
    fitStr.ReplaceAll( parStr, "1." );
  }
  fitStr.ReplaceAll( "{", "[" ); // FIXME: Just stupid manipulation (s. above).
  fitStr.ReplaceAll( "}", "]" ); // FIXME: Just stupid manipulation (s. above).
  TF2 function( "", fitStr );
  for ( unsigned i = 0; i < pars.size(); ++i ) {
    function.SetParameter( ( Int_t )i, pars.at( i ) );
  }
  return function;
}

// FIXME: Adapt to resolution function
TF1 TransferFunction::Function( double dependencyValue, int norm ) const
{
  TString fitStr;
  if ( FitFunction().empty() && ! FitFunctionString().empty() ) {
    fitStr = TString( FitFunctionString() );
  }
  else {
    fitStr = TString( FitFunction() );
  }
  std::vector< double > pars;
  for ( unsigned i = 0; i < NParFit(); ++i ) {
    if ( ( int )i == norm ) continue;
    TF1 depFunc( GetDependencyFunction() );
    for ( unsigned j = 0; j < NParDependency(); ++j ) {
      depFunc.SetParameter( ( Int_t )j, ( Double_t )( Parameter( i, j ) ) );
    }
    TString parStr( "[" + boost::lexical_cast< std::string >( i ) + "]" );
    TString parStrNew( "{" + boost::lexical_cast< std::string >( pars.size() ) + "}" ); // FIXME: Just stupid manipulation.
    fitStr.ReplaceAll( parStr, parStrNew );
    pars.push_back( depFunc.Eval( dependencyValue ) );
  }
  for ( unsigned i = 0; i < NParFit(); ++i ) {
    TString parStr( "[" + boost::lexical_cast< std::string >( i ) + "]" );
    fitStr.ReplaceAll( parStr, "1." );
  }
  fitStr.ReplaceAll( "{", "[" ); // FIXME: Just stupid manipulation (s. above).
  fitStr.ReplaceAll( "}", "]" ); // FIXME: Just stupid manipulation (s. above).
  TF1 function( "", fitStr );
  for ( unsigned i = 0; i < pars.size(); ++i ) {
    function.SetParameter( ( Int_t )i, pars.at( i ) );
  }
  return function;
}

// FIXME: Adapt to resolution function
std::string TransferFunction::Formula( int norm ) const
{
  TString fitStr;
  if ( FitFunction().empty() && ! FitFunctionString().empty() ) {
    fitStr = TString( FitFunctionString() );
  }
  else {
    fitStr = TString( FitFunction() );
  }
  for ( unsigned i = 0; i < NParFit(); ++i ) {
    TString parStr( "[" + boost::lexical_cast< std::string >( i ) + "]" );
    if ( ( int )i == norm ) {
      fitStr.ReplaceAll( parStr, "1." );
      continue;
    }
    TString depParStr( Print( i, false ) );
    depParStr.ReplaceAll( Dependency(), "y" );
    depParStr.Prepend( "(" );
    depParStr.Append( ")" );
    fitStr.ReplaceAll( parStr, depParStr );
  }
  return std::string( fitStr.Data() );
}

// FIXME: Adapt to resolution function
std::string TransferFunction::Formula( double dependencyValue, int norm ) const
{
  TF1 fitFunc;
  if ( FitFunction().empty() && ! FitFunctionString().empty() ) {
    fitFunc = TF1( "fitFunc", FitFunctionString().c_str() );
  }
  else {
    fitFunc = TF1( GetFitFunction() );
  }
  for ( unsigned i = 0; i < NParFit(); ++i ) {
    if ( ( int )i == norm ) {
      fitFunc.SetParameter( ( Int_t )i, 1. );
      continue;
    }
    TF1 depFunc( GetDependencyFunction() );
    for ( unsigned j = 0; j < NParDependency(); ++j ) {
      depFunc.SetParameter( ( Int_t )j, ( Double_t )( Parameter( i, j ) ) );
    }
    fitFunc.SetParameter( ( Int_t )i, ( Double_t )( depFunc.Eval( dependencyValue ) ) );
  }
  return std::string( fitFunc.GetExpFormula( "p" ).Data() );
}

// FIXME: Adapt to resolution function
double TransferFunction::Eval( double value, int norm ) const
{
  TF1 fitFunc;
  if ( FitFunction().empty() && ! FitFunctionString().empty() ) {
    fitFunc = TF1( "fitFunc", FitFunctionString().c_str() );
  }
  else {
    fitFunc = TF1( GetFitFunction() );
  }
  for ( unsigned i = 0; i < NParFit(); ++i ) {
    if ( ( int )i == norm ) {
      fitFunc.SetParameter( ( Int_t )i, 1. );
      continue;
    }
    fitFunc.SetParameter( ( Int_t )i, ( Double_t )( Parameter( i ) ) );
  }
  return fitFunc.Eval( value );
}

// FIXME: Adapt to resolution function
double TransferFunction::Eval( double dependencyValue, double value, int norm ) const
{
  TF1 fitFunc;
  if ( FitFunction().empty() && ! FitFunctionString().empty() ) {
    fitFunc = TF1( "fitFunc", FitFunctionString().c_str() );
  }
  else {
    fitFunc = TF1( GetFitFunction() );
  }
  for ( unsigned i = 0; i < NParFit(); ++i ) {
    if ( ( int )i == norm ) {
      fitFunc.SetParameter( ( Int_t )i, 1. );
      continue;
    }
    TF1 depFunc( GetDependencyFunction() );
    for ( unsigned j = 0; j < NParDependency(); ++j ) {
      depFunc.SetParameter( ( Int_t )j, ( Double_t )( Parameter( i, j ) ) );
    }
    fitFunc.SetParameter( ( Int_t )i, ( Double_t )( depFunc.Eval( dependencyValue ) ) );
  }
  return fitFunc.Eval( value );
}

// // FIXME: Adapt to resolution function
// double TransferFunction::Sigma( double dependencyValue ) const
// {
//   // FIXME: This is too simple. Add checks!
//   TF1 depFunc( GetDependencyFunction() );
//   for ( unsigned j = 0; j < NParDependency(); ++j ) {
//     depFunc.SetParameter( ( Int_t )j, ( Double_t )( Parameter( 2, j ) ) );
//   }
//   const double par2( depFunc.Eval( dependencyValue ) );
//   for ( unsigned j = 0; j < NParDependency(); ++j ) {
//     depFunc.SetParameter( ( Int_t )j, ( Double_t )( Parameter( 3, j ) ) );
//   }
//   const double par3( depFunc.Eval( dependencyValue ) );
//   for ( unsigned j = 0; j < NParDependency(); ++j ) {
//     depFunc.SetParameter( ( Int_t )j, ( Double_t )( Parameter( 5, j ) ) );
//   }
//   const double par5( depFunc.Eval( dependencyValue ) );
//   return par2 + par3 * par5;
// }

// Communication

// FIXME: Adapt to resolution function
std::string TransferFunction::Print( bool only1D, bool useNan ) const
{
  std::stringstream print( std::ios_base::out );
  print << std::endl;
  if ( FitFunction().empty() ) print << "FitFunction       : \t" << ( FitFunctionString().empty() ? "[undetermined]" : FitFunctionString() ) << "\t(constructed from C++ class)" << std::endl;
  else                         print << "FitFunction       : \t" << FitFunction() << std::endl;
  if ( ! only1D ) {
    if ( DependencyFunction().empty() ) print << "DependencyFunction: \t" << ( DependencyFunctionString().empty() ? "[undetermined]" : DependencyFunctionString() ) << "\t(constructed from C++ class) \ton " << Dependency() << std::endl;
    else                                print << "DependencyFunction: \t" << DependencyFunction() << " \ton " << Dependency() << std::endl;
  }
  print << "Comment           : \t" << Comment() << std::endl << std::endl;

  print << "Parameters 1D:" << std::endl;
  for ( unsigned i = 0; i < NParFit(); ++i ) {
    print << "[" << i << "]: \t";
    if ( useNan && Parameter( i ) == transferFunctionInitConst ) print << "NAN";
    else print << Parameter( i ) << "+-" << Error( i );
    print << std::endl;
  }
  print << "[all]: \t" << PrintFit1D( useNan ) << std::endl;
  print << std::endl;

  if ( ! only1D ) {
    print << "Parameters 2D:" << std::endl;
    for ( unsigned i = 0; i < NParFit(); ++i ) {
      print << "[" << i << "]: \t"  << Print( i, useNan ) << std::endl;
    }
    print << "[all]: \t" << PrintFit2D( useNan ) << std::endl;
  }

  return print.str();
}

// FIXME: Adapt to resolution function
std::string TransferFunction::Print( unsigned i, bool useNan ) const
{
  TF1 depFunc;
  if ( DependencyFunction().empty() && ! DependencyFunctionString().empty() ) {
    depFunc = TF1( "depFunc", DependencyFunctionString().c_str() );
  }
  else {
    depFunc = TF1( GetDependencyFunction() );
  }
  for ( unsigned j = 0; j < NParDependency(); ++j ) {
    depFunc.SetParameter( ( Int_t )j, ( Double_t )( Parameter( i, j ) ) );
  }

  if ( ! DependencyFunction().empty() || ! DependencyFunctionString().empty() ) {
    TString depStr( depFunc.GetExpFormula( "p" ) );
    depStr.ReplaceAll( "x", Dependency() );
    TString failStr( "e" + Dependency() + "p" );
    depStr.ReplaceAll( failStr, "x" ); // Fixing unwanted replacements
    if ( useNan ) depStr.ReplaceAll( boost::lexical_cast< std::string >( transferFunctionInitConst ).c_str(), "NAN" );
    return std::string( depStr.Data() );
  }
  else {
    std::stringstream print( std::ios_base::out );
    for ( unsigned j = 0; j < NParDependency(); ++j ) {
      if ( j > 0 ) print << " \t";
      if ( useNan && Parameter( i, j ) == transferFunctionInitConst )
        print << "NAN";
      else
        print << Parameter( i, j );
    }
    return print.str();
  }
}

std::string TransferFunction::PrintFit1D( bool useNan ) const
{
  TString fitStr;
  if ( FitFunction().empty() && ! FitFunctionString().empty() ) {
    fitStr = TString( FitFunctionString() );
  }
  else {
    fitStr = TString( FitFunction() );
  }
  if ( fitStr.Length() > 0 ) {
    for ( unsigned i = 0; i < NParFit(); ++i ) {
      TString valStr( boost::lexical_cast< std::string >( Parameter( i ) ) );
      if ( useNan ) valStr.ReplaceAll( boost::lexical_cast< std::string >( transferFunctionInitConst ).c_str(), "NAN" );
      valStr.Prepend( "(" );
      valStr.Append( ")" );
      TString parStr( "[" + boost::lexical_cast< std::string >( i ) + "]" );
      fitStr.ReplaceAll( parStr, valStr );
    }
  }
  return std::string( fitStr.Data() );
}

// FIXME: Adapt to resolution function
std::string TransferFunction::PrintFit2D( bool useNan ) const
{
  TString fitStr;
  if ( FitFunction().empty() && ! FitFunctionString().empty() ) {
    fitStr = TString( FitFunctionString() );
  }
  else {
    fitStr = TString( FitFunction() );
  }
  if ( fitStr.Length() > 0 ) {
    for ( unsigned i = 0; i < NParFit(); ++i ) {
      TString depParStr( Print( i, useNan ) );
      depParStr.Prepend( "(" );
      depParStr.Append( ")" );
      TString parStr( "[" + boost::lexical_cast< std::string >( i ) + "]" );
      fitStr.ReplaceAll( parStr, depParStr );
    }
  }
  return std::string( fitStr.Data() );
}

TransferFunction TransferFunction::Read( const std::string & stream )
{
  TransferFunction transfer;
  return transfer;
}
