#include "TopQuarkAnalysis/TopMassSemiLeptonic/interface/FitTopTransferFunctionsHistos.h"


#include <string>

#include "boost/lexical_cast.hpp"


using namespace my;


my::HistosTrans::HistosTrans( const std::string& objCat, const std::string& name, const unsigned nPtBinsHistos, const double ptMaxHistos, const unsigned nPtBins, const std::vector< Double_t >& ptBins, const unsigned nEtaBins, const std::vector< Double_t >& etaBins, const std::string& titleTrans, const std::string& baseTitlePt, const std::string& titlePtT, const std::string& titlePt, const std::string& titleEta )
{
  const std::string nameTrans( name + "_Trans" );
  histTrans = new TH1D( nameTrans.c_str(), objCat.c_str(), nPtBinsHistos, -ptMaxHistos, ptMaxHistos );
  histTrans->SetXTitle( titleTrans.c_str() );
  histTrans->SetYTitle( "events" );
  const std::string nameTransMapPt( nameTrans + "_Map_Pt" );
  histTransMapPt = new TH2D( nameTransMapPt.c_str(), objCat.c_str(), nPtBins, ptBins.data(), nPtBinsHistos, -ptMaxHistos, ptMaxHistos );
  histTransMapPt->SetXTitle( titlePt.c_str() );
  histTransMapPt->SetYTitle( titleTrans.c_str() );
  histTransMapPt->SetZTitle( "events" );
  const std::string nameTransMapEta( nameTrans + "_Map_Eta" );
  histTransMapEta = new TH2D( nameTransMapEta.c_str(), objCat.c_str(), nEtaBins, etaBins.data(), nPtBinsHistos, -ptMaxHistos, ptMaxHistos );
  histTransMapEta->SetXTitle( titleEta.c_str() );
  histTransMapEta->SetYTitle( titleTrans.c_str() );
  histTransMapEta->SetZTitle( "events" );

  for ( unsigned uPt = 0; uPt < nPtBins; ++uPt ) {
    const std::string binPt( boost::lexical_cast< std::string >( uPt ) );
    const std::string namePt( name + "_" + baseTitlePt + binPt );
    const std::string namePtTrans( namePt + "_Trans" );
    const std::string titlePtTrans( objCat + ", " + boost::lexical_cast< std::string >( ptBins.at( uPt ) ) + " GeV #leq " + titlePtT + " < " + boost::lexical_cast< std::string >( ptBins.at( uPt + 1 ) ) + " GeV" );
    TH1D* histPtTrans( new TH1D( namePtTrans.c_str(), titlePtTrans.c_str(), nPtBinsHistos, -ptMaxHistos, ptMaxHistos ) );
    histPtTrans->SetXTitle( titleTrans.c_str() );
    histPtTrans->SetYTitle( "events" );
    histVecPtTrans.push_back( histPtTrans );
    const std::string namePtTransMapEta( namePtTrans + "_Map_Eta" );
    TH2D* histPtTransMapEta( new TH2D( namePtTransMapEta.c_str(), titlePtTrans.c_str(), nEtaBins, etaBins.data(), nPtBinsHistos, -ptMaxHistos, ptMaxHistos ) );
    histPtTransMapEta->SetXTitle( titleEta.c_str() );
    histPtTransMapEta->SetYTitle( titleTrans.c_str() );
    histPtTransMapEta->SetZTitle( "events" );
    histVecPtTransMapEta.push_back( histPtTransMapEta );
  }
}

