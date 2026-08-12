#!/usr/bin/env python3
"""Data-integrity validation for the data-analysis-projects portfolio repo.

Run from the repo root:  python3 scripts/validate_data.py

Fails (non-zero exit) on any broken dataset or missing README-referenced
deliverable, so it can gate CI.
"""

import ast
import csv
import glob
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FAILURES = []


def fail(msg):
    FAILURES.append(msg)
    print(f"FAIL: {msg}")


def check_csv(path):
    with open(path, newline="", encoding="utf-8", errors="replace") as fh:
        rows = list(csv.reader(fh))
    if not rows:
        fail(f"{path}: empty CSV")
        return
    widths = {len(r) for r in rows}
    if len(widths) > 1:
        fail(f"{path}: inconsistent column counts -> {sorted(widths)}")
    else:
        print(f"OK: {path} ({len(rows) - 1} data rows, {len(rows[0])} columns)")


def main():
    # 1. Every CSV parses and has consistent columns per file.
    for path in sorted(glob.glob(os.path.join(ROOT, "**", "*.csv"), recursive=True)):
        check_csv(path)

    # 2. Key deliverables referenced by the README exist.
    required = [
        "Python/Customer Segregation/RFM Analysis/RFM_Analysis.ipynb",
        "Python/Customer Segregation/RFM Analysis/RFM_Analysis.py",
        "Python/Customer Segregation/RFM Analysis/Clusters.PNG",
        "Python/Auto Insurance Analysis/AutoInsuranceAnalysis.ipynb",
        "Python/Indian_Air_Quality_Analysis/Indian_Air_Quality_Analysis.ipynb",
        "SQL/AmaSale.sql",
        "SQL/datasets/amazon_sales_data 2025.csv",
        "PowerBI/SuperStoreSalesAnalysis/SalesAnalysis.pbix",
        "PowerBI/SuperStoreSalesAnalysis/AnalysisWriteup.md",
        "Excel/coffee-sales/coffeeOrdersData.xlsx",
        "Excel/coffee-sales/coffeeOrdersDashboard.xlsx",
    ]
    for rel in required:
        if not os.path.exists(os.path.join(ROOT, rel)):
            fail(f"missing README-referenced file: {rel}")

    # 3. Python sources parse (syntax check, no bytecode written).
    for path in sorted(glob.glob(os.path.join(ROOT, "**", "*.py"), recursive=True)):
        try:
            ast.parse(open(path, encoding="utf-8", errors="replace").read())
        except SyntaxError as exc:
            fail(f"{path}: {exc}")

    if FAILURES:
        print(f"\n{len(FAILURES)} failure(s)")
        sys.exit(1)
    print("\nAll data-integrity checks passed.")


if __name__ == "__main__":
    main()
