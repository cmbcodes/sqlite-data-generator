from faker import Faker
import random
import sqlite3
from datetime import datetime, timedelta

fake = Faker()

# Create a SQLite database
conn = sqlite3.connect('vehicles.db')
cursor = conn.cursor()

# Create Manufacturers table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Manufacturers (
        manufacturer_id INTEGER PRIMARY KEY,
        manufacturer_name TEXT,
        country TEXT
    )
''')

# Create Vehicles table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Vehicles (
        vehicle_id INTEGER PRIMARY KEY,
        make TEXT,
        model TEXT,
        year INTEGER,
        owner_id INTEGER,
        FOREIGN KEY (owner_id) REFERENCES Owners(owner_id)
    )
''')

# Create Owners table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Owners (
        owner_id INTEGER PRIMARY KEY,
        owner_name TEXT,
        contact_number TEXT,
        email TEXT
    )
''')

# Create Maintenance Records table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS MaintenanceRecords (
        record_id INTEGER PRIMARY KEY,
        vehicle_id INTEGER,
        maintenance_date DATE,
        maintenance_type TEXT,
        cost REAL,
        description TEXT,
        FOREIGN KEY (vehicle_id) REFERENCES Vehicles(vehicle_id)
    )
''')

# Generate fake data and insert into tables
for _ in range(20):
    manufacturer_name = fake.company()
    country = fake.country()

    cursor.execute('''
        INSERT INTO Manufacturers (manufacturer_name, country)
        VALUES (?, ?)
    ''', (manufacturer_name, country))

for _ in range(80):
    make = fake.company()
    model = fake.word()
    year = fake.random_int(min=2000, max=2023)
    owner_id = random.randint(1, 15)

    cursor.execute('''
        INSERT INTO Vehicles (make, model, year, owner_id)
        VALUES (?, ?, ?, ?)
    ''', (make, model, year, owner_id))

for _ in range(60):
    owner_name = fake.name()
    contact_number = fake.phone_number()
    email = fake.email()

    cursor.execute('''
        INSERT INTO Owners (owner_name, contact_number, email)
        VALUES (?, ?, ?)
    ''', (owner_name, contact_number, email))

for _ in range(100):
    vehicle_id = random.randint(1, 20)
    maintenance_date = fake.date_between(start_date='-2y', end_date='today')
    maintenance_type = fake.random_element(elements=('Oil Change', 'Brake Inspection', 'Tire Rotation', 'Engine Tune-up'))
    cost = round(random.uniform(50, 500), 2)
    description = fake.text()

    cursor.execute('''
        INSERT INTO MaintenanceRecords (vehicle_id, maintenance_date, maintenance_type, cost, description)
        VALUES (?, ?, ?, ?, ?)
    ''', (vehicle_id, maintenance_date, maintenance_type, cost, description))

# Commit changes and close connection
conn.commit()
conn.close()

print("Database created and populated with mock data.")
