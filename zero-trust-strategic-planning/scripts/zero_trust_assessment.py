#!/usr/bin/env python3

import json
from pathlib import Path
from datetime import datetime


PROJECT_ROOT = Path.home() / "zero-trust-strategic-planning"
DATA_FILE = PROJECT_ROOT / "data" / "infrastructure_inventory.json"
REPORT_FILE = PROJECT_ROOT / "reports" / "zero_trust_maturity_report.json"


ZERO_TRUST_PILLARS = {
    "least_privilege": "Least Privilege Access",
    "micro_segmentation": "Micro-Segmentation",
    "continuous_authentication": "Continuous Authentication",
    "encryption": "Encryption",
    "policy_enforcement": "Policy Enforcement"
}


def load_inventory():
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def score_asset(asset):
    controls = set(asset.get("controls", []))
    authentication = set(asset.get("authentication", []))
    encryption = set(asset.get("encryption", []))

    scorecard = {
        "least_privilege": "least_privilege" in controls,
        "micro_segmentation": "network_segmentation" in controls,
        "continuous_authentication": "mfa" in authentication or "conditional_access" in authentication,
        "encryption": bool({"tls_in_transit", "encryption_at_rest", "disk_encryption"} & encryption),
        "policy_enforcement": bool({"policy_enforcement", "reverse_proxy", "waf"} & controls)
    }

    score = sum(scorecard.values())

    if score <= 2:
        maturity = "Initial"
    elif score == 3:
        maturity = "Defined"
    elif score == 4:
        maturity = "Managed"
    else:
        maturity = "Optimized"

    return {
        "asset": asset["name"],
        "type": asset["type"],
        "zone": asset["zone"],
        "score": score,
        "maturity": maturity,
        "scorecard": scorecard
    }


def main():
    inventory = load_inventory()
    results = [score_asset(asset) for asset in inventory["assets"]]

    total_score = sum(item["score"] for item in results)
    max_score = len(results) * len(ZERO_TRUST_PILLARS)
    maturity_percentage = round((total_score / max_score) * 100, 2)

    if maturity_percentage < 40:
        overall_maturity = "Initial"
    elif maturity_percentage < 60:
        overall_maturity = "Defined"
    elif maturity_percentage < 80:
        overall_maturity = "Managed"
    else:
        overall_maturity = "Optimized"

    report = {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "organization": inventory["organization"],
        "overall_maturity": overall_maturity,
        "maturity_percentage": maturity_percentage,
        "total_score": total_score,
        "max_score": max_score,
        "pillar_reference": ZERO_TRUST_PILLARS,
        "asset_results": results
    }

    REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(REPORT_FILE, "w") as file:
        json.dump(report, file, indent=2)

    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
