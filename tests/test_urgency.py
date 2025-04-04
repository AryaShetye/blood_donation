test_patients = [
    Patient(301, "Tom", 90, 120, 98, 30, "O+", "HealthPoint"),  # healthy
    Patient(302, "Jerry", 55, 80, 92, 65, "A-", "CityCare"),    # mid urgency
    Patient(303, "Spike", 40, 60, 70, 85, "B-", "MetroHosp"),   # high urgency
    Patient(304, "Tiny", 100, 200, 99, 15, "O-", "YouthHosp"),  # young but hypertensive
    Patient(305, "OldJoe", 85, 100, 85, 99, "AB+", "OldAgeHosp") # very old, semi-critical
]

# Manually compute expected scores if needed
