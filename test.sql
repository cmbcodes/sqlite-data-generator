-- Opens generated database in SQLite
.open vehicles.db

-- Select all records from the Manufacturers table
SELECT * FROM Manufacturers;

-- Select all records from the Vehicles table
SELECT * FROM Vehicles;

-- Select all records from the Owners table
SELECT * FROM Owners;

-- Select all records from the MaintenanceRecords table
SELECT * FROM MaintenanceRecords;

-- Select vehicles and their owners' details
SELECT v.make, v.model, v.year, o.owner_name, o.contact_number, o.email
FROM Vehicles v
INNER JOIN Owners o ON v.owner_id = o.owner_id;

-- Select vehicles, their manufacturers, and maintenance records
SELECT v.make, v.model, v.year, m.manufacturer_name, mr.maintenance_type, mr.maintenance_date, mr.cost
FROM Vehicles v
INNER JOIN Manufacturers m ON v.vehicle_id = m.manufacturer_id
LEFT JOIN MaintenanceRecords mr ON v.vehicle_id = mr.vehicle_id;

-- Select vehicles and count of maintenance records per vehicle
SELECT v.make, v.model, COUNT(mr.record_id) AS maintenance_count
FROM Vehicles v
LEFT JOIN MaintenanceRecords mr ON v.vehicle_id = mr.vehicle_id
GROUP BY v.vehicle_id;

-- Select vehicles and their latest maintenance record
SELECT v.make, v.model, mr.maintenance_date, mr.maintenance_type, mr.cost
FROM Vehicles v
LEFT JOIN MaintenanceRecords mr ON v.vehicle_id = mr.vehicle_id
WHERE mr.record_id IN (
    SELECT MAX(record_id)
    FROM MaintenanceRecords
    GROUP BY vehicle_id
);
