#!/usr/bin/env python3

import json
from pathlib import Path

PROJECT_ROOT = Path.home() / "zero-trust-strategic-planning"
MATURITY_REPORT = PROJECT_ROOT / "reports" / "zero_trust_maturity_report.json"
GAP_REPORT = PROJECT_ROOT / "reports" / "zero_trust_gap_analysis.json"
OUTPUT_FILE = PROJECT_ROOT / "reports" / "zero_trust_strategy_report.md"

maturity = json.loads(MATURITY_REPORT.read_text())
gaps = json.loads(GAP_REPORT.read_text())

lines = [
    "# Zero Trust Strategic Planning Report",
    "",
    f"Organization: {maturity['organization']}",
    f"Overall Maturity: {maturity['overall_maturity']}",
    f"Maturity Percentage: {maturity['maturity_percentage']}%",
    "",
    "## Asset Maturity Summary",
    "",
    "| Asset | Zone | Score | Maturity |",
    "|---|---|---:|---|"
]

for asset in maturity["asset_results"]:
    lines.append(f"| {asset['asset']} | {asset['zone']} | {asset['score']}/5 | {asset['maturity']} |")

lines.extend([
    "",
    "## Gap Analysis Summary",
    "",
    "| Asset | Risk Level | Gap Count |",
    "|---|---|---:|"
])

for item in gaps["summary"]:
    lines.append(f"| {item['asset']} | {item['risk_level']} | {item['gap_count']} |")

lines.extend(["", "## Remediation Plan", ""])

for finding in gaps["detailed_findings"]:
    lines.append(f"### {finding['asset']}")
    lines.append(f"- Current Maturity: {finding['maturity']}")
    lines.append(f"- Gaps Found: {finding['gap_count']}")

    if finding["gaps"]:
        for gap in finding["gaps"]:
            lines.append(f"- {gap['pillar']}: {gap['recommendation']}")
    else:
        lines.append("- No major gaps detected.")

    lines.append("")

OUTPUT_FILE.write_text("\n".join(lines))
print(OUTPUT_FILE)
print(OUTPUT_FILE.read_text())
