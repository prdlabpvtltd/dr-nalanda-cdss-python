from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any

@dataclass
class StatutoryDisclaimer:
    acknowledged: bool = True
    disclaimer_text: str = (
        "Clinical sandbox & educational reference only. Under NMC Telemedicine Practice "
        "Guidelines 2020 and global clinical protocols, deterministic CDSS outputs must be "
        "reviewed by a licensed medical practitioner."
    )

@dataclass
class PatientCase:
    age: Optional[float] = None
    sex: str = "unknown"  # 'male', 'female', 'other', 'unknown'
    pregnant: bool = False
    
    # Hemodynamics & Vitals
    sbp: Optional[float] = None
    dbp: Optional[float] = None
    hr: Optional[float] = None
    spo2: Optional[float] = None
    
    # Renal & Metabolic Panel
    cr: Optional[float] = None
    cr_unit: str = "mg/dL"
    k: Optional[float] = None
    fpg: Optional[float] = None
    fpg_unit: str = "mg/dL"
    hba1c: Optional[float] = None
    ldl: Optional[float] = None
    
    # Hepatic & Hematology
    alt: Optional[float] = None
    ast: Optional[float] = None
    hemoglobin: Optional[float] = None
    platelets: Optional[float] = None
    
    # Specialty Invariants
    vancomycin: Optional[float] = None
    qtc: Optional[float] = None
    height_cm: Optional[float] = None
    weight_kg: Optional[float] = None
    
    # Qualitative & Medication History
    medications: List[str] = field(default_factory=list)
    symptoms: str = ""
    chest_pain: bool = False
    stroke_signs: bool = False
    
    # Statutory Acceptance
    bypass_disclaimer_confirmed: bool = True

    def to_dict(self) -> Dict[str, Any]:
        return {
            "age": self.age,
            "sex": self.sex,
            "pregnant": self.pregnant,
            "sbp": self.sbp,
            "dbp": self.dbp,
            "hr": self.hr,
            "spo2": self.spo2,
            "cr": self.cr,
            "cr_unit": self.cr_unit,
            "k": self.k,
            "fpg": self.fpg,
            "fpg_unit": self.fpg_unit,
            "hba1c": self.hba1c,
            "ldl": self.ldl,
            "alt": self.alt,
            "ast": self.ast,
            "hemoglobin": self.hemoglobin,
            "platelets": self.platelets,
            "vancomycin": self.vancomycin,
            "qtc": self.qtc,
            "height_cm": self.height_cm,
            "weight_kg": self.weight_kg,
            "medications": self.medications,
            "symptoms": self.symptoms,
            "chest_pain": self.chest_pain,
            "stroke_signs": self.stroke_signs,
            "bypass_disclaimer_confirmed": self.bypass_disclaimer_confirmed
        }

@dataclass
class ClinicalFinding:
    sector: str
    severity: str  # 'EMERGENCY', 'CRITICAL', 'WARNING', 'OPTIMAL'
    invariant: str
    citation: str

@dataclass
class ClinicalResolution:
    status: str
    latency_ms: float
    tier0_emergency: bool
    emergency_alerts: List[str]
    findings_count: int
    hazards_count: int
    red_flags_count: int
    doctor_persona: str
    statutory_citations: List[str]
    markdown_report: str
    raw_response: Dict[str, Any]
