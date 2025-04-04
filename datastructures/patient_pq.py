import heapq

class Patient:
    def __init__(self, id, name, blood_type_needed, urgency_score, hospital):
        self.id = id
        self.name = name
        self.blood_type_needed = blood_type_needed
        self.urgency_score = urgency_score
        self.hospital = hospital

    def __lt__(self, other):
        return self.urgency_score > other.urgency_score  # Max heap

class PatientQueue:
    def __init__(self):
        self.heap = []

    def enqueue(self, patient, urgency):
        p = Patient(patient["PatientID"], patient.get("Name", "Unnamed"), patient["BloodTypeNeeded"], urgency, patient["Hospital"])
        heapq.heappush(self.heap, p)

    def dequeue(self):
        if self.heap:
            return heapq.heappop(self.heap)
        return None

    def peek(self):
        return self.heap[0] if self.heap else None

    def is_empty(self):
        return len(self.heap) == 0

    def get_all(self):
        return [vars(p) for p in sorted(self.heap, reverse=True)]