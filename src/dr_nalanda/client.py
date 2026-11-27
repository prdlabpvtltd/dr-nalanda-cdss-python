import json
import urllib.request
import urllib.error
from typing import Dict, Any, Optional

from .models import PatientCase, ClinicalResolution
from .exceptions import APIConnectionError, DisclaimerRequiredError, DrNalandaError

DEFAULT_BASE_URL = "https://www.polygonal.in/api/drnalanda"

class DrNalandaClient:
    """
    Official Python Client for Dr. Nalanda, MD (Clinical Decision Support System).
    Powered by the TernaryAI MoE Deterministic Engine.
    """
    def __init__(self, base_url: str = DEFAULT_BASE_URL, timeout: int = 10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def check_health(self) -> Dict[str, Any]:
        """Verify API operational health."""
        url = f"{self.base_url}/health"
        req = urllib.request.Request(url, headers={"User-Agent": "DrNalanda-PythonSDK/0.1.0"})
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except Exception as e:
            raise APIConnectionError(f"Health check failed for {url}: {e}")

    def resolve(self, patient: PatientCase) -> ClinicalResolution:
        """
        Execute deterministic clinical decision resolution for the given patient case.
        Evaluates 14 accredited clinical specialty invariants with zero hallucination drift.
        """
        if not patient.bypass_disclaimer_confirmed:
            raise DisclaimerRequiredError("Mandatory statutory disclaimer must be confirmed.")

        url = f"{self.base_url}/resolve"
        payload = json.dumps(patient.to_dict()).encode("utf-8")
        req = urllib.request.Request(
            url,
            data=payload,
            headers={
                "Content-Type": "application/json",
                "User-Agent": "DrNalanda-PythonSDK/0.1.0"
            },
            method="POST"
        )
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                data = json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="ignore")
            raise DrNalandaError(f"HTTP {e.code} Error: {body}")
        except Exception as e:
            raise APIConnectionError(f"Failed to communicate with Dr. Nalanda API: {e}")

        return ClinicalResolution(
            status=data.get("status", "unknown"),
            latency_ms=data.get("latency_ms", 0.0),
            tier0_emergency=data.get("tier0_emergency", False),
            emergency_alerts=data.get("emergency_alerts", []),
            findings_count=data.get("findings_count", 0),
            hazards_count=data.get("hazards_count", 0),
            red_flags_count=data.get("red_flags_count", 0),
            doctor_persona=data.get("doctor_persona", ""),
            statutory_citations=data.get("statutory_citations", []),
            markdown_report=data.get("markdown_report", ""),
            raw_response=data
        )
