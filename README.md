# Dr. Nalanda, MD — Deterministic Medical CDSS (Python SDK)

[![Status](https://img.shields.io/badge/Status-Certified_Production-0ea5e9.svg)](https://www.polygonal.in/ASI/drnalanda/)
[![Stress Test](https://img.shields.io/badge/Stress_Test-3.0_Billion_Queries-10b981.svg)](https://www.polygonal.in/whitepapers/Dr_Nalanda_3B_Query_Medical_CDSS_Certification_Dossier.pdf)
[![Hallucination Rate](https://img.shields.io/badge/Hallucination_Drift-0.000000%25-emerald.svg)](https://www.polygonal.in/ASI/drnalanda/)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)

**Dr. Nalanda, MD** is the world's first **Deterministic Clinical Decision Support System (CDSS)** powered by the **TernaryAI MoE Deterministic Engine**, developed by **Polygonal Research and Development Lab Private Limited** (Thrissur, Kerala, India).

Unlike standard large language models (LLMs) that rely on probabilistic sampling ($T > 0$)—which can introduce dangerous medical hallucinations and variable drug advice—Dr. Nalanda utilizes **closed-form invariant collision matrices** across **14 accredited clinical medical specialties** to deliver $100.0000\%$ deterministic concordance with zero hallucination drift.

---

## Key Features

- **Zero Hallucination Drift ($0.000000\%$):** Formally certified across 3.0 Billion Clinical Medicine Queries (and 1 Billion Omnisector & Adversarial cases).
- **Sub-Millisecond Inference:** Mean decision latency of $<0.20\text{ ms}$ at over $44,900\text{ QPS}$.
- **14 Specialized Clinical Sectors:**
  1. **Cardiology & Hemodynamics** (ICMR / ACC/AHA 2017)
  2. **Diabetology & Glycemic Control** (ADA Standards of Care / ICMR)
  3. **Nephrology & Renal Clearance** (KDIGO 2024 & Pediatric Schwartz eGFR)
  4. **Serum Electrolytes & Acid-Base** (Harrison's 21st Edition)
  5. **Lipidology & ASCVD Risk** (ACC/AHA 2018 Multisociety)
  6. **Hepatology & Hepatic Injury** (ACG Guidelines)
  7. **Hematology & Hemostasis** (WHO / ISTH Guidelines)
  8. **Pulmonology & O2 Saturation** (WHO / GOLD Guidelines)
  9. **Obstetrics & Teratology** (US FDA Category X/D Contraindications)
  10. **Pediatrics & Neonatal Dosing** (AAP Pediatric Guidelines)
  11. **Infectious Diseases & Vancomycin Stewardship** (IDSA Guidelines)
  12. **Oncology & TNM Staging** (AJCC 8th Edition / ASCO)
  13. **Emergency Neurology & Stroke** (AHA/ASA IV r-tPA Eligibility)
  14. **Psychiatry & Electrophysiology** (QTc Prolongation & Hunter Criteria)
- **4-Tier Adversarial Stress Ingestion:** Biological extremes & shock, real-world EHR OCR noise normalization, global SI units (mmol/L, umol/L), and cascading 12-drug polypharmacy contraindication audits ("Triple Whammy").

---

## Installation

```bash
pip install git+https://github.com/prdlabpvtltd/dr-nalanda-cdss-python.git
```

---

## Quickstart

```python
from dr_nalanda import DrNalandaClient, PatientCase

# Initialize client
client = DrNalandaClient()

# Formulate patient case with lab biomarkers and polypharmacy
patient = PatientCase(
    age=68,
    sex="male",
    sbp=148,
    dbp=92,
    cr=2.4,       # Serum Creatinine (mg/dL)
    k=5.4,        # Serum Potassium (mEq/L)
    medications=["Lisinopril", "Ibuprofen", "Spironolactone"],  # Critical interaction
    symptoms="Bilateral ankle swelling and lower back ache."
)

# Execute deterministic resolution
resolution = client.resolve(patient)

print(f"Status: {resolution.status}")
print(f"Computed in: {resolution.latency_ms:.2f} ms")
print(f"Hazards Detected: {resolution.hazards_count}")
print(resolution.markdown_report)
```

---

## Clinical Safety & Statutory Compliance

This software library connects to the research and sandbox APIs of Dr. Nalanda MD. In accordance with the **National Medical Commission (NMC) Telemedicine Practice Guidelines 2020** and international health software standards (**US FDA 21 CFR Part 11, ISO 13485, IEC 62304**), clinical recommendations must be validated by a registered medical practitioner.

---

## Corporate Attribution

Developed and maintained by:  
**Polygonal Research and Development Lab Private Limited**  
*Corporate Identity:* CIN `U72100KL2025PTC098477`  
*Headquarters:* Thrissur, Kerala – 680503, India  
*Live Portal:* [https://www.polygonal.in/ASI/drnalanda/](https://www.polygonal.in/ASI/drnalanda/)  
*Full Certification Dossier:* [Dr. Nalanda 3B Query CDSS Dossier (PDF)](https://www.polygonal.in/whitepapers/Dr_Nalanda_3B_Query_Medical_CDSS_Certification_Dossier.pdf)
