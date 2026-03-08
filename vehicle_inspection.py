import os
import csv
import uuid
from datetime import datetime


# Current Date & Time #

now = datetime.now()
current_datetime = now.strftime("%d/%m/%Y %H:%M:%S")


# Generate Unique Inspection ID #

# create a random unique ID, shortened to 8 characters
inspection_id = str(uuid.uuid4())[:8]


# Driver & Vehicle Details #

print("\n*** Daily Vehicle Inspection ***\n")

driver_name = input("Enter driver name: ").title()
vehicle_reg = input("Enter vehicle registration: ").upper()
mileage = input("Enter current vehicle mileage: ")

# digital signature (typed confirmation)
signature = input("Type your full name as digital signature: ").title()


# Pre Check Defect Questions #

# questions where answering "y" means DEFECT
yes_means_defect = [
    "Are there any deep cuts or sidewall damage to they tyres?",
    "Are there any obvious air leaks?",
    "Any warning lights on dashboard?"
]

questions = [
    ("Do all instruments, gauges, and warning devices work?", "critical"),
    ("Are all mirrors (including camera systems) and windows clean and adjusted correctly?", "minor"),
    ("Do the wipers and washers work properly?", "minor"),
    ("Does the horn work and is it easily reachable?", "minor"),
    ("Does the parking brake work properly?", "critical"),
    ("Is the correct vehicle height indicator displayed in the cab?", "minor"),
    ("Is the tachograph calibrated and the card inserted correctly?", "minor"),
    ("Is the seatbelt in good condition and secure?", "critical"),
    ("Are brakes functioning correctly?", "critical"),
    ("Are lights working?", "minor"),
    ("Are all wheel nut indicators fitted correctly?", "critical"),
    ("Are mudguards securely attached?", "minor"),
    ("Is there number plate clean and visible?", "minor"),
    ("Does the steering wheel operate properly without excessive play or jamming?", "critical"),
    ("Are there any deep cuts or sidewall damage to they tyres?", "critical"),
    ("Are there any obvious air leaks?", "critical"),
    ("Any warning lights on dashboard?", "critical")
]

# We store defects in a dictionary using question index
defects = {}

index = 0


# Question Loop #

while index < len(questions):

    question, severity = questions[index]

    user_input = input(f"{question} (y/n) or 'b' to go back: ").lower()

    # Validate input
    if user_input not in ["y", "n", "b"]:
        print("Please enter only 'y', 'n', or 'b'.\n")
        continue

    # Handle back function
    if user_input == "b":
        if index > 0:
            index -= 1
        else:
            print("Already at first question.\n")
        continue

    # Remove previous defect if it existed (user changed answer)
    if index in defects:
        del defects[index]

    # Determine if defect exists
    defect_found = False

    if question in yes_means_defect:
        if user_input == "y":
            defect_found = True
    else:
        if user_input == "n":
            defect_found = True

    # Ask for notes IMMEDIATELY if defect detected
    if defect_found:
        note = input("Enter defect notes/details: ")
        defects[index] = (question, severity, note)

    index += 1


# Seperate Defect Types #

critical_defects = []
minor_defects = []

for question, severity, note in defects.values():
    if severity == "critical":
        critical_defects.append((question, note))
    else:
        minor_defects.append((question, note))


# Create Folder Structure #

base_folder = "reports"
vehicle_folder = os.path.join(base_folder, vehicle_reg)

# create main reports folder if it doesn't exist
if not os.path.exists(base_folder):
    os.mkdir(base_folder)

# create vehicle specific folder if it doesn't exist
if not os.path.exists(vehicle_folder):
    os.mkdir(vehicle_folder)

# one master file per vehicle
file_path = os.path.join(vehicle_folder, "vehicle_defect_report.csv")

# check if file already exists
file_exists = os.path.isfile(file_path)


# Append Data To Master CSV #

with open(file_path, mode="a", newline="") as file:

    writer = csv.writer(file)

    # if file doesn't exist yet, write header first
    if not file_exists:
        writer.writerow([
            "Inspection ID",
            "Date/Time",
            "Driver Name",
            "Vehicle Registration",
            "Mileage",
            "Defect Type",
            "Defect Description",
            "Defect Notes",
            "Digital Signature"
        ])

    # if no defects found
    if not defects:
        writer.writerow([
            inspection_id,
            current_datetime,
            driver_name,
            vehicle_reg,
            mileage,
            "None",
            "No defects found",
            "",
            signature
        ])

    for question, severity, note in defects.values():
        writer.writerow([
            inspection_id,
            current_datetime,
            driver_name,
            vehicle_reg,
            mileage,
            severity.upper(),
            question,
            note,
            signature
        ])


# Display inspection ID and where where file has been saved to
print("\nInspection complete.")
print(f"Inspection ID: {inspection_id}")
print(f"Saved to: {file_path}\n")