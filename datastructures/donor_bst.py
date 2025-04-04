from datetime import datetime

class Donor:
    def __init__(self, donor_id, name, blood_type, last_donation, location, donation_count, demand_score):
        self.donor_id = donor_id
        self.name = name
        self.blood_type = blood_type
        self.last_donation = last_donation
        self.location = location
        self.donation_count = donation_count
        self.demand_score = demand_score

class BSTNode:
    def __init__(self, donor: Donor):
        self.donor = donor
        self.left = None
        self.right = None

class DonorBST:
    def __init__(self):
        self.root = None

    def insert(self, donor):
        def _insert(node, donor):
            if not node:
                return BSTNode(donor)

            score1 = self.get_priority_score(donor)
            score2 = self.get_priority_score(node.donor)

            if score1 < score2:
                node.left = _insert(node.left, donor)
            else:
                node.right = _insert(node.right, donor)
            return node

        self.root = _insert(self.root, donor)

    def get_priority_score(self, donor):
        days_since = (datetime.now() - datetime.strptime(donor.last_donation, "%Y-%m-%d")).days
        return (days_since * 0.5) + (donor.demand_score * 1)

    def inorder(self, node=None, results=[]):
        if node is None:
            node = self.root
        if node.left:
            self.inorder(node.left, results)
        results.append(node.donor)
        if node.right:
            self.inorder(node.right, results)
        return results

    def search_by_blood_type(self, blood_type):
        donors = self.inorder(self.root, [])
        return [d for d in donors if d.blood_type == blood_type]

