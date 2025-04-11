import sqlite3

def analyze_farmer_input():
    conn = sqlite3.connect("agri_system.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM farmer_input ORDER BY id DESC LIMIT 1")
    data = cursor.fetchone()

    if not data:
        print(" No farmer input found.")
        conn.close()
        return None

    land_size, soil_type, crop_pref, financial_goal = data[1:]
    print(f"[FarmerAdvisor] Received: Soil={soil_type}, CropPref={crop_pref}, Goal={financial_goal}")

    conn.close()

    return {
        "soil_type": soil_type,
        "crop_preference": crop_pref,
        "financial_goal": financial_goal
    }
