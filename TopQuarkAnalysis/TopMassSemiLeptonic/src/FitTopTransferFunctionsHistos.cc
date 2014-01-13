#include "TopQuarkAnalysis/TopMassSemiLeptonic/interface/FitTopTransferFunctionsHistos.h"


#include "boost/lexical_cast.hpp"

#include <TStyle.h>


using namespace my;


my::HistosTransEta::HistosTransEta( const HistosTransEta& histosTransEta, const std::string& baseName, const std::string& baseTitlePt, bool scale )
: name( baseName )
{
  const std::string nameTrans( baseName + "_Trans" );
  histTrans = new TH1D( *( ( TH1D* )( histosTransEta.histTrans->Clone( nameTrans.c_str() ) ) ) );
  legTrans  = new TLegend( gStyle->GetPadLeftMargin() + 0.025, 0.75, 0.4, 0.975 - gStyle->GetPadTopMargin() );
  legTrans->SetFillColor( gStyle->GetPadColor() );
  legTrans->SetHeader( histTrans->GetTitle() );
  const std::string nameTransMapPt( nameTrans + "_Map_Pt" );
  histTransMapPt = new TH2D( *( ( TH2D* )( histosTransEta.histTransMapPt->Clone( nameTransMapPt.c_str() ) ) ) );
  const std::string nameTransScaleMapPt( nameTrans + "_ScaleMap_Pt" );
  histTransScaleMapPt = new TH2D( *( ( TH2D* )( histosTransEta.histTransScaleMapPt->Clone( nameTransScaleMapPt.c_str() ) ) ) );
  histTransScaleMapPt->SetXTitle( histosTransEta.histTransScaleMapPt->GetYaxis()->GetTitle() );
  histTransScaleMapPt->SetYTitle( histosTransEta.histTransScaleMapPt->GetXaxis()->GetTitle() );
  histTransScaleMapPt->SetZTitle( histosTransEta.histTransScaleMapPt->GetZaxis()->GetTitle() );

  for ( unsigned uPt = 0; uPt < histosTransEta.histVecPtTrans.size(); ++uPt ) {
    const std::string binPt( boost::lexical_cast< std::string >( uPt ) );
    const std::string namePtTrans( baseName + "_" + baseTitlePt + binPt + "_Trans" );
    TH1D* histPtTrans( new TH1D( *( ( TH1D* )( histosTransEta.histVecPtTrans.at( uPt)->Clone( namePtTrans.c_str() ) ) ) ) );
    histVecPtTrans.push_back( histPtTrans );
    TLegend* legPtTrans( new TLegend( gStyle->GetPadLeftMargin() + 0.025, 0.75, 0.4, 0.975 - gStyle->GetPadTopMargin() ) );
    legPtTrans->SetFillColor( gStyle->GetPadColor() );
    legPtTrans->SetHeader( histPtTrans->GetTitle() );
    legVecPtTrans.push_back( legPtTrans );
  }

  if ( scale ) this->scale();
}

