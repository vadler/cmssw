#ifndef TopQuarkPhysics_TopMassSemiLeptonic_FitTopTransferFunctionsHistos_h
#define TopQuarkPhysics_TopMassSemiLeptonic_FitTopTransferFunctionsHistos_h


#include <vector>
#include <string>

#include <TROOT.h>
#include <TH1D.h>
#include <TH2D.h>


namespace my {

  struct HistosTrans {

    TH1D * histTrans;
    TH2D * histTransMapPt;
    TH2D * histTransMapEta;
    // Per pt bin
    std::vector< TH1D* > histVecPtTrans;
    std::vector< TH2D* > histVecPtTransMapEta;

    HistosTrans() {};
    explicit HistosTrans( const std::string& objCat, const std::string& name, const unsigned nPtBinsHistos, const double ptMaxHistos, const unsigned nPtBins, const std::vector< Double_t >& ptBins, const unsigned nEtaBins, const std::vector< Double_t >& etaBins, const std::string& titleTrans, const std::string& baseTitlePt, const std::string& titlePtT, const std::string& titlePt, const std::string& titleEta );
    explicit HistosTrans( const std::string& objCat, const std::string& name, const unsigned nPtBinsHistos, const double ptMaxHistos, const unsigned nPtBins, const std::vector< Double_t >& ptBins, const unsigned nEtaBins, const std::vector< Double_t >& etaBins, const std::string& titleTrans, const std::string& baseTitlePt, const std::string& titlePtT, const std::string& titlePt, const std::string& titleEta, const HistosTrans& histosOrig, const double widthFactor );
    ~HistosTrans() {};

    void scale();

  };

  struct HistosTransEta {

    TH1D * histTrans;
    TH2D * histTransMapPt;
    // Per pt bin
    std::vector< TH1D* > histVecPtTrans;

    HistosTransEta() {};
    explicit HistosTransEta( const std::string& objCat, const std::string& name, const unsigned nPtBinsHistos, const double ptMaxHistos, const unsigned nPtBins, const std::vector< Double_t >& ptBins, const std::string& titleTrans, const std::string& baseTitlePt, const std::string& titlePtT, const std::string& titlePt, const std::string& titleEta );
    explicit HistosTransEta( const std::string& objCat, const std::string& name, const unsigned nPtBinsHistos, const double ptMaxHistos, const unsigned nPtBins, const std::vector< Double_t >& ptBins, const std::string& titleTrans, const std::string& baseTitlePt, const std::string& titlePtT, const std::string& titlePt, const std::string& titleEta, const HistosTransEta& histosOrig, const double widthFactor );
    ~HistosTransEta() {};

    void scale();

  };

}


#endif
