# AlphaCare Insurance Solutions (ACIS)
## Insurance Dataset Analysis
### Project Objectives
* The objective of this analysis is to help optimise the marketing strategy as well as discover “low-risk” targets for which the premium could be reduced, hence an opportunity to attract new clients. 
## Dataset Overview 
* Total entries- 1,000,098
* Columns- 52(object:36,float:11,int:4,bool:1)
* Key features:
    1. **Columns about the insurance policy**- `UnderwrittenCoverID` and `PolicyID`
    2. **The Transaction date**- `TransactionMonth`
    3. **Columns about the client**- `Citizenship`, `LegalType`, `Gender`,etc...
    4. **Columns about the client location**- `Country`, `Province`,`PostalCode`,etc...
    5. **Columns about the car insured**- `VehicleType`,`RegistrationYear`,`Make`,etc...
    6. **Columns about the plan**-  `CalculatedPremiumPerTerm`,`ExcessSelected`,`CoverType`,etc...
    7. **Columns about the payment & claim**- `TotalPremium` and `TotalClaims`
## Tools used
1. **Pandas**- for data analysis and manipulation.
2. **Jupyter Notebook**- for an easier view and analysis  
3. **Seaborn/Matplotlib**-for visualization
---
## How to use 
1. Clone this repository.
   ```bash
   git clone https://github.com/Leoul39/AIM-Week_3.git
   ```
2. Install the required dependencies
   ```python
   pip install -r requirements.txt
   ```
3. Run the jupyter notebook that is inside the notebooks directory