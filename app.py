from flask import Flask
from datastructures.donor_bst import Donor, DonorBST
from datastructures.blood_bst import BloodBST
from datastructures.hashmap import DonorHistoryMap
from datastructures.patient_pq import PatientQueue
from services.matchmaker import match_patient
from services.urgency import calculate_urgency

app = Flask(__name__)

donor_bst = DonorBST()
blood_bst = BloodBST()
history_map = DonorHistoryMap()
patient_queue = PatientQueue()

while True:
    print("\n=== Blood Management Console ===")
    print("1. Add Donor")
    print("2. Add Patient")
    print("3. Match Blood for Patient")
    print("4. View Queue")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        donor_id = input("Donor ID: ")
        name = input("Name: ")
        blood_type = input("Blood Type (A+/O-/etc): ")
        last_donation = input("Last Donation Date (YYYY-MM-DD): ")
        location = input("Location/Pincode: ")

        donation_count = int(input("Number of past donations: "))
        input_str = input("Health Flags (comma separated, leave blank if none): ")
        health_flags = input_str.split(",") if input_str else []

        donor = Donor(donor_id, name, blood_type, last_donation, location, donation_count, 1)
        donor_bst.insert(donor)
        history_map.add_donor(donor_id, last_donation, health_flags, donation_count)

        print("\u2705 Donor added successfully!")

    elif choice == '2':
        heart_rate = int(input("Heart Rate: "))
        bp = int(input("Blood Pressure: "))
        oxygen = int(input("Oxygen Level: "))
        age = int(input("Age: "))

        urgency = calculate_urgency(age, heart_rate, bp, oxygen)

        patient = {
            "PatientID": input("Patient ID: "),
            "Name": input("Name: "),
            "BloodTypeNeeded": input("Required Blood Type: "),
            "Age": age,
            "HeartRate": heart_rate,
            "BloodPressure": bp,
            "OxygenLevel": oxygen,
            "Hospital": input("Hospital Name: "),
        }

        patient_queue.enqueue(patient, urgency)
        print(f"\u2705 Patient added with urgency score {urgency}")

    elif choice == '3':
        if patient_queue.is_empty():
            print("No patients in queue.")
            continue
        patient_obj = patient_queue.peek()
        print(f"Trying to match donor for patient: {patient_obj.id} ...")
        # patient_dict = vars(patient_obj)
        matched = match_patient(patient_obj, blood_bst, donor_bst, history_map)
        if "Donor" in matched:
            patient_queue.dequeue()
            print(f"Blood matched! {matched}")
        else:
            print(f"{matched}")

    elif choice == '4':
        print("Current patient queue (in order):")
        for p in patient_queue.get_all():
            urgency = p['urgency_score']
            print(f"- {p['id']} (Urgency: {urgency})")

    elif choice == '5':
        print(" Exiting. Thank you!")
        break

    else:
        print(" Invalid choice. Try again.")
