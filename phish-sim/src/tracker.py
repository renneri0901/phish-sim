# tracker.py
# ----------------------------------------
# Parses phish_log.json and generates reports
# ----------------------------------------

import json
import csv

def generate_csv_report(json_path="../reports/phish_log.json", output="../reports/report.csv"):
    with open(json_path, "r") as f:
        lines = f.readlines()

    with open(output, "w", newline="") as csvfile:
        fieldnames = ["username", "password", "timestamp"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for line in lines:
            data = json.loads(line)
            writer.writerow(data)

    print("[+] Report generated at", output)
