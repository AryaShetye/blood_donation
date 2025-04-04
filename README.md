🩸 **AI-Powered Blood Donation Management System**

An intelligent, data-structure-driven backend application for managing blood requests, donor matching, and live urgency prioritization using BST, HashMap, and Priority Queue.

🚀 Features

⏱ Patient Urgency-Based Queue Management

🌳 Donor and Blood Inventory Management using Binary Search Trees

🧠 Donor Eligibility Tracking using HashMap

🤖 Smart Blood Matching: Matches recipient needs with real-time blood stock or nearest eligible donor

📈 Real-Time Console Monitoring for Admins

🧠 Data Structures Used

Data Structure	Purpose
Binary Search Tree	Organize and retrieve donors or blood units efficiently
Priority Queue	Handle patients by urgency level
HashMap	Track donor history, last donation, and health eligibility

⚙️ How It Works

📝 Donor is added:

Inserted into Donor BST

Stored in HashMap with donation history, last donation, health flags

🧑‍⚕️ Patient Arrives:

Vital stats and blood type are input

Urgency level is calculated (services/urgency.py)

Stored in Priority Queue (patient_pq.py)

🧪 Blood Matching:

Check if matching blood exists in blood_inventory BST

If not, fetch eligible donor from Donor BST (sorted by donation time, proximity, and demand score)

If eligible, notify donor (console simulated)

🧼 Console Admins See:

Current live queue of patients

Donor leaderboard by frequency

Blood type shortage warnings
