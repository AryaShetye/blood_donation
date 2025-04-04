class DonorHistoryMap:
    def __init__(self):
        self.donor_map = {}  # Key: donor_id

    def add_donor(self, donor_id, last_donation, health_flags, donation_count):
        self.donor_map[donor_id] = {
            "last_donation": last_donation,
            "health_flags": health_flags,
            "donation_count": donation_count
        }

    def is_eligible(self, donor_id):
        donor = self.donor_map.get(donor_id)
        if not donor:
            return False
        from datetime import datetime
        days = (datetime.now() - datetime.strptime(donor['last_donation'], "%Y-%m-%d")).days
        if days < 90:
            return False
        if "Anemia" in donor['health_flags'] or donor['donation_count'] >= 6:
            return False
        return True
