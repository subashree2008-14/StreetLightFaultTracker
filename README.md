# Municipal Street Light Fault Register and Repair Tracker

## Problem Statement

Street light faults are usually recorded manually, making it difficult to track complaints, monitor repair progress, and identify frequently affected areas. This project provides a digital complaint management system to register, track, update, and manage street light repair requests efficiently.

---

# Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS
- JavaScript

---

# How to Run the Project

### Step 1
Install Python (3.10 or later).

### Step 2
Install Flask.

```bash
pip install flask
```

### Step 3
Download or clone this repository.

### Step 4
Open the project folder in Visual Studio Code.

### Step 5
Run the application.

```bash
python app.py
```

### Step 6
Open your browser and visit:

```
http://127.0.0.1:5000
```

---

# Project Features

- Register street light complaints
- Store complaint details in SQLite database
- View all registered complaints
- Update complaint status
- Search complaint records
- Track pending and repaired complaints

---

# Meaning of Each Field

| Field | Description |
|--------|-------------|
| Pole ID | Unique identification number of the street light pole |
| Ward | Municipal ward where the pole is located |
| Street | Street name of the reported location |
| Fault Type | Type of fault (Light Off, Flickering, Damaged Pole, etc.) |
| Reported Date | Date on which the complaint was registered |
| Status | Current complaint status (Pending, In Progress, Repaired) |
| Repaired Date | Date on which the repair was completed |

---

# Derived Figures Calculation

### Total Complaints

Calculated by counting all complaint records stored in the database.

```
Total Complaints = Total Number of Complaint Records
```

### Pending Complaints

```
Pending Complaints = Count of records where Status = Pending
```

### In Progress Complaints

```
In Progress Complaints = Count of records where Status = In Progress
```

### Repaired Complaints

```
Repaired Complaints = Count of records where Status = Repaired
```

---

# Project Workflow

1. User registers a street light complaint.
2. Complaint details are stored in the SQLite database.
3. Complaint appears in the complaint list.
4. Technician updates the complaint status.
5. Once repaired, the complaint is marked as **Repaired**.

---

# Screenshots

Screenshot folder is uploaded 

# Demonstration Video

```https://drive.google.com/file/d/19-ZvwvZ8SxTCTLSc5Eb7EoVMACaUipCM/view?usp=drivesdk

---

# Limitations (Not Yet Finished)

- User authentication is not implemented.
- Technician login is not available.
- Google Maps integration is not implemented.
- Email/SMS notifications are not implemented.
- PDF/Excel report generation is not available.

---

# Future Enhancements

- Admin Dashboard
- Technician Login
- Google Maps Integration
- Email Notifications
- SMS Alerts
- Report Export (PDF/Excel)
- Mobile Responsive Interface

---

# Folder Structure

```
StreetLightTracker/
│
├── app.py
├── streetlight.db
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   ├── register.html
│   ├── list.html
│   └── update.html
│
└── static/
    ├── style.css
    └── script.js
```

---

# Author

**Subashree M**

Department of Computer Science and Engineering

SIH 2026 – Skill Assessment Project
