import sqlite3

conn = sqlite3.connect("streetlight.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS complaints (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pole_id TEXT NOT NULL,
    ward TEXT NOT NULL,
    street TEXT NOT NULL,
    fault_type TEXT NOT NULL,
    reported_date TEXT NOT NULL,
    status TEXT NOT NULL,
    repaired_date TEXT
)
""")

sample_data = [
("P101","Ward 1","Anna Nagar","Bulb Not Working","2026-07-01","Pending",None),
("P102","Ward 2","Gandhi Street","Wire Damage","2026-07-02","Repaired","2026-07-03"),
("P103","Ward 3","MG Road","Fuse Damage","2026-07-03","Pending",None),
("P104","Ward 4","Temple Road","Pole Damage","2026-07-04","In Progress",None),
("P105","Ward 5","Bus Stand","Switch Failure","2026-07-05","Pending",None),
("P106","Ward 6","Railway Road","Bulb Not Working","2026-07-06","Repaired","2026-07-07"),
("P107","Ward 7","College Road","Wire Damage","2026-07-07","Pending",None),
("P108","Ward 8","Hospital Road","Fuse Damage","2026-07-08","Pending",None),
("P109","Ward 9","Lake View","Pole Damage","2026-07-09","Repaired","2026-07-10"),
("P110","Ward 10","Market Road","Bulb Not Working","2026-07-10","Pending",None)
]

cursor.executemany("""
INSERT INTO complaints
(pole_id, ward, street, fault_type, reported_date, status, repaired_date)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", sample_data)

conn.commit()
conn.close()

print("streetlight.db created successfully!")