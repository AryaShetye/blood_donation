class BloodNode:
    def __init__(self, blood_type):
        self.blood_type = blood_type
        self.units = 0
        self.expiry_dates = []  # List of expiry timestamps
        self.left = None
        self.right = None

class BloodBST:
    def __init__(self):
        self.root = None

    def insert(self, blood_type, expiry_date):
        def _insert(node, blood_type, expiry):
            if not node:
                n = BloodNode(blood_type)
                n.units += 1
                n.expiry_dates.append(expiry)
                return n
            if blood_type < node.blood_type:
                node.left = _insert(node.left, blood_type, expiry)
            elif blood_type > node.blood_type:
                node.right = _insert(node.right, blood_type, expiry)
            else:
                node.units += 1
                node.expiry_dates.append(expiry)
            return node

        self.root = _insert(self.root, blood_type, expiry_date)

    def get_available_units(self, blood_type):
        node = self.root
        while node:
            if blood_type == node.blood_type:
                return node.units
            elif blood_type < node.blood_type:
                node = node.left
            else:
                node = node.right
        return 0

    def use_blood(self, blood_type):
        node = self.root
        while node:
            if blood_type == node.blood_type and node.units > 0:
                node.units -= 1
                node.expiry_dates.pop(0)
                return True
            elif blood_type < node.blood_type:
                node = node.left
            else:
                node = node.right
        return False
