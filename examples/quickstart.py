from dr_nalanda import DrNalandaClient, PatientCase

client = DrNalandaClient()

# Example: Elderly patient with CKD and Polypharmacy
patient = PatientCase(
    age=68,
    sex="male",
    sbp=148,
    dbp=92,
    cr=2.4,       # Elevated Serum Creatinine
    k=5.4,        # Borderline Hyperkalemia
    medications=["Lisinopril", "Ibuprofen", "Spironolactone"], # "Triple Whammy" hazard
    symptoms="Bilateral lower extremity edema, chronic low back discomfort."
)

resolution = client.resolve(patient)

print(f"Status: {resolution.status} (Computed in {resolution.latency_ms:.2f} ms)")
print(f"Emergency Tier 0: {resolution.tier0_emergency}")
print(f"Identified Hazards: {resolution.hazards_count}")
print(f"Red Flags: {resolution.red_flags_count}")
print("\n--- Clinical Report Summary ---")
print(resolution.markdown_report[:400] + "...")
