import ollama

def ai_analysis(farmer_data):
    model_name = "mistral"
    prompt = f"Given the farmer's conditions: Soil={farmer_data['soil_type']}, CropPref={farmer_data['crop_preference']}, FinancialGoal={farmer_data['financial_goal']}, suggest the best sustainable farming strategy."

    response = ollama.chat(model=model_name, messages=[{"role": "user", "content": prompt}])

    if isinstance(response, dict) and response.get("message") and response["message"].get("content"):
        ai_suggestion = response["message"]["content"]
        print("🤖 AI Insights:", ai_suggestion)
        return ai_suggestion
    else:
        print("❌ AI response error:", response)
        return None