my::HistosTransEta::HistosTransEta( const std::string& objCat, const std::string& baseName, const unsigned nPtBinsHistos, const double ptMaxHistos, const unsigned nPtBins, const std::vector< Double_t >& ptBins, const std::string& titleTrans, const std::string& baseTitlePt, const std::string& titlePtT, const std::string& titlePt, const std::string& titleEta )
{
  const std::string nameTrans( baseName + "_Trans" );
  histTrans = new TH1D( nameTrans.c_str(), objCat.c_str(), nPtBinsHistos, -ptMaxHistos, ptMaxHistos );
  histTrans->SetXTitle( titleTrans.c_str() );
  histTrans->SetYTitle( "events" );
  legTrans  = new TLegend( gStyle->GetPadLeftMargin() + 0.025, 0.75, 0.4, 0.975 - gStyle->GetPadTopMargin() );
  legTrans->SetFillColor( gStyle->GetPadColor() );
  legTrans->SetHeader( histTrans->GetTitle() );
  const std::string nameTransMapPt( nameTrans + "_Map_Pt" );
  histTransMapPt = new TH2D( nameTransMapPt.c_str(), objCat.c_str(), nPtBins, ptBins.data(), nPtBinsHistos, -ptMaxHistos, ptMaxHistos );
  histTransMapPt->SetXTitle( titlePt.c_str() );
  histTransMapPt->SetYTitle( titleTrans.c_str() );
  histTransMapPt->SetZTitle( "events" );
  const std::string nameTransScaleMapPt( nameTrans + "_ScaleMap_Pt" );
  histTransScaleMapPt = new TH2D( nameTransScaleMapPt.c_str(), objCat.c_str(), nPtBinsHistos, -ptMaxHistos, ptMaxHistos, nPtBins, ptBins.data() );
  histTransScaleMapPt->SetXTitle( titleTrans.c_str() );
  histTransScaleMapPt->SetYTitle( titlePt.c_str() );
  histTransScaleMapPt->SetZTitle( "events" );

  for ( unsigned uPt = 0; uPt < nPtBins; ++uPt ) {
    const std::string binPt( boost::lexical_cast< std::string >( uPt ) );
    const std::string namePtTrans( baseName + "_" + baseTitlePt + binPt + "_Trans" );
    const std::string titlePtTrans( objCat + ", " + boost::lexical_cast< std::string >( ptBins.at( uPt ) ) + " GeV #leq " + titlePtT + " < " + boost::lexical_cast< std::string >( ptBins.at( uPt + 1 ) ) + " GeV" );
    TH1D* histPtTrans( new TH1D( namePtTrans.c_str(), titlePtTrans.c_str(), nPtBinsHistos, -ptMaxHistos, ptMaxHistos ) );
    histPtTrans->SetXTitle( titleTrans.c_str() );
    histPtTrans->SetYTitle( "events" );
    histVecPtTrans.push_back( histPtTrans );
    TLegend* legPtTrans( new TLegend( gStyle->GetPadLeftMargin() + 0.025, 0.75, 0.4, 0.975 - gStyle->GetPadTopMargin() ) );
    legPtTrans->SetFillColor( gStyle->GetPadColor() );
    legPtTrans->SetHeader( histPtTrans->GetTitle() );
    legVecPtTrans.push_back( legPtTrans );
  }
}

