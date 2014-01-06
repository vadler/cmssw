#ifndef TopQuarkPhysics_TopMassSemiLeptonic_FitTopTransferFunctionsHistos_h
#define TopQuarkPhysics_TopMassSemiLeptonic_FitTopTransferFunctionsHistos_h


#include <vector>
#include <string>

#include <TROOT.h>
#include <TH1D.h>
#include <TH2D.h>
#include <TLegend.h>


namespace my {

  struct HistosTransEta {

    std::string name;

    TH1D*    histTrans;
    TLegend* legTrans;
    TH2D*    histTransMapPt;
    // Per pt bin
    std::vector< TH1D* >    histVecPtTrans;
    std::vector< TLegend* > legVecPtTrans;

    HistosTransEta() {};
    HistosTransEta( const HistosTransEta& histosTransEta, const std::string& baseName, const std::string& baseTitlePt, bool scale = false );
    explicit HistosTransEta( const std::string& objCat, const std::string& baseName, const unsigned nPtBinsHistos, const double ptMaxHistos, const unsigned nPtBins, const std::vector< Double_t >& ptBins, const std::string& titleTrans, const std::string& baseTitlePt, const std::string& titlePtT, const std::string& titlePt, const std::string& titleEta );
    explicit HistosTransEta( const std::string& objCat, const std::string& baseName, const unsigned nPtBinsHistos, const double ptMaxHistos, const unsigned nPtBins, const std::vector< Double_t >& ptBins, const std::string& titleTrans, const std::string& baseTitlePt, const std::string& titlePtT, const std::string& titlePt, const std::string& titleEta, const HistosTransEta& histosOrig, const double widthFactor );
    virtual ~HistosTransEta() {};

    virtual void scale();

  };

  struct HistosTrans : public HistosTransEta {

    TH2D* histTransMapEta;
    // Per pt bin
    std::vector< TH2D* > histVecPtTransMapEta;

    HistosTrans() : HistosTransEta() {};
    HistosTrans( const HistosTrans& histosTrans, const std::string& baseName, const std::string& baseTitlePt, bool scale = false );
    explicit HistosTrans( const std::string& objCat, const std::string& baseName, const unsigned nPtBinsHistos, const double ptMaxHistos, const unsigned nPtBins, const std::vector< Double_t >& ptBins, const unsigned nEtaBins, const std::vector< Double_t >& etaBins, const std::string& titleTrans, const std::string& baseTitlePt, const std::string& titlePtT, const std::string& titlePt, const std::string& titleEta );
    explicit HistosTrans( const std::string& objCat, const std::string& baseName, const unsigned nPtBinsHistos, const double ptMaxHistos, const unsigned nPtBins, const std::vector< Double_t >& ptBins, const unsigned nEtaBins, const std::vector< Double_t >& etaBins, const std::string& titleTrans, const std::string& baseTitlePt, const std::string& titlePtT, const std::string& titlePt, const std::string& titleEta, const HistosTrans& histosOrig, const double widthFactor );
    virtual ~HistosTrans() {};

    virtual void scale();

  };

  struct HistosDependency {

    std::string name;

    TH1D*    histPtProb;
    TLegend* legPtProb;
    // Per parameter
    std::vector< TH1D* >    histVecPtPar;
    std::vector< TLegend* > legVecPtPar;

    HistosDependency() {};
    explicit HistosDependency( const std::string& objCat, const std::string& baseName, const unsigned nPtBins, const std::vector< Double_t >& ptBins, const unsigned nPar, const std::string& baseTitlePt, const std::string& titlePt );
    virtual ~HistosDependency() {};


  };

}


#endif
