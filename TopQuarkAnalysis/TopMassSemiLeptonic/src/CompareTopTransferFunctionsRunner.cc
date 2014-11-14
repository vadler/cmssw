#include "TopQuarkAnalysis/TopMassSemiLeptonic/interface/CompareTopTransferFunctionsRunner.h"

#include <iostream>

#include "boost/lexical_cast.hpp"

#include <TROOT.h>
#include <TStyle.h>
#include <TH1D.h>
#include <TH2D.h>
#include <TF1.h>
#include <TList.h>
#include <TKey.h>
#include <TCanvas.h>
#include "TLegend.h"

#include "CommonTools/MyTools/interface/RootTools.h"


using namespace my;


CompareTopTransferFunctionsRunner::CompareTopTransferFunctionsRunner( const std::string& iName, const edm::ParameterSet& iConfig )
: myName_( iName )
, status_( 0 )
, config_( iConfig )
, verbose_( config_.getParameter< unsigned >( "verbose" ) )
{

  const edm::ParameterSet& configCompare( config_.getParameter< edm::ParameterSet >( "compare" ) );
  useSymm_ = configCompare.getParameter< bool >( "useSymm" );
  const edm::ParameterSet& configInput( configCompare.getParameter< edm::ParameterSet >( "inputFiles" ) );
  names_ = configInput.getParameterNamesForType< edm::ParameterSet >();
  size_  = names_.size();
  if ( size_ == 0 ) {
    std::cout << myName_ << " --> ERROR:" << std::endl
              << "    no input defined" << std::endl;
    status_ += 0x10;
    return;
  }
  default_ = size_;
  fileNames_.clear();
  cycles_.clear();
  for ( size_t uName = 0; uName < size_; ++uName ) {
    if ( default_ == size_ && names_[ uName ] == "Default" ) default_ = uName;
    const edm::ParameterSet& config( configInput.getParameter< edm::ParameterSet >( names_[ uName ] ) );
    fileNames_.push_back( config.getParameter< std::string >( "fileName" ) );
    legendLabels_.push_back( config.getParameter< std::string >( "legendLabel" ) );
    useAlt_.push_back( config.getParameter< bool >( "useAlt" ) );
    useNonT_.push_back( config.getParameter< bool >( "useNonT" ) );
    useNonP_.push_back( config.getParameter< bool >( "useNonP" ) );
    refGen_.push_back( config.getParameter< bool >( "refGen" ) );
    refSel_.push_back( config.getParameter< bool >( "refSel" ) );
    cycles_.push_back( config.getParameter< int >( "cycle" ) );
    std::string strPt( "_" );
    if ( useNonP_.back() )   strPt.append( "E" );
    else                     strPt.append( "P" );
    if ( ! useNonT_.back() ) strPt.append( "t" );
    strPt_.push_back( strPt );
  }
  if ( default_ == size_ ) {
    std::cout << myName_ << " --> ERROR:" << std::endl
              << "    no default input defined" << std::endl;
    status_ += 0x10;
    return;
  }

  if ( verbose_ > 1 ) {
    std::cout << std::endl
              << myName_ << " --> INFO:" << std::endl
              << "    called for " << size_ << " input files " << std::endl;
    std::cout << "        '" << fileNames_[ default_ ] << "', cycle " << cycles_[ default_ ] << " (default)" << std::endl;
    for ( size_t uName = 0; uName < size_; ++uName ) {
      if ( uName == default_ ) continue;
      std::cout << "        '" << fileNames_[ uName ] << "', cycle " << cycles_[ uName ] << std::endl;
    }
  }

  // Set up ROOT
  TH1D::SetDefaultSumw2();
  TH2D::SetDefaultSumw2();

  // Set constants
  std::vector< std::string > evtSel( 4, "analyzeHitFit" );
  for ( unsigned uFile = 0; uFile < size_; ++uFile ) {
    if ( refSel_[ uFile ] ) evtSel[ uFile ].append( "Reference" );
  }
  const std::string nameDirClass( "TDirectoryFile" );
  const std::string nameHistoClass( "TH1D" );

  filesIn_.clear(); // default_ --> 0 !
  pwds_.clear();    // default_ --> 0 !

  // Open default input file
  objCats_.clear();

  const std::string fileName( fileNames_[ default_ ] );
  if ( verbose_ > 1 ) {
    std::cout << myName_ << " --> INFO:" << std::endl
              << "    opening input file '" << fileName  << "'" << std::endl;
  }
  TFile* file( TFile::Open( fileName.c_str(), "READ" ) );
  if ( ! file ) {
    std::cout << myName_ << " --> ERROR:" << std::endl
              << "    default input file '" << fileName << "' missing" << std::endl;
    status_ += 0x20;
    return;
  }
  filesIn_.push_back( file );
  TDirectory* selDir( ( TDirectory* )( file->Get( evtSel[ default_ ].c_str() ) ) );
  if ( ! selDir ) {
    std::cout << myName_ << " --> ERROR:" << std::endl
              << "    selection '" << evtSel[ default_ ] << "' does not exist in default input file " << fileName << std::endl;
    status_ += 0x30;
    return;
  }

  // Determine objects with default file as reference
  TList* listObj( selDir->GetListOfKeys() );
  if ( verbose_ > 3 ) {
    std::cout << myName_ << " --> INFO:" << std::endl
              << "    in directory " << selDir->GetName() << std::endl;
    listObj->Print();
  }
  TIter nextInListObj( listObj );
  while ( TKey* keyObj = ( TKey* )nextInListObj() ) {
    if ( std::string( keyObj->GetClassName() ) != nameDirClass ) continue;
    const std::string objCat( keyObj->GetName() );
    objCats_.push_back( objCat );
    // Test for required sub-directories
    TDirectory* objDir( ( TDirectory* )( selDir->Get( objCat.c_str() ) ) );
    TDirectory* ptDir( ( TDirectory* )( objDir->Get( "Pt" ) ) );
    if ( ! ptDir ) {
      std::cout << myName_ << " --> ERROR:" << std::endl
                << "    directory 'Pt' does not exist in input file " << fileName << std::endl;
      status_ += 0x40;
      return;
    }
    TList* listPwd( ptDir->GetListOfKeys() );
    if ( verbose_ > 4 ) {
      std::cout << myName_ << " --> INFO:" << std::endl
                << "    in directory " << ptDir->GetName() << std::endl;
      listPwd->Print();
    }
    TIter nextInListPwd( listPwd );
    while ( TKey* keyPwd = ( TKey* )nextInListPwd() ) {
      if ( std::string( keyPwd->GetClassName() ) != nameDirClass ) continue;
      const std::string subFit( keyPwd->GetName() );
      if ( subFit.find( "Inv" ) != std::string::npos ) continue; // nothing to do for inverse
      // These are real switches: depending on configuration, only one setting combination can be run at a time
      if ( useAlt_[ default_ ] == ( subFit.find( "Alt" )  == std::string::npos ) ) continue;
      if ( useSymm_            == ( subFit.find( "Symm" ) == std::string::npos ) ) continue;
      if ( refGen_[ default_ ] == ( subFit.find( "Gen" )  == std::string::npos ) ) continue;
      subFits_.push_back( subFit );
      TDirectory* pwd( ( TDirectory* )( ptDir->Get( subFit.c_str() ) ) );
      if ( ! pwd ) {
        std::cout << myName_ << " --> ERROR:" << std::endl
                  << "    fit directory not found in input file " << fileName << std::endl;
        status_ += 0x50;
        return;
      }
      if ( verbose_ > 4 ) {
        std::cout << myName_ << " --> INFO:" << std::endl
                  << "    fit directory " << pwd->GetName() << " found" << std::endl;
      }
      pwds_.push_back( pwd );
      break;
    }
  }
  for ( size_t uObj = 0; uObj < objCats_.size(); ++uObj ) {
    std::string histo;
    std::vector< std::string > histos;
    const std::string strPt( strPt_[ default_ ] );
    TList* listHisto( pwds_[ uObj ]->GetListOfKeys() );
    if ( verbose_ > 4 ) listHisto->Print();
    TIter nextInListHisto( listHisto );
    while ( TKey* keyHisto = ( TKey* )nextInListHisto() ) {
      if ( std::string( keyHisto->GetClassName() ) != nameHistoClass ) continue;
      std::string histoTmp( keyHisto->GetName() );
      if ( cycles_[ default_ ] <= 0 ) { // Cycle count starts at 1
        if ( histoTmp == histo ) continue;
      }
      else {
        if ( keyHisto->GetCycle() != cycles_[ default_ ] ) continue;
      }
      histo = histoTmp;
      size_t length( strPt.length() );
      size_t pos( histoTmp.find( strPt ) );
      while ( pos != std::string::npos ) {
        histoTmp.replace( pos, length, "_XXX" );
        pos = histoTmp.find( strPt );
      }
      pos = histoTmp.find( subFits_[ uObj ] );
      length = subFits_[ uObj ].length();
      histoTmp.replace( pos, length, "YYY" );
      histos.push_back( histoTmp );
      if ( verbose_ > 3 ) {
        std::cout << "    added to list: ";
        keyHisto->Print();
        std::cout << "        as       : " << histoTmp << std::endl;
      }
    }
    histos_.push_back( histos );
  }

  // Open non-default input files
  for ( size_t uFile = 0; uFile < size_; ++uFile ) {
    if ( uFile == default_ ) continue;
    const std::string fileName( fileNames_[ uFile ] );
    if ( verbose_ > 1 ) {
      std::cout << myName_ << " --> INFO:" << std::endl
                << "    opening input file '" << fileName  << "'" << std::endl;
    }
    TFile* file( TFile::Open( fileName.c_str(), "READ" ) );
    if ( ! file ) {
      std::cout << myName_ << " --> ERROR:" << std::endl
                << "    input file '" << fileName << "' missing" << std::endl;
      status_ += 0x20;
      continue;
    }
    filesIn_.push_back( file );
    TDirectory* selDir( ( TDirectory* )( file->Get( evtSel[ uFile ].c_str() ) ) );
    if ( ! selDir ) {
      std::cout << myName_ << " --> ERROR:" << std::endl
                << "    selection '" << evtSel[ uFile ] << "' does not exist in input file " << fileName << std::endl;
      status_ += 0x30;
      continue;
    }
    // Determine objects with default file as reference
    TList* listObj( selDir->GetListOfKeys() );
    if ( verbose_ > 3 ) listObj->Print();
    TIter nextInListObj( listObj );
    while ( TKey* keyObj = ( TKey* )nextInListObj() ) {
      if ( std::string( keyObj->GetClassName() ) != nameDirClass ) continue;
      const std::string objCat( keyObj->GetName() );
      // Test for required sub-directories
      TDirectory* objDir( ( TDirectory* )( selDir->Get( objCat.c_str() ) ) );
      TDirectory* ptDir( ( TDirectory* )( objDir->Get( "Pt" ) ) );
      if ( ! ptDir ) {
        std::cout << myName_ << " --> ERROR:" << std::endl
                  << "    directory 'Pt' does not exist in input file " << fileName << std::endl;
        status_ += 0x40;
        return;
      }
      TList* listPwd( ptDir->GetListOfKeys() );
      TIter nextInListPwd( listPwd );
      while ( TKey* keyPwd = ( TKey* )nextInListPwd() ) {
        if ( std::string( keyPwd->GetClassName() ) != nameDirClass ) continue;
        const std::string subFit( keyPwd->GetName() );
        if ( subFit.find( "Inv" ) != std::string::npos ) continue; // nothing to do for inverse
        // These are real switches: depending on configuration, only one setting combination can be run at a time
        if ( useAlt_[ uFile ] == ( subFit.find( "Alt" )  == std::string::npos ) ) continue;
        if ( useSymm_         == ( subFit.find( "Symm" ) == std::string::npos ) ) continue;
        if ( refGen_[ uFile ] == ( subFit.find( "Gen" )  == std::string::npos ) ) continue;
        TDirectory* pwd( ( TDirectory* )( ptDir->Get( subFit.c_str() ) ) );
        subFits_.push_back( subFit );
        pwds_.push_back( pwd );
        break;
      }
    }
    if ( ! pwds_.back() ) {
      std::cout << myName_ << " --> ERROR:" << std::endl
                << "    fit directory not found in input file " << fileName << std::endl;
      status_ += 0x50;
      return;
    }
  }

}


