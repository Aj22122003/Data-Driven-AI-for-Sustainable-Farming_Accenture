import sqlite3

def find_best_crop(farmer_data):
    conn = sqlite3.connect("agri_system.db")
    cursor = conn.cursor()

    crop_pref = farmer_data.get('crop_preference', None)

    query = "SELECT crop, AVG(price) as avg_price, SUM(demand_index) as demand FROM market_data"
    params = []
    if crop_pref:
        query += " WHERE crop = ?"
        params.append(crop_pref)
    query += " GROUP BY crop ORDER BY demand DESC, avg_price DESC LIMIT 1"

    cursor.execute(query, params)
    result = cursor.fetchone()

    if result:
        crop, price, demand = result
        reasoning = f"High demand and good price. Demand Index: {demand}, Avg Price: ₹{price}"
        cursor.execute("INSERT INTO recommendations (crop, reasoning) VALUES (?, ?)", (crop, reasoning))
        conn.commit()
        print(f"[MarketResearcher] ✅ Recommended Crop: {crop} | Reason: {reasoning}")
    else:
        print("[MarketResearcher]  No suitable crop found.")

    cursor.close()
    conn.close()
