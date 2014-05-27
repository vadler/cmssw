#ifndef TopQuarkPhysics_TopMassSemiLeptonic_ObjectDataContainer_h
#define TopQuarkPhysics_TopMassSemiLeptonic_ObjectDataContainer_h


#include <vector>
#include <string>

#include <TROOT.h>
#include <TDirectory.h>


namespace my {

  typedef std::vector< std::vector< Double_t > > DataTable;

  struct ObjectDataContainer {

      explicit ObjectDataContainer( const std::string& objCat, TDirectory* dirInCat, Bool_t useSymm, Bool_t useAlt, Bool_t useNonT, Bool_t useNonP, Bool_t refGen, Bool_t usePileUp, const std::string& pileUp, Int_t maxEvents = -1 );
      ~ObjectDataContainer() {};

      /// Get binning
      std::vector< Double_t > etaBins() const { return etaBins_; };
      std::vector< Double_t > ptBins() const { return ptBins_; };
      /// Get number of bins
      unsigned nEtaBins() const { return etaBins_.size() - 1; };
      unsigned nPtBins() const { return ptBins_.size() - 1; };
      /// Get sizes
      std::vector< unsigned >                sizeEta() const { return sizeEta_; };
      std::vector< std::vector< unsigned > > sizePt() const { return sizePt_; };
      /// Get size per eta bin
      unsigned                sizeEta( unsigned uEta ) const { return sizeEta_.at( uEta ); };
      std::vector< unsigned > sizePt( unsigned uEta ) const { return sizePt_.at( uEta ); };
      unsigned sizePt( unsigned uEta, unsigned uPt ) const { return sizePt_.at( uEta ).at( uPt ); };
      /// Get data
      DataTable weight() const { return weightData_; };
      DataTable pt() const { return ptData_; };
      DataTable ptGen() const { return ptGenData_; };
      DataTable energy() const { return energyData_; };
      DataTable energyGen() const { return energyGenData_; };
      DataTable eta() const { return etaData_; };
      DataTable etaGen() const { return etaGenData_; };
      DataTable phi() const { return phiData_; };
      DataTable phiGen() const { return phiGenData_; };
      /// Get data per eta bin
      std::vector< Double_t > weight( unsigned uEta ) const { return weightData_.at( uEta ); };
      std::vector< Double_t > pt( unsigned uEta ) const { return ptData_.at( uEta ); };
      std::vector< Double_t > ptGen( unsigned uEta ) const { return ptGenData_.at( uEta ); };
      std::vector< Double_t > energy( unsigned uEta ) const { return energyData_.at( uEta ); };
      std::vector< Double_t > energyGen( unsigned uEta ) const { return energyGenData_.at( uEta ); };
      std::vector< Double_t > eta( unsigned uEta ) const { return etaData_.at( uEta ); };
      std::vector< Double_t > etaGen( unsigned uEta ) const { return etaGenData_.at( uEta ); };
      std::vector< Double_t > phi( unsigned uEta ) const { return phiData_.at( uEta ); };
      std::vector< Double_t > phiGen( unsigned uEta ) const { return phiGenData_.at( uEta ); };
      /// Get data per eta/pt bin
      DataTable weightPt( unsigned uEta ) const { return weightDataPt_.at( uEta ); };
      DataTable ptPt( unsigned uEta ) const { return ptDataPt_.at( uEta ); };
      DataTable ptGenPt( unsigned uEta ) const { return ptGenDataPt_.at( uEta ); };
      DataTable etaPt( unsigned uEta ) const { return etaDataPt_.at( uEta ); };
      DataTable etaGenPt( unsigned uEta ) const { return etaGenDataPt_.at( uEta ); };
      DataTable phiPt( unsigned uEta ) const { return phiDataPt_.at( uEta ); };
      DataTable phiGenPt( unsigned uEta ) const { return phiGenDataPt_.at( uEta ); };
      /// Get data per eta per pt bin
      std::vector< Double_t > weightPt( unsigned uEta, unsigned uPt ) const { return weightDataPt_.at( uEta ).at( uPt ); };
      std::vector< Double_t > ptPt( unsigned uEta, unsigned uPt ) const { return ptDataPt_.at( uEta ).at( uPt ); };
      std::vector< Double_t > ptGenPt( unsigned uEta, unsigned uPt ) const { return ptGenDataPt_.at( uEta ).at( uPt ); };
      std::vector< Double_t > etaPt( unsigned uEta, unsigned uPt ) const { return etaDataPt_.at( uEta ).at( uPt ); };
      std::vector< Double_t > etaGenPt( unsigned uEta, unsigned uPt ) const { return etaGenDataPt_.at( uEta ).at( uPt ); };
      std::vector< Double_t > phiPt( unsigned uEta, unsigned uPt ) const { return phiDataPt_.at( uEta ).at( uPt ); };
      std::vector< Double_t > phiGenPt( unsigned uEta, unsigned uPt ) const { return phiGenDataPt_.at( uEta ).at( uPt ); };

    private:

      friend class JetDataContainer;

      /// Binning
      std::vector< Double_t > etaBins_;
      std::vector< Double_t > ptBins_;
      /// Sizes
      std::vector< unsigned >                sizeEta_;
      std::vector< std::vector< unsigned > > sizePt_;
      /// Data
      DataTable weightData_;
      DataTable ptData_;
      DataTable ptGenData_;
      DataTable energyData_;
      DataTable energyGenData_;
      DataTable etaData_;
      DataTable etaGenData_;
      DataTable phiData_;
      DataTable phiGenData_;
      /// Data per pt bins
      std::vector< DataTable > weightDataPt_;
      std::vector< DataTable > ptDataPt_;
      std::vector< DataTable > ptGenDataPt_;
      std::vector< DataTable > etaDataPt_;
      std::vector< DataTable > etaGenDataPt_;
      std::vector< DataTable > phiDataPt_;
      std::vector< DataTable > phiGenDataPt_;

  };

}


#endif