my::HistosTrans::HistosTrans( const std::string& objCat, const std::string& name, const unsigned nPtBinsHistos, const double ptMaxHistos, const unsigned nPtBins, const std::vector< Double_t >& ptBins, const unsigned nEtaBins, const std::vector< Double_t >& etaBins, const std::string& titleTrans, const std::string& baseTitlePt, const std::string& titlePtT, const std::string& titlePt, const std::string& titleEta, const HistosTrans& histosOrig, const double widthFactor )
{
  const std::string nameTrans( name + "_Trans" );
  const Double_t meanTrans( histosOrig.histTrans->GetMean() );
  const Double_t widthTrans( histosOrig.histTrans->GetRMS() );
  const Double_t rangeTrans( widthTrans == 0. ? widthFactor * std::fabs( histosOrig.histTrans->GetXaxis()->GetXmax() ) : widthFactor * widthTrans );
  histTrans = new TH1D( nameTrans.c_str(), objCat.c_str(), nPtBinsHistos, meanTrans - rangeTrans, meanTrans + rangeTrans );
  histTrans->SetXTitle( titleTrans.c_str() );
  histTrans->SetYTitle( "events" );
  const std::string nameTransMapPt( nameTrans + "_Map_Pt" );
  histTransMapPt = new TH2D( nameTransMapPt.c_str(), objCat.c_str(), nPtBins, ptBins.data(), nPtBinsHistos, meanTrans - rangeTrans, meanTrans + rangeTrans );
  histTransMapPt->SetXTitle( titlePt.c_str() );
  histTransMapPt->SetYTitle( titleTrans.c_str() );
  histTransMapPt->SetZTitle( "events" );
  const std::string nameTransMapEta( nameTrans + "_Map_Eta" );
  histTransMapEta = new TH2D( nameTransMapEta.c_str(), objCat.c_str(), nEtaBins, etaBins.data(), nPtBinsHistos, meanTrans - rangeTrans, meanTrans + rangeTrans );
  histTransMapEta->SetXTitle( titleEta.c_str() );
  histTransMapEta->SetYTitle( titleTrans.c_str() );
  histTransMapEta->SetZTitle( "events" );

  for ( unsigned uPt = 0; uPt < nPtBins; ++uPt ) {
    const std::string binPt( boost::lexical_cast< std::string >( uPt ) );
    const std::string namePt( name + "_" + baseTitlePt + binPt );
    const std::string namePtTrans( namePt + "_Trans" );
    const std::string titlePtTrans( objCat + ", " + boost::lexical_cast< std::string >( ptBins.at( uPt ) ) + " GeV #leq " + titlePtT + " < " + boost::lexical_cast< std::string >( ptBins.at( uPt + 1 ) ) + " GeV" );
    const Double_t meanPtTrans( histosOrig.histVecPtTrans.at( uPt )->GetMean() );
    const Double_t widthPtTrans( histosOrig.histVecPtTrans.at( uPt )->GetRMS() );
    const Double_t rangePtTrans( widthPtTrans == 0. ? widthFactor * std::fabs( histosOrig.histVecPtTrans.at( uPt )->GetXaxis()->GetXmax() ) : widthFactor * widthPtTrans );
    TH1D* histPtTrans( new TH1D( namePtTrans.c_str(), titlePtTrans.c_str(), nPtBinsHistos, meanPtTrans - rangePtTrans, meanPtTrans + rangePtTrans ) );
    histPtTrans->SetXTitle( titleTrans.c_str() );
    histPtTrans->SetYTitle( "events" );
    histVecPtTrans.push_back( histPtTrans );
    const std::string namePtTransMapEta( namePtTrans + "_Map_Eta" );
    TH2D* histPtTransMapEta( new TH2D( namePtTransMapEta.c_str(), titlePtTrans.c_str(), nEtaBins, etaBins.data(), nPtBinsHistos, meanPtTrans - rangePtTrans, meanPtTrans + rangePtTrans ) );
    histPtTransMapEta->SetXTitle( titleEta.c_str() );
    histPtTransMapEta->SetYTitle( titleTrans.c_str() );
    histPtTransMapEta->SetZTitle( "events" );
    histVecPtTransMapEta.push_back( histPtTransMapEta );
  }
}


void my::HistosTrans::scale()
{
  if ( histTrans->Integral( "width" ) != 0. ) histTrans->Scale( 1. / histTrans->Integral( "width" ) );
  if ( histTransMapPt->Integral( "width" ) != 0. ) histTransMapPt->Scale( 1. / histTransMapPt->Integral( "width" ) );
  if ( histTransMapEta->Integral( "width" ) != 0. ) histTransMapEta->Scale( 1. / histTransMapEta->Integral( "width" ) );
  for ( unsigned uPt = 0; uPt < histVecPtTrans.size(); ++uPt ) {
    if ( histVecPtTrans.at( uPt )->Integral( "width" ) != 0. ) histVecPtTrans.at( uPt )->Scale( 1. / histVecPtTrans.at( uPt )->Integral( "width" ) );
  }
  for ( unsigned uPt = 0; uPt < histVecPtTransMapEta.size(); ++uPt ) {
    if ( histVecPtTransMapEta.at( uPt )->Integral( "width" ) != 0. ) histVecPtTransMapEta.at( uPt )->Scale( 1. / histVecPtTransMapEta.at( uPt )->Integral( "width" ) );
  }
}


