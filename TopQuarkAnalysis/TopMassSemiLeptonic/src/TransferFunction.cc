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
  if ( i < NParFit() && j < pars2D_.at( i ).size() ) {
    pars2D_.at( i ).at( j ) = par;
    return true;
  }
  return false;
}

bool TransferFunction::SetError( unsigned i, unsigned j, double err )
{
  if ( i < NParFit() && j < errs2D_.at( i ).size() ) {
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

double TransferFunction::Parameter( unsigned i, unsigned j ) const
{
  if ( i < NParFit() && j < pars2D_.at( i ).size() ) return pars2D_.at( i ).at( j );
  return transferFunctionInitConst;
}

double TransferFunction::Error( unsigned i, unsigned j ) const
{
  if ( i < NParFit() && j < errs2D_.at( i ).size() ) return errs2D_.at( i ).at( j );
  return transferFunctionInitConst;
}

// Evaluate

TransferFunction TransferFunction::FunctionErrorsUp() const
{
  TransferFunction transferFunction( *this );
  for ( unsigned i = 0; i < transferFunction.NParFit(); ++i ) {
    transferFunction.SetParameter( i, transferFunction.Parameter( i ) + transferFunction.Error( i ) );
    unsigned nPar( transferFunction.SigmaPars().find( i ) == transferFunction.SigmaPars().end() ? transferFunction.NParDependency() : transferFunction.NParResolution() );
    for ( unsigned j = 0; j < nPar; ++j ) {
      transferFunction.SetParameter( i, j, transferFunction.Parameter( i, j ) + transferFunction.Error( i, j ) );
    }
  }
  transferFunction.ClearErrors();
  return transferFunction;
}

TransferFunction TransferFunction::FunctionErrorsDown() const
{
  TransferFunction transferFunction( *this );
  for ( unsigned i = 0; i < transferFunction.NParFit(); ++i ) {
    transferFunction.SetParameter( i, transferFunction.Parameter( i ) - transferFunction.Error( i ) );
    unsigned nPar( transferFunction.SigmaPars().find( i ) == transferFunction.SigmaPars().end() ? transferFunction.NParDependency() : transferFunction.NParResolution() );
    for ( unsigned j = 0; j < nPar; ++j ) {
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
    TString funcStr;
    if ( SigmaPars().find( i ) == SigmaPars().end() ) {
      if ( DependencyFunction().empty() && ! DependencyFunctionString().empty() ) {
        funcStr = TString( DependencyFunctionString() );
      }
      else {
        funcStr = TString( DependencyFunction() );
      }
    }
    else {
      if ( ResolutionFunction().empty() && ! ResolutionFunctionString().empty() ) {
        funcStr = TString( ResolutionFunctionString() );
      }
      else {
        funcStr = TString( ResolutionFunction() );
      }
    }
    if ( funcStr.Length() == 0 ) continue;
    for ( unsigned j = 0; j < pars2D_.at( i ).size(); ++j ) {
      TString parStr( "[" + boost::lexical_cast< std::string >( j ) + "]" );
      TString parStrNew( "{" + boost::lexical_cast< std::string >( pars.size() ) + "}" ); // FIXME: Just stupid manipulation.
      funcStr.ReplaceAll( parStr, parStrNew );
      funcStr.ReplaceAll( "x", "y" );
      funcStr.ReplaceAll( "eyp", "exp" ); // Fixing unwanted replacements
      pars.push_back( pars2D_.at( i ).at( j ) );
    }
    funcStr.Prepend( "(" );
    funcStr.Append( ")" );
    TString parStr( "[" + boost::lexical_cast< std::string >( i ) + "]" );
    fitStr.ReplaceAll( parStr, funcStr );
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
    if ( SigmaPars().find( i ) == SigmaPars().end() ) {
      TF1 depFunc( GetDependencyFunction() );
      for ( unsigned j = 0; j < NParDependency(); ++j ) {
        depFunc.SetParameter( ( Int_t )j, ( Double_t )( Parameter( i, j ) ) );
      }
      TString parStr( "[" + boost::lexical_cast< std::string >( i ) + "]" );
      TString parStrNew( "{" + boost::lexical_cast< std::string >( pars.size() ) + "}" ); // FIXME: Just stupid manipulation.
      fitStr.ReplaceAll( parStr, parStrNew );
      pars.push_back( depFunc.Eval( dependencyValue ) );
    }
    else {
      TF1 resFunc( GetResolutionFunction() );
      for ( unsigned j = 0; j < NParResolution(); ++j ) {
        resFunc.SetParameter( ( Int_t )j, ( Double_t )( Parameter( i, j ) ) );
      }
      TString parStr( "[" + boost::lexical_cast< std::string >( i ) + "]" );
      TString parStrNew( "{" + boost::lexical_cast< std::string >( pars.size() ) + "}" ); // FIXME: Just stupid manipulation.
      fitStr.ReplaceAll( parStr, parStrNew );
      pars.push_back( resFunc.Eval( dependencyValue ) );
    }
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
    TString funcParStr( Print( i, false ) );
    funcParStr.ReplaceAll( Dependency(), "y" );
    funcParStr.Prepend( "(" );
    funcParStr.Append( ")" );
    fitStr.ReplaceAll( parStr, funcParStr );
  }
  return std::string( fitStr.Data() );
}

std::string TransferFunction::Formula( double dependencyValue, int norm ) const
{
  TF1 fitFunc( GetFitFunction( dependencyValue, norm ) );
  return std::string( fitFunc.GetExpFormula( "p" ).Data() );
}

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

double TransferFunction::Eval( double dependencyValue, double value, int norm ) const
{
  TF1 fitFunc( GetFitFunction( dependencyValue, norm ) );
  return fitFunc.Eval( value );
}

TF1 TransferFunction::GetFitFunction( double dependencyValue, int norm ) const
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
    if ( SigmaPars().find( i ) == SigmaPars().end() ) {
      TF1 depFunc( GetDependencyFunction() );
      for ( unsigned j = 0; j < NParDependency(); ++j ) {
        depFunc.SetParameter( ( Int_t )j, ( Double_t )( Parameter( i, j ) ) );
      }
      fitFunc.SetParameter( ( Int_t )i, ( Double_t )( depFunc.Eval( dependencyValue ) ) );
    }
    else {
      TF1 resFunc( GetResolutionFunction() );
      for ( unsigned j = 0; j < NParResolution(); ++j ) {
        resFunc.SetParameter( ( Int_t )j, ( Double_t )( Parameter( i, j ) ) );
      }
      fitFunc.SetParameter( ( Int_t )i, ( Double_t )( resFunc.Eval( dependencyValue ) ) );
    }
  }
  return fitFunc;
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

std::string TransferFunction::Print( bool only1D, bool useNan ) const
{
  std::stringstream print( std::ios_base::out );
  print << std::endl;
  if ( FitFunction().empty() ) print << "FitFunction       : \t" << ( FitFunctionString().empty() ? "[undetermined]" : FitFunctionString() ) << "\t(constructed from C++ class)" << std::endl;
  else                         print << "FitFunction       : \t" << FitFunction() << std::endl;
  if ( ! only1D ) {
    if ( DependencyFunction().empty() ) print << "DependencyFunction: \t" << ( DependencyFunctionString().empty() ? "[undetermined]" : DependencyFunctionString() ) << "\t(constructed from C++ class) \ton " << Dependency() << std::endl;
    else                                print << "DependencyFunction: \t" << DependencyFunction() << " \ton " << Dependency() << std::endl;
    if ( ResolutionFunction().empty() ) print << "ResolutionFunction: \t" << ( ResolutionFunctionString().empty() ? "[undetermined]" : ResolutionFunctionString() ) << "\t(constructed from C++ class) \ton " << Dependency() << std::endl;
    else                                print << "ResolutionFunction: \t" << ResolutionFunction() << " \ton " << Dependency() << std::endl;
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

std::string TransferFunction::Print( unsigned i, bool useNan ) const
{
  TF1 func;
  if ( SigmaPars().find( i ) == SigmaPars().end() ) {
    if ( DependencyFunction().empty() && ! DependencyFunctionString().empty() ) {
      func = TF1( "func", DependencyFunctionString().c_str() );
    }
    else {
      func = TF1( GetDependencyFunction() );
    }
    for ( unsigned j = 0; j < NParDependency(); ++j ) {
      func.SetParameter( ( Int_t )j, ( Double_t )( Parameter( i, j ) ) );
    }
  }
  else {
    if ( ResolutionFunction().empty() && ! ResolutionFunctionString().empty() ) {
      func = TF1( "func", ResolutionFunctionString().c_str() );
    }
    else {
      func = TF1( GetResolutionFunction() );
    }
    for ( unsigned j = 0; j < NParResolution(); ++j ) {
      func.SetParameter( ( Int_t )j, ( Double_t )( Parameter( i, j ) ) );
    }
  }

  if ( ( SigmaPars().find( i ) == SigmaPars().end() && ( ! DependencyFunction().empty() || ! DependencyFunctionString().empty() ) ) || ( SigmaPars().find( i ) != SigmaPars().end() && ( ! ResolutionFunction().empty() || ! ResolutionFunctionString().empty() ) ) ) {
    TString depStr( func.GetExpFormula( "p" ) );
    depStr.ReplaceAll( "x", Dependency() );
    TString failStr( "e" + Dependency() + "p" );
    depStr.ReplaceAll( failStr, "x" ); // Fixing unwanted replacements
    if ( useNan ) depStr.ReplaceAll( boost::lexical_cast< std::string >( transferFunctionInitConst ).c_str(), "NAN" );
    return std::string( depStr.Data() );
  }
  else {
    std::stringstream print( std::ios_base::out );
    unsigned nPar( SigmaPars().find( i ) == SigmaPars().end() ? NParDependency() : NParResolution() );
    for ( unsigned j = 0; j < nPar; ++j ) {
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
