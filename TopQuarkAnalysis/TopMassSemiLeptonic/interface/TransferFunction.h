#ifndef TopQuarkPhysics_TopMassSemiLeptonic_TransferFunction_h
#define TopQuarkPhysics_TopMassSemiLeptonic_TransferFunction_h


// -*- C++ -*-
//
// Package:    TopMassSemiLeptonic
// Class:      my::TransferFunction
//
// $Id: TransferFunction.h,v 1.19 2013/02/27 02:18:01 vadler Exp $
//
/**
  \class    my::TransferFunction TransferFunction.h "TopQuarkAnalsyis/TopMassSemiLeptonic/interface/TransferFunction.h"
  \brief    Representation of transfer functions in 1 and 2 dimensions

   my::TransferFunction implements a representation of functions in
   - 1-D: as simple function with fixed parameters
   - 2-D: as function, whose parameters' dependencies are described by another 1-D function

  \author   Volker Adler
  \version  $Id: TransferFunction.h,v 1.19 2013/02/27 02:18:01 vadler Exp $
*/


#include <vector>
#include <set>
#include <string>

#include <TF2.h>


namespace my {

  /// Constants

  /// Initialiser
  /// This is just an arbitrarily large negative number (here: -999999.) to
  /// signal, that no real value has been assigned yet.
  /// It is necessary, since e.g. "0." is a possible real value.
  static const double transferFunctionInitConst( -999999. );

  class TransferFunction {

      ///
      /// Data Members
      ///

      /// Fit function
      /// Function to be fit to the momentum difference distributions.
      TF1 fitFunction_;

      /// Fit function string
      /// Holds string representing the fit function if constructed from C++
      /// class.
      std::string fitFunctionString_;

      /// Dependency function
      /// Function to be fit to distributions of fit parameters from the fit
      /// function over the dependency variable.
      TF1 dependencyFunction_;

      /// Dependency function string
      /// Holds string representing the dependency function if constructed from
      /// C++ class.
      std::string dependencyFunctionString_;

      /// Resolution function
      /// Function to be fit to distributions of resolution parameters from the fit
      /// function over the dependency variable.
      TF1 resolutionFunction_;

      /// Resolution function string
      /// Holds string representing the resolution function if constructed from
      /// C++ class.
      std::string resolutionFunctionString_;

      /// Name of the dependency variable (e.g. "E_parton", "eta").
      std::string dependency_;

      /// Comment
      /// This string is added to the Print() output, describing e.g. applied
      /// cuts etc.
      std::string comment_;

      /// List of resolution parameter indices
      std::set< int > sigmaPars_;

      /// Parameter vector for 1D
      /// It holds the results of the fit of the fit function, independently
      /// of the dependency variable.
      std::vector< double > pars1D_;
      std::vector< double > errs1D_;

      /// Parameter vectors for 2D
      /// It holds the results of the fit of the dependency function for each
      /// parameter of the fit function.
      std::vector< std::vector< double > > pars2D_;
      std::vector< std::vector< double > > errs2D_;

    public:

      ///
      /// Constructors and Desctructor
      ///

      /// Default constructor
      TransferFunction() { TransferFunction( "", std::set< int >() ); };

      /// Constructor from TransferFunction (copy c'tor)
      TransferFunction( const TransferFunction& transfer );

      /// Constructor from strings
      /// Functions are entered in the format for filling a TFormula
      TransferFunction( const std::string& fitFunction, const std::set< int >& sigmaPars, const std::string& dependencyFunction = "0", const std::string& resolutionFunction = "0", const std::string& dependency = "x" );

      /// Constructor from TF1s
      /// TFormula members of the TF1s are possibly empty (e.g. TF1 from
      /// functor).
      TransferFunction( TF1* fitFunction, const std::set< int >& sigmaPars, TF1* dependencyFunction, TF1* resolutionFunction, const std::string& dependency = "x" );

      /// Destructor
      virtual ~TransferFunction() {};

      ///
      /// Methods
      ///

      /// Setters

      /// Set the fit function.
      /// The function is entered in the format for filling a TFormula (s. data
      /// members).
      /// The corresponding parameter vectors are resized according to the
      /// number of function parameters. If 'clear' is 'false', the existing
      /// values are not overwritten.
      void SetFitFunction( const std::string& fitFunctionString, const std::set< int >& sigmaPars );

      /// Set the fit function.
      /// TFormula members of the TF1s are possibly empty (e.g. TF1 from
      /// functor).
      /// The corresponding parameter vectors are resized according to the
      /// number of function parameters. If 'clear' is 'false', the existing
      /// values are not overwritten.
      void SetFitFunction( TF1* fitFunction, const std::set< int >& sigmaPars );

