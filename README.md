# SDTM-Mapper

## Clinical Trial Data → CDISC SDTM Pipeline

SDTM-Mapper is a Python portfolio project demonstrating how
study-specific clinical trial data can be transformed into
standardized CDISC SDTM domains.

The project simulates a 100-subject Phase II hypertension study.

## Domains

- DM — Demographics
- AE — Adverse Events
- VS — Vital Signs
- LB — Laboratory Tests
- CM — Concomitant Medications
- EX — Exposure

## Pipeline

Raw Clinical Data
        ↓
Mapping Specification
        ↓
SDTM Transformation
        ↓
Controlled Terminology
        ↓
Conformance Checks
        ↓
Validation Report
        ↓
CSV + XPT

## Standards Baseline

This demonstration uses:

- SDTM v1.7
- SDTMIG v3.3
- CDISC/NCI Controlled Terminology concepts

The repository is an educational implementation and is not
intended to represent complete regulatory conformance.

## Features

- Synthetic clinical trial data generation
- Source-to-target mapping specification
- SDTM domain generation
- ISO 8601 dates
- USUBJID derivation
- Sequence variable generation
- Study-day derivation
- Controlled terminology mapping
- Cross-domain mapping
- Validation checks
- CSV export
- SAS XPT export
- Validation report

## Example Transformation

### Raw

SUBJID: 0001
TEST: Systolic Blood Pressure
RESULT: 138
UNIT: mmHg

### SDTM

USUBJID: HYPER-P2-101-0001
VSTESTCD: SYSBP
VSTEST: SYSTOLIC BLOOD PRESSURE
VSORRES: 138
VSORRESU: mmHg
VSSTRESN: 138
VSSTRESU: mmHg

## Validation

The validation engine checks:

- Required variables
- Missing identifiers
- Duplicate keys
- Sequence variables
- Domain values
- Controlled terminology
- ISO date validity
- Event date consistency
- Exposure date consistency
- Numeric Findings values
- Study-day derivations

The rules are inspired by CDISC SDTM/SDTMIG
conformance concepts but are not a replacement for
commercial validation software or official conformance
checking.

## Output

CSV:

data/sdtm/

XPT:

output/xpt/

Validation:

output/validation_report.csv

## Limitations

This is a portfolio/educational project.

The source data are synthetic.

The project does not contain real patient data.

AEDECOD is not actually coded using MedDRA.

The terminology implementation is a simplified demonstration
and must not be treated as a complete implementation of the
current CDISC/NCI terminology package.

The project does not implement:

- Define-XML
- annotated CRF
- controlled terminology package ingestion
- MedDRA licensing/dictionary integration
- WHODrug
- complete SDTMIG conformance
- FDA/PMDA submission validation
- Pinnacle 21
- database audit trails
- electronic signatures
- production security
- full traceability matrix
- ADaM
- statistical programming

Therefore this repository makes no regulatory submission claim.
