# SDTM Domain Guide

## DM — Demographics

Class:
Special Purpose

Structure:
One record per subject.

Main variables:

- STUDYID
- USUBJID
- SUBJID
- RFSTDTC
- BRTHDTC
- SITEID
- SEX
- RACE
- ETHNIC

---

## AE — Adverse Events

Class:
Events

Structure:
One record per adverse event per subject.

Main variables:

- USUBJID
- AESEQ
- AETERM
- AEDECOD
- AESEV
- AESTDTC
- AEENDTC

---

## VS — Vital Signs

Class:
Findings

Structure:
One record per vital-sign test per subject.

Main variables:

- USUBJID
- VSSEQ
- VSTESTCD
- VSTEST
- VSORRES
- VSORRESU
- VSSTRESN
- VSSTRESU
- VSDTC

---

## LB — Laboratory Tests

Class:
Findings

Structure:
One record per laboratory test per subject.

Main variables:

- USUBJID
- LBSEQ
- LBTESTCD
- LBTEST
- LBORRES
- LBORRESU
- LBSTRESN
- LBSTRESU
- LBSPEC
- LBDTC

---

## CM — Concomitant Medications

Class:
Interventions

Main variables:

- USUBJID
- CMSEQ
- CMTRT
- CMDOSE
- CMDOSU
- CMDOSFRQ
- CMROUTE
- CMSTDTC
- CMENDTC

---

## EX — Exposure

Class:
Interventions

Main variables:

- USUBJID
- EXSEQ
- EXTRT
- EXDOSE
- EXDOSU
- EXDOSFRQ
- EXROUTE
- EXSTDTC
- EXENDTC
- EXSTDY
- EXENDY
