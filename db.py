import sqlite3

def init_db():
    conn = sqlite3.connect("agri_system.db")
    cursor = conn.cursor()

    # Create table for farmer input
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS farmer_input (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            land_size TEXT,
            soil_type TEXT,
            crop_preference TEXT,
            financial_goal TEXT
        )
    """)

    # Create table for market data
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS market_data (
            crop TEXT,
            region TEXT,
            price REAL,
            demand_index INTEGER
        )
    """)

    # Create recommendations table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS recommendations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            crop TEXT,
            reasoning TEXT
        )
    """)

    cursor.execute("""
    INSERT INTO farmer_input (land_size, soil_type, crop_preference, financial_goal)
    VALUES ('5 acres', 'Loamy', 'Wheat', 'High Profit')
""")

    conn.commit()
    cursor.close()
    conn.close()
    print(" Database initialized successfully.")
