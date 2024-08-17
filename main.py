import os
import json
from datetime import datetime

# Directory to store patient data
DATA_DIR = "data"

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def save_patient_record(patient_id, record):
    file_path = os.path.join(DATA_DIR, f"{patient_id}.json")
    with open(file_path, "w") as file:
        json.dump(record, file)

def load_patient_record(patient_id):
    file_path = os.path.join(DATA_DIR, f"{patient_id}.json")
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    return None

def main():
    while True:
        print("\n--- Automatic Health Monitoring System ---")
        patient_id = input("Enter Patient ID: ")
        existing_record = load_patient_record(patient_id)

        if existing_record:
            print("\nExisting Record Found:")
            print(json.dumps(existing_record, indent=4))
            print("No need for repetitive diagnosis!")
        else:
            print("\nNo record found. Please input new diagnosis data.")
            diagnosis = input("Enter Diagnosis: ")
            doctor = input("Enter Doctor's Name: ")

            record = {
                "patient_id": patient_id,
                "diagnosis": diagnosis,
                "doctor": doctor,
                "date": str(datetime.now())
            }

            save_patient_record(patient_id, record)
            print("Record saved successfully.")

        cont = input("Do you want to continue? (y/n): ")
        if cont.lower() != 'y':
            break

if __name__ == "__main__":
    main()