      /// Set the fit function string.
      /// This has only effect, if the original function's title is empty.
      void SetFitFunctionString( const std::string& fitFunctionString );

      /// Set the dependency function.
      /// The function is entered in the format for filling a TFormula (s. data
      /// members).
      /// The corresponding vector of parameter vectors are resized according
      /// to the number of function parameters. If 'clear' is 'false', the
      /// existing values are not overwritten.
      void SetDependencyFunction( const std::string& dependencyFunctionString );

      /// Set the dependency function.
      /// TFormula members of the TF1s are possibly empty (e.g. TF1 from
      /// functor).
      /// The corresponding vector of parameter vectors are resized according
      /// to the number of function parameters. If 'clear' is 'false', the
      /// existing values are not overwritten.
      void SetDependencyFunction( TF1* dependencyFunction );

      /// Set the dependency function string.
      /// This has only effect, if the original function's title is empty.
      void SetDependencyFunctionString( const std::string& dependencyFunctionString );

      /// Set the resolution function.
      /// The function is entered in the format for filling a TFormula (s. data
      /// members).
      /// The corresponding vector of parameter vectors are resized according
      /// to the number of function parameters. If 'clear' is 'false', the
      /// existing values are not overwritten.
      void SetResolutionFunction( const std::string& resolutionFunctionString );

      /// Set the resolution function.
      /// TFormula members of the TF1s are possibly empty (e.g. TF1 from
      /// functor).
      /// The corresponding vector of parameter vectors are resized according
      /// to the number of function parameters. If 'clear' is 'false', the
      /// existing values are not overwritten.
      void SetResolutionFunction( TF1* resolutionFunction );

      /// Set the dependency function string.
      /// This has only effect, if the original function's title is empty.
      void SetResolutionFunctionString( const std::string& resolutionFunctionString );

      /// Set the name of the dependency variable (e.g. "E_parton", "eta").
      void SetDependency( const std::string& dependency ) { dependency_ = dependency; };

      /// Set the comment string.
      void SetComment( const std::string& comment ) { comment_ = comment; };

      /// Set the list of resolution parameter indices.
      void SetSigmaPars( const std::set< int >& sigmaPars ) { sigmaPars_ = sigmaPars; };

      /// Set a fit parameter of the fit function, which is independent of the
      /// dependency variable.
      /// 'i' denotes the parameter number as defined in the fit function
      /// string. If 'i' is beyond the number of available parameters in the
      /// fit function, 'false' is returned.
      bool SetParameter( unsigned i, double par );
      bool SetError( unsigned i, double err );

      /// Set a fit parameter of the dependency function.
      /// 'i' denotes the parameter number as defined in the fit function
      /// string; 'j' the parameter number as defines in the dependency
      /// function string. If 'i' is beyond the number of available parameters
      /// in the fit function or 'j' is beyond the number of available
      /// parameters in the dependency function, 'false' is returned.
      bool SetParameter( unsigned i, unsigned j, double par );
      bool SetError( unsigned i, unsigned j, double err );

      /// Set all fit parameter of the fit function, which is independent of
      /// the dependency variable.
      /// The order of the vector elements has to correspond to the parameter
      /// numbers as defined in the fit function string. If the length of the
      /// vector does not agree with the number of available parameters in the
      /// fit function, 'false' is returned.
      bool SetParameters( std::vector< double > pars );
      bool SetErrors( std::vector< double > errs );

    private:

      /// Resize all vectors according to the number of parameters in the
      /// functions and set them to the initialisation constant.
      void ClearParameters();
      void ClearErrors();

    public:

      /// Getters

      /// Get the fit function.
      TF1 GetFitFunction() const { return fitFunction_; };

      /// Get the fit function.
      /// The function is returned in the format for filling a TFormula (s.
      /// data members).
      std::string FitFunction() const { return std::string( fitFunction_.GetTitle() ); };

      /// Get the dependency function string.
      std::string FitFunctionString() const { return fitFunctionString_; };

      /// Get the number of parameters in the fit function.
      unsigned NParFit() const { return fitFunction_.GetNpar(); };

      /// Get the dependency function.
      TF1 GetDependencyFunction() const { return dependencyFunction_; };

      /// Get the dependency function.
      /// The function is returned in the format for filling a TFormula (s.
      /// data members).
      std::string DependencyFunction() const { return std::string( dependencyFunction_.GetTitle() ); };

      /// Get the dependency function string.
      std::string DependencyFunctionString() const { return dependencyFunctionString_; };