my::HistosTransEta::HistosTransEta( const std::string& objCat, const std::string& baseName, const unsigned nPtBinsHistos, const double ptMaxHistos, const unsigned nPtBins, const std::vector< Double_t >& ptBins, const std::string& titleTrans, const std::string& baseTitlePt, const std::string& titlePtT, const std::string& titlePt, const std::string& titleEta, const HistosTransEta& histosOrig, const double widthFactor )
{
  const Double_t meanTrans( histosOrig.histTrans->GetMean() );
  const Double_t widthTrans( histosOrig.histTrans->GetRMS() );
  const Double_t rangeTrans( widthTrans == 0. ? widthFactor * std::fabs( histosOrig.histTrans->GetXaxis()->GetXmax() ) : widthFactor * widthTrans );
  const std::string nameTrans( baseName + "_Trans" );
  histTrans = new TH1D( nameTrans.c_str(), objCat.c_str(), nPtBinsHistos, meanTrans - rangeTrans, meanTrans + rangeTrans );
  histTrans->SetXTitle( titleTrans.c_str() );
  histTrans->SetYTitle( "events" );
  legTrans  = new TLegend( gStyle->GetPadLeftMargin() + 0.025, 0.75, 0.4, 0.975 - gStyle->GetPadTopMargin() );
  legTrans->SetFillColor( gStyle->GetPadColor() );
  legTrans->SetHeader( histTrans->GetTitle() );
  const std::string nameTransMapPt( nameTrans + "_Map_Pt" );
  histTransMapPt = new TH2D( nameTransMapPt.c_str(), objCat.c_str(), nPtBins, ptBins.data(), nPtBinsHistos, meanTrans - rangeTrans, meanTrans + rangeTrans );
  histTransMapPt->SetXTitle( titlePt.c_str() );
  histTransMapPt->SetYTitle( titleTrans.c_str() );
  histTransMapPt->SetZTitle( "events" );
  const std::string nameTransScaleMapPt( nameTrans + "_ScaleMap_Pt" );
  histTransScaleMapPt = new TH2D( nameTransScaleMapPt.c_str(), objCat.c_str(), nPtBinsHistos, -ptMaxHistos, ptMaxHistos, nPtBins, ptBins.data() );
  histTransScaleMapPt->SetXTitle( titleTrans.c_str() );
  histTransScaleMapPt->SetYTitle( titlePt.c_str() );
  histTransScaleMapPt->SetZTitle( "events" );

  for ( unsigned uPt = 0; uPt < nPtBins; ++uPt ) {
    const Double_t meanPtTrans( histosOrig.histVecPtTrans.at( uPt )->GetMean() );
    const Double_t widthPtTrans( histosOrig.histVecPtTrans.at( uPt )->GetRMS() );
    const Double_t rangePtTrans( widthPtTrans == 0. ? widthFactor * std::fabs( histosOrig.histVecPtTrans.at( uPt )->GetXaxis()->GetXmax() ) : widthFactor * widthPtTrans );
    const std::string binPt( boost::lexical_cast< std::string >( uPt ) );
    const std::string namePtTrans( baseName + "_" + baseTitlePt + binPt + "_Trans" );
    const std::string titlePtTrans( objCat + ", " + boost::lexical_cast< std::string >( ptBins.at( uPt ) ) + " GeV #leq " + titlePtT + " < " + boost::lexical_cast< std::string >( ptBins.at( uPt + 1 ) ) + " GeV" );
    TH1D* histPtTrans( new TH1D( namePtTrans.c_str(), titlePtTrans.c_str(), nPtBinsHistos, meanPtTrans - rangePtTrans, meanPtTrans + rangePtTrans ) );
    histPtTrans->SetXTitle( titleTrans.c_str() );
    histPtTrans->SetYTitle( "events" );
    histVecPtTrans.push_back( histPtTrans );
    TLegend* legPtTrans( new TLegend( gStyle->GetPadLeftMargin() + 0.025, 0.75, 0.4, 0.975 - gStyle->GetPadTopMargin() ) );
    legPtTrans->SetFillColor( gStyle->GetPadColor() );
    legPtTrans->SetHeader( histPtTrans->GetTitle() );
    legVecPtTrans.push_back( legPtTrans );
  }
}


void my::HistosTransEta::scale()
{
  if ( histTrans->Integral( "width" ) != 0. ) histTrans->Scale( 1. / histTrans->Integral( "width" ) );
  if ( histTransMapPt->Integral( "width" ) != 0. ) histTransMapPt->Scale( 1. / histTransMapPt->Integral( "width" ) ); // FIXME: Is this correct?
  for ( unsigned uPt = 0; uPt < histVecPtTrans.size(); ++uPt ) {
    if ( histVecPtTrans.at( uPt )->Integral( "width" ) != 0. ) histVecPtTrans.at( uPt )->Scale( 1. / histVecPtTrans.at( uPt )->Integral( "width" ) );
    for ( Int_t iDeltaPt = 0; iDeltaPt <= histVecPtTrans.at( uPt )->GetNbinsX(); ++iDeltaPt ) {
      histTransScaleMapPt->SetBinContent( iDeltaPt, ( Int_t )uPt + 1, histVecPtTrans.at( uPt )->GetBinContent( iDeltaPt ) );
    }
  }
  if ( histTransScaleMapPt->Integral( "width" ) != 0. ) histTransScaleMapPt->Scale( 1. / histTransScaleMapPt->Integral( "width" ) ); // FIXME: Is this correct?
}


my::HistosTrans::HistosTrans( const HistosTrans& histosTrans, const std::string& baseName, const std::string& baseTitlePt, bool scale )
: HistosTransEta( histosTrans, baseName, baseTitlePt, scale )
{
  const std::string nameTransMapEta( baseName + "_Trans_Map_Eta" );
  histTransMapEta = new TH2D( *( ( TH2D* )( histosTrans.histTransMapEta->Clone( nameTransMapEta.c_str() ) ) ) );

  for ( unsigned uPt = 0; uPt < histosTrans.histVecPtTrans.size(); ++uPt ) {
    const std::string binPt( boost::lexical_cast< std::string >( uPt ) );
    const std::string namePtTransMapEta( baseName + "_" + baseTitlePt + binPt + "_Trans_Map_Eta" );
    TH2D* histPtTransMapEta( new TH2D( *( ( TH2D* )( histosTrans.histVecPtTransMapEta.at( uPt)->Clone( namePtTransMapEta.c_str() ) ) ) ) );
    histVecPtTransMapEta.push_back( histPtTransMapEta );
  }

  if ( scale ) this->scale();
}


