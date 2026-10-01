# Raw Data vs SDTM vs ADaM

## Raw Clinical Data

Raw data represents the information collected or received
from clinical systems.

Examples:

- CRF exports
- Laboratory vendor files
- Medication data
- Vital signs
- Exposure data

Raw data is generally study/vendor-specific.

---

## SDTM

SDTM standardizes collected clinical study data into
standardized domains.

Examples:

DM
AE
VS
LB
CM
EX

SDTM is primarily intended to support standardized
tabulation and review.

Example:

Raw:

SUBJID = 0001
TEST = Systolic Blood Pressure
RESULT = 138
UNIT = mmHg

SDTM:

USUBJID = HYPER-P2-101-0001
VSTESTCD = SYSBP
VSORRES = 138
VSORRESU = mmHg
VSSTRESN = 138

---

## ADaM

ADaM datasets are analysis-ready datasets derived from
standardized data, generally using SDTM as an important
source.

Examples:

ADSL
ADAE
ADLB
ADVS

ADaM supports statistical analysis and traceability
from analysis results back toward the source data.

---

## Simplified Flow

Raw Data
    ↓
SDTM
    ↓
ADaM
    ↓
Statistical Analysis