      /// Get the number of parameters in the dependency function.
      unsigned NParDependency() const { return dependencyFunction_.GetNpar(); };

      /// Get the resolution function.
      TF1 GetResolutionFunction() const { return resolutionFunction_; };

      /// Get the resolution function.
      /// The function is returned in the format for filling a TFormula (s.
      /// data members).
      std::string ResolutionFunction() const { return std::string( resolutionFunction_.GetTitle() ); };

      /// Get the resolution function string.
      std::string ResolutionFunctionString() const { return resolutionFunctionString_; };

      /// Get the number of parameters in the dependency function.
      unsigned NParResolution() const { return resolutionFunction_.GetNpar(); };

      /// Get the name of the dependency variable.
      std::string Dependency() const { return dependency_; };

      /// Get the comment string.
      std::string Comment() const { return comment_; };

      /// Get the list of resolution parameter indices.
      std::set< int > SigmaPars() const { return sigmaPars_; };

      /// Get a fit parameter of the fit function, which is independent of the
      /// dependency variable.
      /// 'i' denotes the parameter number as defined in the fit function
      /// string. If 'i' is beyond the number of available parameters in the
      /// fit function, the initialisation constant is returned.
      double Parameter( unsigned i ) const { return i < NParFit() ? pars1D_.at( i ) : transferFunctionInitConst; };
      double Error( unsigned i ) const { return i < NParFit() ? errs1D_.at( i ) : transferFunctionInitConst; };

      /// Get a fit parameter of the dependency function.
      /// 'i' denotes the parameter number as defined in the fit function
      /// string; 'j' the parameter number as defines in the dependency
      /// function string. If 'i' is beyond the number of available parameters
      /// in the fit function or 'j' is beyond the number of available
      /// parameters in the dependency function, the initialisation constant is
      /// returned.
      double Parameter( unsigned i, unsigned j ) const;
      double Error( unsigned i, unsigned j ) const;

      /// Get all fit parameter of the fit function, which is independent of
      /// the dependency variable.
      /// The order of the vector elements corresponds to the parameter numbers
      /// as defined in the fit function string.
      std::vector< double > Parameters() const { return pars1D_; };
      std::vector< double > Errors() const { return errs1D_; };

      /// Evaluate

      /// Get the TransferFunction with errors applied
      TransferFunction FunctionErrorsUp() const;
      TransferFunction FunctionErrorsDown() const;

      /// Get the 2D transfer function as ROOT function.
      TF2 Function( int norm = 0 ) const;

      /// Get the 1D transfer function as ROOT function, with its parameters
      /// set to the numerical values for the given value of the dependency
      /// variable.
      TF1 Function( double dependencyValue, int norm = 0 ) const;

      /// Get the 2D transfer function as string.
      /// The function is returned in the format for filling a TFormula (s.
      /// data members).
      std::string Formula( int norm = 0 ) const;

      /// Get the 1D transfer function as string, with its parameters set to
      /// the numerical values for the given value of the dependency variable.
      /// The function is returned in the format for filling a TFormula (s.
      /// data members).
      std::string Formula( double dependencyValue, int norm = 0 ) const;

      /// Get the numerical value of the 1D fit function for given values of
      /// the fit variable.
      double Eval( double value, int norm = 0 ) const;

      /// Get the numerical value of the 2D fit function for given values of
      /// the fit and dependency variables.
      double Eval( double dependencyValue, double value, int norm = 0 ) const;

      /// Get the 1D fit function for given values of the dependency variable.
      TF1 GetFitFunction( double dependencyValue, int norm = 0 ) const;

      ///
//       double Sigma() const { return Parameter( 2 ) + Parameter( 3 ) * Parameter( 5 ); };

      ///
//       double Sigma( double dependencyValue ) const;

      /// Communication

      /// Returns a formatted string for human readability with all important
      /// parameters of the transfer function.
      std::string Print( bool only1D = false, bool useNan = true ) const;

      /// Returns a formatted string for human readability of the dependency
      /// or resolution function for the given parameter of the fit function.
      std::string Print( unsigned i, bool useNan = true ) const;

      /// Returns a formatted string for human readability of the 1D fit
      /// function.
      std::string PrintFit1D( bool useNan = true ) const;

      /// Returns a formatted string for human readability of the 2D fit
      /// function.
      std::string PrintFit2D( bool useNan = true ) const;

      /// Creates a transfer function from a string as produced by Print().
      /// NOT IMPLEMENTED YET!
      static TransferFunction Read( const std::string & stream );

  };


  /// Collection of TransferFunction
  typedef std::vector< TransferFunction > TransferFunctionCollection;

}


#endif