my::HistosTrans::HistosTrans( const std::string& objCat, const std::string& baseName, const unsigned nPtBinsHistos, const double ptMaxHistos, const unsigned nPtBins, const std::vector< Double_t >& ptBins, const unsigned nEtaBins, const std::vector< Double_t >& etaBins, const std::string& titleTrans, const std::string& baseTitlePt, const std::string& titlePtT, const std::string& titlePt, const std::string& titleEta )
: HistosTransEta( objCat, baseName, nPtBinsHistos, ptMaxHistos, nPtBins, ptBins, titleTrans, baseTitlePt, titlePtT, titlePt, titleEta )
{
  const std::string nameTransMapEta( baseName + "_Trans_Map_Eta" );
  histTransMapEta = new TH2D( nameTransMapEta.c_str(), objCat.c_str(), nEtaBins, etaBins.data(), nPtBinsHistos, -ptMaxHistos, ptMaxHistos );
  histTransMapEta->SetXTitle( titleEta.c_str() );
  histTransMapEta->SetYTitle( titleTrans.c_str() );
  histTransMapEta->SetZTitle( "events" );

  for ( unsigned uPt = 0; uPt < nPtBins; ++uPt ) {
    const std::string binPt( boost::lexical_cast< std::string >( uPt ) );
    const std::string namePtTransMapEta( baseName + "_" + baseTitlePt + binPt + "_Trans_Map_Eta" );
    const std::string titlePtTrans( objCat + ", " + boost::lexical_cast< std::string >( ptBins.at( uPt ) ) + " GeV #leq " + titlePtT + " < " + boost::lexical_cast< std::string >( ptBins.at( uPt + 1 ) ) + " GeV" );
    TH2D* histPtTransMapEta( new TH2D( namePtTransMapEta.c_str(), titlePtTrans.c_str(), nEtaBins, etaBins.data(), nPtBinsHistos, -ptMaxHistos, ptMaxHistos ) );
    histPtTransMapEta->SetXTitle( titleEta.c_str() );
    histPtTransMapEta->SetYTitle( titleTrans.c_str() );
    histPtTransMapEta->SetZTitle( "events" );
    histVecPtTransMapEta.push_back( histPtTransMapEta );
  }
}

my::HistosTrans::HistosTrans( const std::string& objCat, const std::string& baseName, const unsigned nPtBinsHistos, const double ptMaxHistos, const unsigned nPtBins, const std::vector< Double_t >& ptBins, const unsigned nEtaBins, const std::vector< Double_t >& etaBins, const std::string& titleTrans, const std::string& baseTitlePt, const std::string& titlePtT, const std::string& titlePt, const std::string& titleEta, const HistosTrans& histosOrig, const double widthFactor )
: HistosTransEta( objCat, baseName, nPtBinsHistos, ptMaxHistos, nPtBins, ptBins, titleTrans, baseTitlePt, titlePtT, titlePt, titleEta, histosOrig, widthFactor )
{
  const Double_t meanTrans( histosOrig.histTrans->GetMean() );
  const Double_t widthTrans( histosOrig.histTrans->GetRMS() );
  const Double_t rangeTrans( widthTrans == 0. ? widthFactor * std::fabs( histosOrig.histTrans->GetXaxis()->GetXmax() ) : widthFactor * widthTrans );
  const std::string nameTransMapEta( baseName + "_Trans_Map_Eta" );
  histTransMapEta = new TH2D( nameTransMapEta.c_str(), objCat.c_str(), nEtaBins, etaBins.data(), nPtBinsHistos, meanTrans - rangeTrans, meanTrans + rangeTrans );
  histTransMapEta->SetXTitle( titleEta.c_str() );
  histTransMapEta->SetYTitle( titleTrans.c_str() );
  histTransMapEta->SetZTitle( "events" );

  for ( unsigned uPt = 0; uPt < nPtBins; ++uPt ) {
    const Double_t meanPtTrans( histosOrig.histVecPtTrans.at( uPt )->GetMean() );
    const Double_t widthPtTrans( histosOrig.histVecPtTrans.at( uPt )->GetRMS() );
    const Double_t rangePtTrans( widthPtTrans == 0. ? widthFactor * std::fabs( histosOrig.histVecPtTrans.at( uPt )->GetXaxis()->GetXmax() ) : widthFactor * widthPtTrans );
    const std::string binPt( boost::lexical_cast< std::string >( uPt ) );
    const std::string namePtTransMapEta( baseName + "_" + baseTitlePt + binPt + "_Trans_Map_Eta" );
    const std::string titlePtTrans( objCat + ", " + boost::lexical_cast< std::string >( ptBins.at( uPt ) ) + " GeV #leq " + titlePtT + " < " + boost::lexical_cast< std::string >( ptBins.at( uPt + 1 ) ) + " GeV" );
    TH2D* histPtTransMapEta( new TH2D( namePtTransMapEta.c_str(), titlePtTrans.c_str(), nEtaBins, etaBins.data(), nPtBinsHistos, meanPtTrans - rangePtTrans, meanPtTrans + rangePtTrans ) );
    histPtTransMapEta->SetXTitle( titleEta.c_str() );
    histPtTransMapEta->SetYTitle( titleTrans.c_str() );
    histPtTransMapEta->SetZTitle( "events" );
    histVecPtTransMapEta.push_back( histPtTransMapEta );
  }
}


