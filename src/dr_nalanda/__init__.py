"""
Dr. Nalanda, MD — Deterministic Medical Clinical Decision Support System (CDSS) Python SDK
Powered by Polygonal R&D Lab's TernaryAI MoE Deterministic Engine.
"""

from .client import DrNalandaClient
from .models import PatientCase, ClinicalResolution, ClinicalFinding, StatutoryDisclaimer
from .exceptions import DrNalandaError, APIConnectionError, DisclaimerRequiredError

__version__ = "0.1.0"
__all__ = [
    "DrNalandaClient",
    "PatientCase",
    "ClinicalResolution",
    "ClinicalFinding",
    "StatutoryDisclaimer",
    "DrNalandaError",
    "APIConnectionError",
    "DisclaimerRequiredError",
]
