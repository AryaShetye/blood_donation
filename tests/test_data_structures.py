donors = [
    Donor(1, "Alice", "A+", "2023-04-10", "Pune", 2, []),
    Donor(2, "Bob", "O-", "2022-01-20", "Mumbai", 5, ["HIV"]),
    Donor(3, "Charlie", "B+", "2023-08-15", "Delhi", 3, []),
]

patients = [
    Patient(1, "David", 85, 120, 98, 25, "B+", "CityCare"),
    Patient(2, "Eva", 60, 90, 85, 70, "A+", "Medico"),
]

queue = PriorityQueue()
queue.enqueue(patients[0], 75.5)
queue.enqueue(patients[1], 30.1)

# Expected: Eva (higher urgency) dequeued first


