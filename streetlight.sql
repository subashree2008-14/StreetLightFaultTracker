-- =====================================
-- Street Light Fault Register Database
-- =====================================

DROP TABLE IF EXISTS complaints;

CREATE TABLE complaints (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    pole_id TEXT NOT NULL,

    ward TEXT NOT NULL,

    street TEXT NOT NULL,

    fault_type TEXT NOT NULL,

    reported_date TEXT NOT NULL,

    status TEXT NOT NULL,

    repaired_date TEXT

);

-- =====================================
-- Sample Data
-- =====================================

INSERT INTO complaints
(pole_id,ward,street,fault_type,reported_date,status,repaired_date)
VALUES
('P101','Ward 1','Anna Nagar','Bulb Not Working','2026-07-01','Pending',NULL),

('P102','Ward 2','Gandhi Street','Wire Damage','2026-07-02','Repaired','2026-07-03'),

('P103','Ward 3','Nehru Street','Fuse Damage','2026-07-03','Pending',NULL),

('P104','Ward 4','Market Road','Pole Damage','2026-07-04','In Progress',NULL),

('P105','Ward 5','Temple Road','Switch Failure','2026-07-05','Pending',NULL),

('P106','Ward 1','Bus Stand','Bulb Not Working','2026-07-06','Repaired','2026-07-07'),

('P107','Ward 2','Railway Road','Wire Damage','2026-07-07','Pending',NULL),

('P108','Ward 3','Lake View','Fuse Damage','2026-07-08','Pending',NULL),

('P109','Ward 4','College Road','Bulb Not Working','2026-07-09','Repaired','2026-07-10'),

('P110','Ward 5','Hospital Road','Pole Damage','2026-07-10','Pending',NULL),

('P111','Ward 6','Beach Road','Bulb Not Working','2026-07-11','Pending',NULL),

('P112','Ward 7','Main Road','Wire Damage','2026-07-12','In Progress',NULL),

('P113','Ward 8','Church Street','Fuse Damage','2026-07-13','Pending',NULL),

('P114','Ward 9','School Road','Bulb Not Working','2026-07-14','Repaired','2026-07-15'),

('P115','Ward 10','Old Bus Stand','Pole Damage','2026-07-15','Pending',NULL),

('P116','Ward 1','Anna Nagar','Wire Damage','2026-07-16','Pending',NULL),

('P117','Ward 2','Market Road','Fuse Damage','2026-07-17','Repaired','2026-07-18'),

('P118','Ward 3','Temple Road','Bulb Not Working','2026-07-18','Pending',NULL),

('P119','Ward 4','Nehru Street','Switch Failure','2026-07-19','Pending',NULL),

('P120','Ward 5','Lake View','Wire Damage','2026-07-20','In Progress',NULL),

('P121','Ward 6','College Road','Bulb Not Working','2026-07-21','Pending',NULL),

('P122','Ward 7','Beach Road','Pole Damage','2026-07-22','Repaired','2026-07-23'),

('P123','Ward 8','Hospital Road','Fuse Damage','2026-07-23','Pending',NULL),

('P124','Ward 9','Railway Road','Bulb Not Working','2026-07-24','Pending',NULL),

('P125','Ward 10','Main Road','Wire Damage','2026-07-25','Pending',NULL),

('P126','Ward 1','Church Street','Bulb Not Working','2026-07-26','Repaired','2026-07-27'),

('P127','Ward 2','School Road','Pole Damage','2026-07-27','Pending',NULL),

('P128','Ward 3','Anna Nagar','Fuse Damage','2026-07-28','Pending',NULL),

('P129','Ward 4','Temple Road','Wire Damage','2026-07-29','Repaired','2026-07-30'),

('P130','Ward 5','Market Road','Bulb Not Working','2026-07-30','Pending',NULL),

('P131','Ward 6','Lake View','Switch Failure','2026-07-31','Pending',NULL),

('P132','Ward 7','Bus Stand','Bulb Not Working','2026-08-01','Repaired','2026-08-02'),

('P133','Ward 8','Hospital Road','Pole Damage','2026-08-02','Pending',NULL),

('P134','Ward 9','Main Road','Fuse Damage','2026-08-03','Pending',NULL),

('P135','Ward 10','College Road','Wire Damage','2026-08-04','In Progress',NULL),

('P136','Ward 1','Beach Road','Bulb Not Working','2026-08-05','Pending',NULL),

('P137','Ward 2','Railway Road','Pole Damage','2026-08-06','Pending',NULL),

('P138','Ward 3','Church Street','Wire Damage','2026-08-07','Repaired','2026-08-08'),

('P139','Ward 4','School Road','Bulb Not Working','2026-08-08','Pending',NULL),

('P140','Ward 5','Anna Nagar','Fuse Damage','2026-08-09','Pending',NULL);