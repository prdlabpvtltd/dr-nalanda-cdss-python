_D=b'RHJOYWxhbmRhLVB5dGhvblNESy8wLjEuMA=='
_C=b'VXNlci1BZ2VudA=='
_B='utf-8'
_A='base64'
import json,urllib.request,urllib.error
from typing import Dict,Any,Optional
from.models import PatientCase,ClinicalResolution
from.exceptions import APIConnectionError,DisclaimerRequiredError,DrNalandaError
DEFAULT_BASE_URL=__import__(_A).b64decode(b'aHR0cHM6Ly93d3cucG9seWdvbmFsLmluL2FwaS9kcm5hbGFuZGE=').decode()
class DrNalandaClient:
	def __init__(self,base_url=DEFAULT_BASE_URL,timeout=10):self.base_url=base_url.rstrip('/');self.timeout=timeout
	def check_health(self):
		A=f"{self.base_url}/health";B=urllib.request.Request(A,headers={__import__(_A).b64decode(_C).decode():__import__(_A).b64decode(_D).decode()})
		try:
			with urllib.request.urlopen(B,timeout=self.timeout)as C:return json.loads(C.read().decode(_B))
		except Exception as D:raise APIConnectionError(f"Health check failed for {A}: {D}")
	def resolve(self,patient):
		if not patient.bypass_disclaimer_confirmed:raise DisclaimerRequiredError('Mandatory statutory disclaimer must be confirmed.')
		C=f"{self.base_url}/resolve";D=json.dumps(patient.to_dict()).encode(_B);E=urllib.request.Request(C,data=D,headers={__import__(_A).b64decode(b'Q29udGVudC1UeXBl').decode():__import__(_A).b64decode(b'YXBwbGljYXRpb24vanNvbg==').decode(),__import__(_A).b64decode(_C).decode():__import__(_A).b64decode(_D).decode()},method='POST')
		try:
			with urllib.request.urlopen(E,timeout=self.timeout)as F:A=json.loads(F.read().decode(_B))
		except urllib.error.HTTPError as B:G=B.read().decode(_B,errors='ignore');raise DrNalandaError(f"HTTP {B.code} Error: {G}")
		except Exception as B:raise APIConnectionError(f"Failed to communicate with Dr. Nalanda API: {B}")
		return ClinicalResolution(status=A.get('status','unknown'),latency_ms=A.get('latency_ms',.0),tier0_emergency=A.get('tier0_emergency',False),emergency_alerts=A.get('emergency_alerts',[]),findings_count=A.get('findings_count',0),hazards_count=A.get('hazards_count',0),red_flags_count=A.get('red_flags_count',0),doctor_persona=A.get('doctor_persona',''),statutory_citations=A.get('statutory_citations',[]),markdown_report=A.get('markdown_report',''),raw_response=A)