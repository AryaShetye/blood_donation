# def add_donor(self, donor):
#     self.map[donor["DonorID"]] = {
#         "Name": donor["Name"],
#         "BloodType": donor["BloodType"],
#         "LastDonation": donor["LastDonation"],
#         "HealthFlags": donor.get("HealthFlags", []),
#         "TimesDonated": donor.get("TimesDonated", 0)
#     }

# def get_donor(self, donor_id):
#     return self.map.get(donor_id, None)

# def update_donation(self, donor_id, new_date):
#     if donor_id in self.map:
#         self.map[donor_id]["LastDonation"] = new_date
#         self.map[donor_id]["TimesDonated"] += 1

# def is_eligible(self, donor_id):
#     donor = self.get_donor(donor_id)
#     if not donor:
#         return False
#     if "Recent Surgery" in donor["HealthFlags"] or "Anemia" in donor["HealthFlags"]:
#         return False
#     # Simple 90-day check for now (expandable)
#     from datetime import datetime
#     try:
#         last = datetime.strptime(donor["LastDonation"], "%Y-%m-%d")
#         days_since = (datetime.now() - last).days
#         return days_since >= 90
#     except:
#         return False
    
# def add_blood(self, blood_type, units):
#     self.inventory[blood_type] = self.inventory.get(blood_type, 0) + units

# def use_blood(self, blood_type):
#     if self.inventory.get(blood_type, 0) > 0:
#         self.inventory[blood_type] -= 1
#         return True
#     return False

# def check_availability(self, blood_type):
#     return self.inventory.get(blood_type, 0) > 0