CompareTopTransferFunctionsRunner::~CompareTopTransferFunctionsRunner()
{

  for ( size_t uFile = 0; uFile < filesIn_.size(); ++uFile ) {
    if ( filesIn_[ uFile ] ) filesIn_[ uFile ]->Close();
  }

}


int CompareTopTransferFunctionsRunner::run()
{

  if ( status_ != 0 ) return status_;

  const edm::ParameterSet& configIO( config_.getParameter< edm::ParameterSet >( "io" ) );
  const bool configIOFullStats( configIO.getParameter< bool >( "fullStats" ) );
  const bool configIOPlot( configIO.getParameter< bool >( "plot" ) );
  const std::string configIOPathPlots( configIO.getParameter< std::string >( "pathPlots" ) );
  const std::vector< std::string > configIOFormatPlots( configIO.getParameter< std::vector< std::string > >( "formatPlots" ) );

  const std::string nameFuncClass( "TF1" );

  setPlotEnvironment( gStyle );
  if ( configIOFullStats ) {
    gStyle->SetOptStat( 111111 );
    gStyle->SetOptFit( 1111 );
    gStyle->SetStatW( 0.1 );
  }
  else {
    gStyle->SetOptStat( 0 );
    gStyle->SetOptFit( 0 );
  }

  for ( size_t uObj = 0; uObj < objCats_.size(); ++uObj ) {
    for ( size_t uHisto = 0; uHisto < histos_[ uObj ].size(); ++uHisto ) {
      pwds_[ uObj ]->cd();
      std::string histo( histos_[ uObj ][ uHisto ] );
      size_t pos( histo.find( "YYY" ) );
      if ( pos != std::string::npos ) histo.replace( pos, 3, subFits_[ uObj ] );
      pos = histo.find( "_XXX" );
      while ( pos != std::string::npos ) {
        histo.replace( pos, 4, strPt_[ default_ ] );
        pos = histo.find( "_XXX" );
      }
      const int cycle( cycles_[ 0 ] );
      std::string refCycle( "" );
      if ( cycle > 0 ) {
        refCycle.append( ";" );
        refCycle.append( boost::lexical_cast< std::string >( cycle ) );
      }
      const std::string refNamecycle( histo + refCycle );
      if ( verbose_ > 3 ) {
        std::cout << "    loading   : " << refNamecycle << std::endl;
      }
      TH1D* refHisto( ( TH1D* )( gDirectory->Get( refNamecycle.c_str() ) ) );
      refHisto->SetLineColor( kRed );
      refHisto->SetMarkerColor( kRed );
      refHisto->SetFillColor( kYellow );
      TList* listRefFunc( refHisto->GetListOfFunctions() );
      TIter nextInListRefFunc( listRefFunc );
//       Int_t lineStyle( 0 );
      while ( TObject* objRefFunc = ( TObject* )nextInListRefFunc() ) {
        if ( std::string( objRefFunc->ClassName() ) != nameFuncClass ) continue;
        const std::string func( objRefFunc->GetName() );
        if ( verbose_ > 4 ) {
          std::cout << "        with function: " << func << std::endl;
        }
        TF1* refFunc( refHisto->GetFunction( func.c_str() ) );
        refFunc->SetLineColor( kRed );
//         ++lineStyle;
//         refFunc->SetLineStyle( lineStyle );
      }
      TCanvas canvas;
      refHisto->Draw( "H" );
      TLegend * legend( new TLegend( 0.65, 0.8, 0.89, 0.89 ) );
      legend->AddEntry( refHisto, legendLabels_[ default_ ].c_str(), "FL" );

      size_t countFile( 0 );
      for ( size_t uFile = 0; uFile < size_; ++uFile ) {
        if ( uFile == default_ ) continue;
        size_t index( ( 1 + countFile ) * objCats_.size() + uObj );
        pwds_[ index ]->cd();
        std::string histo2( histos_[ uObj ][ uHisto ] );
        size_t pos2( histo2.find( "YYY" ) );
        if ( pos2 != std::string::npos ) histo2.replace( pos2, 3, subFits_[ index ] );
        pos2 = histo2.find( "_XXX" );
        while ( pos2 != std::string::npos ) {
          histo2.replace( pos2, 4, strPt_[ uFile ] );
          pos2 = histo2.find( "_XXX" );
        }
        const int cycle2( cycles_[ uFile ] );
        std::string overlayCycle( "" );
        if ( cycle2 > 0 ) {
          overlayCycle.append( ";" );
          overlayCycle.append( boost::lexical_cast< std::string >( cycle2 ) );
        }
        const std::string overlayNamecycle( histo2 + overlayCycle );
        if ( verbose_ > 3 ) {
          std::cout << "    overlaying: " << overlayNamecycle << std::endl;
        }
        TH1D* overlayHisto( ( TH1D* )( gDirectory->Get( overlayNamecycle.c_str() ) ) );
        overlayHisto->SetLineColor( kBlue ); // FIXME: How to loop over (pretty) colors
        overlayHisto->SetMarkerColor( kBlue ); // FIXME: How to loop over (pretty) colors
        TList* listOverlayFunc( overlayHisto->GetListOfFunctions() );
        TIter nextInListOverlayFunc( listOverlayFunc );
//         Int_t lineStyle2( 0 );
        while ( TObject* objOverlayFunc = ( TObject* )nextInListOverlayFunc() ) {
          if ( std::string( objOverlayFunc->ClassName() ) != nameFuncClass ) continue;
          const std::string func( objOverlayFunc->GetName() );
          if ( verbose_ > 4 ) {
            std::cout << "        with function: " << func << std::endl;
          }
          TF1* overlayFunc( overlayHisto->GetFunction( func.c_str() ) );
          overlayFunc->SetLineColor( kBlue );
//           ++lineStyle2;
//           overlayFunc->SetLineStyle( lineStyle2 );
        }
        overlayHisto->Draw( "HSame" );
        legend->AddEntry( overlayHisto, legendLabels_[ uFile ].c_str(), "FL" );
        ++countFile;
      }

      legend->Draw();
      if ( configIOPlot ) {
        for ( unsigned uForm = 0; uForm < configIOFormatPlots.size(); ++uForm ) canvas.Print( std::string( configIOPathPlots + histos_[ uObj ][ uHisto ] + "." + configIOFormatPlots[ uForm ] ).c_str() );
      }
    }
  }

  return status_;

}
