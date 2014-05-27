#ifndef TopQuarkPhysics_TopMassSemiLeptonic_JetDataContainer_h
#define TopQuarkPhysics_TopMassSemiLeptonic_JetDataContainer_h

#include "TopQuarkAnalysis/TopMassSemiLeptonic/interface/ObjectDataContainer.h"


namespace my {

  struct JetDataContainer : public ObjectDataContainer {

      explicit JetDataContainer( const std::string& objCat, TDirectory* dirInCat, Bool_t useSymm, Bool_t useAlt, Bool_t useNonT, Bool_t useNonP, Bool_t refGen, Bool_t usePileUp, const std::string& pileUp, Int_t maxEvents = -1 );
      ~JetDataContainer() {};

      /// Get data
      DataTable ptGenJet() const { return ptGenJetData_; };
      DataTable energyGenJet() const { return energyGenJetData_; };
      DataTable etaGenJet() const { return etaGenJetData_; };
      DataTable phiGenJet() const { return phiGenJetData_; };
      DataTable tagCSV() const { return tagCSVData_; };
      /// Get data per eta bin
      std::vector< Double_t > ptGenJet( unsigned uEta ) const { return ptGenJetData_.at( uEta ); };
      std::vector< Double_t > energyGenJet( unsigned uEta ) const { return energyGenJetData_.at( uEta ); };
      std::vector< Double_t > etaGenJet( unsigned uEta ) const { return etaGenJetData_.at( uEta ); };
      std::vector< Double_t > phiGenJet( unsigned uEta ) const { return phiGenJetData_.at( uEta ); };
      std::vector< Double_t > tagCSV( unsigned uEta ) const { return tagCSVData_.at( uEta ); };
      /// Get data per eta/pt bin
      DataTable ptGenJetPt( unsigned uEta ) const { return ptGenJetDataPt_.at( uEta ); };
      DataTable etaGenJetPt( unsigned uEta ) const { return etaGenJetDataPt_.at( uEta ); };
      DataTable phiGenJetPt( unsigned uEta ) const { return phiGenJetDataPt_.at( uEta ); };
      DataTable tagCSVPt( unsigned uEta ) const { return tagCSVDataPt_.at( uEta ); };
      /// Get data per eta per pt bin
      std::vector< Double_t > ptGenJetPt( unsigned uEta, unsigned uPt ) const { return ptGenJetDataPt_.at( uEta ).at( uPt ); };
      std::vector< Double_t > etaGenJetPt( unsigned uEta, unsigned uPt ) const { return etaGenJetDataPt_.at( uEta ).at( uPt ); };
      std::vector< Double_t > phiGenJetPt( unsigned uEta, unsigned uPt ) const { return phiGenJetDataPt_.at( uEta ).at( uPt ); };
      std::vector< Double_t > tagCSVPt( unsigned uEta, unsigned uPt ) const { return tagCSVDataPt_.at( uEta ).at( uPt ); };

    private:

      /// Data
      DataTable ptGenJetData_;
      DataTable energyGenJetData_;
      DataTable etaGenJetData_;
      DataTable phiGenJetData_;
      DataTable tagCSVData_;
      /// Data per pt bins
      std::vector< DataTable > ptGenJetDataPt_;
      std::vector< DataTable > etaGenJetDataPt_;
      std::vector< DataTable > phiGenJetDataPt_;
      std::vector< DataTable > tagCSVDataPt_;

  };

}


#endif
