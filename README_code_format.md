
# 🌾 AgroSakha: A Multi-Agent AI Advisor for Sustainable Farming

**Team Name**: Team AgriMind  
**Hackathon**: Accenture Gen AI Sprint – *Hack the Future: Powered by Data*  
**Project Type**: AI-based Sustainable Agriculture Advisor using Multi-Agent Systems

---

## 📌 Problem Statement

Farmers in rural regions face serious challenges in choosing optimal crops due to:

- Unpredictable weather patterns  
- Fluctuating market prices  
- Limited access to personalized, data-driven insights  
- High environmental costs (e.g., water usage, pesticide overuse, soil degradation)  

There is a **critical need** for a solution that integrates AI-driven insights to support sustainability and profitability.

---

## 💡 Our Solution: AgroSakha

AgroSakha is a multi-agent AI system designed to empower farmers with intelligent, sustainable, and real-time decision support.  
It integrates Farmer Advisory, Market Trends, Weather Forecasting, and Sustainability Evaluation using lightweight LLMs, IoT data, and geospatial intelligence.

---

## 🧠 Key Features

- Multi-Agent AI System: Modular agents collaborating on soil, crop, market, and weather data.
- Data-Driven Crop Recommendation: Based on land, soil, region, market, and environment.
- Geospatial Analysis: Uses Google Earth Engine & QGIS for soil/land classification.
- LLM-Powered Advisory: Uses TinyLlama, GPT-4 API for NLP-based farmer interaction.
- SQLite Integration: Long-term memory for adaptive recommendations.
- Sustainability Evaluator: Suggests low-carbon, low-water-consuming crops.

---

## 🛠️ Tech Stack

| Category            | Technology Used              |
|---------------------|-------------------------------|
| AI/ML               | Scikit-learn, XGBoost         |
| Multi-Agent System  | Python-based modular agents   |
| Geospatial Tools    | Google Earth Engine, QGIS     |
| Visualization       | Power BI, Tableau             |
| Cloud & Storage     | AWS, GCP, SQLite              |
| IoT Integration     | Real-time field sensor data   |
| LLMs                | GPT-4 API, TinyLlama, Gemma-2B|

---

## ⚙️ Agent Workflow

```text
Farmer Input
   ↓
Farmer Advisor Agent
   ↓
Weather Agent + Market Researcher
   ↓
Sustainability Evaluator
   ↓
Final Recommendation to Farmer
```

---

## 📁 Folder Structure

```text
├── agents/
│   ├── farmer_advisor.py
│   ├── market_researcher.py
│   └── weather_agent.py
├── data/
│   └── soil_weather_inputs.csv
├── models/
│   └── sustainability_rules.pkl
├── db/
│   └── farming_ai.db
├── main.py
├── requirements.txt
└── README.md
```

---

## 🧪 Sample Output

```python
Input:
  region = "South India"
  land = "Loamy"
  goals = ["maximize profit", "reduce water use"]

Output:
  recommended_crops = ["Millet", "Pulses"]
  financial_plan = "Low investment, high yield"
  sustainability_score = 87%
```

---

## 🔬 Code Snippet

```python
class FarmerAdvisor(BaseAgent):
    def process(self, input_data):
        return {
            "recommended_crops": ["Millet", "Pulses"],
            "financial_plan": "Low investment, high yield crops"
        }
```

```python
def store_data(agent_name, data):
    conn = sqlite3.connect('farming_ai.db')
    conn.execute("INSERT INTO agent_logs VALUES (?, ?)", (agent_name, json.dumps(data)))
    conn.commit()
```

---

## 📹 Demo Links

- GitHub Repo: https://github.com/aj22122003/Data-Driven-AI-for-Sustainable-Farming_Accenture
- Demo Videos:
  - https://youtube.com/shorts/JceJ6_JooPA?si=Gap-8RTLIVtxCu59
  - https://youtu.be/5jr3cZ0tUg0?si=q-wPCh9FwPVCXRPA
  - https://youtu.be/NYELIwX0K4?si=Oft8W9JQjPJN_Glj

---

## ✅ Conclusion

- Solves key challenges in modern farming.
- Offers a modular, real-time AI-based recommendation system.
- Reduces environmental impact while improving farmer profitability.
- Empowers farmers with easy-to-use, tech-driven tools.

> Empowering sustainable farming through intelligence, one decision at a time.
