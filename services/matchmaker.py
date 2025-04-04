def match_patient(patient, blood_bst, donor_bst, history_map):
    blood_type = patient.blood_type_needed  # ✅ Works if patient is object

    # Step 1: Check hospital stock
    if blood_bst.get_available_units(blood_type) > 0:
        blood_bst.use_blood(blood_type)
        return "Blood available in hospital. Transfusion successful."

    # Step 2: Search BST for donor
    potential_donors = donor_bst.search_by_blood_type(blood_type)
    for donor in potential_donors:
        if history_map.is_eligible(donor.donor_id):
            return f"Blood not available. Donor {donor.name} contacted for donation."
    
    return "No eligible donor found."