void my::HistosTrans::scale()
{
  my::HistosTransEta::scale();
  if ( histTransMapEta->Integral( "width" ) != 0. ) histTransMapEta->Scale( 1. / histTransMapEta->Integral( "width" ) ); // FIXME: Is this correct?
  for ( unsigned uPt = 0; uPt < histVecPtTransMapEta.size(); ++uPt ) {
    if ( histVecPtTransMapEta.at( uPt )->Integral( "width" ) != 0. ) histVecPtTransMapEta.at( uPt )->Scale( 1. / histVecPtTransMapEta.at( uPt )->Integral( "width" ) ); // FIXME: Is this correct?
  }
}


my::HistosDependency::HistosDependency( const std::string& objCat, const std::string& baseName, const unsigned nPtBins, const std::vector< Double_t >& ptBins, const unsigned nPar, const std::string& baseTitlePt, const std::string& titlePt )
: name( baseName )
{
  const std::string namePtFitMapProb( baseName + "_FitMap_Prob" );
  const std::string titlePtFitMapProb( objCat + ", fit prob." );
  histPtProb = new TH1D( namePtFitMapProb.c_str(), titlePtFitMapProb.c_str(), nPtBins, ptBins.data() );
  histPtProb->SetXTitle( titlePt.c_str() );
  histPtProb->SetYTitle( "log_{10}(prob.)" );
  legPtProb  = new TLegend( gStyle->GetPadLeftMargin() + 0.025, 0.75, 0.4, 0.975 - gStyle->GetPadTopMargin() );
  legPtProb->SetFillColor( gStyle->GetPadColor() );
  legPtProb->SetHeader( histPtProb->GetTitle() );

  for ( unsigned uPar = 0; uPar < nPar; ++uPar ) {
    const std::string parFit( boost::lexical_cast< std::string >( uPar ) );
    const std::string namePtFitMap( baseName + "_FitMap_Par" + parFit );
    const std::string titlePtFitMap( objCat + ", par. " + parFit );
    TH1D * histPtPar( new TH1D( namePtFitMap.c_str(), titlePtFitMap.c_str(), nPtBins, ptBins.data() ) );
    histPtPar->SetXTitle( titlePt.c_str() );
    histVecPtPar.push_back( histPtPar );
    TLegend* legPtPar( new TLegend( gStyle->GetPadLeftMargin() + 0.025, 0.75, 0.4, 0.975 - gStyle->GetPadTopMargin() ) );
    legPtPar->SetFillColor( gStyle->GetPadColor() );
    legPtPar->SetHeader( histPtPar->GetTitle() );
    legVecPtPar.push_back( legPtPar );
  }
}
