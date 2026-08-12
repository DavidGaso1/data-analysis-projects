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
import re
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


def normalize(name):
    return name.lower().replace("_", "").replace(" ", "").replace('-', '')


def check_sql_csv_alignment():
    """Ensure the Amazon SQL table columns match the source CSV header."""
    sql_path = os.path.join(ROOT, "SQL", "AmaSale.sql")
    csv_path = os.path.join(ROOT, "SQL", "datasets", "amazon_sales_data 2025.csv")
    if not (os.path.exists(sql_path) and os.path.exists(csv_path)):
        fail("SQL/CSV alignment check skipped: file(s) missing")
        return

    sql = open(sql_path, encoding="utf-8", errors="replace").read()
    create = sql.find("CREATE TABLE")
    if create == -1:
        fail(f"{sql_path}: no CREATE TABLE found")
        return
    # Skip the table name itself (also quoted), then collect quoted columns.
    after_name = sql.find('"', sql.find('"', create) + 1)
    table_block = sql[after_name : sql.find(";", after_name)]
    sql_cols = re.findall(r'"([A-Za-z_]+)"', table_block)
    if not sql_cols:
        fail(f"{sql_path}: no quoted columns found in CREATE TABLE")
        return

    with open(csv_path, newline="", encoding="utf-8", errors="replace") as fh:
        csv_cols = next(csv.reader(fh))
    csv_norm = {normalize(c) for c in csv_cols}

    for col in sql_cols:
        if normalize(col) not in csv_norm:
            fail(f"{sql_path}: column {col!r} not found in CSV header")
    print(f"OK: {len(sql_cols)} SQL columns all present in CSV header")


def main():
    # 1. Every CSV parses and has consistent columns per file.
    for path in sorted(glob.glob(os.path.join(ROOT, "**", "*.csv"), recursive=True)):
        check_csv(path)

    # 1b. SQL table columns must align with the CSV they describe.
    check_sql_csv_alignment()

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
