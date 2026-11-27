# Dr. Nalanda, MD — CDSS API & Parameter Reference

## `PatientCase` Schema

| Parameter | Type | Default | Description | Clinical Invariant Domain |
| :--- | :--- | :--- | :--- | :--- |
| `age` | `float` | `None` | Patient age in years | All sectors (Pediatric vs Adult thresholds) |
| `sex` | `str` | `"unknown"` | `'male'`, `'female'`, `'other'`, `'unknown'` | CKD-EPI eGFR, ASCVD, QTc limits |
| `pregnant` | `bool` | `False` | Pregnancy status | Obstetrics & Teratogenic Category X/D screening |
| `sbp` | `float` | `None` | Systolic Blood Pressure (mmHg) | Malignant crisis ($\ge 240$), Shock ($<80$) |
| `dbp` | `float` | `None` | Diastolic Blood Pressure (mmHg) | Malignant crisis ($\ge 140$), Pulse Pressure |
| `hr` | `float` | `None` | Heart Rate (bpm) | Tachyarrhythmias, Bradycardia |
| `spo2` | `float` | `None` | Oxygen Saturation (%) | Critical Hypoxia ($<85\%$), GOLD guidelines |
| `cr` | `float` | `None` | Serum Creatinine | CKD-EPI 2021 & Schwartz Pediatric eGFR |
| `cr_unit` | `str` | `"mg/dL"` | `"mg/dL"` or `"umol/L"` | Automatic SI unit normalization |
| `k` | `float` | `None` | Serum Potassium ($K^+$ in mEq/L) | Lethal Hyperkalemia ($\ge 6.5$), Hypokalemia ($<2.5$) |
| `fpg` | `float` | `None` | Fasting Plasma Glucose | DKA/HHS ($\ge 600	ext{ mg/dL}$), Hypoglycemia ($<70$) |
| `fpg_unit` | `str` | `"mg/dL"` | `"mg/dL"` or `"mmol/L"` | Automatic SI unit normalization |
| `hba1c` | `float` | `None` | Glycated Hemoglobin (%) | ADA Glycemic Targets ($\ge 6.5\%$ Diabetes) |
| `ldl` | `float` | `None` | LDL Cholesterol (mg/dL) | ACC/AHA Extreme Risk ($\ge 190	ext{ mg/dL}$) |
| `alt` | `float` | `None` | Alanine Aminotransferase (U/L) | Acute Transaminitis ($>3	imes	ext{ ULN}$) |
| `ast` | `float` | `None` | Aspartate Aminotransferase (U/L) | Hepatic Necrosis, De Ritis Ratio |
| `hemoglobin`| `float` | `None` | Hemoglobin (g/dL) | Severe Anemia ($<7.0	ext{ g/dL}$) |
| `platelets` | `float` | `None` | Platelet Count ($	imes 10^3/\mu	ext{L}$) | Severe Thrombocytopenia ($<50	imes 10^3$) |
| `vancomycin`| `float` | `None` | Serum Trough Level ($\mu	ext{g/mL}$) | IDSA Nephrotoxicity Ceiling ($>20\mu	ext{g/mL}$) |
| `qtc` | `float` | `None` | Corrected QT Interval (ms) | Torsades de Pointes hazard ($>500	ext{ ms}$) |
| `height_cm` | `float` | `None` | Patient height (cm) | Required for Bedside Schwartz Pediatric eGFR |
| `weight_kg` | `float` | `None` | Patient weight (kg) | Pediatric weight-based dosing calculations |
| `medications`| `List[str]`| `[]` | List of concurrent medications | 12-Drug Polypharmacy & "Triple Whammy" |
| `symptoms` | `str` | `""` | Free-text clinical narrative | Evaluated via Deterministic EHR parser |
| `chest_pain`| `bool` | `False` | Acute chest discomfort | Tier 0 Red Flag: Emergent ACS / MI workup |
| `stroke_signs`| `bool` | `False`| Acute facial droop / arm drift | Tier 0 Red Flag: F.A.S.T. / Emergent r-tPA window |
| `bypass_disclaimer_confirmed` | `bool` | `True` | Statutory terms confirmation | Mandatory NMC Telemedicine compliance |

---

## `ClinicalResolution` Return Object

```python
resolution = client.resolve(patient)
```

- `resolution.status`: Execution status (`"success"` or error state).
- `resolution.latency_ms`: Invariant resolution latency in milliseconds ($<0.4	ext{ ms}$).
- `resolution.tier0_emergency`: Boolean flag for immediate life threats.
- `resolution.emergency_alerts`: Array of urgent triage alert strings.
- `resolution.hazards_count`: Total clinical counter-indications detected.
- `resolution.red_flags_count`: Immediate red-flag biological invariants.
- `resolution.doctor_persona`: Statutory doctor identity declaration.
- `resolution.statutory_citations`: List of accredited guidelines referenced.
- `resolution.markdown_report`: Complete, formatted clinical report.