my::HistosTransEta::HistosTransEta( const std::string& objCat, const std::string& name, const unsigned nPtBinsHistos, const double ptMaxHistos, const unsigned nPtBins, const std::vector< Double_t >& ptBins, const std::string& titleTrans, const std::string& baseTitlePt, const std::string& titlePtT, const std::string& titlePt, const std::string& titleEta )
{
  const std::string nameTrans( name + "_Trans" );
  histTrans = new TH1D( nameTrans.c_str(), objCat.c_str(), nPtBinsHistos, -ptMaxHistos, ptMaxHistos );
  histTrans->SetXTitle( titleTrans.c_str() );
  histTrans->SetYTitle( "events" );
  const std::string nameTransMapPt( nameTrans + "_Map_Pt" );
  histTransMapPt = new TH2D( nameTransMapPt.c_str(), objCat.c_str(), nPtBins, ptBins.data(), nPtBinsHistos, -ptMaxHistos, ptMaxHistos );
  histTransMapPt->SetXTitle( titlePt.c_str() );
  histTransMapPt->SetYTitle( titleTrans.c_str() );
  histTransMapPt->SetZTitle( "events" );

  for ( unsigned uPt = 0; uPt < nPtBins; ++uPt ) {
    const std::string binPt( boost::lexical_cast< std::string >( uPt ) );
    const std::string namePt( name + "_" + baseTitlePt + binPt );
    const std::string namePtTrans( namePt + "_Trans" );
    const std::string titlePtTrans( objCat + ", " + boost::lexical_cast< std::string >( ptBins.at( uPt ) ) + " GeV #leq " + titlePtT + " < " + boost::lexical_cast< std::string >( ptBins.at( uPt + 1 ) ) + " GeV" );
    TH1D* histPtTrans( new TH1D( namePtTrans.c_str(), titlePtTrans.c_str(), nPtBinsHistos, -ptMaxHistos, ptMaxHistos ) );
    histPtTrans->SetXTitle( titleTrans.c_str() );
    histPtTrans->SetYTitle( "events" );
    histVecPtTrans.push_back( histPtTrans );
  }
}

my::HistosTransEta::HistosTransEta( const std::string& objCat, const std::string& name, const unsigned nPtBinsHistos, const double ptMaxHistos, const unsigned nPtBins, const std::vector< Double_t >& ptBins, const std::string& titleTrans, const std::string& baseTitlePt, const std::string& titlePtT, const std::string& titlePt, const std::string& titleEta, const HistosTransEta& histosOrig, const double widthFactor )
{
  const std::string nameTrans( name + "_Trans" );
  const Double_t meanTrans( histosOrig.histTrans->GetMean() );
  const Double_t widthTrans( histosOrig.histTrans->GetRMS() );
  const Double_t rangeTrans( widthTrans == 0. ? widthFactor * std::fabs( histosOrig.histTrans->GetXaxis()->GetXmax() ) : widthFactor * widthTrans );
  histTrans = new TH1D( nameTrans.c_str(), objCat.c_str(), nPtBinsHistos, meanTrans - rangeTrans, meanTrans + rangeTrans );
  histTrans->SetXTitle( titleTrans.c_str() );
  histTrans->SetYTitle( "events" );
  const std::string nameTransMapPt( nameTrans + "_Map_Pt" );
  histTransMapPt = new TH2D( nameTransMapPt.c_str(), objCat.c_str(), nPtBins, ptBins.data(), nPtBinsHistos, meanTrans - rangeTrans, meanTrans + rangeTrans );
  histTransMapPt->SetXTitle( titlePt.c_str() );
  histTransMapPt->SetYTitle( titleTrans.c_str() );
  histTransMapPt->SetZTitle( "events" );

  for ( unsigned uPt = 0; uPt < nPtBins; ++uPt ) {
    const std::string binPt( boost::lexical_cast< std::string >( uPt ) );
    const std::string namePt( name + "_" + baseTitlePt + binPt );
    const std::string namePtTrans( namePt + "_Trans" );
    const std::string titlePtTrans( objCat + ", " + boost::lexical_cast< std::string >( ptBins.at( uPt ) ) + " GeV #leq " + titlePtT + " < " + boost::lexical_cast< std::string >( ptBins.at( uPt + 1 ) ) + " GeV" );
    const Double_t meanPtTrans( histosOrig.histVecPtTrans.at( uPt )->GetMean() );
    const Double_t widthPtTrans( histosOrig.histVecPtTrans.at( uPt )->GetRMS() );
    const Double_t rangePtTrans( widthPtTrans == 0. ? widthFactor * std::fabs( histosOrig.histVecPtTrans.at( uPt )->GetXaxis()->GetXmax() ) : widthFactor * widthPtTrans );
    TH1D* histPtTrans( new TH1D( namePtTrans.c_str(), titlePtTrans.c_str(), nPtBinsHistos, meanPtTrans - rangePtTrans, meanPtTrans + rangePtTrans ) );
    histPtTrans->SetXTitle( titleTrans.c_str() );
    histPtTrans->SetYTitle( "events" );
    histVecPtTrans.push_back( histPtTrans );
  }
}


void my::HistosTransEta::scale()
{
  if ( histTrans->Integral( "width" ) != 0. ) histTrans->Scale( 1. / histTrans->Integral( "width" ) );
  if ( histTransMapPt->Integral( "width" ) != 0. ) histTransMapPt->Scale( 1. / histTransMapPt->Integral( "width" ) );
  for ( unsigned uPt = 0; uPt < histVecPtTrans.size(); ++uPt ) {
    if ( histVecPtTrans.at( uPt )->Integral( "width" ) != 0. ) histVecPtTrans.at( uPt )->Scale( 1. / histVecPtTrans.at( uPt )->Integral( "width" ) );
  }
}
