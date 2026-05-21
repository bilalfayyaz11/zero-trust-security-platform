#!/usr/bin/env python3

import json
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path.home() / "zero-trust-strategic-planning"
INPUT_REPORT = PROJECT_ROOT / "reports" / "zero_trust_maturity_report.json"
OUTPUT_REPORT = PROJECT_ROOT / "reports" / "zero_trust_gap_analysis.json"

REMEDIATIONS = {
    "least_privilege": "Implement role-based access control and least privilege policies.",
    "micro_segmentation": "Segment sensitive systems into isolated security zones.",
    "continuous_authentication": "Deploy MFA and conditional access validation.",
    "encryption": "Encrypt sensitive data both in transit and at rest.",
    "policy_enforcement": "Deploy automated policy enforcement using proxies, firewalls, and centralized identity systems."
}

def risk_level(gap_count):
    if gap_count >= 4:
        return "High"
    if gap_count >= 2:
        return "Medium"
    if gap_count == 1:
        return "Low"
    return "Minimal"

report = json.loads(INPUT_REPORT.read_text())

findings = []
summary = []

for asset in report["asset_results"]:
    gaps = []
    for pillar, implemented in asset["scorecard"].items():
        if not implemented:
            gaps.append({
                "pillar": pillar,
                "recommendation": REMEDIATIONS[pillar]
            })

    findings.append({
        "asset": asset["asset"],
        "maturity": asset["maturity"],
        "gap_count": len(gaps),
        "gaps": gaps
    })

    summary.append({
        "asset": asset["asset"],
        "maturity": asset["maturity"],
        "risk_level": risk_level(len(gaps)),
        "gap_count": len(gaps)
    })

output = {
    "generated_at": datetime.utcnow().isoformat() + "Z",
    "organization": report["organization"],
    "overall_maturity": report["overall_maturity"],
    "summary": summary,
    "detailed_findings": findings
}

OUTPUT_REPORT.write_text(json.dumps(output, indent=2))
print(json.dumps(output, indent=2))
