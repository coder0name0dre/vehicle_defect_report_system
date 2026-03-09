# HGV Vehicle Pre Check Automation System

This script is a Python based command line vehicle inspection system designed to digitise daily HGV walkaround checks.

This project simulates a real world fleet compliance tool used in HGV transport operations.

---

## Overview

This script allows drivers to:

- Complete a structured daily vehicle inspection
- Record critical and minor defects
- Enter defect notes immediately when issues are found
- Navigate back to previous questions during inspection (`b` to go back)
- Log mileage
- Apply a digital signature
- Automatically generate a unique inspection ID
- Store all inspections in a structured folder system
- Append inspections to a master CSV file per vehicle

All inspections records are stored in:

reports/<VEHICLE_REG>/vehicle_defect_report.csv

---

## Features

### Input Validation

- Only accepts `y`, `n`, or `b`
- Prevents invalid entries
- Allows back navigation during inspection

### Immediate Defect Logging

- When a defect is detected, the user is prompted to enter notes in regards to the defect
- If the user goes back and changes their answer, the defect is removed automatically

### Inspection Metadata

Each inspection logs:

- Inspection ID (UUID-based)
- Date & Time (dd/mm/yyyy hh:mm:ss format)
- Driver name
- Vehicle registration
- Mileage
- Defect type (Critical / Minor)
- Defect description
- Defect notes
- Digital signature

---

## Requirements

- Python 3
- `os` module (folder management)
- `csv` module (data storage)
- `uuid` module (unique ID generation)
- `datetime` module (timestamp formatting)

No extenal libraries required.

---

## How To Run (macOS / Linux)

1. Clone the repository:

```
git clone https://github.com/coder0name0dre/vehicle_defect_report_system.git
cd vehicle_defect_report_system
```

2. Run the script:

```
python3 vehicle_inspection.py
```

---

## Example Folder Structure

project/
│
├── vehicle_inspection.py
├── README.md
│
└── reports/
    └── <VEHICLE_REG>/
        └── vehicle_defect_report.csv

---

## Author

Andre Pinnock

**HGV Driver | Self-taught Python Automation Developer**

---

## License

This project is licensed under the [MIT License](https://github.com/coder0name0dre/vehicle_defect_report_system/blob/main/LICENSE).